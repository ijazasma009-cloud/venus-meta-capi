# -*- coding: utf-8 -*-
"""Reference library v3. Matched by FORMAT and by content type.

A carousel post only ever references a real carousel post. A video only references a video.
Every entry was crawled from a logged-in Instagram session on 26 and 27 Aug 2026 with its real
engagement. If no exact-format reference exists for a post, that post carries NO reference
rather than a loose one.
"""

# key: (url, account, format, what it demonstrates, real result)
REFS = {

# ============================================================ CAROUSEL references
 "car_sensation": ("https://instagram.com/p/DbCGcx9DwhK", "SkinSpirit", "Carousel, 4 slides",
   "Things that hurt more than microneedling. Turns the pain question into a joke, then answers it honestly. "
   "Slide 1 is the joke, middle slides are the comparisons, last slide reassures and sells.",
   "766 likes, 35 comments"),

 "car_why_results_differ": ("https://instagram.com/p/DcNiQjIiFpi", "Dr Rashmi Shetty", "Carousel, 7 slides",
   "Why two patients having the same treatment get different results. Educational, sequential, "
   "and it explicitly continues from a previous post so people go back and look.",
   "1,787 likes, 28 comments"),

 "car_prewedding_compare": ("https://instagram.com/p/DaSKpcYAeZD", "Dr Jaishree Sharad", "Carousel, 3 slides",
   "Skin boosters, lasers or regenerative treatments. Which pre-wedding treatments are worth the money. "
   "A direct comparison carousel that helps someone choose rather than pushing one option.",
   "390 likes, 15 comments"),

 "car_expectation": ("https://instagram.com/p/DbhObcpGpyU", "SkinSpirit", "Carousel, 3 slides",
   "One appointment does not always mean the final result. Sets expectations before the booking, "
   "which is what stops disappointment later.",
   "496 likes, 21 comments"),

 "car_one_session": ("https://instagram.com/p/DbhxnXFkfgr", "Dr Rashmi Shetty", "Carousel, 5 slides",
   "One session, maybe two, but never just the under eye alone. Explains why a concern cannot be "
   "treated in isolation. The most persuasive kind of education because it sounds like a caution.",
   "423 likes, 20 comments"),

 "car_beginner": ("https://instagram.com/p/DFwKaBjNXTC", "SkinSpirit", "Carousel, 3 slides",
   "New to medical aesthetics. A first-timer entry point that assumes nothing.",
   "544 likes, 25 comments"),

 "car_why_us": ("https://instagram.com/p/DFtgsFSMdtd", "SkinSpirit", "Carousel, 3 slides",
   "Our team trains the trainers. Authority stated as a fact rather than a boast.",
   "542 likes, 36 comments"),

 "car_the_room": ("https://instagram.com/p/DF1GC74OC5S", "SkinSpirit", "Carousel, 3 slides",
   "Step into the space. The clinic environment sold as an experience, not a facility.",
   "746 likes, 70 comments"),

 "car_new_branch": ("https://instagram.com/p/DbyWRuTlLx8", "SkinSpirit", "Carousel, 3 slides",
   "A new location announced as news, with a countdown feel and no discount attached.",
   "533 likes, 39 comments"),

 "car_industry_honesty": ("https://instagram.com/p/DbGU_X7CGaQ", "Dr Rashmi Shetty", "Carousel, 7 slides",
   "The aesthetics industry has a marketing problem and it is costing patients. "
   "Taking a position against your own category is the strongest trust play available.",
   "465 likes, 16 comments"),

# ============================================================ VIDEO references
 "vid_course_progress": ("https://instagram.com/p/DbdowHqk8H-", "Sono Bello", "Reel",
   "Three months on, results still building. Progress shown over real elapsed time rather than a single reveal.",
   "92k plays, 1,930 likes, 2.16% ER"),

 "vid_course_parts": ("https://instagram.com/p/DbYJ9SjCpZe", "Pulse Light London", "Reel",
   "Part two of a numbered series. The part number is what brings people back.",
   "Named series, beats their results-only content"),

 "vid_result": ("https://instagram.com/p/DcByqkjFjzn", "Sono Bello", "Reel",
   "Completed treatment, patient on camera speaking for herself, no brand voiceover.",
   "78k plays, 2,003 likes, 2.69% ER"),

 "vid_result_male": ("https://instagram.com/p/DboqG0evGyt", "LaserAway", "Reel",
   "Male patient, filmed on his own terms, plain and undramatic.",
   "38k plays, 700 likes, 1.86% ER"),

 "vid_sensation": ("https://instagram.com/p/DbIZKAIFRJK", "Pulse Light London", "Reel",
   "What the treatment actually feels like, narrated while it happens, including the uncomfortable parts.",
   "Named series, outperforms their results content"),

 "vid_device_explainer": ("https://instagram.com/p/Db8aXJkig1N", "Alchemy 43", "Reel",
   "Four sessions, four hundred percent more collagen, let me explain. Opens on the hard number.",
   "2k plays, 2.00% ER"),

 "vid_practitioner_qa": ("https://instagram.com/p/DQ7tEOBD9a4", "Ideal Image", "Reel",
   "Named Lead Injector answers one specific question. Their single best performing post.",
   "14k plays, 162 likes, 1.30% ER"),

 "vid_practitioner_qa2": ("https://instagram.com/p/DbWn5UlhfRx", "Alchemy 43", "Reel",
   "Named practitioner Q&A. What it is, who suits it, what she would add.",
   "3k plays, 21 comments, 1.97% ER"),

 "vid_new_treatment": ("https://instagram.com/p/DcTlsl8OeKN", "Ever/Body", "Reel",
   "One treatment named and its benefits listed plainly by someone who administers it.",
   "2k plays, 2.52% ER"),

 "vid_one_liner": ("https://instagram.com/p/DcZhRGkAMFZ", "Milan Laser", "Reel",
   "Nine words, one treatment, no explanation. An entire chain runs on this.",
   "6k plays, 0.76% ER"),

 "vid_one_liner_attitude": ("https://instagram.com/p/DcBxwo1CCE2", "Pulse Light London", "Reel",
   "You are not going to believe this, but we think you should wear sunscreen. Personality over information.",
   "3k plays, 1.17% ER"),

 "vid_life_context": ("https://instagram.com/p/DbdqueMOmLU", "Skin Laundry", "Reel",
   "Between the errands, the emails and everything else. The clinic is never mentioned.",
   "10k plays, 0.46% ER"),

 "vid_life_family": ("https://instagram.com/p/DbWQkkDP7uk", "LaserAway", "Reel",
   "A mother teaching her daughter that looking after yourself is necessary. Highest engagement found anywhere in this audit.",
   "56k plays, 2,444 likes, 4.45% ER"),

 "vid_branch": ("https://instagram.com/p/Da3Vg47xYUq", "Face Haus", "Reel",
   "A new place filmed as a destination. Scale and setting do the selling.",
   "91k plays, 2,011 likes, 2.29% ER"),

 "vid_treatment_film": ("https://instagram.com/p/DcOsYaChl8J", "Skin Laundry", "Reel",
   "The hero treatment filmed and named in the caption every single time.",
   "9k plays, 0.57% ER"),

# ============================================================ ENGAGING references
# Every engaging video in this calendar must be shot. These are the formats to copy.
 "eng_deadpan": ("https://instagram.com/p/DcO5LR-AqU0", "Sculpt Spa", "Reel",
   "No time to gossip. Six words, deadpan, shot on a phone in the treatment room. "
   "One staff member, one line, no production.",
   "2k plays, 95 likes, 4.46% ER, the best humour result in the whole audit"),

 "eng_secret": ("https://instagram.com/p/DZ0ZWodCjuC", "Sculpt Spa", "Reel",
   "All jokes aside, we are totally fine with being your little secret. "
   "Plays on the fact that people do not tell anyone they come.",
   "3k plays, 115 likes, 3.60% ER"),

 "eng_fail": ("https://instagram.com/p/Da3V-BPDlj9", "Sculpt Spa", "Reel",
   "Guess I will try again tomorrow. The failed attempt is the entire joke.",
   "4k plays, 83 likes, 2.37% ER"),

 "eng_trend_pair": ("https://instagram.com/p/DbWn5UlhfRx", "Alchemy 43", "Reel",
   "Two staff, one trending audio, treatment as the punchline rather than the subject.",
   "3k plays, 1.97% ER"),
}

def get(key):
    return REFS.get(key)
