# -*- coding: utf-8 -*-
import json, io, os, re, html, datetime, collections
import v2_days_a, v2_days_b, v2_days_c, v2_shows, v2_refs, v2_edits

APP_DATA = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app\data"
INVENTORY = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\research\drive_inventory.json"
os.makedirs(APP_DATA, exist_ok=True)

ROWS = v2_days_a.ROWS + v2_days_b.ROWS + v2_days_c.ROWS

# ---------------------------------------------------------------- Drive link resolution
inv = json.load(io.open(INVENTORY, encoding="utf-8"))

# Real measured durations, read straight off the files in Drive. Used so the edit brief
# can say how long the source actually is instead of guessing.
DURATIONS = os.path.join(os.path.dirname(INVENTORY), "durations_clean.json")
try:
    _dur = json.load(io.open(DURATIONS, encoding="utf-8"))
except Exception:
    _dur = {}
DUR_BY_FILE = {}
for _k, _v in _dur.items():
    DUR_BY_FILE[_k.rsplit(" / ", 1)[-1].strip().lower()] = _v
def norm(p):
    p = html.unescape(p)
    # Apostrophes are inconsistent between Drive, the export and the source files, so drop them entirely.
    p = p.replace("\u2019", "").replace("\u2018", "").replace("'", "")
    p = re.sub(r"\s+", " ", p).strip().lower()
    return p
BY_PATH = {}
BY_NAME = {}
for x in inv:
    if x.get("type") != "FILE":
        continue
    full = norm(x["path"])
    BY_PATH[full] = x["id"]
    BY_NAME.setdefault(norm(x["path"].rsplit(" / ", 1)[-1]), x["id"])

def resolve(asset):
    """Return (driveUrl, folderPath, fileName, resolved?) for a 'Drive: ...' asset string."""
    if not asset.startswith("Drive:"):
        return None, None, None, False
    raw = asset[len("Drive:"):].strip()
    raw = re.sub(r"\s*\([^)]*\)\s*$", "", raw).strip()      # drop trailing "(interview segment)"
    key = norm("ROOT / " + raw)
    fid = BY_PATH.get(key)
    if not fid:                                              # fall back to filename match
        fid = BY_NAME.get(norm(raw.rsplit(" / ", 1)[-1]))
    folder, _, fname = raw.rpartition(" / ")
    url = ("https://drive.google.com/file/d/%s/view" % fid) if fid else None
    return url, folder, fname, bool(fid)

# ---------------------------------------------------------------- blocks
BLOCKS = [
 (1,5,  "THE PROOF ENGINE",
  "Weeks 1 to 5. Four case files open and start running in parallel. The job of this block is to prove Venus can "
  "carry a real patient through a real course, and to establish the machine names so they start meaning something."),
 (6,9,  "THE FULL MENU",
  "Weeks 6 to 9. Case files 02 and 03 close while 04 and 05 run. Botox and hyperhidrosis enter the calendar for the "
  "first time, both of which generate leads today with zero content behind them."),
 (10,13,"SEASON AND PROOF",
  "Weeks 10 to 13. Wedding season is live so short-runway treatments lead. Two male case files close, and the quarter "
  "ends on a six month follow up and a seven-file compilation nobody in the category has attempted."),
]
def block_for(w):
    for a,b,n,d in BLOCKS:
        if a <= w <= b: return n
    return ""

def owner_for(asset):
    a = asset.strip().upper()
    if a.startswith("SHOOT"):  return "Videographer"
    if a.startswith("DESIGN"): return "Designer"
    return "Editor"

