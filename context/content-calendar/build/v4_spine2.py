# -*- coding: utf-8 -*-
"""v4.2 spine and allocation.

Changes the client asked for after seeing v4.1
  1. Saturday becomes a dedicated ENGAGEMENT DAY, 13 posts, every one with an exact
     content reference and an exact editing reference.
  2. Maximum use of existing footage: the 7 Dr. Uzair FAQs about limits move to Wednesday,
     which turns 7 planned shoots into ready-to-post video, and every DESIGN row gets a
     frameSource so no slide is ever built from stock.
  3. Named week themes so no two weeks repeat, plus real break weeks at the holiday clusters.
  4. The Men's Room folds into Monday as male-directed device clips. The Tray folds into
     Wednesday. Branch Desk runs on the break days.
"""
import json, io, os, re, collections, datetime as dt

SCRATCH = r"C:\Users\Masroor\AppData\Local\Temp\claude\C--Users-Masroor\85b36120-1bdd-41ac-9941-bda2b8c1a109\scratchpad"
pool = json.load(io.open(os.path.join(SCRATCH, "build_list.json"), encoding="utf-8"))

# ---------------------------------------------------------------- assets
def base(n): return re.sub(r"_?subtitling", "", n, flags=re.I).replace(".mp4", "").strip().lower()
uz_groups, others = collections.defaultdict(list), []
for p in pool:
    if p["isUzair"]: uz_groups[base(p["name"])].append(p)
    else: others.append(p)
uz = []
for b, g in uz_groups.items():
    g.sort(key=lambda x: (0 if "subtitl" in x["name"].lower() else 1)); uz.append(g[0])

SKIP = ("intro reel", "introfortv", "venus_music", "thank you being a part", "free consultation for story")
def qkey(n):
    n = re.sub(r"_?subtitling|\.mp4|opt\s*0?2|-", "", n, flags=re.I); return re.sub(r"[^a-z]", "", n.lower())
seen, uz_faq = set(), []
for p in sorted([x for x in uz if not any(s in x["name"].lower() for s in SKIP)], key=lambda x: x["name"].lower()):
    k = qkey(p["name"])
    if k not in seen: seen.add(k); uz_faq.append(p)

LIMITS = ["sideeffects", "what should yo avoid", "is rf micro neddling af", "when do you see results",
          "will i see immediate", "is aftercare is imp", "what skin concern"]
uz_limits = [p for p in uz_faq if any(k in p["name"].lower() for k in LIMITS)]
uz_questions = [p for p in uz_faq if p not in uz_limits]

by_treat = collections.defaultdict(list)
for p in others: by_treat[p["treat"]].append(p)
for k in by_treat: by_treat[k].sort(key=lambda x: x["name"])
MALE = ("malemodel", "kabeer", "assbeah")
male = [p for p in others if any(h in p["name"].lower() for h in MALE)]

# engaging clips I watched frame by frame. Nothing unwatched gets scheduled.
WATCHED = {
 "Engaging content_02.mp4": "Gloved hand against the yellow-lit wall. Words on each finger unfold one at a time: Treatment, YOU, NEED, VENUS, AESTHTIC, then the palm turns to show BOOK NOW. 7s. DEFECT: the glove reads AESTHTIC, misspelled.",
 "Engaging content_04.mp4": "POV walk through reception, hand held forward, past the GET THE GLOW neon, ending on a purple brochure reading WE PUT ETHICS IN AESTHETICS. 6s. Clean, no text defects.",
 "Engaging content_05.mp4": "Rotating cast in one treatment chair. A doctor in a white coat, then staff in black uniforms take turns sitting and posing while the group stands around. 7s. Clean.",
 "Engaging content_07.mp4": "Paper aeroplane POV flying the length of the clinic, past HELLO BEAUTY, the brochure stand, GET THE GLOW and BEYOND SKIN BEYOND BEAUTY. 22s. Handheld and shaky, needs stabilising.",
 "Engaging content_11.mp4": "A staff member holds up cards to camera: Thank You, then For Visitng, then the Venus logo card. 3s. DEFECT: the card reads For Visitng, misspelled.",
 "Engaging content_12.mp4": "Two staff in black uniforms and gloves talking across a consultation desk to a seated patient, shot over the patient's shoulder. No burned-in text. 8s. Clean.",
 "WHO'S YOUR DREAM PATENT.mp4": "The whole team stands looking at their phones, then all look up and point at the lens. Text asks who our dream patient is, answer YOU. 6s. DEFECT: the burned-in text reads PATENT, not PATIENT.",
 "have you heard the news.mp4": "Gossip chain. One staff member gasps at her phone then whispers to the next, down a row of seated staff. Text: Have You Heard The News. 9s. ALREADY USED for the November 2025 sale announcement, so it must be re-cut with new text.",
 "Confidence.mp4": "A woman walks through the clinic looking at her phone showing a contact called Bill Gates. The joke is post-treatment confidence. 6s. DEFECT: the line reads The Confidence you get when you done with Fat Frezze, broken English and misspelled.",
 "location.mp4": "Slow clean interior tour, no people, no text. Reception, MAKE YOUR SOUL SHINE wall, GET THE GLOW neon, waiting area, product shelves, corridor, YOU DESERVE TO SHINE arch. 20s. The best brand b-roll in the library.",
}
watched = [p for p in others if p["name"] in WATCHED]

