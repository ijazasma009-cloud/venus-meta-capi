# -*- coding: utf-8 -*-
"""Merge the written posts with the v4.3 spine and emit calendar.json for the board."""
import json, io, os, collections, datetime as dt

ROOT = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026"
SCRATCH = r"C:\Users\Masroor\AppData\Local\Temp\claude\C--Users-Masroor\85b36120-1bdd-41ac-9941-bda2b8c1a109\scratchpad"
OUT = os.path.join(ROOT, "venus-calendar-app", "data", "calendar.json")

spine = json.load(io.open(os.path.join(SCRATCH, "spine3.json"), encoding="utf-8"))
written = json.load(io.open(os.path.join(SCRATCH, "written.json"), encoding="utf-8"))

rows = [r for w in spine["weeks"] for r in w["rows"]]
byid = {int(p["id"]): p for w in written["weeks"] for p in w["posts"]}

SRC_LABEL = {"DRIVE_READY": "Ready to post", "DRIVE_EDIT": "Edit needed",
             "SHOOT_TALK": "Shoot, scripted", "SHOOT_BROLL": "Shoot, b-roll",
             "SHOOT_ENGAGE": "Shoot, engaging", "DESIGN": "Design"}
OWNER = {"DRIVE_READY": "Social", "DRIVE_EDIT": "Editor", "SHOOT_TALK": "Production",
         "SHOOT_BROLL": "Production", "SHOOT_ENGAGE": "Production", "DESIGN": "Designer"}
TREAT = {"laser": "Laser Hair Reduction", "skintighten": "Skin Tightening", "fatfreeze": "Fat Freezing",
         "prp": "PRP", "hydra": "Venus Glow HydraFacial", "peel": "Chemical and Party Peel",
         "viva": "Venus Viva Resurfacing", "dermapen": "Dermapen", "darkcircle": "Dark Circles",
         "engaging": "Brand", "event": "Brand", "other": "Brand", "music": "Brand"}

