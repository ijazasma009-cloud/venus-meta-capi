# -*- coding: utf-8 -*-
"""v4.3 final spine.

What changed after the client's two notes
  1. REPETITION. Every pillar now rotates through named VARIANTS so its shape never repeats
     inside four weeks, on top of the 14 week themes. Fourteen weeks, no two alike.
  2. WASTED FOOTAGE. The library is 45.7 minutes across 95 clips with a median of 28.5 seconds.
     Cutting 8 seconds out of a 50 second film throws away the asset. Monday becomes THE FULL PASS,
     a 25 to 45 second treatment film that uses the whole arc, and every long clip is also banked
     for a second short cut and for carousel stills. One shoot, three uses.
"""
import json, io, os, re, collections, datetime as dt

SCRATCH = r"C:\Users\Masroor\AppData\Local\Temp\claude\C--Users-Masroor\85b36120-1bdd-41ac-9941-bda2b8c1a109\scratchpad"
pool = json.load(io.open(os.path.join(SCRATCH, "build_list_dur.json"), encoding="utf-8"))

def base(n): return re.sub(r"_?subtitling", "", n, flags=re.I).replace(".mp4", "").strip().lower()
groups, others = collections.defaultdict(list), []
for p in pool:
    if p["isUzair"]: groups[base(p["name"])].append(p)
    else: others.append(p)
uz = []
for b, g in groups.items():
    g.sort(key=lambda x: (0 if "subtitl" in x["name"].lower() else 1)); uz.append(g[0])

SKIP = ("intro reel", "introfortv", "venus_music", "thank you being a part", "free consultation for story")
def qkey(n): return re.sub(r"[^a-z]", "", re.sub(r"_?subtitling|\.mp4|opt\s*0?2|-", "", n, flags=re.I).lower())
seen, uz_faq = set(), []
for p in sorted([x for x in uz if not any(s in x["name"].lower() for s in SKIP)], key=lambda x: x["name"].lower()):
    k = qkey(p["name"])
    if k not in seen: seen.add(k); uz_faq.append(p)
LIMITS = ["sideeffects", "what should yo avoid", "is rf micro neddling af", "when do you see results",
          "will i see immediate", "is aftercare is imp", "what skin concern"]
uz_limits = [p for p in uz_faq if any(k in p["name"].lower() for k in LIMITS)]
uz_questions = [p for p in uz_faq if p not in uz_limits]

D = lambda p: p.get("dur") or 0
treatment = [p for p in others if p["treat"] not in ("engaging", "event", "music")]
LONG = sorted([p for p in treatment if D(p) >= 24], key=lambda x: -D(x))     # carry a full film
SHORT = sorted([p for p in treatment if D(p) < 24], key=lambda x: -D(x))
MALE = ("malemodel", "kabeer", "assbeah")
male_long = [p for p in LONG if any(h in p["name"].lower() for h in MALE)]

WATCHED = {
 "Engaging content_02.mp4": ("Gloved hand against the yellow-lit wall. Words on each finger unfold one at a time: Treatment, YOU, NEED, VENUS, AESTHTIC, then the palm turns to show BOOK NOW.", "DEFECT: the glove reads AESTHTIC, misspelled. Either reshoot the hand or mask and relabel that finger."),
 "Engaging content_04.mp4": ("POV walk through reception, hand held forward, past the GET THE GLOW neon, ending on a purple brochure reading WE PUT ETHICS IN AESTHETICS.", "Clean, no text defects."),
 "Engaging content_05.mp4": ("Rotating cast in one treatment chair. A doctor in a white coat, then staff in black uniforms take turns sitting and posing while the group stands around.", "Clean."),
 "Engaging content_07.mp4": ("Paper aeroplane POV flying the length of the clinic, past HELLO BEAUTY, the brochure stand, GET THE GLOW and BEYOND SKIN BEYOND BEAUTY.", "Handheld and shaky, needs stabilising."),
 "Engaging content_11.mp4": ("A staff member holds up cards to camera: Thank You, then For Visitng, then the Venus logo card.", "DEFECT: the card reads For Visitng, misspelled. Reprint the card and reshoot the middle beat, it is three seconds of work."),
 "Engaging content_12.mp4": ("Two staff in black uniforms and gloves talking across a consultation desk to a seated patient, shot over the patient's shoulder. No burned-in text.", "Clean. The patient is unidentifiable from behind, which is the point."),
 "WHO'S YOUR DREAM PATENT.mp4": ("The whole team stands looking at their phones, then all look up and point at the lens. Text asks who our dream patient is, answer YOU.", "DEFECT: the burned-in text reads PATENT, not PATIENT. The text must be re-rendered."),
 "have you heard the news.mp4": ("Gossip chain. One staff member gasps at her phone then whispers to the next, down a row of seated staff.", "ALREADY USED for the November 2025 sale announcement. Strip the old text and re-cut it to a non-sale reveal."),
 "Confidence.mp4": ("A woman walks through the clinic looking at her phone showing a contact called Bill Gates. The joke is post-treatment confidence.", "DEFECT: the line reads The Confidence you get when you done with Fat Frezze, broken English and misspelled twice. Re-render the text."),
 "location.mp4": ("Slow clean interior tour, no people, no text. Reception, MAKE YOUR SOUL SHINE wall, GET THE GLOW neon, waiting area, product shelves, corridor, YOU DESERVE TO SHINE arch.", "Clean and the best brand b-roll in the library. Do not add heavy text over it."),
}
watched = [p for p in others if p["name"] in WATCHED]

