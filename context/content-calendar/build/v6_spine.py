# -*- coding: utf-8 -*-
"""v6: 8 weeks, 56 posts, Mon 28 Sep to Sun 22 Nov 2026.
Every post is a named idea from the verified idea bank, matched to a service and a date.
Only 2 posts need staff on camera. Prop stills are batched into 3 afternoon sessions.
"""
import json, io, os, re, collections, datetime as dt

SCRATCH = r"C:\Users\Masroor\AppData\Local\Temp\claude\C--Users-Masroor\85b36120-1bdd-41ac-9941-bda2b8c1a109\scratchpad"
bank = {i["name"].strip().lower(): i for i in json.load(io.open(os.path.join(SCRATCH, "ideabank.json"), encoding="utf-8"))}
pool = json.load(io.open(os.path.join(SCRATCH, "build_list_dur.json"), encoding="utf-8"))

# ---- assets -----------------------------------------------------------------
def basename(n): return re.sub(r"_?subtitling", "", n, flags=re.I).replace(".mp4", "").strip().lower()
uzg, others = collections.defaultdict(list), []
for p in pool:
    (uzg[basename(p["name"])] if p["isUzair"] else others).append(p) if p["isUzair"] else others.append(p)
uz = [sorted(g, key=lambda x: (0 if "subtitl" in x["name"].lower() else 1))[0] for g in uzg.values()]
FAQ_ORDER = ["is laser removal painful", "is fat freezing is painful", "sideeffects of rf micro neddling",
             "how is prp for hair loss performed", "doesrfhave minimal downtime",
             "how many sessios are needed for fat freeing", "what should yo avoid", "does venus use fda approved"]
uz_faq = []
for want in FAQ_ORDER:
    for p in uz:
        if want in p["name"].lower(): uz_faq.append(p); break

BAN = ("hydra", "facial", "glow", "peel")            # client bans, peels included
byname = {p["name"]: p for p in others}
def clip(n): return byname.get(n)

# engaging clips confirmed unposted in the client's own sheet
ENG_OK = ["Engaging content_04.mp4", "Engaging content_05.mp4", "Engaging content_07.mp4",
          "Engaging content_11.mp4", "Engaging content_12.mp4"]