R = lambda a, f, w, m: (a, f, w, m)
REF_META = {
 "https://instagram.com/p/DcO5LR-AqU0": R("Sculpt Spa","Reel","Six words, deadpan, one staff member, shot on a phone in the treatment room. No production at all.","2k plays, 95 likes, 4.46% ER, the best humour result in the whole audit"),
 "https://instagram.com/p/DZ0ZWodCjuC": R("Sculpt Spa","Reel","All jokes aside, we are fine with being your little secret. Plays on the fact that nobody tells anyone they come.","3k plays, 115 likes, 3.60% ER"),
 "https://instagram.com/p/Da3V-BPDlj9": R("Sculpt Spa","Reel","Guess I will try again tomorrow. The failed attempt is the entire joke.","4k plays, 83 likes, 2.37% ER"),
 "https://instagram.com/p/DbWn5UlhfRx": R("Alchemy 43","Reel","Two staff, one trending audio, the treatment as the punchline rather than the subject.","3k plays, 21 comments, 1.97% ER"),
 "https://instagram.com/p/DbWQkkDP7uk": R("LaserAway","Reel","A mother teaching her daughter that looking after yourself is necessary.","56k plays, 2,444 likes, 4.45% ER, the highest engagement found anywhere"),
 "https://instagram.com/p/DbdqueMOmLU": R("Skin Laundry","Reel","Between the errands, the emails and everything else. The clinic is never mentioned.","10k plays, 0.46% ER"),
 "https://instagram.com/p/DcBxwo1CCE2": R("Pulse Light London","Reel","You are not going to believe this, but we think you should wear sunscreen. Personality over information.","3k plays, 1.17% ER"),
 "https://instagram.com/p/DcZhRGkAMFZ": R("Milan Laser","Reel","Nine words, one treatment, no explanation. An entire chain runs on this.","6k plays, 0.76% ER"),
 "https://instagram.com/p/DcBiLzXCXoW": R("Venus Aesthetics","Reel","Venus's own. The team celebrating Independence Day, no treatment in sight.","8,900 plays, 87 likes, 0.99% ER, one of their three best ever"),
 "https://www.instagram.com/p/DcBiLzXCXoW/": R("Venus Aesthetics","Reel","Venus's own. The team celebrating Independence Day, no treatment in sight.","8,900 plays, 87 likes, 0.99% ER"),
 "https://instagram.com/p/DYIP3yWCjc6": R("Venus Aesthetics","Reel","Venus's own. The team on Mother's Day.","7,682 plays, 70 likes, 0.98% ER"),
 "https://instagram.com/p/DUDpXQDFTfk": R("Venus Aesthetics","Reel","Venus's own absurdist penguin post.","1,783,781 plays, 2,656 likes"),
 "https://instagram.com/p/DaddvlVkZyk": R("Venus Aesthetics","Reel","Venus's own POV blooper where the balloon had other plans.","26,766 plays, 118 likes, 0.47% ER"),
 "https://instagram.com/p/DQe0j3BCOWI": R("Venus Aesthetics","Reel","Venus's own. POV, you open something you were not supposed to.","55,827 plays, 122 likes, 22 comments"),
 "https://instagram.com/p/DN7FCmVkvnX": R("Venus Aesthetics","Reel","Venus's own pause-the-video game, Stop the Sunblock and Win.","2,388,358 plays, 206 comments, their highest comment count outside a giveaway"),
 "https://instagram.com/p/DP0GawgAQSH": R("Venus Aesthetics","Reel","Venus's own Babar Azam post.","6,699,036 plays, 54,026 likes, 0.81% ER, the biggest engagement event in the account's history"),
 "https://www.instagram.com/p/DctTDGeS6fQ/": R("aashrayy0","Reel","One static camera, face large, no cuts, all the work done by overlays. Raw screenshots rather than designed graphics.","233,952 plays, 3,554 likes, 10,022 comments"),
 "https://instagram.com/p/DctTDGeS6fQ": R("aashrayy0","Reel","One static camera, no cuts, overlays do the work.","233,952 plays, 3,554 likes, 10,022 comments"),
 "https://www.instagram.com/p/DdNliMKI8tx/": R("aashrayy0","Reel","Opens on proof of failure in the first 3 seconds, flips to proof of success by second 10, then the method as a document.","1,536,752 plays, 27,490 likes, 53,954 comments"),
 "https://instagram.com/p/DdNliMKI8tx": R("aashrayy0","Reel","Failure proof, then success proof, then the method.","1,536,752 plays, 27,490 likes, 53,954 comments"),
 "https://www.instagram.com/p/DdWx_IIlPpl/": R("Venus Aesthetics","Reel","Venus's own best ever engagement rate. A doctor answering a pre-event worry with the question as the subject.","4,553 plays, 41 likes, 1.03% ER"),
 "https://instagram.com/p/DdWx_IIlPpl": R("Venus Aesthetics","Reel","Venus's own best ever engagement rate, the question as the subject.","4,553 plays, 41 likes, 1.03% ER"),
 "https://www.instagram.com/p/DP8oCpqDsQm/": R("Venus Aesthetics","Reel","Venus's own wedding-timed treatment question.","104,989 plays, 276 likes, 37 comments, 0.30% ER"),
 "https://instagram.com/p/DP8oCpqDsQm": R("Venus Aesthetics","Reel","Venus's own wedding-timed treatment question.","104,989 plays, 276 likes, 37 comments, 0.30% ER"),
 "https://instagram.com/p/DbdowHqk8H-": R("Sono Bello","Reel","Three months on, progress shown over real elapsed time rather than one reveal.","92k plays, 1,930 likes, 2.16% ER"),
 "https://instagram.com/p/DcByqkjFjzn": R("Sono Bello","Reel","Completed treatment, the patient speaks for herself with no brand voiceover.","78k plays, 2,003 likes, 2.69% ER"),
 "https://instagram.com/p/DboqG0evGyt": R("LaserAway","Reel","A male patient filmed plainly on his own terms.","38k plays, 700 likes, 1.86% ER"),
 "https://instagram.com/p/DbIZKAIFRJK": R("Pulse Light London","Reel","What the treatment actually feels like, narrated while it happens, including the uncomfortable parts.","Named series, outperforms their results content"),
 "https://instagram.com/p/DbYJ9SjCpZe": R("Pulse Light London","Reel","Part two of a numbered series. The part number is what brings people back.","Named series, beats their results-only content"),
 "https://instagram.com/p/DQ7tEOBD9a4": R("Ideal Image","Reel","A named practitioner answers one specific question. Their single best performing post.","14k plays, 162 likes, 1.30% ER"),
 "https://instagram.com/p/DcOsYaChl8J": R("Skin Laundry","Reel","The hero treatment filmed and named in the caption every time.","9k plays, 0.57% ER"),
 "https://instagram.com/p/Da3Vg47xYUq": R("Face Haus","Reel","A new place filmed as a destination. Scale and setting do the selling.","91k plays, 2,011 likes, 2.29% ER"),
 "https://instagram.com/p/DbCGcx9DwhK": R("SkinSpirit","Carousel, 4 slides","Things that hurt more than microneedling. Turns the pain question into a joke, then answers it honestly.","766 likes, 35 comments"),
 "https://instagram.com/p/DcNiQjIiFpi": R("Dr Rashmi Shetty","Carousel, 7 slides","Why two patients having the same treatment get different results. Sequential, and it continues a previous post.","1,787 likes, 28 comments"),
 "https://instagram.com/p/DaSKpcYAeZD": R("Dr Jaishree Sharad","Carousel, 3 slides","Which pre-wedding treatments are worth the money. A comparison that helps someone choose.","390 likes, 15 comments"),
 "https://instagram.com/p/DbhObcpGpyU": R("SkinSpirit","Carousel, 3 slides","One appointment does not always mean the final result. Sets expectations before the booking.","496 likes, 21 comments"),
 "https://instagram.com/p/DbhxnXFkfgr": R("Dr Rashmi Shetty","Carousel, 5 slides","One session, maybe two, but never the under eye alone. Persuasive because it sounds like a caution.","423 likes, 20 comments"),
 "https://instagram.com/p/DFwKaBjNXTC": R("SkinSpirit","Carousel, 3 slides","New to medical aesthetics. A first-timer entry point that assumes nothing.","544 likes, 25 comments"),
 "https://instagram.com/p/DFtgsFSMdtd": R("SkinSpirit","Carousel, 3 slides","Our team trains the trainers. Authority stated as fact rather than boast.","542 likes, 36 comments"),
 "https://instagram.com/p/DF1GC74OC5S": R("SkinSpirit","Carousel, 3 slides","Step into the space. The clinic sold as an experience rather than a facility.","746 likes, 70 comments"),
 "https://instagram.com/p/DbyWRuTlLx8": R("SkinSpirit","Carousel, 3 slides","A new location announced as news, with no discount attached.","533 likes, 39 comments"),
 "https://instagram.com/p/DbGU_X7CGaQ": R("Dr Rashmi Shetty","Carousel, 7 slides","The aesthetics industry has a marketing problem and it is costing patients. Taking a position against your own category.","465 likes, 16 comments"),
 "https://www.instagram.com/sonobello/p/C30amLssmwL/": R("Sono Bello","Carousel","A results post with a six field spec block where the practitioner is one line of data, not a face.","Chain benchmark for credible result posts"),
 "https://www.instagram.com/p/DdIvEhsoN6J/": R("Clinic Dermatech","Carousel","Not Wedding-Ready, Life-Ready. Refuses the panic frame.","Well written, 3 likes from 41.6K followers"),
 "https://www.instagram.com/p/DdB3R1BE8bB/": R("Oliva Skin and Hair","Carousel","A concern-led hook that stays on behaviour rather than attacking appearance.","Indian chain, comparable skin tones"),
 "https://www.instagram.com/olivaclinics/p/DdboieCE7N8/": R("Oliva Skin and Hair","Carousel","Drops the hashtag wall for brand tags plus plain search phrases in brackets.","Caption structure benchmark"),
 "https://instagram.com/p/DXcNEnGjc_V": R("Creator clinic visit","Carousel","A paid creator visit with a personal experience disclaimer, not a barter.","371 likes, 37 comments"),
}
def norm(u):
    u = (u or "").strip()
    if not u: return ""
    return u.rstrip("/").replace("https://www.instagram.com", "https://instagram.com")