# -------------------------------------------------------------- variants, so nothing repeats
VARIANTS = {
 "The Full Pass": ["the whole pass, start to finish", "what it actually feels like, narrated on screen",
                   "the prep nobody films", "the settings on the screen", "the aftercare in the first hour",
                   "one area, one session, real time", "the handpiece changing over"],
 "The Decision Table": ["this or that, after six sessions", "the order to do them in",
                        "what it costs you in time, not money", "who it will not work on",
                        "what each one actually treats", "the three questions to ask any clinic",
                        "what changes if your skin is deeper"],
 "The Honest Number": ["the real session arithmetic", "three things worth knowing before you book",
                       "who we turn away and why", "what we will not promise",
                       "the thing that goes wrong when you rush it"],
 "Matched Frame": ["session 3 of 6, partial on purpose", "same light, same angle, months apart",
                   "the area nobody photographs", "progress with the spec block",
                   "what week two really looks like"],
 # The Room variants are set per row from the footage itself, see ROOM_VARIANT below
 "The Room": [],
 "Biology Countdown": ["a dated card for a December function", "the March bride's session map",
                       "what still fits in three weeks", "start now for next season",
                       "the Ramadan 2027 window"],
 "Smog Diary": ["this week's reading and one mechanism", "the barrier one", "the acne one",
                "the scalp and hair one", "the pigment one"],
 "Branch Desk": ["hours and the holiday note", "which branch for which treatment"],
 "Asked and Answered": ["the question as the whole first frame"],
}

START, END = dt.date(2026, 9, 28), dt.date(2026, 12, 31)
days = [START + dt.timedelta(days=i) for i in range((END - START).days + 1)]
THEMES = {1:"The season opens",2:"How many sessions, really",3:"Before the event",4:"Hair, honestly",
 5:"What is on the tray",6:"The air changes",7:"Barrier week",8:"The laser window opens",
 9:"Scalp and fall",10:"Choosing a clinic",11:"Wavelength week",12:"The December bride",
 13:"Quiet days",14:"What next year needs"}
NOTE = {1:"Wedding season opens in October and a course started now finishes in time. Set the arithmetic up.",
 2:"The published average is close to nine sessions, not three. Spend the week on honest numbers.",
 3:"Peels and glow timed to a function, and what genuinely fits inside three weeks.",
 4:"Seasonal shedding is easing rather than peaking. Say so, then separate it from real hair loss.",
 5:"Sterility, provenance and paperwork, in a market where the regulator is sealing clinics weekly.",
 6:"November opens. The Sunday slot becomes the smog card and holds for five weeks.",
 7:"Two public holidays back to back. Lead with hours and utility, then barrier science.",
 8:"UV drops to an average daily maximum of 4. The clinically correct season to start laser.",
 9:"Pollution and hair loss evidence, handled carefully, with a countermeasure in every post.",
 10:"December is when the researching patient finally picks. Shift from acquisition to comparison.",
 11:"Wavelength is the one variable most competitors running IPL cannot match. Move the talk off price.",
 12:"Be honest about what no longer fits before a December function and what still moves in three weeks.",
 13:"Quaid-e-Azam Day and Christmas. Hours, aftercare, low effort, high utility.",
 14:"Four days. Year end, January course planning, and the Ramadan 2027 window."}
