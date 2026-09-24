# -*- coding: utf-8 -*-
"""Merge the written posts with the allocated spine and emit calendar.json for the board."""
import json, io, os, sys, collections, re, datetime as dt

ROOT = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026"
SCRATCH = r"C:\Users\Masroor\AppData\Local\Temp\claude\C--Users-Masroor\85b36120-1bdd-41ac-9941-bda2b8c1a109\scratchpad"
OUT = os.path.join(ROOT, "venus-calendar-app", "data", "calendar.json")

alloc = json.load(io.open(os.path.join(SCRATCH, "allocated.json"), encoding="utf-8"))
written = json.load(io.open(os.path.join(SCRATCH, "written.json"), encoding="utf-8"))

byid = {}
for w in written["weeks"]:
    for p in w["posts"]:
        byid[int(p["id"])] = p

SRC_LABEL = {
    "DRIVE_READY": "Ready to post", "DRIVE_EDIT": "Edit needed",
    "SHOOT_TALK": "Shoot, scripted", "SHOOT_BROLL": "Shoot, b-roll", "DESIGN": "Design",
}
OWNER = {
    "DRIVE_READY": "Social", "DRIVE_EDIT": "Editor", "SHOOT_TALK": "Production",
    "SHOOT_BROLL": "Production", "DESIGN": "Designer",
}
TREAT_NAME = {
    "laser": "Laser Hair Reduction", "skintighten": "Skin Tightening", "fatfreeze": "Fat Freezing",
    "prp": "PRP", "hydra": "Venus Glow HydraFacial", "peel": "Chemical and Party Peel",
    "viva": "Venus Viva Resurfacing", "dermapen": "Dermapen", "darkcircle": "Dark Circles",
    "engaging": "Brand", "event": "Brand", "other": "Brand", "music": "Brand",
}

REF_META = {
 "https://www.instagram.com/reel/DcdhVOWopJe/": ("Skin and Shape", "Reel", "Episodic RF vs MNRF comparison. Turns a decision into a numbered series people come back for.", "216 likes, 21 comments"),
 "https://www.instagram.com/bodycraftclinic/reel/DdjA0XSzEcm/": ("Bodycraft Clinic", "Reel", "A de-sell. Three things worth knowing BEFORE you book, stated as limitations.", "19 likes, 6 comments, the highest comment to like ratio on that account"),
 "https://www.instagram.com/p/DctTDGeS6fQ/": ("aashrayy0", "Reel", "Opens on proof of failure, flips to proof of success, shows the method as a raw document, closes on a one word CTA.", "233,952 plays, 3,554 likes, 10,022 comments"),
 "https://www.instagram.com/p/DdNliMKI8tx/": ("aashrayy0", "Reel", "The same formula scaled 6x. Comments beat likes 2 to 1, deliberately.", "1,536,752 plays, 27,490 likes, 53,954 comments"),
 "https://www.instagram.com/p/DdWx_IIlPpl/": ("Venus Aesthetics", "Reel", "Venus's own best engagement rate. A doctor answering a pre-event worry, with the question as the subject.", "4,553 plays, 41 likes, 1.03% ER, the best on the account"),
 "https://www.instagram.com/p/DP8oCpqDsQm/": ("Venus Aesthetics", "Reel", "Venus's own. A wedding-timed treatment question outperformed every treatment explainer.", "104,989 plays, 276 likes, 37 comments, 0.30% ER"),
 "https://www.instagram.com/p/DcBiLzXCXoW/": ("Venus Aesthetics", "Reel", "Venus's own. The team being human on Independence Day, no treatment in sight.", "8,900 plays, 87 likes, 0.99% ER"),
 "https://www.instagram.com/sonobello/p/C30amLssmwL/": ("Sono Bello", "Carousel", "A results post carrying a six field spec block, where the practitioner is one line of data and not a face.", "Chain benchmark for credible result posts"),
 "https://www.instagram.com/p/DdIvEhsoN6J/": ("Clinic Dermatech", "Carousel", "Refuses the wedding panic frame. Your wedding is one day, your skin stays for a thousand.", "Well written, 3 likes from 41.6K followers, proof that good writing alone is not enough"),
 "https://www.instagram.com/p/DdB3R1BE8bB/": ("Oliva Skin and Hair", "Carousel", "A concern-led hook that stays on behaviour rather than attacking appearance.", "Indian chain, comparable skin tones"),
 "https://www.instagram.com/olivaclinics/p/DdboieCE7N8/": ("Oliva Skin and Hair", "Carousel", "Drops the hashtag wall for two brand tags plus plain search phrases in brackets.", "Caption structure benchmark, strip their superlatives"),
 "https://www.instagram.com/p/DXcNEnGjc_V/": ("Creator clinic visit", "Carousel", "A paid creator visit with a personal experience disclaimer, not a barter.", "371 likes, 37 comments"),
}

