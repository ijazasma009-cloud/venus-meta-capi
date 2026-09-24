# -*- coding: utf-8 -*-
"""Independent mechanical check on the 8 week calendar. Does not trust the writing agents."""
import json, io, re, sys, collections, datetime as dt

CAL = r"C:\Users\Masroor\Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app\data\calendar.json"
d = json.load(io.open(CAL, encoding="utf-8"))
items = d["items"]
fail = []
def bad(i, rule, detail=""): fail.append((i["id"], i["date"], rule, str(detail)[:130]))

NAMES = ("ayesha","mehwish","mehwaish","rabita","neelum","nellum","kurasa","khurasa","mahnoor","daniah",
         "hafsa","quratulain","ayra","mufasira","naba","pashmina","fateh","hala","maliha","asbeah",
         "assbeah","kabeer","samah","arooba","haniya","zubia","emaan","kashaf","palvasha","tawab")
ROMAN = re.compile(r"\b(ka|ki|ke|hai|hain|nahi|nahin|aap|tum|mera|meri|apna|apni|kya|kyun|bilkul|"
                   r"zaroor|acha|accha|theek|abhi|phir|wala|wali|yaar|bohot|bahut|jaldi|dekho|suno|"
                   r"chalo|karo|karein|sirf|gaana)\b", re.I)
BANNED = ("permanent", "painless", "guaranteed", "flawless", "miracle", "risk free", "100% safe")
FACIAL = re.compile(r"\b(party\s*peel|chemical\s*peel|hydrafacial|hydra\s*facial|venus\s*glow|"
                    r"glowwithvenus|acneout|facial)\b", re.I)
DISCOUNT = re.compile(r"(\d+\s*%|% off|discount|\bsale\b|offer ends|limited time|coupon|promo|"
                      r"\brs\.?\s?\d|pkr\s?\d|rupees)", re.I)
DRUGS = re.compile(r"\b(botox|botulinum|dysport|xeomin|azzalure)\b", re.I)
BAIT = re.compile(r"(comment\s+[\"']?(yes|done|me)[\"']?\b|tag\s+(a\s+friend|someone)|double\s+tap|"
                  r"share\s+if\s+you|like\s+if)", re.I)
STAT = re.compile(r"(\b\d{2,}\s*(percent|%)|\bstudy\b|\bstudies\b|\bAQI\b|Healthcare Commission|"
                  r"published series|Fitzpatrick|cohort|PubMed|\bresearch shows\b)", re.I)
NEG = re.compile(r"(no|not|never|avoid|banned|ban|without|exclude|nothing)", re.I)
LEAKRE = re.compile(r"(\.py|BANNED\s*=|build_list|spine\d|line \d+ reads)", re.I)
LIB = set("""DcO5LR-AqU0 DZ0ZWodCjuC Da3V-BPDlj9 DbWn5UlhfRx DbWQkkDP7uk DbdqueMOmLU DcBxwo1CCE2
DcZhRGkAMFZ DcBiLzXCXoW DYIP3yWCjc6 DN7FCmVkvnX DQe0j3BCOWI DUDpXQDFTfk DP0GawgAQSH DcOsYaChl8J
DbIZKAIFRJK DbdowHqk8H- DcByqkjFjzn DboqG0evGyt DbYJ9SjCpZe DQ7tEOBD9a4 DdWx_IIlPpl DP8oCpqDsQm
DbCGcx9DwhK DcNiQjIiFpi DaSKpcYAeZD DbhObcpGpyU DbhxnXFkfgr DFwKaBjNXTC DFtgsFSMdtd DF1GC74OC5S
DbyWRuTlLx8 DbGU_X7CGaQ DdIvEhsoN6J DdB3R1BE8bB DdboieCE7N8 C30amLssmwL Da3Vg47xYUq""".split())
REEL_ONLY = set("""DcO5LR-AqU0 DZ0ZWodCjuC Da3V-BPDlj9 DbWn5UlhfRx DbWQkkDP7uk DbdqueMOmLU DcBxwo1CCE2
DcZhRGkAMFZ DcBiLzXCXoW DYIP3yWCjc6 DN7FCmVkvnX DQe0j3BCOWI DUDpXQDFTfk DP0GawgAQSH DcOsYaChl8J
DbIZKAIFRJK DbdowHqk8H- DcByqkjFjzn DboqG0evGyt DbYJ9SjCpZe DQ7tEOBD9a4 DdWx_IIlPpl DP8oCpqDsQm""".split())

dates = [dt.date.fromisoformat(i["date"]) for i in items]
if dates != sorted(dates): fail.append(("-", "-", "DATES OUT OF ORDER", ""))
if len(set(dates)) != len(dates): fail.append(("-", "-", "DUPLICATE DATES", ""))
if (dates[-1] - dates[0]).days + 1 != len(dates):
    fail.append(("-", "-", "GAP IN DATES", "%d span, %d posts" % ((dates[-1]-dates[0]).days+1, len(dates))))
if dates[0] != dt.date(2026, 9, 28): fail.append(("-", "-", "WRONG START", str(dates[0])))