SLOTS = {0:("The Full Pass","Reel"),1:("The Decision Table","Carousel"),2:("The Honest Number","Reel"),
         3:("Matched Frame","Carousel"),4:("Asked and Answered","Reel"),5:("The Room","Reel"),
         6:("The Forward","Carousel")}
MARKERS = {dt.date(2026,11,8):"Diwali, public holiday",
           dt.date(2026,11,9):"Iqbal Day, public holiday. Reconfirm with the Cabinet Division in late October.",
           dt.date(2026,12,25):"Quaid-e-Azam Day and Christmas, public holiday",
           dt.date(2026,12,26):"Holiday for Christians only"}
BREAKS = {dt.date(2026,11,9):("Branch Desk","Carousel"), dt.date(2026,12,24):("Branch Desk","Carousel")}

rows = []
for i, d in enumerate(days):
    wd = d.weekday(); pillar, fmt = SLOTS[wd]
    if wd == 6: pillar = "Smog Diary" if d.month == 11 else "Biology Countdown"
    if d in BREAKS: pillar, fmt = BREAKS[d]
    wk = (d - START).days // 7 + 1
    rows.append({"id": i+1, "date": d.isoformat(), "dayFull": d.strftime("%A"), "week": wk,
                 "theme": THEMES[wk], "themeNote": NOTE[wk], "pillar": pillar, "creative": fmt,
                 "marker": MARKERS.get(d, "")})

vc = collections.Counter()
for r in rows:
    v = VARIANTS.get(r["pillar"])
    if v:
        r["variant"] = v[vc[r["pillar"]] % len(v)]; vc[r["pillar"]] += 1

# The Room: the first seven match the footage that exists, the last six are new formats to shoot
ROOM_FROM_FOOTAGE = {
 "WHO'S YOUR DREAM PATENT.mp4": "the whole team points at the lens",
 "Engaging content_02.mp4": "the gloved hand reveal, one word per finger",
 "Engaging content_04.mp4": "the walk in, POV from the front door",
 "Engaging content_05.mp4": "the chair swap, the whole team takes a turn",
 "Engaging content_07.mp4": "the paper aeroplane tour of the clinic",
 "Engaging content_11.mp4": "cards held to camera, no words spoken",
 "Engaging content_12.mp4": "what actually happens at the consultation desk",
}
ROOM_TO_SHOOT = [
 "a deadpan one liner in the treatment room, one staff member, no cuts",
 "two staff, one trending sound, the treatment as the punchline",
 "the thing patients always say at the front desk",
 "a failed attempt, kept in, because the fail is the joke",
 "the clinic at 9am before anyone arrives",
 "the gossip chain, re-cut around a real announcement",
]

# -------------------------------------------------------------- allocation
used = set()
def take(lst):
    for c in lst:
        if c["path"] not in used: used.add(c["path"]); return c
    return None
def link(a):
    return {"driveName": a["name"], "drivePath": a["path"], "driveUrl": a["url"],
            "model": a.get("model") or "", "treat": a["treat"], "dur": a.get("dur")}

def series(sub): return [a for a in treatment if sub.lower() in a["name"].lower()]
SER, s_seen = [], set()
for nm in ("Mehwish","Mehwaish","Nelum","Neelum","Nellum","Kurasa","Mahnoor","Rabia","Daniah","Hafsa",
           "Quratulain","Rabita","Ayra","Mufasira","Naba","Pashmina","Ayesha","Fateh","Hala"):
    for a in series(nm):
        if a["path"] not in s_seen: s_seen.add(a["path"]); SER.append(a)

