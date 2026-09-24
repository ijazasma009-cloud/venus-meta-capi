# -*- coding: utf-8 -*-
"""WEEKS 1-4  |  7 Sep - 4 Oct 2026

source values:
  DRIVE_READY   footage exists and is ready to post as is
  DRIVE_EDIT    footage exists but needs a cut, spec says exactly what
  SHOOT_TALK    someone speaks to camera, full script supplied
  SHOOT_ENGAGE  engaging video, must be shot, record guide supplied
  SHOOT_BROLL   filming needed, no speaking
  DESIGN        carousel or static, slide by slide spec supplied
Nobody is ever quoted. Where a patient speaks on camera the spec says subtitle their real words.
"""

ROWS = [

# ───────────────────────────────── WEEK 1 ─────────────────────────────────
{"date":"2026-09-07","week":1,"format":"Treatment Film","treatment":"Laser Hair Removal (Primelase)","creative":"Reel",
 "hook":"Shaving every second day? There is a way out. ✨",
 "caption":"Let's be honest. Shaving is a chore that never ends. Two days later you are back where you started. 😮‍💨\n\nLaser hair removal at Venus uses Primelase with Crystal Freeze cooling, so the session is quick and far more comfortable than people expect. Underarms take minutes. You are back in the car before your tea goes cold. ☕\n\nIt works as a course, not a one off, and we will tell you exactly how many sessions your hair type needs at your free patch test. No guessing, no pressure.\n\nBook your free consultation at any of our 8 branches. 💛",
 "hashtags":"#VenusAesthetics #LaserHairRemoval #Primelase #SmoothSkin #LahoreClinic #KarachiBeauty #IslamabadSkin #PakistanSkincare #LaserHairRemovalPakistan",
 "cta":"Comment SMOOTH or DM us and we will book your free patch test.",
 "source":"DRIVE_READY","asset":"Drive: Models Videos / Mehwish / Visit_01 / Mehwaish Laser.mp4",
 "editNeeded":False,
 "spec":"READY TO POST AS IS. Verified 48 seconds of finished treatment b-roll: gel application in black gloves, "
        "Primelase Blend handpiece, underarm and arm passes, patient in goggles, dark cinematic grade.\n\n"
        "IF you want it tighter: trim to the first 30 seconds and end on the close up of the handpiece. Nothing else needed. "
        "Do not add a voiceover. There is no patient audio in this file and none should be invented.",
 "script":None,"recordGuide":None,"ref":"vid_treatment_film"},

{"date":"2026-09-08","week":1,"format":"The Course","treatment":"Skin Rejuvenation (Venus Viva)","creative":"Reel",
 "hook":"Session 1 of 3. Watch this space. 👀",
 "caption":"Texture is the thing foundation cannot fix. 🙃\n\nThis is session one of a three session Venus Viva course. RF microneedling, which works below the surface where texture and pigment actually sit. A facial cannot reach that layer. This can.\n\nWe are filming all three sessions and posting them with the real dates on screen, so you can see how long it genuinely takes rather than a before and after with no timeline. ⏳\n\nSessions are four weeks apart. Session 2 lands in October.\n\nIs your skin suitable? That is a five minute conversation, and it is free. 💛",
 "hashtags":"#VenusAesthetics #VenusViva #RFMicroneedling #SkinTexture #GlowUp #AcneScars #SkinRejuvenation #PakistanSkincare #LahoreAesthetics",
 "cta":"Comment VIVA and we will check if your skin suits this course.",
 "source":"DRIVE_EDIT","asset":"Drive: Models Videos / Neelum / VenusViva_Nelum_Opt_01.mp4",
 "editNeeded":True,
 "spec":"EDIT NEEDED. Cut to 25 to 30 seconds.\n\n"
        "SHOT ORDER\n"
        "0:00-0:03  Open on the Venus Viva handpiece close up, not on a face. Hard cut in on the beat.\n"
        "0:03-0:10  Numbing cream going on. Keep this. It is the unglamorous part that makes it believable.\n"
        "0:10-0:20  The treatment pass itself. Use the tightest available framing.\n"
        "0:20-0:25  Patient sitting up, calm, end frame.\n\n"
        "ON SCREEN TEXT\n"
        "Frame 1, top left, held for the entire clip: SESSION 1 OF 3\n"
        "Under it, smaller: 8 SEPTEMBER 2026\n"
        "Both stay up the whole way through. This is the device that makes the series work.\n"
        "Last 3 seconds, centre: SESSION 2 IN OCTOBER\n\n"
        "AUDIO  Music bed only. No voiceover. There is no usable patient audio in this file.\n"
        "GRADE  Leave as shot. It is already graded dark and warm.",
 "script":None,"recordGuide":None,"ref":"vid_course_parts"},

{"date":"2026-09-09","week":1,"format":"Skin School","treatment":"Dermatology / Pigmentation","creative":"Carousel",
 "hook":"Melasma, tan and acne marks are not the same thing 🛑",
 "caption":"And that is exactly why the cream you have been using for eight months has done nothing. 😔\n\nThree different problems. Three different causes. Three completely different treatments. Most people are treating all of them as one, and then blaming their skin.\n\nSwipe through and find yours. Slide 4 is the one almost everybody gets wrong.\n\nIf you are not sure which one you have, that is genuinely what a consultation is for, and ours costs nothing. 💛",
 "hashtags":"#VenusAesthetics #Melasma #Pigmentation #AcneScars #SkinEducation #DermatologyPakistan #SkincareTips #LahoreSkinClinic #GlowingSkin",
 "cta":"Save this. Comment SKIN and we will tell you which one you are dealing with.",
 "source":"DESIGN","asset":"Carousel, 5 slides","editNeeded":False,
 "spec":"CAROUSEL, 5 SLIDES. 1080x1350. Brand: white ground, black type, one accent per slide.\n\n"
        "SLIDE 1  THE HOOK\n"
        "  Background: white\n"
        "  Heading, large, centred: Melasma, tan or acne marks?\n"
        "  Sub line under it, smaller grey: Three problems. Three treatments. One of them is yours.\n"
        "  Bottom right, small: SWIPE →\n"
        "  Image: none. Type only. Keep it clean so it reads at thumbnail size.\n\n"
        "SLIDE 2  MELASMA\n"
        "  Background: white, with a soft close up of cheek pigmentation on the right half\n"
        "  Heading top left: MELASMA\n"
        "  Body, 3 short lines:\n"
        "    Sits deeper in the skin\n"
        "    Triggered by hormones, heat and sun\n"
        "    Comes back if the trigger is not managed\n"
        "  Footer strip: Treated with a dermatology plan, not a cream alone\n\n"
        "SLIDE 3  SUN TAN\n"
        "  Background: white, close up of forearm or face showing even darkening\n"
        "  Heading: SUN TAN\n"
        "  Body:\n"
        "    Sits on the surface\n"
        "    Even, and it fades on its own over months\n"
        "    Responds fastest of the three\n"
        "  Footer strip: Treated with peels and Venus Glow\n\n"
        "SLIDE 4  POST ACNE MARKS  (mark this slide THE ONE PEOPLE GET WRONG)\n"
        "  Background: white, close up showing flat brown marks where spots have healed\n"
        "  Heading: POST ACNE MARKS\n"
        "  Body:\n"
        "    Not scars. Flat, not pitted.\n"
        "    Left behind after a spot heals\n"
        "    Fades, but slowly, and picking makes it worse\n"
        "  Footer strip: Treated with Venus Viva or a dermatology plan\n\n"
        "SLIDE 5  THE CTA\n"
        "  Background: black, white type. Only dark slide in the set, so it lands.\n"
        "  Heading: Not sure which one is yours?\n"
        "  Body: A dermatologist can tell in five minutes. Our consultation is free.\n"
        "  Bottom: 8 branches. Lahore. Karachi. Islamabad. Faisalabad. Gujranwala.\n"
        "  Small: Comment SKIN or send us a message\n\n"
        "DESIGNER NOTE  Use real skin close ups from the Dr. Uzair stills set if suitable. "
        "Do not use stock imagery of European skin. Pakistani skin tones only.",
 "script":None,"recordGuide":None,"ref":"car_why_results_differ"},

{"date":"2026-09-10","week":1,"format":"Ask Venus","treatment":"Laser Hair Removal","creative":"Reel",
 "hook":"How many sessions will I actually need? 🤔",
 "caption":"The honest answer is that it depends, and anyone giving you a single number before they have seen your hair is guessing. 🙂\n\nOur laser practitioner explains what actually decides it: your hair colour, your hormones, and how well you keep to the four week gaps.\n\nThis is why we do a free patch test first. We would rather tell you the real number up front than sell you a package that does not fit.\n\nAsk us anything. We answer these on camera every week. 💛",
 "hashtags":"#VenusAesthetics #LaserHairRemoval #AskVenus #SkincareQuestions #Primelase #PakistanClinic #LaserSessions #SmoothSkin",
 "cta":"Drop your question in the comments and we may film the answer next week.",
 "source":"SHOOT_TALK","asset":"SHOOT: Ask Venus 01","editNeeded":True,
 "spec":"SHOOT. One practitioner, seated, single angle, 35 to 45 seconds.\n\n"
        "SETUP\n"
        "  Location: consultation room, Primelase machine visible but softly out of focus behind\n"
        "  Framing: chest up, camera at eye level, vertical 9:16\n"
        "  Wardrobe: Venus black scrubs, name badge visible\n"
        "  Lighting: soft key from window side, no harsh overhead\n\n"
        "ON SCREEN TEXT\n"
        "  0:00-0:04  Practitioner NAME and ROLE, lower third, e.g. AYESHA · LASER PRACTITIONER\n"
        "  0:00-0:03  Question as a title card top of frame: HOW MANY SESSIONS WILL I NEED?\n"
        "  Burned in English subtitles for the whole clip. Most people watch on mute.\n\n"
        "EDIT\n"
        "  Cut all preamble. The answer must start within 2 seconds.\n"
        "  No cutaways, no music under speech. Single angle throughout.\n"
        "  End frame 2 seconds: ASK US ANYTHING, plus the Venus logo.\n\n"
        "B-ROLL to grab while you are there, for later posts: handpiece close up, machine screen, "
        "gel bottle, goggles going on.",
 "script":"ASK VENUS 01  ·  HOW MANY LASER SESSIONS WILL I NEED?\n"
          "Speaker: laser practitioner. Target 40 seconds. Speak normally, do not read this flat.\n\n"
          "[Look straight to camera]\n"
          "The question we get most is how many laser sessions you will need. And I am not going to give you one number, "
          "because anyone who does that before seeing your hair is guessing.\n\n"
          "[Beat]\n"
          "Here is what actually decides it. First, your hair colour. Darker, coarser hair responds faster, which is good "
          "news for most Pakistani skin. Second, your hormones. If there is a hormonal cause behind the growth, that changes "
          "the plan. And third, and this is the one people underestimate, whether you keep to your four week gaps.\n\n"
          "[Slight smile]\n"
          "The people who get the best results are not the ones with the best hair. They are the ones who show up on schedule.\n\n"
          "[Close]\n"
          "So come in for the free patch test. We will look at your hair, tell you the real range, and if laser is not right "
          "for you, we will say that too.",
 "recordGuide":None,"ref":"vid_practitioner_qa"},

{"date":"2026-09-11","week":1,"format":"Really Feels Like","treatment":"Laser Hair Removal","creative":"Carousel",
 "hook":"Things that hurt more than laser 😅",
 "caption":"Waxing. Threading your eyebrows. Stubbing your toe on the bed frame at 2am. 🛏️\n\nWe are not going to tell you laser feels like nothing, because that would be a lie and you would find out in about four seconds. It feels like a warm elastic band. The Crystal Freeze cooling on our Primelase runs at the same time, which takes most of it away.\n\nUnderarms are over before you have settled. Upper lip is nothing. The bikini line is the one everyone talks about afterwards. 😬\n\nSwipe for the honest version, area by area.",
 "hashtags":"#VenusAesthetics #LaserHairRemoval #DoesItHurt #HonestSkincare #Primelase #CrystalFreeze #PakistanBeauty #LaserTruth",
 "cta":"Comment LASER and ask us the question you are too shy to ask.",
 "source":"DESIGN","asset":"Carousel, 4 slides","editNeeded":False,
 "spec":"CAROUSEL, 4 SLIDES. 1080x1350. Playful, not clinical. This is modelled on SkinSpirit's pain carousel.\n\n"
        "SLIDE 1  THE JOKE\n"
        "  Background: white\n"
        "  Heading, very large, centred: Things that hurt more than laser\n"
        "  Below, a simple list in lighter grey, one per line with a small emoji each:\n"
        "    Waxing 😖\n"
        "    Threading 😣\n"
        "    That bed frame at 2am 🛏️\n"
        "  Bottom right: SWIPE for the honest version →\n\n"
        "SLIDE 2  WHAT IT ACTUALLY FEELS LIKE\n"
        "  Background: white, with a soft close up of the Primelase handpiece on the right\n"
        "  Heading: So what does it feel like?\n"
        "  Body, short lines:\n"
        "    A warm elastic band, snapped quickly\n"
        "    Crystal Freeze cooling runs at the same time\n"
        "    Most people describe it as odd, not painful\n\n"
        "SLIDE 3  AREA BY AREA  (the useful slide)\n"
        "  Background: white. Simple two column layout, area on the left, rating on the right.\n"
        "  Heading: Area by area, honestly\n"
        "  Rows:\n"
        "    Underarms          Easy. Over in minutes.\n"
        "    Upper lip          Barely anything.\n"
        "    Legs               Long, but comfortable.\n"
        "    Bikini line        This is the one people mention.\n"
        "  Use a small filled dot scale (1 to 3 dots) beside each row rather than numbers.\n\n"
        "SLIDE 4  THE CTA\n"
        "  Background: black, white type\n"
        "  Heading: Still not sure?\n"
        "  Body: Come in for a free patch test. You will feel exactly one pulse and then you will know.\n"
        "  Bottom: 8 branches across Pakistan · Free consultation\n\n"
        "DESIGNER NOTE  Keep the humour in the type, not in clip art. No cartoon graphics.",
 "script":None,"recordGuide":None,"ref":"car_sensation"},

{"date":"2026-09-12","week":1,"format":"Engaging","treatment":"None","creative":"Reel",
 "hook":"When she says she is going for a facial 💅",
 "caption":"Every single one of you booking a consultation and telling nobody. 🤫\n\nYour secret is safe with us.",
 "hashtags":"#VenusAesthetics #ClinicLife #Relatable #SkincareSecret #PakistanBeauty #TeamVenus",
 "cta":"Tag the friend who does exactly this.",
 "source":"SHOOT_ENGAGE","asset":"SHOOT: Engaging 01","editNeeded":True,
 "spec":"ENGAGING VIDEO, must be shot. 10 to 15 seconds. Phone shot, vertical. Do not over produce it.\n\n"
        "ON SCREEN TEXT\n"
        "  Single line, top third, held throughout: When she says she is 'just going for a facial'\n"
        "  No other text. Let the performance carry it.\n\n"
        "EDIT  Almost none. One or two cuts maximum. Trending audio, no voiceover.",
 "script":None,
 "recordGuide":"HOW TO RECORD THIS\n\n"
        "Who: two staff members. One at reception, one walking past.\n"
        "Where: reception desk, normal lighting, no special setup.\n"
        "Kit: a phone. Vertical. That is genuinely all.\n\n"
        "THE BEAT\n"
        "  1. Staff member A is at the desk, being deliberately casual and innocent.\n"
        "  2. Staff member B walks past and gives a knowing look straight down the lens.\n"
        "  3. Hold on that look for a full second. The pause is the joke.\n\n"
        "DIRECTION\n"
        "  Deadpan. Nobody laughs, nobody mugs at the camera. The straighter they play it, the funnier it is.\n"
        "  Shoot it four or five times and take the flattest one.\n"
        "  Total time on set: under ten minutes.\n\n"
        "WHY THIS WORKS  The reference below is the same joke structure and it is the highest engaging result "
        "found anywhere in this research, at 4.46 percent, shot on a phone with two staff and no budget.",
 "ref":"eng_secret"},

{"date":"2026-09-13","week":1,"format":"Patient Result","treatment":"Skin Rejuvenation","creative":"Reel",
 "hook":"She finished her course. Here is what she said. 💬",
 "caption":"We asked one question on her last session and let the camera run. ✨\n\nVenus Viva is a course of three, four weeks apart, and results keep building for weeks after the last one. Every skin responds differently, which is why we assess before we ever sell a package.\n\nHer words, not our caption.",
 "hashtags":"#VenusAesthetics #VenusViva #RealResults #ClientReview #SkinRejuvenation #PakistanSkincare #GlowUp #LahoreClinic",
 "cta":"Comment VIVA to book your free skin assessment.",
 "source":"DRIVE_EDIT","asset":"Drive: Models Videos / Hafsa / Testimonial_Hafsa.mp4",
 "editNeeded":True,
 "spec":"EDIT NEEDED. Verified: this file is a patient speaking to camera. Roughly 20 seconds.\n\n"
        "CRITICAL  Subtitle EXACTLY what she says. Do not paraphrase, do not write a line for her, "
        "do not add a voiceover. If a sentence is unclear, cut it rather than guessing at it.\n\n"
        "EDIT\n"
        "  Trim any dead air at the top so she is speaking within the first second.\n"
        "  Single angle, no cutaways over her face.\n"
        "  If you need to shorten, cut whole sentences, never mid sentence.\n\n"
        "ON SCREEN TEXT\n"
        "  Lower third for the first 4 seconds: HAFSA · VENUS VIVA · 3 SESSIONS\n"
        "  Burned in English subtitles throughout, high contrast, bottom third.\n"
        "  End frame 2 seconds: FREE SKIN ASSESSMENT AT ALL 8 BRANCHES\n\n"
        "AUDIO  Her voice clean and forward. Light music bed underneath at low level, nothing over her words.",
 "script":None,"recordGuide":None,"ref":"vid_result"},
]