# ---- the 56, curated by hand from the bank ----------------------------------
# (idea name, service, bucket, format, source kind, asset or None)
P = [
 # WEEK 1  the season opens
 ("Treatment Film", "Laser Hair Reduction", "Treatment", "Reel",   "DRIVE_EDIT", "Mehwaish Laser.mp4"),
 ("THE RAZOR IS CALLING", "Laser Hair Reduction", "Educational", "Single graphic", "DESIGN", None),
 ("ASK VENUS", "Laser Hair Reduction", "Educational", "Reel", "DRIVE_READY", None),
 ("SHAVE THE CACTUS", "Laser Hair Reduction", "Treatment", "Reel", "PROPS", None),
 ("THE RAZOR JAR", "Laser Hair Reduction", "Engaging", "Single graphic", "PROPS", None),
 ("FOUR STAMPS, ONE YEAR", "K-Glow Boosters", "Conversion", "Single graphic", "PROPS", None),
 ("ONE FREE TUESDAY", "Multi service", "Conversion", "Single graphic", "DESIGN", None),
 # WEEK 2  how many sessions
 ("Treatment Film", "Skin Tightening", "Treatment", "Reel", "DRIVE_EDIT", "Rabita_SkinTightning_02.mp4"),
 ("SIX LITTLE CACTI", "Laser Hair Reduction", "Educational", "Single graphic", "PROPS", None),
 ("ASK VENUS", "Fat Freezing", "Educational", "Reel", "DRIVE_READY", None),
 ("THE HOLE THAT WAS NEVER USED", "Fat Freezing", "Treatment", "Single graphic", "PROPS", None),
 ("LEFT ON READ", "Laser Hair Reduction", "Engaging", "Single graphic", "DESIGN", None),
 ("TWO KIWIS", "Men, Laser", "Engaging", "Single graphic", "PROPS", None),
 ("THE CARD THAT IS ABOUT YOU", "K-Glow Boosters", "Conversion", "Single graphic", "PROPS", None),
 # WEEK 3  before the event
 ("Treatment Film", "Laser Hair Reduction", "Treatment", "Reel", "DRIVE_EDIT", "Kabeer_Laser.mp4"),
 ("THE TICK MATRIX", "Multi service", "Educational", "Single graphic", "DESIGN", None),
 ("ASK VENUS", "RF Microneedling", "Educational", "Reel", "DRIVE_READY", None),
 ("SURFACE OR ROOT", "Laser Hair Reduction", "Treatment", "Reel", "PROPS", None),
 ("MAYOUN THAAL, ONE EXTRA ITEM", "Laser Hair Reduction", "Engaging", "Single graphic", "PROPS", None),
 ("ONE GRAPE, ONE RAISIN", "K-Glow Boosters", "Treatment", "Single graphic", "PROPS", None),
 ("THE COUSIN WHO ZOOMS IN", "Multi service", "Conversion", "Single graphic", "PROPS", None),
 # WEEK 4  hair, honestly
 ("Treatment Film", "PRP", "Treatment", "Reel", "DRIVE_EDIT", "Kabeer_PRP.mp4"),
 ("MOVE THE LAMP", "Dark Circles", "Educational", "Reel", "PROPS", None),
 ("ASK VENUS", "PRP", "Educational", "Reel", "DRIVE_READY", None),
 ("TURF", "Men, PRP", "Treatment", "Carousel", "PROPS", None),
 ("THE WALK IN", "Brand", "Engaging", "Reel", "DRIVE_EDIT", "Engaging content_04.mp4"),
 ("THE K-GLOW MENU", "K-Glow Boosters", "Conversion", "Carousel", "PROPS", None),
 ("DECEMBERISTAN RAIL", "Multi service", "Conversion", "Single graphic", "PROPS", None),
 # WEEK 5  what the machine actually does
 ("Treatment Film", "Fat Freezing", "Treatment", "Reel", "DRIVE_EDIT", "Maliha Fat Freeze.mp4"),
 ("TWO ICE TRAYS", "Fat Freezing", "Educational", "Reel", "PROPS", None),
 ("ASK VENUS", "RF Microneedling", "Educational", "Reel", "DRIVE_READY", None),
 ("THE SCALE THAT DID NOT MOVE", "Fat Freezing", "Treatment", "Carousel", "PROPS", None),
 ("THE CHAIR SWAP", "Brand", "Engaging", "Reel", "DRIVE_EDIT", "Engaging content_05.mp4"),
 ("THE PANE TEST", "K-Glow Boosters", "Treatment", "Single graphic", "PROPS", None),
 ("STILL IN USE IN 2030", "Laser Hair Reduction", "Conversion", "Single graphic", "PROPS", None),
 # WEEK 6  the air changes
 ("Treatment Film", "Venus Viva Resurfacing", "Treatment", "Reel", "DRIVE_EDIT", "Hala_Viva.mp4"),
 ("THE CABIN FILTER", "RF Microneedling", "Educational", "Single graphic", "PROPS", None),
 ("ASK VENUS", "Fat Freezing", "Educational", "Reel", "DRIVE_READY", None),
 ("ONE CLEAN STRIPE", "Dark Circles", "Treatment", "Reel", "PROPS", None),
 ("THE PAPER AEROPLANE TOUR", "Brand", "Engaging", "Reel", "DRIVE_EDIT", "Engaging content_07.mp4"),
 ("WINDSCREEN SEASON", "K-Glow Boosters", "Treatment", "Reel", "SHOOT", None),
 ("THE SUN KEEPS A RECORD", "Dark Circles", "Conversion", "Carousel", "PROPS", None),
 # WEEK 7  barrier week, two holidays
 ("Treatment Film", "Skin Tightening", "Treatment", "Reel", "DRIVE_EDIT", "Daniah Belly tightning (1).mp4"),
 ("TWO WAISTBANDS", "Skin Tightening", "Educational", "Single graphic", "PROPS", None),
 ("ASK VENUS", "Laser Hair Reduction", "Educational", "Reel", "DRIVE_READY", None),
 ("JAWLINE, JOWL", "Skin Tightening", "Treatment", "Carousel", "PROPS", None),
 ("CARDS TO CAMERA", "Brand", "Engaging", "Reel", "DRIVE_EDIT", "Engaging content_11.mp4"),
 ("NECK LINE", "Men, Laser", "Engaging", "Reel", "SHOOT", None),
 ("TWO CUPS, ONE STAIN", "Dark Circles", "Conversion", "Carousel", "PROPS", None),
 # WEEK 8  choosing a clinic
 ("Treatment Film", "Laser Hair Reduction", "Treatment", "Reel", "DRIVE_EDIT", "MaleModel_Laser.mp4"),
 ("THE GRIT CARD", "RF Microneedling", "Educational", "Single graphic", "PROPS", None),
 ("ASK VENUS", "Multi service", "Educational", "Reel", "DRIVE_READY", None),
 ("THE WALL PATCH", "RF Microneedling", "Treatment", "Reel", "PROPS", None),
 ("THE CONSULTATION DESK", "Brand", "Engaging", "Reel", "DRIVE_EDIT", "Engaging content_12.mp4"),
 ("FIND THE FOUR", "K-Glow Boosters", "Engaging", "Single graphic", "PROPS", None),
 ("THE RAZOR GRAVEYARD", "Multi service", "Conversion", "Single graphic", "PROPS", None),
]
assert len(P) == 56, len(P)