items, missing = [], []
for r in alloc["rows"]:
    p = byid.get(r["id"])
    if not p:
        missing.append(r["id"]); continue
    a = r.get("asset") or {}
    src = r["source"]
    treat = TREAT_NAME.get(a.get("treat", ""), "Brand")
    if not a and r["pillar"] in ("Smog Diary", "Biology Countdown", "Branch Desk", "The Decision Table"):
        treat = "Multiple"
    ref = (p.get("reference") or "").strip()
    rm = REF_META.get(ref, ("", "", "", ""))
    items.append({
        "id": r["id"], "date": r["date"],
        "day": dt.date.fromisoformat(r["date"]).strftime("%a"),
        "dayFull": r["dayFull"],
        "dateLabel": dt.date.fromisoformat(r["date"]).strftime("%d %b %Y"),
        "week": r["week"], "block": r["season"].split(",")[0].title(),
        "show": r["pillar"], "treatment": treat, "creative": r["creative"],
        "goal": p.get("goal", ""),
        "hook": p.get("hook", ""), "caption": p.get("caption", ""),
        "hashtags": p.get("hashtags", ""), "keywordBlock": p.get("keywordBlock", ""),
        "cta": p.get("cta", ""),
        "source": src, "sourceLabel": SRC_LABEL.get(src, src),
        "asset": a.get("driveName") or ("DESIGN: " + r["pillar"] if src == "DESIGN" else "SHOOT: " + r["pillar"]),
        "fromDrive": bool(a), "driveUrl": a.get("driveUrl", ""),
        "driveFolder": " / ".join((a.get("drivePath", "") or "").split("/")[1:-1]).strip(),
        "driveFile": a.get("driveName", ""),
        "editNeeded": src == "DRIVE_EDIT",
        "spec": p.get("spec", ""), "script": p.get("script", "") or "",
        "recordGuide": p.get("recordGuide", "") or "", "editNote": p.get("editNote", "") or "",
        "isVideo": r["creative"] == "Reel",
        "needsProduction": src in ("SHOOT_TALK", "SHOOT_BROLL"),
        "marker": r.get("marker", ""),
        "owner": OWNER.get(src, "Social"),
        "ref": ref, "refAccount": rm[0], "refFormat": rm[1], "refWhy": rm[2], "refMetric": rm[3],
    })

if missing:
    print("!! MISSING WRITTEN POSTS FOR IDS:", missing)

items.sort(key=lambda x: x["id"])

# production = the videos that must be shot, numbered
production = []
for i in [x for x in items if x["needsProduction"]]:
    production.append({
        "no": len(production) + 1, "id": i["id"], "date": i["dateLabel"], "week": i["week"],
        "kind": "Talking script" if i["source"] == "SHOOT_TALK" else "B-roll shoot",
        "title": i["show"], "treatment": i["treatment"], "hook": i["hook"],
        "spec": i["spec"], "script": i["script"], "recordGuide": i["recordGuide"],
        "ref": i["ref"], "refAccount": i["refAccount"], "refWhy": i["refWhy"], "refMetric": i["refMetric"],
        "hasScript": bool(i["script"]), "hasGuide": bool(i["recordGuide"]),
    })

usedrefs = collections.Counter(i["ref"] for i in items if i["ref"])
reflib = []
for url, n in usedrefs.most_common():
    m = REF_META.get(url)
    if not m: continue
    reflib.append({"key": m[0].lower().replace(" ", "_") + "_" + m[1].lower(),
                   "url": url, "account": m[0], "format": m[1], "why": m[2], "metric": m[3], "usedOn": n})

stats = {
    "total": len(items),
    "fromDrive": sum(1 for i in items if i["fromDrive"]),
    "driveLinked": sum(1 for i in items if i["driveUrl"]),
    "readyToPost": sum(1 for i in items if i["source"] == "DRIVE_READY"),
    "editNeeded": sum(1 for i in items if i["source"] == "DRIVE_EDIT"),
    "toShoot": sum(1 for i in items if i["needsProduction"]),
    "toDesign": sum(1 for i in items if i["source"] == "DESIGN"),
    "scripts": sum(1 for i in items if i["script"]),
    "guides": sum(1 for i in items if i["recordGuide"]),
    "editNotes": sum(1 for i in items if i["editNote"]),
    "byShow": dict(collections.Counter(i["show"] for i in items)),
    "byOwner": dict(collections.Counter(i["owner"] for i in items)),
    "byCreative": dict(collections.Counter(i["creative"] for i in items)),
    "bySource": dict(collections.Counter(i["sourceLabel"] for i in items)),
    "byGoal": dict(collections.Counter(i["goal"] for i in items)),
}

doc = {
    "brand": "Venus Aesthetics",
    "title": "Q4 Content Calendar",
    "period": "Monday 28 September to Thursday 31 December 2026",
    "generated": "2026-09-23",
    "blocks": ["October", "November", "December"],
    "items": items, "production": production,
    "referenceLibrary": reflib, "stats": stats,
}
json.dump(doc, io.open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

print("wrote", OUT)
print("items %d | ready %d | edit %d | shoot %d | design %d" % (
    stats["total"], stats["readyToPost"], stats["editNeeded"], stats["toShoot"], stats["toDesign"]))
print("drive links %d | scripts %d | guides %d | edit notes %d" % (
    stats["driveLinked"], stats["scripts"], stats["guides"], stats["editNotes"]))
print("creative:", stats["byCreative"])
print("goals:", stats["byGoal"])
print("production rows:", len(production), "| references:", len(reflib))
