# -*- coding: utf-8 -*-
"""Merge the 56 written posts with the v5 concept spine and emit calendar.json."""
import json, io, os, collections, datetime as dt

ROOT = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026"
SCRATCH = r"C:\Users\Masroor\AppData\Local\Temp\claude\C--Users-Masroor\85b36120-1bdd-41ac-9941-bda2b8c1a109\scratchpad"
OUT = os.path.join(ROOT, "venus-calendar-app", "data", "calendar.json")

spine = json.load(io.open(os.path.join(SCRATCH, "spine5.json"), encoding="utf-8"))
written = json.load(io.open(os.path.join(SCRATCH, "written5.json"), encoding="utf-8"))
rows = [r for w in spine["weeks"] for r in w["rows"]]
byid = {int(p["id"]): p for w in written["weeks"] for p in w["posts"]}
print("spine rows %d, written posts %d" % (len(rows), len(byid)))

SRC_LABEL = {"DRIVE_READY": "Ready to post", "DRIVE_EDIT": "Edit needed",
             "SHOOT_PROP": "Shoot, props", "SHOOT_ENGAGE": "Shoot, engaging", "DESIGN": "Design"}
OWNER = {"DRIVE_READY": "Social", "DRIVE_EDIT": "Editor", "SHOOT_PROP": "Production",
         "SHOOT_ENGAGE": "Production", "DESIGN": "Designer"}
GOAL = {"Treatment": "profile", "Educational": "save", "Engaging": "comment", "Conversion": "dm"}
TREAT = {"laser": "Laser Hair Reduction", "skintighten": "Skin Tightening", "fatfreeze": "Fat Freezing",
         "prp": "PRP", "peel": "Chemical and Party Peel", "viva": "Venus Viva Resurfacing",
         "dermapen": "Dermapen", "darkcircle": "Dark Circles", "other": "Brand"}

