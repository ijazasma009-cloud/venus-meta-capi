# -*- coding: utf-8 -*-
"""Targeted caption repairs after the compliance pass and my own validation.

Five captions were disproportionate to their video length and are rewritten here.
One claim was overstated against the fact whitelist and is corrected everywhere it appears.
"""
import json, io, os, re

SCRATCH = r"C:\Users\Masroor\AppData\Local\Temp\claude\C--Users-Masroor\85b36120-1bdd-41ac-9941-bda2b8c1a109\scratchpad"
W = os.path.join(SCRATCH, "written.json")
written = json.load(io.open(W, encoding="utf-8"))
byid = {int(p["id"]): p for w in written["weeks"] for p in w["posts"]}

TAIL = {
 26: "\n\nVenus Aesthetics, 8 branches in Lahore, Karachi, Islamabad, Faisalabad and Gujranwala. Monday to Saturday, 11am to 8pm.\nCall or WhatsApp on the number in bio.",
 34: "\n\nVenus Aesthetics, MM Alam Road Lahore. Monday to Saturday, 11am to 8pm.\nCall or WhatsApp on the number in bio.",
 59: "\n\nVenus Aesthetics, F-7 Islamabad. Monday to Saturday, 11am to 8pm.\nCall or WhatsApp on the number in bio.",
 62: "\n\nVenus Aesthetics, Johar Town Lahore. Monday to Saturday, 11am to 8pm.\nCall or WhatsApp on the number in bio.",
 82: "\n\nVenus Aesthetics, Karachi. Monday to Saturday, 11am to 8pm.\nCall or WhatsApp on the number in bio.",
}

NEW_BODY = {
26: """Glowing skin is a maintenance plan, and Venus Glow is one line in it.

Skin answers in weeks. Hair answers in months, because it only responds in its growth phase.

One treatment does not hold a result on its own, whatever the day after looks like.
A plan holds it, because the interval is chosen rather than left to whenever you are free.

What we will not pick in a caption is your interval. That comes out of the consultation.

Which question should we take on next Friday?""",

34: """Everyone comes in for one room. A Venus Glow chair, then straight back out.

Eight branches since 2018, and most people only ever see one room in one of them.
This is the rest of it, at the altitude of a paper plane.

A flight is not a consultation and it tells you nothing clinical.
It tells you what the place looks like before you walk in.

What it skips is your own session range. That comes off a patch test at 48 hours.

Which branch should the next flight be filmed in?""",

59: """PRP for hair comes with a tray you can inspect and a number we will not promise.

Every needle, syringe and tube in this take is opened on camera. Single use means single use.
The Punjab Healthcare Commission sealed 1,415 centres, 1,153 of them operating illegally.

We will not tell you how many hairs come back, because nobody can promise that.
What you get is a straight answer on whether you are a candidate, including when that answer is no.

What is not on the tray is the preparation protocol and the spin settings. Those we show you in the room.

What would you want opened in front of you first?""",

62: """PRP for hair starts with an examination, not with a brush waved at a colleague.

A Korean cohort of 5,591,500 adults found more new androgenetic alopecia with higher particulate exposure, even at moderate air quality.

Nothing we do undoes what the air does, and we will not imply otherwise.
An examination separates out the part of your hair fall that has another explanation.

Who is a candidate is not a caption answer. That comes after the examination.

Send this to the person in your group who blames the air for everything.""",

82: """The honest answer on how laser hair reduction feels, sensation by sensation.

Fitzpatrick IV and V are common in Pakistan, and the long pulsed 1064 nm Nd:YAG competes least with epidermal melanin.
Sessions sit four to six weeks apart, so this is a sensation you will meet more than once.

Nobody can promise you feel nothing, and different areas report differently.
What we can do is tell you which sensation to expect where.

What we will not put in a caption is your own tolerance. The patch test is read at 48 hours.

Which is closer to what you imagined, a warm snap or a pinch?""",
}

for pid, body in NEW_BODY.items():
    p = byid[pid]
    old = p["caption"]
    tags = re.search(r"(#\w+(?:\s+#\w+)*)\s*$", old.split("[")[0].strip())
    kw = re.search(r"(\[[^\]]*\])", old)
    p["caption"] = body + TAIL[pid] + ("\n\n" + tags.group(1) if tags else "") + ("\n" + kw.group(1) if kw else "")
    print("id=%-3s rewritten, %d -> %d chars" % (pid, len(old), len(p["caption"])))

# the whitelist says Fitzpatrick IV to V are COMMON in Pakistan, not that they are the majority
n = 0
for p in byid.values():
    for f in ("caption", "hook", "spec", "cta", "script", "recordGuide", "editNote"):
        if not p.get(f): continue
        new = re.sub(r"Most Pakistani skin is Fitzpatrick IV or V",
                     "Fitzpatrick IV and V are common in Pakistan", p[f])
        new = re.sub(r"most Pakistani skin is Fitzpatrick IV or V",
                     "Fitzpatrick IV and V are common in Pakistan", new)
        if new != p[f]: p[f] = new; n += 1
print("overstated Fitzpatrick claim corrected in %d fields" % n)

json.dump(written, io.open(W, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("written.json updated")
