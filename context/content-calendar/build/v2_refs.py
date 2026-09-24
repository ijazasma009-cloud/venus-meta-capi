# -*- coding: utf-8 -*-
"""Reference library, matched by CONTENT TYPE rather than by format name.

Every reference below is a real post, crawled from a logged-in Instagram session on 26 Aug 2026,
with its real engagement rate. A reference is only ever attached to a Venus post of the same
KIND of content, so a doctor explaining a device is never referenced against a brand mood post.
"""

# key: (url, account, description, metric)
REFS = {

 # ---------- patient voice, by beat ----------
 "patient_decision": ("https://instagram.com/p/Da1Gb7dxXU-", "Sono Bello",
   "Vulnerability post. Patient explains, in first person, why she booked and what she felt at the consultation.",
   "34k plays, 775 likes, 2.48% ER"),
 "patient_session": ("https://instagram.com/p/DbIZKAIFRJK", "Pulse Light London",
   "Patient narrates what the treatment actually feels like, minute by minute, while it happens.",
   "Named series, beats their results-only content"),
 "patient_wait": ("https://instagram.com/p/DbdowHqk8H-", "Sono Bello",
   "The in-between beat. Three months on, results still building, patient talks about the waiting.",
   "92k plays, 1,930 likes, 2.16% ER"),
 "patient_result": ("https://instagram.com/p/DcByqkjFjzn", "Sono Bello",
   "Completed course, patient speaks the result herself. No brand voiceover anywhere in it.",
   "78k plays, 2,003 likes, 2.69% ER"),
 "patient_longterm": ("https://instagram.com/p/DZaAM2Coo6P", "Biolite Clinic Dubai",
   "Seven months after the procedure. The long-term follow up almost nobody in the category films.",
   "31k plays, 233 likes, 0.81% ER"),
 "patient_male": ("https://instagram.com/p/DboqG0evGyt", "LaserAway",
   "Male-voiced first person appointment story, filmed on the patient's own terms.",
   "38k plays, 700 likes, 1.86% ER"),
 "patient_parallel": ("https://instagram.com/p/DcUPRSkNp2H", "Sono Bello",
   "Patient running more than one thing at once, telling both stories in one post.",
   "43k plays, 742 likes, 1.85% ER"),

 # ---------- device and technology ----------
 "device_explainer": ("https://instagram.com/p/Db8aXJkig1N", "Alchemy 43",
   "Number-led device explainer. Opens on the hard figure, then explains the mechanism.",
   "2k plays, 2.00% ER"),
 "device_comparison": ("https://instagram.com/p/Dbh75l0og4F", "Biolite Clinic Dubai",
   "Head to head device comparison. Names all the machines, refuses to declare one universal winner.",
   "6k plays, 0.44% ER, the exact format for Primelase vs Soprano"),
 "device_named_hero": ("https://instagram.com/p/DcOsYaChl8J", "Skin Laundry",
   "The hero treatment named in the caption every single time, until the name means something.",
   "9k plays, 0.57% ER, repeated across their entire feed"),
 "treatment_menu": ("https://instagram.com/p/DcTlsl8OeKN", "Ever/Body",
   "One treatment named and its benefits listed plainly, by someone who administers it.",
   "2k plays, 2.52% ER"),

 # ---------- practitioner ----------
 "practitioner_qa": ("https://instagram.com/p/DbWn5UlhfRx", "Alchemy 43",
   "Named practitioner Q&A. What it is, who is a good candidate, what she would add.",
   "3k plays, 21 comments, 1.97% ER"),
 "practitioner_named": ("https://instagram.com/p/DQ7tEOBD9a4", "Ideal Image",
   "Their Lead Injector, named on screen, answers one specific question. Their best performing post.",
   "14k plays, 162 likes, 1.30% ER"),
 "practitioner_rating": ("https://instagram.com/p/DbRocaSsZQC", "SkinSpirit",
   "Practitioner rates treatments against each other and explains which goal each one suits.",
   "35k plays, 464 likes, 1.42% ER"),

 # ---------- education ----------
 "aftercare": ("https://instagram.com/p/DcMwh87MWh_", "SkinSpirit",
   "What happens after the treatment matters as much as the treatment. Aftercare as its own content.",
   "13k plays, 327 likes, 2.73% ER"),
 "candidacy": ("https://instagram.com/p/DQxDySAjFue", "Ideal Image",
   "Is it worth the hype. Honest candidacy framing after a set number of sessions.",
   "14k plays, 0.93% ER"),
 "honest_limits": ("https://instagram.com/p/Db3ZRmiKt4j", "LaserAway",
   "Your feed has opinions, we have board-certified dermatologists. Names what to skip and why.",
   "48k plays, 769 likes, 1.65% ER"),

 # ---------- voice and tone ----------
 "one_liner": ("https://instagram.com/p/DcZhRGkAMFZ", "Milan Laser",
   "Nine words, one treatment, no explanation. An entire chain runs on this.",
   "6k plays, 0.76% ER"),
 "one_liner_attitude": ("https://instagram.com/p/DcBxwo1CCE2", "Pulse Light London",
   "You are not going to believe this, but we think you should wear sunscreen. Personality over information.",
   "3k plays, 1.17% ER"),
 "life_context": ("https://instagram.com/p/DbdqueMOmLU", "Skin Laundry",
   "Between the errands, the emails and everything else. The clinic is never mentioned.",
   "10k plays, 0.46% ER"),
 "life_context_family": ("https://instagram.com/p/DbWQkkDP7uk", "LaserAway",
   "A mother teaching her daughter that self care is necessary. Highest engagement in the entire audit.",
   "56k plays, 2,444 likes, 4.45% ER"),

 # ---------- humour ----------
 "humour_deadpan": ("https://instagram.com/p/DcO5LR-AqU0", "Sculpt Spa",
   "No time to gossip. Six words, deadpan, filmed on a phone.",
   "2k plays, 95 likes, 4.46% ER, the best humour result found"),
 "humour_secret": ("https://instagram.com/p/DZ0ZWodCjuC", "Sculpt Spa",
   "All jokes aside, we are totally fine with being your little secret.",
   "3k plays, 115 likes, 3.60% ER"),
 "humour_fail": ("https://instagram.com/p/Da3V-BPDlj9", "Sculpt Spa",
   "Guess I will try again tomorrow. The failed attempt as the whole joke.",
   "4k plays, 83 likes, 2.37% ER"),
 "humour_team": ("https://instagram.com/p/DaddvlVkZyk", "Venus Aesthetics",
   "Your own balloon blooper. 16x your account median with zero production value.",
   "26k plays, 117 likes, 0.47% ER"),

 # ---------- proof and place ----------
 "before_after": ("https://instagram.com/p/DanYQHfj81V", "Venus Aesthetics",
   "Your own best testimonial format, with the client tagged so it reaches her audience too.",
   "241k plays, 1,064 likes, 0.44% ER"),
 "branch_open": ("https://instagram.com/p/Db9UCkdhctV", "SkinSpirit",
   "New location announcement treated as real news rather than an advert.",
   "12k plays, 251 likes, 2.30% ER"),
 "branch_tour": ("https://instagram.com/p/Da3Vg47xYUq", "Face Haus",
   "A new place, filmed as a destination. Scale and setting do the selling.",
   "91k plays, 2,011 likes, 2.29% ER"),
 "creator_visit": ("https://instagram.com/p/Da0zd2lvNf5", "Face Haus",
   "Friendly reminder to book the facial. A creator, in her own words, about her own visit.",
   "13k plays, 393 likes, 3.04% ER"),
 "celebrity_visit": ("https://instagram.com/p/DaiIPy5K6VX", "Biolite Clinic Dubai",
   "Malaika Arora at the clinic. The single biggest clinic post found anywhere in this audit.",
   "1,973k plays, 40,516 likes, 2.08% ER"),
}

