# -*- coding: utf-8 -*-
# VENUS CONTENT SYSTEM v3. Treatment-led. No discount posts. Nobody is quoted.
#
# Formats are assigned to footage that can actually carry them. That is the change from v2:
# the treatment b-roll in Drive is SILENT, so no format here asks a patient to narrate.
# Where a patient speaks on camera, the edit spec says to subtitle their real words.

SHOWS = [
 ("The Course","Rotating","Reel",
  "One treatment followed across its real course, session by session. Every post carries SESSION N OF X "
  "and the real date on screen. That on-screen device is the whole narrative, because the footage is silent.",
  "Serialised progress outperforms one-off before and afters at every clinic chain we measured. Sono Bello and "
  "Pulse Light both build their best content this way. The difference here is that Venus's footage has no audio, "
  "so the dates carry the story instead of a voice.",
  ["https://instagram.com/p/DbdowHqk8H-","https://instagram.com/p/DbYJ9SjCpZe"],
  "VERIFIED silent b-roll. Mehwish across 6 laser visits, Neelum across 3 Viva sessions, plus body and tightening sessions."),

 ("Off Duty","Rotating","Reel",
  "The team unpolished. Bloopers, trends, the things that happen between appointments.",
  "Venus's own proven vein and the cheapest engagement available. The balloon blooper hit 0.47% and the penguin "
  "reel did 1.77M plays, both far above the 0.029% account median. Sculpt Spa runs an entire feed on deadpan humour at 4.46%.",
  ["https://instagram.com/p/DaddvlVkZyk","https://instagram.com/p/DcO5LR-AqU0","https://instagram.com/p/DMrQXVJCkcg"],
  "VERIFIED: the Engaging content clips are only 2.8 to 4.7 seconds each. They must be stitched three or four at a time."),

 ("Skin School","Rotating","Carousel",
  "One concept explained properly across five slides. Ingredient, condition or mechanism.",
  "The highest saving format in aesthetics. SkinSpirit's aftercare education post hit 2.73%, their best of the quarter. "
  "Saves and sends are what the algorithm counts and what turns into a referral.",
  ["https://instagram.com/p/DcMwh87MWh_"],
  "Design only, no shoot. Uses the 622 unused Dr. Uzair stills for authority frames."),

 ("Side by Side","Rotating","Reel",
  "Before and after, or a patient speaking on camera. Dates and session count always on screen.",
  "Proof is the second thing a patient checks after finding you. Venus's own best version reached 0.44%, "
  "roughly 15x the account median.",
  ["https://instagram.com/p/DanYQHfj81V"],
  "VERIFIED: testimonial files DO contain patients speaking, 18 to 28 seconds. Subtitle their real words. Never write a line for them."),

 ("Really Feels Like","Rotating","Reel or Carousel",
  "Honest sensory description. What the treatment feels like minute by minute, including the uncomfortable parts.",
  "Pulse Light runs this as a named series and it consistently beats their results-only content. "
  "Naming the discomfort makes every other claim on the account more believable.",
  ["https://instagram.com/p/DbIZKAIFRJK","https://instagram.com/p/DQxDySAjFue"],
  "Doctor explainer files with burned-in subtitles cover several of these already."),

 ("The Machine","Rotating","Reel",
  "The technology, named and specified. Primelase, Venus Viva, Venus Legacy, Venus Fat Freeze.",
  "Skin Laundry says its hero treatment name in every single post. Sono Bello does the same with TriSculpt. "
  "Venus already owns the names and has not been repeating them.",
  ["https://instagram.com/p/DcOsYaChl8J","https://instagram.com/p/Db_V7CTCB8l"],
  "Machine b-roll exists for most. Alchemy 43's number-led device explainer is the model at 2.00%."),

 ("Is This You","Rotating","Carousel",
  "Self qualification across five slides. One slide always says who the treatment is NOT for.",
  "People screenshot it and send it to a friend, which is a share the algorithm counts and a referral you get free. "
  "Saying who a treatment is wrong for is what makes the yes credible.",
  ["https://instagram.com/p/DQxDySAjFue"],
  "Design only."),

 ("The One Liner","Rotating","Reel",
  "One treatment, one line, under ten seconds. No education, no offer.",
  "Milan Laser runs almost an entire chain on this and lands 0.57% to 1.07% on a single-treatment account. "
  "Pulse Light's sunscreen line is the same move with more attitude.",
  ["https://instagram.com/p/DcZhRGkAMFZ","https://instagram.com/p/DcBxwo1CCE2"],
  "Any treatment b-roll, cut hard. Several source files are already under 10 seconds."),

 ("The Menu","Rotating","Carousel",
  "Several treatments compared on the same axes so a reader can place themselves.",
  "Biolite's head-to-head device comparison is the model. It refuses to name one universal winner, "
  "which is what makes it useful rather than promotional.",
  ["https://instagram.com/p/Dbh75l0og4F","https://instagram.com/p/DcOsYaChl8J"],
  "Design only. This is where the treatment names get repeated until they mean something."),

 ("Ask the Room","Rotating","Reel",
  "A NAMED practitioner, not the founder, answers one specific question. Name and role on screen.",
  "Ideal Image's single best post is their Lead Injector answering one question about jowls. "
  "The named practitioner beats everything else on that account, including the owner.",
  ["https://instagram.com/p/DQ7tEOBD9a4","https://instagram.com/p/DbWn5UlhfRx"],
  "Needs shooting. One practitioner, several questions in one sitting, one take each."),

 ("New at Venus","Rotating","Reel or Carousel",
  "A treatment that has never been posted before. SlimFit, AcneOUT, masseter, lip flip, hyperhidrosis, "
  "CelluLITE, Scalp Detox, Fusion PRP, melasma, alopecia.",
  "Eleven live treatments had zero content behind them. Botox, sweating and dermatology alone produced "
  "4,460 leads last quarter with nothing supporting them.",
  ["https://instagram.com/p/Db_V7CTCB8l","https://instagram.com/p/DcTlsl8OeKN"],
  "Mostly needs shooting. These are the highest return shoots in the quarter."),

 ("In Real Life","Rotating","Reel",
  "The treatment inside an ordinary Pakistani day. Rishta at six, three functions in nine days, shaadi in six months.",
  "Skin Laundry never mentions the clinic in its captions, only the life the treatment fits into. "
  "LaserAway's highest post of the year, at 4.45%, is a mother and daughter, not a treatment.",
  ["https://instagram.com/p/DbdqueMOmLU","https://instagram.com/p/DbWQkkDP7uk"],
  "Existing footage recut with life-context captions. Urdu hooks used deliberately."),

 ("The Room","Rotating","Reel",
  "One branch filmed on a normal working day, at a busy hour.",
  "Venus's own branch posts reached 0.91% and 0.57%, roughly 30x the account median. "
  "Real places and real news outperform polished treatment films.",
  ["https://instagram.com/p/DGVyH5wvy1M","https://instagram.com/p/Db9UCkdhctV"],
  "Needs shooting, one pass per branch."),

 ("Men of Venus","Rotating","Reel",
  "Shot for men, cut for men. No soft focus, no pastel grade.",
  "Male laser is tied for the cheapest lead in the Meta account at PKR 104 and has five videos behind it in total. "
  "Male patients arrive through friends, not adverts.",
  ["https://instagram.com/p/DboqG0evGyt","https://instagram.com/p/DbWQkkDP7uk"],
  "Five male files exist. Week 11 is given entirely to men."),

 ("The Result","Rotating","Static",
  "Awards, milestones and verified numbers, treated as news.",
  "SkinSpirit and Skin Pharm both treat openings and milestones as news rather than advertising, at 2.30% and above.",
  ["https://instagram.com/p/Db9UCkdhctV"],
  "The Sunday Times award from 14 Aug 2026. Use 9,861 reviews, the verified count, never 10,000+."),

 ("The Offer Free Consultation","Rotating","Static",
  "The only commercial post in the calendar, and it is not a discount. The free consultation is a standing service.",
  "No major clinic chain runs a discount rail in the feed. Offers live in stories, bio links and paid. "
  "24 percent of Venus's last 600 posts were discounts and they carry near zero engagement.",
  ["https://instagram.com/p/DQxDySAjFue"],
  "Design only. No percentage, no deadline, no urgency strip."),
]

# Treatment courses followed across the quarter, with their real footage.
CASE_FILES = {
 "C1":("Mehwish","Laser Hair Removal, sessions 1 to 6",6,
       "Models Videos / Mehwish / Visit_01 to Visit_06",
       "VERIFIED silent b-roll, no interview. Session numbers and dates carry the story on screen."),
 "C2":("Neelum","Venus Viva, sessions 1 to 3",3,
       "Models Videos / Neelum, Neelum 2nd Visit, Neelum 3rd Visit",
       "Three filmed sessions. Completes inside the quarter."),
 "C3":("Rabia","Skin Tightening and Dark Circles",3,
       "Models Videos / Lhr Data / Rabia",
       "Two treatments sequenced rather than stacked. Includes a talking-head shoutout to subtitle."),
 "C4":("Fateh","PRP and Party Peel",3,
       "Models Videos / Lhr Data / Fateh",
       "Male course. Kabeer's PRP films are already posted, so Fateh's footage is used instead."),
 "C5":("Male Model 01","Male laser and tightening",3,
       "Models Videos / Lhr Data / Male Model 01",
       "Carries Week 11, which is given entirely to men."),
}
