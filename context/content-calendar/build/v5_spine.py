# -*- coding: utf-8 -*-
"""v5: 8 weeks, 56 posts, Mon 28 Sep to Sun 22 Nov 2026.
Every post carries a specific creative concept. No Venus Glow and no facial footage.
"""
import json, io, os, re, collections, datetime as dt

SCRATCH = r"C:\Users\Masroor\AppData\Local\Temp\claude\C--Users-Masroor\85b36120-1bdd-41ac-9941-bda2b8c1a109\scratchpad"
pool = json.load(io.open(os.path.join(SCRATCH, "build_list_dur.json"), encoding="utf-8"))

# ---------------------------------------------------------------- assets
def base(n): return re.sub(r"_?subtitling", "", n, flags=re.I).replace(".mp4", "").strip().lower()
g, others = collections.defaultdict(list), []
for p in pool:
    if p["isUzair"]: g[base(p["name"])].append(p)
    else: others.append(p)
uz = []
for b, grp in g.items():
    grp.sort(key=lambda x: (0 if "subtitl" in x["name"].lower() else 1)); uz.append(grp[0])
SKIP = ("intro reel", "introfortv", "venus_music", "thank you being a part", "free consultation for story")
def qk(n): return re.sub(r"[^a-z]", "", re.sub(r"_?subtitling|\.mp4|opt\s*0?2|-", "", n, flags=re.I).lower())
seen, allfaq = set(), []
for p in sorted([x for x in uz if not any(s in x["name"].lower() for s in SKIP)], key=lambda x: x["name"].lower()):
    k = qk(p["name"])
    if k not in seen: seen.add(k); allfaq.append(p)
# the eight strongest treatment questions, in the order they run. Brand-fluff answers are dropped.
PICK = ["is laser removal painful", "does venus use fda approved", "is fat freezing is painful",
        "how many sessios are needed for fat freeing", "sideeffects of rf micro neddling",
        "doesrfhave minimal downtime", "what should yo avoid", "how is prp for hair loss performed"]
uz_faq = []
for want in PICK:
    for p in allfaq:
        if want in p["name"].lower().replace(".mp4", ""):
            uz_faq.append(p); break
print("curated Ask Venus questions: %d" % len(uz_faq))
for p in uz_faq: print("   ", p["name"])

# CLIENT RULE: no Venus Glow, no hydrafacial, no facial videos
BANNED = ("hydra", "facial", "glow")
treatment = [p for p in others
             if p["treat"] not in ("engaging", "event", "music", "hydra")
             and not any(b in p["name"].lower() for b in BANNED)]
D = lambda p: p.get("dur") or 0
LONG = sorted([p for p in treatment if D(p) >= 24], key=lambda x: -D(x))
print("treatment clips after removing Venus Glow and facials: %d (%d are 24s or longer)" % (len(treatment), len(LONG)))

WATCHED = {
 "Engaging content_02.mp4": ("Gloved hand against the yellow-lit wall. Words on each finger unfold one at a time: Treatment, YOU, NEED, VENUS, AESTHTIC, then the palm turns to show BOOK NOW.", "DEFECT: the glove reads AESTHTIC. Mask and relabel that finger, or crop it out."),
 "Engaging content_04.mp4": ("POV walk through reception, hand held forward, past the GET THE GLOW neon, ending on a purple brochure reading WE PUT ETHICS IN AESTHETICS.", "Clean, no text defects."),
 "Engaging content_05.mp4": ("Rotating cast in one treatment chair. A doctor in a white coat, then staff in black uniforms take turns sitting and posing while the group stands around.", "Clean."),
 "Engaging content_07.mp4": ("Paper aeroplane POV flying the length of the clinic, past HELLO BEAUTY, the brochure stand, GET THE GLOW and BEYOND SKIN BEYOND BEAUTY.", "Handheld and shaky, needs stabilising."),
 "Engaging content_11.mp4": ("A staff member holds up cards to camera: Thank You, then For Visitng, then the Venus logo card.", "DEFECT: the card reads For Visitng. Reprint the card and reshoot that one beat."),
 "Engaging content_12.mp4": ("Two staff in black uniforms and gloves talking across a consultation desk to a seated patient, shot over the patient's shoulder. No burned-in text.", "Clean. The patient is unidentifiable from behind."),
 "WHO'S YOUR DREAM PATENT.mp4": ("The whole team stands looking at their phones, then all look up and point at the lens.", "DEFECT: the burned-in text reads PATENT. It must read CLIENT. Re-type it completely."),
}
watched = [p for p in others if p["name"] in WATCHED]