R = lambda a, f, w, m: (a, f, w, m)
REF = {
 "https://instagram.com/p/DcO5LR-AqU0": R("Sculpt Spa","Reel","Six words, deadpan, one staff member, shot on a phone in the treatment room.","2k plays, 95 likes, 4.46% ER, the best humour result in the audit"),
 "https://instagram.com/p/DZ0ZWodCjuC": R("Sculpt Spa","Reel","We are fine with being your little secret. Plays on the fact that nobody tells anyone they come.","3k plays, 115 likes, 3.60% ER"),
 "https://instagram.com/p/Da3V-BPDlj9": R("Sculpt Spa","Reel","The failed attempt is the entire joke.","4k plays, 83 likes, 2.37% ER"),
 "https://instagram.com/p/DbWn5UlhfRx": R("Alchemy 43","Reel","Two staff, one trending audio, the treatment as the punchline.","3k plays, 21 comments, 1.97% ER"),
 "https://instagram.com/p/DbWQkkDP7uk": R("LaserAway","Reel","A mother teaching her daughter that looking after yourself is necessary.","56k plays, 2,444 likes, 4.45% ER, the highest found anywhere"),
 "https://instagram.com/p/DbdqueMOmLU": R("Skin Laundry","Reel","Between the errands and the emails. The clinic is never mentioned.","10k plays, 0.46% ER"),
 "https://instagram.com/p/DcBxwo1CCE2": R("Pulse Light London","Reel","Personality over information.","3k plays, 1.17% ER"),
 "https://instagram.com/p/DcZhRGkAMFZ": R("Milan Laser","Reel","Nine words, one treatment, no explanation.","6k plays, 0.76% ER"),
 "https://instagram.com/p/DcBiLzXCXoW": R("Venus Aesthetics","Reel","Your own team on Independence Day, no treatment in sight.","8,900 plays, 87 likes, 0.99% ER, one of your three best ever"),
 "https://instagram.com/p/DYIP3yWCjc6": R("Venus Aesthetics","Reel","Your own team on Mother's Day.","7,682 plays, 70 likes, 0.98% ER"),
 "https://instagram.com/p/DN7FCmVkvnX": R("Venus Aesthetics","Reel","Your own pause the video game.","2,388,358 plays, 206 comments, your highest comment count outside a giveaway"),
 "https://instagram.com/p/DQe0j3BCOWI": R("Venus Aesthetics","Reel","Your own POV, you open something you were not supposed to.","55,827 plays, 122 likes, 22 comments"),
 "https://instagram.com/p/DUDpXQDFTfk": R("Venus Aesthetics","Reel","Your own absurdist penguin post.","1,783,781 plays, 2,656 likes"),
 "https://instagram.com/p/DP0GawgAQSH": R("Venus Aesthetics","Reel","Your own Babar Azam post.","6,699,036 plays, 54,026 likes, 0.81% ER"),
 "https://instagram.com/p/DcOsYaChl8J": R("Skin Laundry","Reel","The treatment filmed plainly and named every time.","9k plays, 0.57% ER"),
 "https://instagram.com/p/DbIZKAIFRJK": R("Pulse Light London","Reel","What it actually feels like, narrated while it happens.","Named series, outperforms their results content"),
 "https://instagram.com/p/DbdowHqk8H-": R("Sono Bello","Reel","Progress over real elapsed time rather than one reveal.","92k plays, 1,930 likes, 2.16% ER"),
 "https://instagram.com/p/DcByqkjFjzn": R("Sono Bello","Reel","The client speaks for herself, no brand voiceover.","78k plays, 2,003 likes, 2.69% ER"),
 "https://instagram.com/p/DboqG0evGyt": R("LaserAway","Reel","A male client filmed plainly on his own terms.","38k plays, 700 likes, 1.86% ER"),
 "https://instagram.com/p/DbYJ9SjCpZe": R("Pulse Light London","Reel","Part two of a numbered series. The number brings people back.","Named series"),
 "https://instagram.com/p/DQ7tEOBD9a4": R("Ideal Image","Reel","A practitioner answers one specific question.","14k plays, 162 likes, 1.30% ER"),
 "https://instagram.com/p/DdWx_IIlPpl": R("Venus Aesthetics","Reel","Your own best ever engagement rate, the question as the subject.","4,553 plays, 41 likes, 1.03% ER"),
 "https://instagram.com/p/DP8oCpqDsQm": R("Venus Aesthetics","Reel","Your own wedding timed question.","104,989 plays, 276 likes, 0.30% ER"),
 "https://instagram.com/p/DbCGcx9DwhK": R("SkinSpirit","Carousel","Turns the pain question into a joke then answers it honestly.","766 likes, 35 comments"),
 "https://instagram.com/p/DcNiQjIiFpi": R("Dr Rashmi Shetty","Carousel","Why two people get different results. Sequential and it continues a previous post.","1,787 likes, 28 comments"),
 "https://instagram.com/p/DaSKpcYAeZD": R("Dr Jaishree Sharad","Carousel","Which pre wedding treatments are worth it.","390 likes, 15 comments"),
 "https://instagram.com/p/DbhObcpGpyU": R("SkinSpirit","Carousel","One appointment is not the final result.","496 likes, 21 comments"),
 "https://instagram.com/p/DbhxnXFkfgr": R("Dr Rashmi Shetty","Carousel","Why a concern cannot be treated in isolation.","423 likes, 20 comments"),
 "https://instagram.com/p/DFwKaBjNXTC": R("SkinSpirit","Carousel","A first timer entry point that assumes nothing.","544 likes, 25 comments"),
 "https://instagram.com/p/DFtgsFSMdtd": R("SkinSpirit","Carousel","Authority stated as fact rather than boast.","542 likes, 36 comments"),
 "https://instagram.com/p/DF1GC74OC5S": R("SkinSpirit","Carousel","The clinic sold as an experience rather than a facility.","746 likes, 70 comments"),
 "https://instagram.com/p/DbyWRuTlLx8": R("SkinSpirit","Carousel","A new location announced as news, no discount attached.","533 likes, 39 comments"),
 "https://instagram.com/p/DbGU_X7CGaQ": R("Dr Rashmi Shetty","Carousel","Taking a position against your own category.","465 likes, 16 comments"),
 "https://instagram.com/p/DdIvEhsoN6J": R("Clinic Dermatech","Carousel","Wedding content that refuses to panic people.","Well written, 3 likes from 41.6K followers"),
 "https://instagram.com/p/DdB3R1BE8bB": R("Oliva Skin and Hair","Carousel","A concern led hook that stays on behaviour.","Indian chain, comparable skin tones"),
 "https://instagram.com/p/DdboieCE7N8": R("Oliva Skin and Hair","Carousel","Search phrases in brackets instead of a hashtag wall.","Caption structure benchmark"),
 "https://instagram.com/p/C30amLssmwL": R("Sono Bello","Carousel","A result with a clean spec block, the practitioner is data not a face.","Chain benchmark"),
 "https://instagram.com/p/Da3Vg47xYUq": R("Face Haus","Reel","A new place filmed as a destination.","91k plays, 2,011 likes, 2.29% ER"),
}
def norm(u):
    u = (u or "").strip()
    if not u: return ""
    u = u.rstrip("/").replace("https://www.instagram.com", "https://instagram.com")
    import re
    m = re.search(r"/(?:p|reel)/([A-Za-z0-9_-]+)", u)
    return "https://instagram.com/p/" + m.group(1) if m else u