START = dt.date(2026, 9, 28)
SRC_LABEL = {"DRIVE_EDIT": "Edit existing footage", "DRIVE_READY": "Ready to post",
             "PROPS": "Prop still, batch session", "DESIGN": "Design only", "SHOOT": "Staff shoot"}
MARK = {dt.date(2026,11,8): "Diwali, public holiday", dt.date(2026,11,9): "Iqbal Day, public holiday"}
THEME = ["The season opens", "How many sessions", "Before the event", "Hair, honestly",
         "What the machine actually does", "The air changes", "Barrier week", "Choosing a clinic"]
DAYSLOT = ["Treatment Film", "Skin School", "Ask Venus", "The Proof", "Real Talk", "New at Venus", "The Forward"]

rows, faq_i, missing = [], 0, []
for n, (idea, service, bucket, fmt, src, asset) in enumerate(P):
    d = START + dt.timedelta(days=n)
    wk = n // 7 + 1
    r = {"id": n + 1, "date": d.isoformat(), "dayFull": d.strftime("%A"), "week": wk,
         "theme": THEME[wk - 1], "slot": DAYSLOT[d.weekday()], "bucket": bucket,
         "service": service, "creative": fmt, "source": src, "sourceLabel": SRC_LABEL[src],
         "idea": idea, "marker": MARK.get(d, ""), "asset": None, "ideaSpec": None}
    if src == "DRIVE_READY":
        a = uz_faq[faq_i % len(uz_faq)]; faq_i += 1
        r["asset"] = {"driveName": a["name"], "driveUrl": a["url"], "dur": round(a.get("dur") or 0, 1),
                      "drivePath": a["path"]}
        r["idea"] = "Ask Venus, " + re.sub(r"[_-]?[Ss]ubtitling|\.mp4", "", a["name"]).strip()
    elif asset:
        a = clip(asset)
        if not a: missing.append(asset)
        else: r["asset"] = {"driveName": a["name"], "driveUrl": a["url"],
                            "dur": round(a.get("dur") or 0, 1), "drivePath": a["path"]}
    if src in ("PROPS", "DESIGN"):
        b = bank.get(idea.strip().lower())
        if b: r["ideaSpec"] = {"whatYouSee": b["whatYouSee"], "whyItWorks": b["whyItWorks"],
                               "props": b.get("props", ""), "sourceUrl": b["sourceUrl"], "bankFormat": b["format"]}
        else: missing.append("IDEA: " + idea)
    rows.append(r)

if missing: print("!! MISSING:", missing)
print("rows %d, weeks %d" % (len(rows), rows[-1]["week"]))
print("buckets:", dict(collections.Counter(r["bucket"] for r in rows)))
print("sources:", dict(collections.Counter(r["sourceLabel"] for r in rows)))
print("formats:", dict(collections.Counter(r["creative"] for r in rows)))
print("services:", dict(collections.Counter(r["service"] for r in rows)))
print("STAFF SHOOTS:", sum(1 for r in rows if r["source"] == "SHOOT"))
print("banned words in any service/idea:",
      [r["idea"] for r in rows if any(b in (r["idea"] + r["service"]).lower() for b in BAN) and "K-Glow" not in r["service"]])

byw = collections.OrderedDict()
for r in rows: byw.setdefault(r["week"], []).append(r)
json.dump({"weeks": [{"week": w, "theme": rr[0]["theme"], "rows": rr} for w, rr in byw.items()]},
          io.open(os.path.join(SCRATCH, "spine6.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("\nsaved spine6.json")