# ---------------------------------------------------------------- the 56 concepts
MON = [
 ("The 20 minute timer", "A live timer burns in the corner counting the real session time while the footage plays sped up. People think laser takes an afternoon. The timer answers it without anyone speaking."),
 ("Split screen, session 1 against session 5", "The same area, two sessions, side by side in the same frame at the same speed. The difference plays out live rather than being claimed."),
 ("Sound on", "No music and no voiceover. The treatment narrated entirely by the sound of the machine, with the sounds labelled on screen as they happen."),
 ("The client's eyeline", "Camera propped exactly where her head rests, so the viewer sees the appointment from the chair. Ceiling, light, the practitioner leaning in."),
 ("The machine's eye view", "Camera mounted low looking up at the handpiece as it works. A view nobody has seen of a treatment everybody has seen."),
 ("Sixty times, then real time", "The whole session at 60x speed, then it drops to full real time for the single moment that actually matters, and holds there."),
 ("Three areas, three reactions", "Same client, three different zones, cut tight. The reaction changes and that is the honest information."),
 ("The checklist", "A real printed treatment card sits in frame and a gloved hand ticks each line off as the session progresses."),
]
TUE = [
 ("THE RECEIPT", "A supermarket style till receipt itemising what a year of shaving costs in hours, not rupees. Receipts are one of the most screenshotted formats on Instagram."),
 ("The bus timetable", "Hair growth cycles drawn as a departure board. Your hairs do not all arrive at once, which is exactly why one session cannot catch them all."),
 ("What your hairbrush is telling you", "A real hairbrush photographed flat and annotated with pointer lines, like a museum diagram."),
 ("The ingredient label", "A treatment presented as a nutrition label on the back of a packet. Serving size, what is in it, what it is not."),
 ("The season gauge", "A temperature dial graphic showing which treatments suit which month in Pakistan, and why winter is the right window."),
 ("Choose your fighter", "A video game character select screen, one treatment per tile, each with its stats."),
 ("The boarding pass", "A treatment course laid out as a flight itinerary. Departure, duration, layovers, arrival."),
 ("Cross section", "A clean anatomical cut through skin layers, with each treatment labelled at the exact depth it works."),
]
WED = [
 ("The DM", "Frame 1 is a mocked up Instagram DM sliding in with the question typed the way a real person types it, typing dots, then cut to the answer."),
 ("The search bar", "Frame 1 is a Google search box with the question being typed and autocomplete filling in underneath."),
 ("The sticky note", "Frame 1 is a yellow sticky note stuck on the side of the machine with the question written on it in biro."),
 ("The group chat", "Frame 1 is a group chat, one friend asking the question, three dots from the others, nobody knowing the answer."),
 ("The note across the desk", "Frame 1 is a handwritten note being slid across the consultation desk, shot from above."),
 ("The notification", "Frame 1 is a phone notification banner dropping down from the top of the screen carrying the question."),
 ("Written on the mirror", "Frame 1 is the question written by a finger in the steam on a bathroom mirror."),
 ("The comment", "Frame 1 is a real comment screenshot from one of your own posts, with the username blurred."),
]
THU = [
 ("THE RAZOR GRAVEYARD", "A glass jar at reception where clients drop their razor after finishing a course. A physical brand object that costs nothing and gives you content forever."),
 ("Same light, same angle", "Two frames shot in identical light, distance and posture, weeks apart. The discipline of the setup is the proof."),
 ("The cancelled appointments", "A wax appointment diary with the recurring bookings crossed out one by one across the months."),
 ("The last shave", "A client's final shave filmed like a small ceremony, slow and deliberate, then the razor goes in the jar."),
 ("The tape measure", "The same spot measured at week one and again weeks later, the tape held in the same position both times."),
 ("The hairbrush", "The same brush after the same number of strokes, before a PRP course and partway through it."),
 ("The clothes, not the body", "A jacket or kameez that sits differently now. The garment carries the story so nobody has to show skin."),
 ("The progress wall", "Polaroids pinned to a board in the clinic, dated in marker, filling up over a course."),
]
FRI = [
 ("Rating every hair removal method", "Two staff hold up threading string, wax strips, an epilator, hair removal cream and a razor, and score each one out of ten with a one line verdict."),
 ("Things clients say in the first five minutes", "Staff reenact the lines they hear at the start of every appointment, back to back, deadpan."),
 ("Myth or truth, rapid fire", "Two staff, a buzzer, ten seconds per myth. Fast cuts, real answers."),
 ("Guess the treatment from the sound", "A staff member is blindfolded and has to name the machine from its sound alone."),
 ("The receptionist's top five", "The five questions the front desk answers every single day, delivered completely deadpan straight to camera."),
 ("The debate", "Two staff argue for different treatments for the same concern. Viewers pick a side in the comments."),
 ("Shaadi season POV", "The group chat panic six weeks before a wedding, acted out by the team."),
 ("Explain your job to a five year old", "Staff try to describe what they do without using a single technical word."),
]
SAT = [
 ("The team points", None), ("The gloved hand reveal", None), ("The walk in", None),
 ("The chair swap", None), ("The paper aeroplane tour", None), ("Cards to camera", None),
 ("The consultation desk", None), ("The clinic at 9am", "Nobody there yet. Lights coming on, trays being set, the first kettle. Quiet and human."),
]
SUN = [
 ("THE SHAADI COUNTDOWN", "A December wall calendar with treatment start dates circled in real pen, like someone actually planned it. Built to be screenshotted and forwarded."),
 ("The departure board", "An airport departure board where each treatment is a flight with a boarding time, so starting late means you miss it."),
 ("The prescription pad", "A plan written out on a styled prescription pad, legible on purpose, one line per treatment."),
 ("The winter skin kit", "A flat lay graphic of what Lahore winter does to skin and what to keep on the shelf for it."),
 ("The consultation invite", "A boarding pass styled invitation to a free consultation, with a tear off stub."),
 ("The sessions map", "A treatment course drawn as a metro line, each station a session, the destination named."),
 ("The skin weather report", "A mock weather bulletin card for Lahore skin this week. Recurring, ownable and useful."),
 ("The glow passport", "A passport page styled card, one stamp per completed session, for the course you start now."),
]