MALE_WEEKS, TRAY_WEEKS = {2,5,8,11,14}, {5,9,13}
uzl = uzq = eng = 0
for r in rows:
    p, wk = r["pillar"], r["week"]
    r["asset"] = None; r["frameSource"] = None; r["source"] = "DESIGN"; r["subPillar"] = ""

    if p == "The Full Pass":
        a = take(male_long) if wk in MALE_WEEKS else None
        if a: r["subPillar"] = "The Men's Room"
        if not a: a = take([x for x in LONG if x not in male_long]) or take(LONG) or take(SHORT)
        if a: r["asset"] = link(a); r["source"] = "DRIVE_EDIT"

    elif p == "The Honest Number":
        if wk in TRAY_WEEKS: r["subPillar"] = "The Tray"; r["source"] = "SHOOT_BROLL"
        elif uzl < len(uz_limits):
            a = uz_limits[uzl]; uzl += 1; used.add(a["path"]); r["asset"] = link(a); r["source"] = "DRIVE_READY"
        else: r["source"] = "SHOOT_TALK"

    elif p == "Matched Frame":
        a = take(SER) or take(treatment)
        if a: r["asset"] = link(a); r["source"] = "DRIVE_EDIT"
        else: r["source"] = "SHOOT_BROLL"

    elif p == "Asked and Answered":
        if uzq < len(uz_questions):
            a = uz_questions[uzq]; uzq += 1; used.add(a["path"]); r["asset"] = link(a); r["source"] = "DRIVE_READY"

    elif p == "The Room":
        if eng < len(watched):
            a = watched[eng]; eng += 1; used.add(a["path"])
            r["asset"] = link(a); r["source"] = "DRIVE_EDIT"
            r["watchedDesc"], r["defect"] = WATCHED[a["name"]]
            r["variant"] = ROOM_FROM_FOOTAGE.get(a["name"], "re-cut of existing clinic footage")
        else:
            r["source"] = "SHOOT_ENGAGE"
            r["variant"] = ROOM_TO_SHOOT[(eng - len(watched)) % len(ROOM_TO_SHOOT)]; eng += 1

frames = [a for a in treatment] + watched
fi = 0
for r in rows:
    if r["source"] == "DESIGN":
        a = frames[fi % len(frames)]; fi += 1; r["frameSource"] = link(a)

# second short cut banked from every long Monday film
for r in rows:
    if r["pillar"] == "The Full Pass" and r["asset"] and (r["asset"]["dur"] or 0) >= 24:
        r["bankSecondCut"] = True

print("rows %d, weeks %d" % (len(rows), rows[-1]["week"]))
print("pillars:", dict(collections.Counter(r["pillar"] for r in rows)))
print("sources:", dict(collections.Counter(r["source"] for r in rows)))
fp = [r for r in rows if r["pillar"] == "The Full Pass" and r["asset"]]
print("Full Pass films: %d, average source length %.1fs, shortest %.1fs, longest %.1fs"
      % (len(fp), sum(r["asset"]["dur"] or 0 for r in fp)/max(1,len(fp)),
         min(r["asset"]["dur"] or 0 for r in fp), max(r["asset"]["dur"] or 0 for r in fp)))
print("rows touching real footage: %d of %d" % (sum(1 for r in rows if r["asset"] or r["frameSource"]), len(rows)))
print("second cuts banked:", sum(1 for r in rows if r.get("bankSecondCut")))

byw = collections.OrderedDict()
for r in rows: byw.setdefault(r["week"], []).append(r)
weeks = [{"week": w, "theme": rr[0]["theme"], "themeNote": rr[0]["themeNote"], "rows": rr} for w, rr in byw.items()]
KEEP = ("id","date","dayFull","pillar","subPillar","variant","creative","source","marker",
        "watchedDesc","defect","bankSecondCut")
compact = {"weeks": [{"week": w["week"], "theme": w["theme"], "themeNote": w["themeNote"],
  "rows": [{k: v for k, v in r.items() if k in KEEP and v}
           | ({"asset": {"driveName": r["asset"]["driveName"], "treat": r["asset"]["treat"],
                         "model": r["asset"]["model"], "dur": r["asset"]["dur"]}} if r["asset"] else {})
           | ({"frameSource": r["frameSource"]["driveName"] + (" (%.0fs)" % r["frameSource"]["dur"] if r["frameSource"]["dur"] else "")} if r["frameSource"] else {})
           for r in w["rows"]]} for w in weeks]}
json.dump({"weeks": weeks}, io.open(os.path.join(SCRATCH, "spine3.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
out = json.dumps(compact, ensure_ascii=False, separators=(",", ":"))
io.open(os.path.join(SCRATCH, "weeks_args3.json"), "w", encoding="utf-8").write(out)
print("args bytes:", len(out))