NREF = {norm(k): v for k, v in REF.items()}

items, missing = [], []
for r in rows:
    p = byid.get(r["id"])
    if not p: missing.append(r["id"]); continue
    a = r.get("asset") or {}
    fs = r.get("frameSource") or {}
    src = r["source"]
    ref = norm(p.get("reference"))
    rm = NREF.get(ref, ("", "", "", ""))
    d = dt.date.fromisoformat(r["date"])
    items.append({
        "id": r["id"], "date": r["date"], "day": d.strftime("%a"), "dayFull": r["dayFull"],
        "dateLabel": d.strftime("%d %b %Y"), "week": r["week"],
        "block": d.strftime("%B"), "bucket": r["bucket"],
        "show": r["format"], "variant": r["concept"],
        "conceptLine": p.get("conceptLine", ""), "conceptNote": r.get("conceptNote", ""),
        "voice": r["voice"], "theme": r["bucket"] + " · " + r["format"],
        "treatment": TREAT.get(a.get("treat") or fs.get("treat") or "other", "Brand"),
        "creative": r["creative"], "goal": GOAL.get(r["bucket"], "save"),
        "hook": p.get("hook", ""), "caption": p.get("caption", ""),
        "hashtags": p.get("hashtags", ""), "keywordBlock": "",
        "cta": "", "source": src, "sourceLabel": SRC_LABEL.get(src, src),
        "asset": a.get("driveName") or (("DESIGN: " + r["concept"]) if src == "DESIGN" else ("SHOOT: " + r["concept"])),
        "fromDrive": bool(a), "driveUrl": a.get("driveUrl", "") or fs.get("driveUrl", ""),
        "driveFolder": " / ".join((a.get("drivePath", "") or "").split("/")[1:-1]).strip(),
        "driveFile": a.get("driveName", "") or fs.get("driveName", ""),
        "sourceSeconds": a.get("dur") or fs.get("dur") or None,
        "frameSource": fs.get("driveName", ""), "bankSecondCut": False,
        "editNeeded": src == "DRIVE_EDIT",
        "spec": p.get("spec", ""), "script": "", "recordGuide": p.get("recordGuide", "") or "",
        "editNote": "", "isVideo": r["creative"] == "Reel",
        "needsProduction": src in ("SHOOT_PROP", "SHOOT_ENGAGE"),
        "marker": r.get("marker", ""), "owner": OWNER.get(src, "Social"),
        "ref": ref, "refAccount": rm[0], "refFormat": rm[1],
        "refWhy": p.get("refWhy") or rm[2], "refMetric": rm[3],
        "editRef": "", "editRefAccount": "", "editRefWhy": "", "editRefMetric": "",
    })
