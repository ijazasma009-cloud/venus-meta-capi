# -*- coding: utf-8 -*-
import json, io, os, re, html, datetime, collections
import v3_days_1, v3_days_2, v3_days_3, v3_days_4, v3_refs

APP_DATA  = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app\data"
INVENTORY = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\research\drive_inventory.json"
os.makedirs(APP_DATA, exist_ok=True)

ROWS = v3_days_1.ROWS + v3_days_2.ROWS + v3_days_3.ROWS + v3_days_4.ROWS

# ---------------------------------------------------------------- Drive links
inv = json.load(io.open(INVENTORY, encoding="utf-8"))
def norm(p):
    p = html.unescape(p).replace("\u2019","").replace("\u2018","").replace("'","")
    return re.sub(r"\s+"," ",p).strip().lower()
BY_PATH, BY_NAME = {}, {}
for x in inv:
    if x.get("type") != "FILE": continue
    BY_PATH[norm(x["path"])] = x["id"]
    BY_NAME.setdefault(norm(x["path"].rsplit(" / ",1)[-1]), x["id"])

def resolve(asset):
    if not asset.startswith("Drive:"):
        return None, None, None
    raw = re.sub(r"\s*\([^)]*\)\s*$","", asset[len("Drive:"):].strip()).strip()
    fid = BY_PATH.get(norm("ROOT / " + raw)) or BY_NAME.get(norm(raw.rsplit(" / ",1)[-1]))
    folder, _, fname = raw.rpartition(" / ")
    return ("https://drive.google.com/file/d/%s/view" % fid if fid else None), folder, fname

# ---------------------------------------------------------------- blocks
BLOCKS = [
 (1,5,  "BUILD THE HABIT",
  "Weeks 1 to 5. Establish the recurring formats, get the treatment courses running with real dates on screen, "
  "and put the first engaging videos out so the audience starts expecting one every Saturday."),
 (6,9,  "THE FULL MENU",
  "Weeks 6 to 9. Every treatment Venus actually sells enters the calendar, including the eleven that have never "
  "been posted about. Botox, hyperhidrosis, AcneOUT, SlimFit and the rest."),
 (10,13,"SEASON, MEN AND PROOF",
  "Weeks 10 to 13. Wedding season is live so short-runway treatments lead. Week 11 goes entirely to men, "
  "week 12 is proof and trust, and the quarter closes on the machine reference post."),
]
def block_for(w):
    for a,b,n,_ in BLOCKS:
        if a <= w <= b: return n
    return ""

OWNER = {"DRIVE_READY":"Social manager","DRIVE_EDIT":"Editor","SHOOT_TALK":"Videographer",
         "SHOOT_ENGAGE":"Videographer","SHOOT_BROLL":"Videographer","DESIGN":"Designer"}
STATE_LABEL = {"DRIVE_READY":"Ready to post","DRIVE_EDIT":"Edit needed","SHOOT_TALK":"Shoot, scripted",
               "SHOOT_ENGAGE":"Shoot, engaging","SHOOT_BROLL":"Shoot, b-roll","DESIGN":"Design"}

items, unresolved = [], []
for i, r in enumerate(ROWS, 1):
    d = datetime.date.fromisoformat(r["date"])
    url, folder, fname = resolve(r["asset"])
    if r["asset"].startswith("Drive:") and not url:
        unresolved.append(r["asset"])
    ref = v3_refs.REFS.get(r.get("ref")) if r.get("ref") else None
    code = re.search(r"(SHOOT|DESIGN|EDIT):?\s*([A-Za-z ]*\d{2}|[A-Za-z ,]+)", r["asset"])

    items.append({
      "id": i,
      "date": r["date"], "day": d.strftime("%a"), "dayFull": d.strftime("%A"),
      "dateLabel": d.strftime("%d %b %Y"), "week": r["week"], "block": block_for(r["week"]),
      "show": r["format"], "treatment": r["treatment"], "creative": r["creative"],
      "hook": r["hook"], "caption": r["caption"], "hashtags": r["hashtags"], "cta": r["cta"],
      "source": r["source"], "sourceLabel": STATE_LABEL[r["source"]],
      "asset": r["asset"], "fromDrive": r["asset"].startswith("Drive:"),
      "driveUrl": url, "driveFolder": folder, "driveFile": fname,
      "editNeeded": bool(r.get("editNeeded")),
      "spec": r["spec"], "script": r.get("script"), "recordGuide": r.get("recordGuide"),
      "isVideo": r["creative"] == "Reel",
      "needsProduction": r["source"] in ("SHOOT_TALK","SHOOT_ENGAGE","SHOOT_BROLL"),
      "prodCode": (code.group(0) if code else None),
      "owner": OWNER[r["source"]],
      "ref": (ref[0] if ref else None), "refAccount": (ref[1] if ref else None),
      "refFormat": (ref[2] if ref else None), "refWhy": (ref[3] if ref else None),
      "refMetric": (ref[4] if ref else None),
    })

