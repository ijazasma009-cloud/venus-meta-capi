# -*- coding: utf-8 -*-
"""Independent hard-rule check on the finished calendar. Does not trust the writing agents."""
import json, io, os, re, sys, collections, datetime as dt

CAL = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app\data\calendar.json"
d = json.load(io.open(CAL, encoding="utf-8"))
items = d["items"]
fail = []
def bad(i, rule, detail):
    fail.append((i["id"], i["date"], rule, detail[:140]))

# text fields that face the public
def public_text(i):
    return " \n".join([i["hook"], i["caption"], i["cta"], i["hashtags"], i["keywordBlock"]])
def all_text(i):
    return public_text(i) + " \n" + i["spec"] + " \n" + i["script"] + " \n" + i["recordGuide"] + " \n" + i["editNote"]

# 1. dates: complete, no gaps, no dupes
dates = [dt.date.fromisoformat(i["date"]) for i in items]
assert dates == sorted(dates), "dates out of order"
start, end = dates[0], dates[-1]
span = (end - start).days + 1
if span != len(dates): fail.append(("-", "-", "DATE SPAN", "%d days but %d posts" % (span, len(dates))))
if len(set(dates)) != len(dates): fail.append(("-", "-", "DUPLICATE DATES", "found"))
if start != dt.date(2026, 9, 28): fail.append(("-", "-", "START DATE", str(start)))
if end != dt.date(2026, 12, 31): fail.append(("-", "-", "END DATE", str(end)))

# 2. Roman Urdu
ROMAN = re.compile(r"\b(ka|ki|ke|hai|hain|nahi|nahin|aap|tum|mera|meri|apna|apni|kya|kyun|"
                   r"bilkul|zaroor|acha|accha|theek|abhi|phir|wala|wali|yaar|bohot|bahut|"
                   r"jaldi|dekho|suno|chalo|banao|karo|karein|hogaya|hojaye|"
                   r"sirf|gaana|glow ka|ap ki|ap ka)\b", re.I)
# 3. em dash / en dash
DASH = re.compile(r"[\u2013\u2014]")
# 4. banned words
BANNED = ["permanent", "painless", "guaranteed", "flawless", "miracle",
          "best version of yourself", "say goodbye to", "number one", "100% safe",
          "completely safe", "risk free", "risk-free"]
BANNED_SOFT = ["magic"]
# 5. discounts
DISCOUNT = re.compile(r"\b(\d+\s*%\s*off|% off|discount|sale|offer ends|limited time|"
                      r"flat \d|save \d|bundle|was rs|now rs|coupon|promo)\b", re.I)
# 6. drug brand names
DRUGS = re.compile(r"\b(botox|botulinum|dysport|xeomin|azzalure|bo-tox|botulin)\b", re.I)
# 7. engagement bait
BAIT = re.compile(r"(comment\s+[\"']?(yes|done|me|guide|plan|consult)[\"']?\b|tag\s+(a\s+friend|someone)|"
                  r"double\s+tap|share\s+if\s+you|like\s+if\s+you)", re.I)
# 8. price
PRICE = re.compile(r"\b(rs\.?\s?\d|pkr\s?\d|rupees\s?\d|₨)", re.I)