NORM_META = {norm(k): v for k, v in REF_META.items()}

items, missing = [], []
for r in rows:
    p = byid.get(r["id"])
    if not p: missing.append(r["id"]); continue
    a = r.get("asset") or {}
    fs = r.get("frameSource") or {}
    src = r["source"]
    ref, eref = norm(p.get("reference")), norm(p.get("editReference"))
    rm = NORM_META.get(ref, ("", "", "", ""))
    em = NORM_META.get(eref, ("", "", "", ""))
    treat = TREAT.get(a.get("treat") or fs.get("treat") or "other", "Brand")
    items.append({
        "id": r["id"], "date": r["date"], "day": dt.date.fromisoformat(r["date"]).strftime("%a"),
        "dayFull": r["dayFull"], "dateLabel": dt.date.fromisoformat(r["date"]).strftime("%d %b %Y"),
        "week": r["week"], "theme": r["theme"], "themeNote": r["themeNote"],
        "block": ("October" if r["date"] < "2026-11-01" else "November" if r["date"] < "2026-12-01" else "December"),
        "show": r["pillar"], "subPillar": r.get("subPillar", ""), "variant": r.get("variant", ""),
        "treatment": treat, "creative": r["creative"], "goal": p.get("goal", ""),
        "hook": p.get("hook", ""), "caption": p.get("caption", ""),
        "hashtags": p.get("hashtags", ""), "keywordBlock": p.get("keywordBlock", ""),
        "cta": p.get("cta", ""),
        "source": src, "sourceLabel": SRC_LABEL.get(src, src),
        "asset": a.get("driveName") or (("DESIGN: " + r["pillar"]) if src == "DESIGN" else ("SHOOT: " + r["pillar"])),
        "fromDrive": bool(a), "driveUrl": a.get("driveUrl", "") or fs.get("driveUrl", ""),
        "driveFolder": " / ".join((a.get("drivePath", "") or fs.get("drivePath", "") or "").split("/")[1:-1]).strip(),
        "driveFile": a.get("driveName", "") or fs.get("driveName", ""),
        "sourceSeconds": a.get("dur") or fs.get("dur") or None,
        "frameSource": fs.get("driveName", ""),
        "bankSecondCut": bool(r.get("bankSecondCut")),
        "editNeeded": src == "DRIVE_EDIT",
        "spec": p.get("spec", ""), "script": p.get("script", "") or "",
        "recordGuide": p.get("recordGuide", "") or "", "editNote": p.get("editNote", "") or "",
        "isVideo": r["creative"] == "Reel",
        "needsProduction": src in ("SHOOT_TALK", "SHOOT_BROLL", "SHOOT_ENGAGE"),
        "marker": r.get("marker", ""), "owner": OWNER.get(src, "Social"),
        "ref": ref, "refAccount": rm[0], "refFormat": rm[1], "refWhy": p.get("refWhy") or rm[2], "refMetric": rm[3],
        "editRef": eref, "editRefAccount": em[0], "editRefWhy": p.get("editRefWhy") or em[2], "editRefMetric": em[3],
    })
