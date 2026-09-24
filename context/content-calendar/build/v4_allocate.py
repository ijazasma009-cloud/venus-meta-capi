# -*- coding: utf-8 -*-
"""Allocate real Drive assets to the 95 slot rows. Deterministic, no asset used twice."""
import json, io, os, collections, re

SCRATCH = r"C:\Users\Masroor\AppData\Local\Temp\claude\C--Users-Masroor\85b36120-1bdd-41ac-9941-bda2b8c1a109\scratchpad"
S = json.load(io.open(os.path.join(SCRATCH, "spine.json"), encoding="utf-8"))
rows, uz_faq, by_treat, male = S["rows"], S["uzFaq"], S["byTreat"], S["male"]

used = set()
def take(cands):
    for c in cands:
        if c["path"] not in used:
            used.add(c["path"]); return c
    return None

def link(a):
    return {"driveName": a["name"], "drivePath": a["path"],
            "driveUrl": a["url"], "model": a.get("model") or "",
            "treat": a["treat"]}

# --- Thursday MATCHED FRAME wants the longitudinal series --------------------
def series(sub):
    return [a for t in by_treat.values() for a in t if sub.lower() in a["name"].lower()]
SERIES = (series("Mehwish") + series("Mehwaish") + series("Nelum") + series("Neelum")
          + series("Nellum") + series("Kurasa") + series("Mahnoor") + series("Rabia")
          + series("Daniah") + series("Hafsa") + series("Quratulain") + series("Rabita")
          + series("Ayra") + series("Mufasira") + series("Naba") + series("Pashmina"))
seen = set(); SERIES = [a for a in SERIES if not (a["path"] in seen or seen.add(a["path"]))]

# --- Monday EIGHT SECONDS rotates treatments ---------------------------------
MON_ORDER = ["laser", "hydra", "peel", "skintighten", "viva", "fatfreeze",
             "prp", "dermapen", "laser", "hydra", "skintighten", "peel", "viva", "laser"]

mon_i = thu_i = uz_i = male_i = eng_i = 0
engaging = by_treat.get("engaging", [])

for r in rows:
    p = r["pillar"]
    r["asset"] = None
    r["source"] = "DESIGN"

    if p == "Eight Seconds":
        want = MON_ORDER[mon_i % len(MON_ORDER)]; mon_i += 1
        a = take(by_treat.get(want, [])) or take([x for t in by_treat.values() for x in t
                                                  if x["treat"] not in ("engaging", "event", "other")])
        if a: r["asset"] = link(a); r["source"] = "DRIVE_EDIT"

    elif p == "Matched Frame":
        a = take(SERIES) or take([x for t in by_treat.values() for x in t])
        if a: r["asset"] = link(a); r["source"] = "DRIVE_EDIT"
        else: r["source"] = "SHOOT_BROLL"

    elif p == "Asked and Answered":
        if uz_i < len(uz_faq):
            a = uz_faq[uz_i]; uz_i += 1
            r["asset"] = link(a); r["source"] = "DRIVE_READY"

    elif p == "The Men's Room":
        a = take(male)
        if a: r["asset"] = link(a); r["source"] = "DRIVE_EDIT"
        else: r["source"] = "SHOOT_BROLL"

    elif p == "The Tray":
        r["source"] = "SHOOT_BROLL"

    elif p == "The Honest Number":
        # every third one gets an existing engaging clip as the carrier
        if eng_i < len(engaging) and r["week"] % 2 == 1:
            a = take(engaging)
            if a: r["asset"] = link(a); r["source"] = "DRIVE_EDIT"; eng_i += 1
            else: r["source"] = "SHOOT_TALK"
        else:
            r["source"] = "SHOOT_TALK"

    elif p in ("The Decision Table", "Branch Desk", "Biology Countdown", "Smog Diary"):
        r["source"] = "DESIGN"

print("allocated. source mix:", dict(collections.Counter(r["source"] for r in rows)))
print("rows with a real Drive link:", sum(1 for r in rows if r["asset"]))
print("assets consumed: %d" % len(used))

# leftovers for the team
allassets = [a for t in by_treat.values() for a in t] + uz_faq
left = [a for a in allassets if a["path"] not in used]
print("unused assets left in reserve: %d" % len(left))

json.dump({"rows": rows, "reserve": [link(a) for a in left]},
          io.open(os.path.join(SCRATCH, "allocated.json"), "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)

for r in rows[:14]:
    print("  %-2d %s %-10s %-20s %-12s %s" % (r["id"], r["date"], r["dayFull"][:9],
          r["pillar"], r["source"], (r["asset"] or {}).get("driveName", "")[:34]))
print("saved ->", os.path.join(SCRATCH, "allocated.json"))