# ---------------------------------------------------------------- the spine
START, END = dt.date(2026, 9, 28), dt.date(2026, 12, 31)
days = [START + dt.timedelta(days=i) for i in range((END - START).days + 1)]

THEMES = {
 1:  "The season opens", 2: "How many sessions, really", 3: "Before the event",
 4:  "Hair, honestly", 5: "What is on the tray", 6: "The air changes",
 7:  "Barrier week", 8: "The laser window opens", 9: "Scalp and fall",
 10: "Choosing a clinic", 11: "Wavelength week", 12: "The December bride",
 13: "Quiet days", 14: "What next year needs",
}
NOTE = {
 1: "Wedding season opens in October and a course started now finishes in time. Set the arithmetic up.",
 2: "The published average is close to nine sessions, not three. Spend the week on honest numbers.",
 3: "Peels and glow timed to a function, and what genuinely fits inside three weeks.",
 4: "Seasonal shedding is easing rather than peaking. Say so, then separate it from real hair loss.",
 5: "Sterility, provenance and paperwork, in a market where the regulator is sealing clinics weekly.",
 6: "November opens. The Sunday slot becomes the smog card and holds for five weeks.",
 7: "Two public holidays back to back. Lead with hours and utility, then barrier science.",
 8: "UV drops to an average daily maximum of 4. The clinically correct season to start laser.",
 9: "Pollution and hair loss evidence, handled carefully, with a countermeasure in every post.",
 10: "December is when the researching patient finally picks. Shift from acquisition to comparison.",
 11: "Wavelength is the one variable most competitors running IPL cannot match. Move the talk off price.",
 12: "Be honest about what no longer fits before a December function and what still moves in three weeks.",
 13: "Quaid-e-Azam Day and Christmas. Hours, aftercare, low effort, high utility.",
 14: "Four days. Year end, January course planning, and the Ramadan 2027 window.",
}
SLOTS = {0: ("Eight Seconds", "Reel"), 1: ("The Decision Table", "Carousel"),
         2: ("The Honest Number", "Reel"), 3: ("Matched Frame", "Carousel"),
         4: ("Asked and Answered", "Reel"), 5: ("The Room", "Reel"),
         6: ("The Forward", "Carousel")}
MARKERS = {dt.date(2026,11,8): "Diwali, public holiday",
           dt.date(2026,11,9): "Iqbal Day, public holiday. Reconfirm with the Cabinet Division in late October.",
           dt.date(2026,12,25): "Quaid-e-Azam Day and Christmas, public holiday",
           dt.date(2026,12,26): "Holiday for Christians only"}
BREAKS = {dt.date(2026,11,9): ("Branch Desk", "Carousel"),
          dt.date(2026,12,24): ("Branch Desk", "Carousel")}

rows = []
for i, d in enumerate(days):
    wd = d.weekday()
    pillar, fmt = SLOTS[wd]
    if wd == 6: pillar = "Smog Diary" if d.month == 11 else "Biology Countdown"
    if d in BREAKS: pillar, fmt = BREAKS[d]
    wk = (d - START).days // 7 + 1
    rows.append({"id": i+1, "date": d.isoformat(), "dayFull": d.strftime("%A"),
                 "week": wk, "theme": THEMES[wk], "themeNote": NOTE[wk],
                 "pillar": pillar, "creative": fmt,
                 "season": ("OCTOBER, acquisition and course starts" if d.month in (9,10)
                            else "NOVEMBER, the smog month" if d.month == 11
                            else "DECEMBER, the decision month"),
                 "marker": MARKERS.get(d, "")})

# ---------------------------------------------------------------- allocation
used = set()
def take(cands):
    for c in cands:
        if c["path"] not in used: used.add(c["path"]); return c
    return None
def link(a):
    return {"driveName": a["name"], "drivePath": a["path"], "driveUrl": a["url"],
            "model": a.get("model") or "", "treat": a["treat"]}

def series(sub): return [a for t in by_treat.values() for a in t if sub.lower() in a["name"].lower()]
SER, s_seen = [], set()
for nm in ("Mehwish","Mehwaish","Nelum","Neelum","Nellum","Kurasa","Mahnoor","Rabia","Daniah",
           "Hafsa","Quratulain","Rabita","Ayra","Mufasira","Naba","Pashmina","Ayesha","Fateh"):
    for a in series(nm):
        if a["path"] not in s_seen: s_seen.add(a["path"]); SER.append(a)