for i in items:
    pub, everything = public_text(i), all_text(i)

    m = ROMAN.search(pub)
    if m: bad(i, "ROMAN URDU", m.group(0) + " :: " + pub[max(0, m.start()-40):m.start()+40])

    m = DASH.search(everything)
    if m: bad(i, "EM/EN DASH", everything[max(0, m.start()-50):m.start()+50])

    low = pub.lower()
    for b in BANNED:
        if b in low: bad(i, "BANNED WORD", b)
    for b in BANNED_SOFT:
        if re.search(r"\b" + b + r"\b", low): bad(i, "BANNED WORD", b)

    # "hair removal" allowed ONLY inside the bracketed keyword block
    stripped = re.sub(r"\[[^\]]*\]", "", pub, flags=re.S).lower()
    if "hair removal" in stripped: bad(i, "HAIR REMOVAL AS CLAIM", "use 'hair reduction'")

    m = DISCOUNT.search(pub)
    if m: bad(i, "DISCOUNT", m.group(0))
    m = DRUGS.search(pub)
    if m: bad(i, "DRUG BRAND NAME", m.group(0))
    m = BAIT.search(pub)
    if m: bad(i, "ENGAGEMENT BAIT", m.group(0))
    m = PRICE.search(pub)
    if m: bad(i, "PRICE PUBLISHED", m.group(0))

    # quoted speech attributed to a patient
    for q in re.findall(r"[\"\u201c]([^\"\u201d]{25,})[\"\u201d]", i["caption"]):
        if re.search(r"\b(i |my |me |we )", q.lower()[:30]):
            bad(i, "POSSIBLE PATIENT QUOTE", q)

    # doctor must not be in the hook or the first caption line
    if re.search(r"uzair", i["hook"], re.I): bad(i, "DOCTOR IN HOOK", i["hook"])
    first = (i["caption"].split("\n")[0] if i["caption"] else "")
    if re.search(r"uzair", first, re.I): bad(i, "DOCTOR IN FIRST CAPTION LINE", first)

    # hashtags
    tags = re.findall(r"#\w+", i["hashtags"])
    if not (3 <= len(tags) <= 5): bad(i, "HASHTAG COUNT", "%d tags" % len(tags))
    for t in tags:
        tl = t.lower()
        if tl in ("#laserhairremoval", "#permanenthairremoval", "#skinwhitening", "#botox",
                  "#sale", "#discount", "#offer", "#skincare", "#beauty"):
            bad(i, "BANNED HASHTAG", t)
        if re.search(r"best|no1|number1|top", tl): bad(i, "SUPERLATIVE HASHTAG", t)

    # emoji discipline
    emo = re.findall(r"[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF]", i["caption"])
    if len(emo) > 1: bad(i, "TOO MANY EMOJI", "%d in caption" % len(emo))
    if i["caption"] and re.search(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", i["caption"].split("\n")[0]):
        bad(i, "EMOJI IN LINE 1", i["caption"].split("\n")[0][:60])

    # required content
    if not i["hook"].strip(): bad(i, "NO HOOK", "")
    if not i["caption"].strip(): bad(i, "NO CAPTION", "")
    if not i["spec"].strip(): bad(i, "NO SPEC", "")
    if len(i["spec"]) < 200: bad(i, "SPEC TOO THIN", "%d chars" % len(i["spec"]))
    if not i["goal"]: bad(i, "NO DECLARED GOAL", "")
    if not i["keywordBlock"].strip(): bad(i, "NO KEYWORD BLOCK", "")


    # extra checks raised by the compliance pass
    m = re.search(r"(safe|safely|safety)", pub, re.I)
    if m: bad(i, "BANNED WORD safe", pub[max(0, m.start()-55):m.start()+55])
    for comp in ("laseraway","milan laser","ideal image","sono bello","skin laundry","sculpt spa",
                 "oliva","kaya","clinic dermatech","3d lifestyle","cosmetique","aesthetics lab",
                 "enfield","glamorous clinic","skinspirit","bodycraft","alchemy 43","pulse light"):
        if comp in pub.lower(): bad(i, "NAMED COMPETITOR IN PUBLIC COPY", comp)
    # caption length, body only: exclude the branch block, hashtags and keyword block
    body = i["caption"]
    for cut in ("Venus Aesthetics,", "Call or WhatsApp"):
        k = body.find(cut)
        if k > 0: body = body[:k]
    body = re.sub(r"\[[^\]]*\]", "", body)
    body = re.sub(r"#\w+", "", body)
    words = len([w for w in body.split() if w.strip()])
    # the ceiling scales with how long the video is: a 40 second film earns a longer caption
    CAP = {"The Full Pass": 115, "The Honest Number": 110, "Asked and Answered": 100,
           "The Room": 95}
    cap = CAP.get(i["show"], 95) if i["creative"] == "Reel" else 165
    if words > cap: bad(i, "CAPTION BODY TOO LONG", "%d words, ceiling %d" % (words, cap))
    # the engagement day must carry both references
    if i["show"] == "The Room":
        if not i["ref"]: bad(i, "ROOM POST WITHOUT A CONTENT REFERENCE", "")
        if not i["editRef"]: bad(i, "ROOM POST WITHOUT AN EDITING REFERENCE", "")
        if not (i["editRefWhy"] or "").strip(): bad(i, "ROOM POST WITHOUT AN EDIT REF NOTE", "")
    # Full Pass specs must name both the source length and a finished runtime.
    # The exact runtime is checked by eye, phrasing varies too much to regex reliably.
    if i["show"] == "The Full Pass" and (i.get("sourceSeconds") or 0) >= 24:
        head = i["spec"][:400].lower()
        if "second" not in head and "0:" not in head:
            bad(i, "FULL PASS SPEC WITH NO LENGTHS", "source %.1fs" % (i.get("sourceSeconds") or 0))
    # source-specific requirements
    if i["source"] == "SHOOT_TALK" and not i["script"].strip():
        bad(i, "TALKING VIDEO WITH NO SCRIPT", "")
    if i["source"] in ("SHOOT_TALK", "SHOOT_BROLL") and not i["recordGuide"].strip():
        bad(i, "SHOOT WITH NO RECORD GUIDE", "")
    if i["source"] == "DRIVE_EDIT" and not i["editNote"].strip():
        bad(i, "REUSED FOOTAGE WITH NO EDIT NOTE", "")
    if i["fromDrive"] and not i["driveUrl"]:
        bad(i, "DRIVE ASSET WITH NO LINK", i["driveFile"])

    # reference must match format
    if i["ref"]:
        rf = (i["refFormat"] or "").lower()
        if i["creative"] == "Carousel" and "reel" in rf:
            bad(i, "REF FORMAT MISMATCH", "carousel post referencing a reel")
        if i["creative"] == "Reel" and "carousel" in rf:
            bad(i, "REF FORMAT MISMATCH", "reel referencing a carousel")
        if not rf: bad(i, "UNKNOWN REFERENCE URL", i["ref"])

# hooks must all differ
hooks = [i["hook"].strip().lower() for i in items]
for h, n in collections.Counter(hooks).items():
    if n > 1: fail.append(("-", "-", "DUPLICATE HOOK", "%dx: %s" % (n, h[:70])))

print("=" * 78)
print("VENUS Q4 2026 CALENDAR, INDEPENDENT VALIDATION")
print("=" * 78)
print("posts: %d   %s to %s" % (len(items), items[0]["date"], items[-1]["date"]))
print("source mix:", d["stats"]["bySource"])
print("creative:  ", d["stats"]["byCreative"])
print("goals:     ", d["stats"]["byGoal"])
print("drive links %d | scripts %d | guides %d | edit notes %d" % (
    d["stats"]["driveLinked"], d["stats"]["scripts"], d["stats"]["guides"], d["stats"].get("editNotes", 0)))
print("production rows:", len(d["production"]))
print()
if not fail:
    print("RESULT: CLEAN. No rule violations found.")
else:
    print("RESULT: %d ISSUES" % len(fail))
    by = collections.Counter(f[2] for f in fail)
    for k, n in by.most_common(): print("   %-36s %d" % (k, n))
    print()
    for f in fail[:60]:
        print("  id=%-3s %-11s %-30s %s" % f)
    if len(fail) > 60: print("  ... and %d more" % (len(fail) - 60))
sys.exit(1 if fail else 0)