if missing: print("!! MISSING WRITTEN POSTS:", missing)
items.sort(key=lambda x: x["id"])

production = []
for i in [x for x in items if x["needsProduction"]]:
    production.append({"no": len(production)+1, "id": i["id"], "date": i["dateLabel"], "week": i["week"],
        "kind": {"SHOOT_TALK": "Talking script", "SHOOT_BROLL": "B-roll shoot", "SHOOT_ENGAGE": "Engaging shoot"}[i["source"]],
        "title": i["show"], "variant": i["variant"], "treatment": i["treatment"], "hook": i["hook"],
        "spec": i["spec"], "script": i["script"], "recordGuide": i["recordGuide"],
        "ref": i["ref"], "refAccount": i["refAccount"], "refWhy": i["refWhy"], "refMetric": i["refMetric"],
        "editRef": i["editRef"], "editRefWhy": i["editRefWhy"],
        "hasScript": bool(i["script"]), "hasGuide": bool(i["recordGuide"])})

used = collections.Counter()
for i in items:
    if i["ref"]: used[i["ref"]] += 1
    if i["editRef"]: used[i["editRef"]] += 1
reflib = []
for url, n in used.most_common():
    m = NORM_META.get(url)
    if not m: continue
    reflib.append({"key": (m[0] + " " + m[1]).lower().replace(" ", "_"), "url": url,
                   "account": m[0], "format": m[1], "why": m[2], "metric": m[3], "usedOn": n})