MON = ["laser","hydra","peel","skintighten","viva","fatfreeze","prp","dermapen",
       "laser","hydra","skintighten","peel","viva","darkcircle"]
MALE_WEEKS = {2, 5, 8, 11, 14}          # Monday goes male-directed on these weeks
TRAY_WEEKS = {5, 9, 13}                  # Wednesday becomes The Tray on these weeks
mon_i = uzl_i = uzq_i = eng_i = 0

for r in rows:
    p, wk = r["pillar"], r["week"]
    r["asset"] = None; r["frameSource"] = None; r["source"] = "DESIGN"; r["subPillar"] = ""

    if p == "Eight Seconds":
        if wk in MALE_WEEKS:
            a = take(male); r["subPillar"] = "The Men's Room"
        else:
            want = MON[mon_i % len(MON)]; mon_i += 1
            a = take([x for x in by_treat.get(want, []) if x not in male])
        if not a: a = take([x for t in by_treat.values() for x in t if x["treat"] not in ("engaging","event","other")])
        if a: r["asset"] = link(a); r["source"] = "DRIVE_EDIT"

    elif p == "The Honest Number":
        if wk in TRAY_WEEKS:
            r["subPillar"] = "The Tray"; r["source"] = "SHOOT_BROLL"
        elif uzl_i < len(uz_limits):
            a = uz_limits[uzl_i]; uzl_i += 1; used.add(a["path"])
            r["asset"] = link(a); r["source"] = "DRIVE_READY"
        else:
            r["source"] = "SHOOT_TALK"

    elif p == "Matched Frame":
        a = take(SER) or take([x for t in by_treat.values() for x in t])
        if a: r["asset"] = link(a); r["source"] = "DRIVE_EDIT"
        else: r["source"] = "SHOOT_BROLL"

    elif p == "Asked and Answered":
        if uzq_i < len(uz_questions):
            a = uz_questions[uzq_i]; uzq_i += 1; used.add(a["path"])
            r["asset"] = link(a); r["source"] = "DRIVE_READY"

    elif p == "The Room":                       # the engagement day
        if eng_i < len(watched):
            a = watched[eng_i]; eng_i += 1; used.add(a["path"])
            r["asset"] = link(a); r["source"] = "DRIVE_EDIT"
            r["watchedDesc"] = WATCHED[a["name"]]
        else:
            r["source"] = "SHOOT_ENGAGE"

# every DESIGN row pulls its stills from real Venus footage
frame_pool = [a for t in by_treat.values() for a in t] + [a for a in watched]
fi = 0
for r in rows:
    if r["source"] == "DESIGN":
        a = frame_pool[fi % len(frame_pool)]; fi += 1
        r["frameSource"] = link(a)

print("rows: %d, weeks %d" % (len(rows), rows[-1]["week"]))
print("pillar mix:", dict(collections.Counter(r["pillar"] for r in rows)))
print("source mix:", dict(collections.Counter(r["source"] for r in rows)))
print("engagement day posts:", sum(1 for r in rows if r["pillar"] == "The Room"),
      "of which existing footage:", sum(1 for r in rows if r["pillar"] == "The Room" and r["asset"]),
      "new shoots:", sum(1 for r in rows if r["pillar"] == "The Room" and not r["asset"]))
print("rows touching real footage:", sum(1 for r in rows if r["asset"] or r["frameSource"]), "of", len(rows))
print("Dr Uzair used: %d limits on Wednesday + %d questions on Friday = %d of %d"
      % (uzl_i, uzq_i, uzl_i + uzq_i, len(uz_faq)))

byw = collections.OrderedDict()
for r in rows: byw.setdefault(r["week"], []).append(r)
weeks = [{"week": w, "theme": rr[0]["theme"], "themeNote": rr[0]["themeNote"], "rows": rr} for w, rr in byw.items()]
json.dump({"weeks": weeks}, io.open(os.path.join(SCRATCH, "spine2.json"), "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)

compact = {"weeks": [{"week": w["week"], "theme": w["theme"], "themeNote": w["themeNote"],
  "rows": [{k: v for k, v in r.items() if k in
            ("id","date","dayFull","pillar","subPillar","creative","source","marker","watchedDesc")}
           | ({"asset": {"driveName": r["asset"]["driveName"], "treat": r["asset"]["treat"], "model": r["asset"]["model"]}} if r["asset"] else {})
           | ({"frameSource": r["frameSource"]["driveName"]} if r["frameSource"] else {})
           for r in w["rows"]]} for w in weeks]}
out = json.dumps(compact, ensure_ascii=False, separators=(",", ":"))
io.open(os.path.join(SCRATCH, "weeks_args2.json"), "w", encoding="utf-8").write(out)
print("\nargs bytes:", len(out))