# ---------------------------------------------------------------- production: VIDEOS ONLY, numbered
prod = []
n = 0
for it in items:
    if not it["needsProduction"]:
        continue
    n += 1
    prod.append({
      "no": n, "id": it["id"], "date": it["dateLabel"], "week": it["week"],
      "kind": ("Talking video" if it["source"]=="SHOOT_TALK"
               else "Engaging video" if it["source"]=="SHOOT_ENGAGE" else "B-roll"),
      "title": it["asset"].replace("SHOOT: ",""),
      "treatment": it["treatment"], "hook": it["hook"],
      "spec": it["spec"], "script": it.get("script"), "recordGuide": it.get("recordGuide"),
      "ref": it["ref"], "refAccount": it["refAccount"], "refWhy": it["refWhy"], "refMetric": it["refMetric"],
      "hasScript": bool(it.get("script")), "hasGuide": bool(it.get("recordGuide")),
    })

reference_library = [
  {"key":k, "url":v[0], "account":v[1], "format":v[2], "why":v[3], "metric":v[4],
   "usedOn": sum(1 for i in items if i["ref"] == v[0])}
  for k, v in v3_refs.REFS.items()]

payload = {
  "brand":"Venus Aesthetics", "title":"Venus Content Calendar",
  "period":{"start":items[0]["date"],"end":items[-1]["date"],"weeks":13,"posts":len(items)},
  "generated":"2026-08-27",
  "blocks":[{"from":a,"to":b,"name":nm,"desc":ds} for a,b,nm,ds in BLOCKS],
  "items":items, "production":prod,
  "referenceLibrary":sorted(reference_library, key=lambda r:-r["usedOn"]),
  "stats":{
    "total":len(items),
    "fromDrive":sum(1 for i in items if i["fromDrive"]),
    "driveLinked":sum(1 for i in items if i["driveUrl"]),
    "readyToPost":sum(1 for i in items if i["source"]=="DRIVE_READY"),
    "editNeeded":sum(1 for i in items if i["source"]=="DRIVE_EDIT"),
    "toShoot":sum(1 for i in items if i["needsProduction"]),
    "toDesign":sum(1 for i in items if i["source"]=="DESIGN"),
    "scripts":sum(1 for i in items if i.get("script")),
    "guides":sum(1 for i in items if i.get("recordGuide")),
    "byShow":dict(collections.Counter(i["show"] for i in items)),
    "byOwner":dict(collections.Counter(i["owner"] for i in items)),
    "byCreative":dict(collections.Counter(i["creative"] for i in items)),
    "bySource":dict(collections.Counter(i["sourceLabel"] for i in items)),
  },
}

with io.open(os.path.join(APP_DATA,"calendar.json"),"w",encoding="utf-8") as f:
    json.dump(payload,f,ensure_ascii=False,indent=1)

s = payload["stats"]
print("items:", s["total"])
print("  ready to post :", s["readyToPost"])
print("  edit needed   :", s["editNeeded"])
print("  to shoot      :", s["toShoot"], "(production page)")
print("  to design     :", s["toDesign"])
print("drive links:", s["driveLinked"], "| scripts:", s["scripts"], "| record guides:", s["guides"])
print("creative:", s["byCreative"])
print("production items (videos only):", len(prod))
print("reference library:", len(reference_library), "| in use:", sum(1 for r in reference_library if r["usedOn"]))
print("UNRESOLVED:", unresolved or "none")