START = dt.date(2026, 9, 28)
days = [START + dt.timedelta(days=i) for i in range(56)]
SLOT = {0: ("Treatment", "Treatment Film", "warm"), 1: ("Educational", "Skin School", "useful"),
        2: ("Educational", "Ask Venus", "useful"), 3: ("Treatment", "The Results", "warm"),
        4: ("Engaging", "Real Talk", "playful"), 5: ("Engaging", "The Team", "playful"),
        6: ("Conversion", "Your Glow Plan", "warm")}
CONCEPTS = {0: MON, 1: TUE, 2: WED, 3: THU, 4: FRI, 5: SAT, 6: SUN}
MARKERS = {dt.date(2026, 11, 8): "Diwali, public holiday",
           dt.date(2026, 11, 9): "Iqbal Day, public holiday"}

used = set()
def take(lst):
    for c in lst:
        if c["path"] not in used: used.add(c["path"]); return c
    return None
def link(a):
    return {"driveName": a["name"], "drivePath": a["path"], "driveUrl": a["url"],
            "model": a.get("model") or "", "treat": a["treat"], "dur": round(D(a), 1)}

rows, uzi, engi = [], 0, 0
for i, d in enumerate(days):
    wd, wk = d.weekday(), i // 7 + 1
    bucket, fmt, voice = SLOT[wd]
    name, note = CONCEPTS[wd][wk - 1]
    r = {"id": i + 1, "date": d.isoformat(), "dayFull": d.strftime("%A"), "week": wk,
         "bucket": bucket, "format": fmt, "voice": voice,
         "concept": name, "conceptNote": note or "",
         "creative": "Carousel" if wd in (1, 6) else "Reel",
         "marker": MARKERS.get(d, ""), "asset": None, "source": "DESIGN"}

    if wd == 0:                                   # Monday treatment film
        a = take(LONG) or take(treatment)
        if a: r["asset"] = link(a); r["source"] = "DRIVE_EDIT"
    elif wd == 2:                                 # Ask Venus
        if uzi < len(uz_faq):
            a = uz_faq[uzi]; uzi += 1; used.add(a["path"]); r["asset"] = link(a); r["source"] = "DRIVE_READY"
    elif wd == 3:                                 # Results, props need shooting
        if name in ("Same light, same angle", "The tape measure", "The clothes, not the body"):
            a = take(LONG) or take(treatment)
            if a: r["asset"] = link(a); r["source"] = "DRIVE_EDIT"
        else:
            r["source"] = "SHOOT_PROP"
    elif wd == 4:
        r["source"] = "SHOOT_ENGAGE"
    elif wd == 5:
        if engi < len(watched):
            a = watched[engi]; engi += 1; used.add(a["path"])
            r["asset"] = link(a); r["source"] = "DRIVE_EDIT"
            r["watchedDesc"], r["defect"] = WATCHED[a["name"]]
        else:
            r["source"] = "SHOOT_ENGAGE"
    rows.append(r)