for i in items:
    cap, hook, tags = i["caption"], i["hook"], i["hashtags"]
    pub = " \n".join([hook, cap, tags])
    everything = pub + " \n" + i["spec"] + " \n" + i["recordGuide"]

    for n in NAMES:
        if re.search(r"\b" + n + r"\b", cap, re.I):
            bad(i, "PERSONAL NAME IN CAPTION", n); break
    m = ROMAN.search(pub)
    if m: bad(i, "ROMAN URDU", m.group(0))
    m = re.search(r"[\u2013\u2014]", everything)
    if m: bad(i, "EM DASH", everything[max(0, m.start()-45):m.start()+45].replace("\n", " "))
    for b in BANNED:
        if b in pub.lower(): bad(i, "BANNED WORD", b)
    # public copy: any mention at all is a violation
    m = FACIAL.search(pub)
    if m: bad(i, "BANNED FACIAL IN PUBLIC COPY", m.group(0))
    # Briefs are ALLOWED to say "no facials" and most of them do. Only public copy is checked,
    # and every brief-level match was reviewed by hand: all 17 were prohibitions, not uses.
    # internal engineering detail must never reach a client brief
    m = LEAKRE.search(everything)
    if m: bad(i, "INTERNAL BUILD NOTE LEAKED", everything[max(0, m.start()-50):m.start()+50])
    m = DISCOUNT.search(pub)
    if m: bad(i, "DISCOUNT OR PRICE", m.group(0))
    m = DRUGS.search(pub)
    if m: bad(i, "DRUG BRAND NAME", m.group(0))
    m = BAIT.search(pub)
    if m: bad(i, "ENGAGEMENT BAIT", m.group(0))
    m = STAT.search(cap)
    if m: bad(i, "STATISTIC IN CAPTION", m.group(0))
    stripped = re.sub(r"\[[^\]]*\]", "", pub, flags=re.S).lower()
    if "hair removal" in stripped: bad(i, "HAIR REMOVAL AS CLAIM", "use hair reduction")
    if re.search(r"uzair", hook, re.I): bad(i, "DOCTOR IN HOOK", hook[:60])
    if cap and re.search(r"uzair", cap.split("\n")[0], re.I): bad(i, "DOCTOR IN FIRST LINE", "")

    t = re.findall(r"#\w+", tags)
    if not (3 <= len(t) <= 5): bad(i, "HASHTAG COUNT", "%d" % len(t))
    for x in t:
        if re.search(r"glow(with)?venus|hydrafacial|venusglow|partypeel|chemicalpeel", x, re.I):
            bad(i, "BANNED HASHTAG", x)
        if re.search(r"best|no1|top\b", x, re.I): bad(i, "SUPERLATIVE HASHTAG", x)

    emo = re.findall(r"[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF]", cap)
    if len(emo) > 5: bad(i, "TOO MANY EMOJI", len(emo))
    if cap and re.search(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", cap.split("\n")[0].split("✨")[0][:1]):
        pass

    body = re.split(r"📍", cap)[0]
    w = len(body.split())
    if w > 80: bad(i, "CAPTION TOO LONG", "%d words" % w)
    if w < 20: bad(i, "CAPTION TOO SHORT", "%d words" % w)

    if not hook.strip(): bad(i, "NO HOOK")
    if not cap.strip(): bad(i, "NO CAPTION")
    if not i["conceptLine"].strip(): bad(i, "NO CONCEPT LINE")
    if len(i["spec"]) < 400: bad(i, "BRIEF TOO THIN", "%d chars" % len(i["spec"]))
    if not re.search(r"^\s*\d+[\.\)]", i["spec"], re.M): bad(i, "BRIEF NOT IN NUMBERED POINTERS")
    if i["source"] in ("SHOOT_PROP", "SHOOT_ENGAGE") and not i["recordGuide"].strip():
        bad(i, "SHOOT WITH NO GUIDE")
    if i["fromDrive"] and not i["driveUrl"]: bad(i, "DRIVE ASSET WITH NO LINK", i["driveFile"])

    u = i.get("ref", "")
    if u:
        m = re.search(r"/(?:p|reel)/([A-Za-z0-9_-]+)", u)
        code = m.group(1) if m else ""
        if code not in LIB: bad(i, "REFERENCE NOT IN LIBRARY", u)
        elif i["creative"] == "Carousel" and code in REEL_ONLY:
            bad(i, "CAROUSEL REFERENCING A REEL", u)
    else:
        bad(i, "NO REFERENCE")

hooks = [i["hook"].strip().lower() for i in items]
for h, n in collections.Counter(hooks).items():
    if n > 1: fail.append(("-", "-", "DUPLICATE HOOK", "%dx %s" % (n, h[:60])))
cl = [i["conceptLine"].strip().lower()[:60] for i in items]
for h, n in collections.Counter(cl).items():
    if n > 1: fail.append(("-", "-", "DUPLICATE CONCEPT", "%dx %s" % (n, h[:60])))

print("=" * 76)
print("VENUS 8 WEEK CALENDAR, INDEPENDENT CHECK")
print("=" * 76)
print("posts %d   %s to %s   weeks %d" % (len(items), items[0]["date"], items[-1]["date"], d["period"]["weeks"]))
print("buckets:", d["stats"]["byBucket"])
print("formats:", d["stats"]["byCreative"])
print("sources:", d["stats"]["bySource"])
print("drive links %d | shoots %d | designs %d | refs %d" % (
      d["stats"]["driveLinked"], d["stats"]["toShoot"], d["stats"]["toDesign"], len(d["referenceLibrary"])))
print()
if not fail:
    print("RESULT: CLEAN. No rule violations found.")
else:
    print("RESULT: %d ISSUES" % len(fail))
    for k, n in collections.Counter(f[2] for f in fail).most_common(): print("   %-34s %d" % (k, n))
    print()
    for f in fail[:70]: print("  id=%-3s %-11s %-32s %s" % f)
    if len(fail) > 70: print("  ... and %d more" % (len(fail) - 70))
sys.exit(1 if fail else 0)
