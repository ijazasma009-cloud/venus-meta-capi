# -*- coding: utf-8 -*-
"""Build the 95-day slot plan and allocate real Drive assets to each row."""
import json, io, os, datetime as dt, collections, re

ROOT = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026"
SCRATCH = r"C:\Users\Masroor\AppData\Local\Temp\claude\C--Users-Masroor\85b36120-1bdd-41ac-9941-bda2b8c1a109\scratchpad"

pool = json.load(io.open(os.path.join(SCRATCH, "build_list.json"), encoding="utf-8"))

# ---- drop duplicate Uzair pairs: keep the subtitled master -------------------
def base(n): return re.sub(r"_?subtitling", "", n, flags=re.I).replace(".mp4", "").strip().lower()
uz_by_base = collections.defaultdict(list)
others = []
for p in pool:
    if p["isUzair"]: uz_by_base[base(p["name"])].append(p)
    else: others.append(p)
uz = []
for b, group in uz_by_base.items():
    group.sort(key=lambda x: (0 if "subtitl" in x["name"].lower() else 1))
    uz.append(group[0])

# Uzair assets that are FAQ questions (exclude intro reels / music video)
SKIP_UZ = ("intro reel", "introfortv", "venus_music", "thank you being a part", "free consultation for story")
uz_faq = [p for p in uz if not any(s in p["name"].lower() for s in SKIP_UZ)]
# drop near-duplicate questions (Opt02 / trailing-dash variants of the same question)
def qkey(n):
    n = re.sub(r"_?subtitling|\.mp4|opt\s*0?2|-", "", n, flags=re.I)
    return re.sub(r"[^a-z]", "", n.lower())
seen_q, dedup = set(), []
for p in sorted(uz_faq, key=lambda x: x["name"].lower()):
    k = qkey(p["name"])
    if k in seen_q: continue
    seen_q.add(k); dedup.append(p)
uz_faq = dedup

print("unique Uzair assets: %d, of which FAQ questions: %d" % (len(uz), len(uz_faq)))

by_treat = collections.defaultdict(list)
for p in others: by_treat[p["treat"]].append(p)
for k in by_treat: by_treat[k].sort(key=lambda x: x["name"])
print("non-Uzair by treatment:", {k: len(v) for k, v in sorted(by_treat.items())})

MALE_HINTS = ("malemodel", "kabeer", "assbeah", "male")
male_assets = [p for p in others if any(h in p["name"].lower() or h in (p.get("model") or "").lower() for h in MALE_HINTS)]
print("male-model assets: %d -> %s" % (len(male_assets), [p["name"] for p in male_assets]))

# ---- the 95 day spine -------------------------------------------------------
START = dt.date(2026, 9, 28)
END   = dt.date(2026, 12, 31)
days  = [START + dt.timedelta(days=i) for i in range((END - START).days + 1)]
assert len(days) == 95, len(days)

SLOTS = {
 0: ("Eight Seconds",      "Reel",     "reach"),
 1: ("The Decision Table", "Carousel", "saves"),
 2: ("The Honest Number",  "Reel",     "trust"),
 3: ("Matched Frame",      "Carousel", "proof"),
 4: ("Asked and Answered", "Reel",     "authority"),
 5: ("Trust and Utility",  "Reel",     "local"),
 6: ("The Forward",        "Carousel", "sends"),
}

# Pakistani Q4 2026 fixed points (verified in research)
MARKERS = {
 dt.date(2026,11,8):  "Diwali, public holiday",
 dt.date(2026,11,9):  "Iqbal Day, public holiday (reconfirm with Cabinet Division in late Oct)",
 dt.date(2026,12,25): "Quaid-e-Azam Day and Christmas, public holiday",
 dt.date(2026,12,26): "Holiday for Christians only",
}

def season(d):
    if d.month == 9 or (d.month == 10): return "OCTOBER, acquisition and course starts"
    if d.month == 11: return "NOVEMBER, the smog month"
    return "DECEMBER, the decision month"

# Saturday rotation: Tray / Branch Desk / The Men's Room
SAT_ROT = ["The Tray", "The Men's Room", "Branch Desk", "The Men's Room"]
# Sunday spine: Biology Countdown in Oct+Dec, Smog Diary in Nov
def sunday_pillar(d):
    return "Smog Diary" if d.month == 11 else "Biology Countdown"

rows = []
sat_i = 0
for i, d in enumerate(days):
    wd = d.weekday()
    pillar, fmt, goal = SLOTS[wd]
    if wd == 5:
        pillar = SAT_ROT[sat_i % len(SAT_ROT)]; sat_i += 1
        fmt = "Carousel" if pillar == "Branch Desk" else "Reel"
    if wd == 6:
        pillar = sunday_pillar(d)
    rows.append({
        "id": i + 1,
        "date": d.isoformat(),
        "dateLabel": d.strftime("%d %b %Y"),
        "dayFull": d.strftime("%A"),
        "week": (d - START).days // 7 + 1,
        "pillar": pillar,
        "creative": fmt,
        "goal": goal,
        "season": season(d),
        "marker": MARKERS.get(d, ""),
    })

print("\n95 rows, weeks 1..%d" % rows[-1]["week"])
print("pillar mix:", dict(collections.Counter(r["pillar"] for r in rows)))
print("format mix:", dict(collections.Counter(r["creative"] for r in rows)))

json.dump({"rows": rows,
           "uzFaq": uz_faq,
           "byTreat": {k: v for k, v in by_treat.items()},
           "male": male_assets},
          io.open(os.path.join(SCRATCH, "spine.json"), "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)
print("\nsaved spine ->", os.path.join(SCRATCH, "spine.json"))