if missing: print("!! NOT YET WRITTEN:", missing)
items.sort(key=lambda x: x["id"])

production = []
for i in [x for x in items if x["needsProduction"]]:
    production.append({"no": len(production)+1, "id": i["id"], "date": i["dateLabel"], "week": i["week"],
        "kind": "Prop shoot" if i["source"] == "SHOOT_PROP" else "Engaging shoot",
        "title": i["show"], "variant": i["variant"], "treatment": i["treatment"], "hook": i["hook"],
        "conceptLine": i["conceptLine"], "spec": i["spec"], "script": "", "recordGuide": i["recordGuide"],
        "ref": i["ref"], "refAccount": i["refAccount"], "refWhy": i["refWhy"], "refMetric": i["refMetric"],
        "editRef": "", "editRefWhy": "", "hasScript": False, "hasGuide": bool(i["recordGuide"])})

used = collections.Counter(i["ref"] for i in items if i["ref"])
reflib = [{"key": (NREF[u][0] + " " + NREF[u][1]).lower().replace(" ", "_"), "url": u,
           "account": NREF[u][0], "format": NREF[u][1], "why": NREF[u][2],
           "metric": NREF[u][3], "usedOn": n} for u, n in used.most_common() if u in NREF]

stats = {"total": len(items), "fromDrive": sum(1 for i in items if i["fromDrive"]),
    "driveLinked": sum(1 for i in items if i["driveUrl"]),
    "readyToPost": sum(1 for i in items if i["source"] == "DRIVE_READY"),
    "editNeeded": sum(1 for i in items if i["source"] == "DRIVE_EDIT"),
    "toShoot": sum(1 for i in items if i["needsProduction"]),
    "toDesign": sum(1 for i in items if i["source"] == "DESIGN"),
    "scripts": 0, "guides": sum(1 for i in items if i["recordGuide"]), "editNotes": 0, "bankedCuts": 0,
    "byShow": dict(collections.Counter(i["show"] for i in items)),
    "byBucket": dict(collections.Counter(i["bucket"] for i in items)),
    "byOwner": dict(collections.Counter(i["owner"] for i in items)),
    "byCreative": dict(collections.Counter(i["creative"] for i in items)),
    "bySource": dict(collections.Counter(i["sourceLabel"] for i in items)),
    "byGoal": dict(collections.Counter(i["goal"] for i in items))}

blocks = []
for name in ("September", "October", "November"):
    wk = [i["week"] for i in items if i["block"] == name]
    if wk: blocks.append({"name": name, "from": min(wk), "to": max(wk)})

json.dump({"brand": "Venus Aesthetics", "title": "8 Week Content Calendar",
  "period": {"start": items[0]["date"], "end": items[-1]["date"],
             "weeks": max(i["week"] for i in items), "posts": len(items),
             "label": "Monday 28 September to Sunday 22 November 2026"},
  "generated": "2026-09-24", "blocks": blocks, "items": items, "production": production,
  "referenceLibrary": reflib, "stats": stats},
  io.open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

print("wrote", OUT)
print("items %d | ready %d | edit %d | shoot %d | design %d" % (stats["total"], stats["readyToPost"],
      stats["editNeeded"], stats["toShoot"], stats["toDesign"]))
print("buckets:", stats["byBucket"]); print("creative:", stats["byCreative"])
print("drive links %d | guides %d | production %d | refs %d" % (
      stats["driveLinked"], stats["guides"], len(production), len(reflib)))
bad = sorted({i["ref"] for i in items if i["ref"] and i["ref"] not in NREF})
print("UNRECOGNISED REFS:", bad or "none")