stats = {"total": len(items),
    "fromDrive": sum(1 for i in items if i["fromDrive"]),
    "driveLinked": sum(1 for i in items if i["driveUrl"]),
    "readyToPost": sum(1 for i in items if i["source"] == "DRIVE_READY"),
    "editNeeded": sum(1 for i in items if i["source"] == "DRIVE_EDIT"),
    "toShoot": sum(1 for i in items if i["needsProduction"]),
    "toDesign": sum(1 for i in items if i["source"] == "DESIGN"),
    "scripts": sum(1 for i in items if i["script"]),
    "guides": sum(1 for i in items if i["recordGuide"]),
    "editNotes": sum(1 for i in items if i["editNote"]),
    "bankedCuts": sum(1 for i in items if i["bankSecondCut"]),
    "sourceMinutes": round(sum(i["sourceSeconds"] or 0 for i in items if i["fromDrive"]) / 60, 1),
    "byShow": dict(collections.Counter(i["show"] for i in items)),
    "byOwner": dict(collections.Counter(i["owner"] for i in items)),
    "byCreative": dict(collections.Counter(i["creative"] for i in items)),
    "bySource": dict(collections.Counter(i["sourceLabel"] for i in items)),
    "byGoal": dict(collections.Counter(i["goal"] for i in items))}

blocks = []
for name in ("October", "November", "December"):
    wk = [i["week"] for i in items if i["block"] == name]
    if wk: blocks.append({"name": name, "from": min(wk), "to": max(wk)})

json.dump({"brand": "Venus Aesthetics", "title": "Q4 Content Calendar",
  "period": {"start": items[0]["date"], "end": items[-1]["date"],
             "weeks": max(i["week"] for i in items), "posts": len(items),
             "label": "Monday 28 September to Thursday 31 December 2026"},
  "generated": "2026-09-23",
  "blocks": blocks, "items": items, "production": production,
  "referenceLibrary": reflib, "stats": stats},
  io.open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

print("wrote", OUT)
print("items %d | ready %d | edit %d | shoot %d | design %d" % (stats["total"], stats["readyToPost"],
      stats["editNeeded"], stats["toShoot"], stats["toDesign"]))
print("drive links %d | scripts %d | guides %d | edit notes %d | banked cuts %d" % (
      stats["driveLinked"], stats["scripts"], stats["guides"], stats["editNotes"], stats["bankedCuts"]))
print("creative:", stats["byCreative"]); print("goals:", stats["byGoal"])
print("production rows:", len(production), "| references in use:", len(reflib))
unknown = sorted({i["ref"] for i in items if i["ref"] and not NORM_META.get(i["ref"])} |
                 {i["editRef"] for i in items if i["editRef"] and not NORM_META.get(i["editRef"])})
print("UNRECOGNISED REFERENCE URLS:", unknown or "none")