# design rows pull their stills from real Venus footage
frames = [a for a in treatment]
fi = 0
for r in rows:
    if r["source"] == "DESIGN":
        a = frames[fi % len(frames)]; fi += 1
        r["frameSource"] = {"driveName": a["name"], "driveUrl": a["url"], "dur": round(D(a), 1)}

print("rows %d, weeks %d" % (len(rows), rows[-1]["week"]))
print("buckets:", dict(collections.Counter(r["bucket"] for r in rows)))
print("sources:", dict(collections.Counter(r["source"] for r in rows)))
print("formats:", dict(collections.Counter(r["creative"] for r in rows)))
print("with real footage:", sum(1 for r in rows if r["asset"] or r.get("frameSource")), "of", len(rows))
print("hydra or facial assets used:", sum(1 for r in rows if r["asset"] and
      any(b in r["asset"]["driveName"].lower() for b in ("hydra", "facial", "glow"))))

byw = collections.OrderedDict()
for r in rows: byw.setdefault(r["week"], []).append(r)
weeks = [{"week": w, "rows": rr} for w, rr in byw.items()]
json.dump({"weeks": weeks}, io.open(os.path.join(SCRATCH, "spine5.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)

KEEP = ("id","date","dayFull","bucket","format","voice","concept","conceptNote","creative",
        "marker","source","watchedDesc","defect")
compact = {"weeks": [{"week": w["week"], "rows": [
    {k: v for k, v in r.items() if k in KEEP and v}
    | ({"asset": {"driveName": r["asset"]["driveName"], "treat": r["asset"]["treat"],
                  "model": r["asset"]["model"], "dur": r["asset"]["dur"]}} if r["asset"] else {})
    | ({"frameSource": r["frameSource"]["driveName"]} if r.get("frameSource") else {})
    for r in w["rows"]]} for w in weeks]}
out = json.dumps(compact, ensure_ascii=False, separators=(",", ":"))
io.open(os.path.join(SCRATCH, "weeks5.json"), "w", encoding="utf-8").write(out)
print("args bytes:", len(out))