items = []
unresolved = []
for i, r in enumerate(ROWS, 1):
    date, week, show, treatment, creative, hook, caption, cta, asset, _oldref, note = r
    d = datetime.date.fromisoformat(date)
    url, folder, fname, ok = resolve(asset)
    if asset.startswith("Drive:") and not ok:
        unresolved.append(asset)

    refkey, (refurl, refacct, refdesc, refmetric) = v2_refs.ref_for(date, show)
    spec = v2_edits.spec_for(show)
    code = re.search(r"\b((?:SHOOT|DESIGN|EDIT)\s+[A-C]-\d{2})", asset)

    items.append({
        "id": i,
        "date": date, "day": d.strftime("%a"), "dayFull": d.strftime("%A"),
        "dateLabel": d.strftime("%d %b %Y"),
        "week": week, "block": block_for(week),
        "show": show, "treatment": treatment, "creative": creative,
        "hook": hook, "caption": caption, "cta": cta,
        "asset": asset,
        "fromDrive": asset.startswith("Drive:"),
        "driveUrl": url, "driveFolder": folder, "driveFile": fname,
        "seconds": (int(round(DUR_BY_FILE[(fname or "").strip().lower()]))
                    if (fname or "").strip().lower() in DUR_BY_FILE else None),
        "prodCode": (code.group(1) if code else None),
        "owner": owner_for(asset),
        "edit": ({"length": spec[0], "cut": spec[1], "onScreen": spec[2], "audio": spec[3]} if spec else None),
        "editWarnings": v2_edits.notes_for(asset),
        "ref": refurl, "refType": refkey, "refAccount": refacct,
        "refWhy": refdesc, "refMetric": refmetric,
        "note": note,
    })

shows = [{"name":s[0],"slot":s[1],"creative":s[2],"what":s[3],"why":s[4],"refs":s[5],"assets":s[6]}
         for s in v2_shows.SHOWS]
case_files = [{"id":k,"patient":v[0],"treatment":v[1],"beats":v[2],"assets":v[3],"note":v[4]}
              for k,v in v2_shows.CASE_FILES.items()]

production = collections.OrderedDict()
for it in items:
    if it["prodCode"]:
        p = production.setdefault(it["prodCode"], {
            "code": it["prodCode"], "owner": it["owner"],
            "brief": it["asset"], "dates": [], "posts": 0})
        p["dates"].append(it["dateLabel"]); p["posts"] += 1

reference_library = [{"key":k, "url":v[0], "account":v[1], "why":v[2], "metric":v[3],
                      "usedOn": sum(1 for i in items if i["refType"] == k)}
                     for k, v in v2_refs.REFS.items()]

payload = {
  "brand": "Venus Aesthetics",
  "title": "Venus Content Calendar",
  "period": {"start": items[0]["date"], "end": items[-1]["date"], "weeks": 13, "posts": len(items)},
  "generated": "2026-08-26",
  "blocks": [{"from":a,"to":b,"name":n,"desc":d} for a,b,n,d in BLOCKS],
  "items": items, "shows": shows, "caseFiles": case_files,
  "production": list(production.values()),
  "referenceLibrary": sorted(reference_library, key=lambda r: -r["usedOn"]),
  "editSpecs": {k: {"length":v[0],"cut":v[1],"onScreen":v[2],"audio":v[3]} for k,v in v2_edits.EDIT_SPEC.items()},
  "stats": {
    "total": len(items),
    "fromDrive": sum(1 for i in items if i["fromDrive"]),
    "driveLinked": sum(1 for i in items if i["driveUrl"]),
    "toProduce": sum(1 for i in items if not i["fromDrive"]),
    "refTypes": len(set(i["refType"] for i in items)),
    "byShow": dict(collections.Counter(i["show"] for i in items)),
    "byOwner": dict(collections.Counter(i["owner"] for i in items)),
    "byTreatment": dict(collections.Counter(i["treatment"] for i in items)),
    "byRefType": dict(collections.Counter(i["refType"] for i in items)),
  },
}

with io.open(os.path.join(APP_DATA, "calendar.json"), "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=1)

print("items:", len(items))
print("from Drive:", payload["stats"]["fromDrive"], "| with a real Drive link:", payload["stats"]["driveLinked"])
print("to produce:", payload["stats"]["toProduce"])
print("distinct reference types in use:", payload["stats"]["refTypes"], "of", len(v2_refs.REFS), "in the library")
print("posts carrying edit warnings:", sum(1 for i in items if i["editWarnings"]))
if unresolved:
    print("UNRESOLVED DRIVE PATHS:")
    for u in unresolved: print("   ", u)
else:
    print("every Drive asset resolved to a real file id")