# Which reference type each Venus post gets. Keyed by date where the content type is specific,
# otherwise falls back to the format default below.
FORMAT_DEFAULT = {
 "The Course":        "patient_session",
 "Skin School":       "aftercare",
 "The Menu":          "device_named_hero",
 "New at Venus":      "device_explainer",
 "Men of Venus":      "patient_male",
 "The Offer Free Consultation": "candidacy",
 "The Result":        "branch_open",
 "Case File":         "patient_session",
 "The Machine":       "device_explainer",
 "The One Liner":     "one_liner",
 "Really Feels Like": "patient_session",
 "In Real Life":      "life_context",
 "Ask the Room":      "practitioner_named",
 "Side by Side":      "before_after",
 "Is This You":       "candidacy",
 "The Room":          "branch_tour",
 "Off Duty":          "humour_deadpan",
}

# Per-date overrides where the content type differs from the format default.
OVERRIDES = {
 # device comparison, not a brand mood post. This was the mismatch worth fixing.
 "2026-09-07": "device_comparison",
 "2026-11-17": "device_comparison",
 "2026-12-01": "practitioner_rating",
 "2026-11-19": "device_comparison",

 # case file beats
 "2026-09-08": "patient_decision", "2026-09-15": "patient_session",
 "2026-09-18": "patient_decision", "2026-09-22": "patient_wait",
 "2026-09-24": "patient_session",  "2026-09-29": "patient_decision",
 "2026-10-02": "patient_wait",     "2026-10-05": "patient_wait",
 "2026-10-08": "patient_male",     "2026-10-12": "patient_result",
 "2026-10-14": "patient_decision", "2026-10-16": "patient_wait",
 "2026-10-21": "patient_session",  "2026-10-23": "patient_wait",
 "2026-10-27": "patient_decision", "2026-10-29": "patient_wait",
 "2026-11-03": "patient_wait",     "2026-11-05": "patient_male",
 "2026-11-09": "patient_result",   "2026-11-11": "patient_session",
 "2026-11-16": "patient_male",     "2026-11-18": "patient_parallel",
 "2026-11-23": "patient_result",   "2026-11-26": "patient_male",
 "2026-11-30": "patient_longterm", "2026-12-02": "patient_result",
 "2026-12-06": "before_after",

 # honest limits content
 "2026-09-23": "honest_limits", "2026-09-11": "honest_limits",
 "2026-12-04": "aftercare",     "2026-10-19": "aftercare",
 "2026-10-30": "aftercare",     "2026-11-20": "patient_session",
 "2026-10-07": "patient_session",

 # practitioner Q&A
 "2026-09-16": "practitioner_qa", "2026-10-01": "practitioner_qa",
 "2026-10-20": "practitioner_qa", "2026-11-04": "practitioner_qa",
 "2026-11-13": "practitioner_qa", "2026-11-25": "practitioner_named",

 # life context
 "2026-09-14": "life_context_family", "2026-10-18": "life_context_family",
 "2026-11-06": "life_context_family",

 # one liners with attitude
 "2026-09-21": "one_liner_attitude", "2026-11-24": "one_liner_attitude",
 "2026-10-04": "one_liner", "2026-10-13": "one_liner",
 "2026-10-22": "one_liner_attitude", "2026-11-02": "one_liner",
 "2026-11-17b": "one_liner",

 # humour variety so it is not the same reference 13 times
 "2026-09-12": "humour_team",   "2026-09-19": "humour_deadpan",
 "2026-09-26": "humour_secret", "2026-10-03": "humour_fail",
 "2026-10-10": "humour_deadpan","2026-10-17": "humour_fail",
 "2026-10-24": "humour_secret", "2026-10-31": "humour_team",
 "2026-11-07": "humour_deadpan","2026-11-14": "humour_secret",
 "2026-11-21": "humour_fail",   "2026-11-28": "humour_team",
 "2026-12-05": "humour_secret",

 # branches
 "2026-09-20": "branch_tour", "2026-11-01": "branch_open", "2026-11-29": "branch_open",

 # named hero treatment repetition
 "2026-09-17": "device_named_hero", "2026-09-28": "device_explainer",
 "2026-10-06": "device_explainer",  "2026-10-15": "device_explainer",
 "2026-10-26": "treatment_menu",    "2026-11-10": "device_comparison",
 "2026-12-03": "life_context",

 # proof
 "2026-09-13": "before_after", "2026-09-27": "before_after",
 "2026-10-11": "before_after", "2026-10-25": "before_after",
 "2026-11-08": "before_after", "2026-11-15": "creator_visit",
 "2026-11-22": "patient_male",

 # candidacy
 "2026-09-10": "candidacy", "2026-09-25": "candidacy",
 "2026-10-09": "candidacy", "2026-10-28": "candidacy",
 "2026-11-12": "patient_session",
}

def ref_for(date, show):
    key = OVERRIDES.get(date) or FORMAT_DEFAULT.get(show) or "device_explainer"
    return key, REFS[key]
