export const meta = {
  name: 'venus-q4-calendar-write-v2',
  description: 'Write 95 Venus Aesthetics posts for Q4 2026 with a dedicated engagement day, then compliance-verify every one',
  phases: [
    { title: 'Write', detail: 'one agent per themed week, 7 posts each, against a locked fact whitelist' },
    { title: 'Verify', detail: 'compliance pass per week: banned words, Roman Urdu, invented facts, caption shape' },
  ],
}

const RULES = `
YOU ARE WRITING FOR: Venus Aesthetics, a premium 8-branch aesthetic clinic chain in Pakistan.
Lahore, Karachi, Islamabad, Faisalabad, Gujranwala. 148,000 followers. Operating since 2018.
Treatments: laser hair reduction, skin tightening (RF), RF microneedling, fat freezing, PRP for hair
and face, Venus Glow HydraFacial, chemical and party peels, Venus Viva resurfacing, dermapen,
dark circle treatment, hyperhidrosis, K-Beauty glow boosters.

=== ABSOLUTE RULES. Breaking any one makes the post unusable. ===
1. ENGLISH ONLY. No Roman Urdu anywhere, not in captions, on-screen text or scripts.
   No "glow ka mood", no "bilkul", no "ye sirf", nothing transliterated.
2. NEVER invent a fact, number, statistic, patient quote, review or result. Use ONLY the FACT
   WHITELIST below. If a number is not on the list, do not write it.
3. NEVER put words in a patient's mouth. No invented testimonial text, no quotation marks around
   anything a patient supposedly said.
4. NO DISCOUNTS of any kind. A standing free consultation may be mentioned as a service.
5. NO EM DASHES. Use commas or full stops.
6. BANNED WORDS: permanent, painless, safe, guaranteed, cure, flawless, best, number one, magic,
   miracle, "best version of yourself", "say goodbye to". The permitted term is "hair reduction",
   never "hair removal", except inside the bracketed search keyword block.
7. NEVER name Botox or any botulinum brand. Pakistan's Therapeutic Goods Advertisement Rules 2025
   require DRAP approval. Write "an assessment for lines and wrinkles following professional evaluation".
8. NO ENGAGEMENT BAIT. Banned: "comment YES", "tag a friend", "tag someone", "double tap", "share if
   you agree". A genuine specific question is fine. "Send this to the friend who..." is fine.
9. THE DOCTOR IS NEVER THE SUBJECT. Dr. Uzair may answer a question but his name never appears in the
   hook, the first caption line, or frame 1. The QUESTION is the subject.
10. NO APPEARANCE-DEFECT HOOKS. Frame on behaviour or outcome, never attack a body part.
11. NEVER claim a treatment reverses or prevents pollution damage, or that particles penetrate intact skin.
12. NO exosome regrowth claims. NO prices.
13. Emojis: zero or one per caption, never in line 1.

=== FACT WHITELIST. The ONLY numbers and claims you may state. ===
LASER: A 150 patient series on Fitzpatrick IV to VI skin averaged 8.9 treatments, range 4 to 22, and
54.3% mean hair reduction. Hair responds only in its growth phase and no area is ever entirely in that
phase at once, which is why sessions sit 4 to 6 weeks apart. Most Pakistani skin is Fitzpatrick IV or V.
The long-pulsed 1064 nm Nd:YAG competes least with epidermal melanin. A patch test is read at 48 hours.
FAT FREEZING: changes as early as 3 weeks, more obvious at about 2 months, 15 to 28% fat reduction at
around 4 months, no repeat on the same area before 6 to 8 weeks. It is not weight loss.
LAHORE AIR: AQI 331 on 29 October 2025 with PM2.5 at 48.1 times the WHO annual guideline. AQI 527 at
8pm on Saturday 13 December 2025. November 2024 citywide peaks of 1067. Average daily maximum UV index
6 in October, 4 in November, 3 in December. Named mechanisms you may use: reactive oxygen species
generation, NF-kB and MAPK activation, downregulation of filaggrin and loricrin causing barrier
dysfunction and increased transepidermal water loss, PPAR-gamma driven sebum increase relevant to acne,
MMP-1 upregulation, increased melanin via the IRE1 alpha pathway. A Korean cohort of 5,591,500 adults
followed a median 12.5 years found more new androgenetic alopecia with higher particulate exposure,
rising even at moderate air quality. PERMITTED CLAIM: the evidence links air pollution to hair loss risk
even at moderate levels. You may NOT quantify a Lahore figure and may NOT say any treatment undoes it.
HAIR SHEDDING: studies find telogen shedding highest around August to October, lowest December to
February, BUT those are 1996 and 1999 European cohorts of people already complaining of hair loss, and
the effect is described as more summer than autumnal above the Tropic of Cancer, which includes Lahore.
So the honest October message is that shedding is already underway and easing, NOT peaking.
PEELS: strict sun avoidance with broad spectrum sunscreen before and after. Fitzpatrick III to VI carry
elevated risk of post-peel hyperpigmentation, the most common complication of TCA peeling, and it can
occur at any time after. UV 3 in December is still the level at which sunscreen is routinely advised.
PAKISTAN REGULATORY: the Punjab Healthcare Commission ran 6,380 raids in six weeks and sealed 1,415
centres, including 1,153 operational illegal treatment centres. The Sindh Healthcare Commission sealed
18 aesthetic centres in Karachi of more than 80 inspected, and 10 more in DHA, where operators included
a sociology graduate, a midwife and a physiotherapist performing PRP. Only 26 aesthetic facilities are
registered with the SHCC against industry estimates of around 10,000 practitioners. NEVER name a
competitor and never imply a specific rival is illegal. Speak about the category.
WEDDING SEASON: opens October, runs to March. Sunday is the peak function day. Couples begin venue
hunting about three months before the date. Ramadan 2027 is expected to begin around 8 February 2027
with Eid al-Fitr around 10 March 2027, subject to the Ruet-e-Hilal Committee.
DATES: Sunday 8 November 2026 Diwali. Monday 9 November 2026 Iqbal Day. Friday 25 December 2026
Quaid-e-Azam Day and Christmas. Saturday 26 December 2026 holiday for Christians only.
VENUS'S OWN: 8 branches, operating since 2018, more than 10,000 Google reviews.

=== PLATFORM FACTS THAT SHAPE THE WRITING (never put these in captions) ===
Average reel watch time is 8.5 seconds and nothing in the first 3 seconds may be branding. Instagram's
top ranking signals are watch time, likes and sends, and sends matter most for reaching non-followers.
Carousels out-engage reels per person reached and drive far more saves. Instagram's Pakistani audience
is roughly 63% male and male-directed content is under-served. Since 30 April 2026 Instagram demotes
accounts posting content they did not create, so everything must be shot in-branch.
VENUS'S OWN REALITY: organic reach is about 5,000 to 25,000 plays. Anything above that was paid. Their
best engagement ever came from the team being human, not from treatment films.

=== CAPTION ARCHITECTURE. Follow exactly. Reels 40 to 70 words, carousels 90 to 150. ===
  L1   The promise, worded DIFFERENTLY from the on-screen hook, containing the treatment name.
       Under 90 characters. No greeting, no brand name, no emoji.
  L2   blank
  L3-4 The proof detail. One fact per line.
  L5   blank
  L6-7 The objection answered plainly. The limitation goes BEFORE the benefit.
  L8   blank
  L9   The withheld thing, named. Rotate between three only: the patch test range, candidacy,
       and machine settings.
  L10  blank
  L11  ONE genuine specific answerable question, OR one send-ask naming a recipient. Never both.
  L12  blank
  L13  Branch line, e.g. "Venus Aesthetics, DHA Phase 5 Lahore. Monday to Saturday, 11am to 8pm."
  L14  "Call or WhatsApp on the number in bio."
  L15  blank
  L16  3 to 5 hashtags
  L17  A bracketed keyword block of 5 to 7 plain search phrases

WORKED EXAMPLE, laser:
  Nine sessions, not three. That is what the published research says about skin like ours.

  Hair only responds while it is in its growth phase, and no area is ever entirely in that phase at once.
  That is why your sessions sit four to six weeks apart and not two.

  A 150 patient series on Fitzpatrick IV to VI skin averaged close to nine sessions, with a range from
  four to twenty two. Nobody can honestly quote you three.

  What we will not put in a caption is your range. You get that at the patch test, read at 48 hours.

  Which area were you told would take three sessions?

  Venus Aesthetics, DHA Phase 5 Lahore. Monday to Saturday, 11am to 8pm.
  Call or WhatsApp on the number in bio.

  #laserhairreduction #laserhairremovallahore #dhalahore #venusaesthetics
  [laser hair reduction how many sessions, laser hair removal Lahore price, laser on brown skin
  Pakistan, Nd YAG for deeper skin tones, underarm laser sessions, laser patch test Lahore]

=== HASHTAGS: 3 to 5, in the caption. ===
Treatment: #laserhairreduction #hydrafacial #microneedlingrf #skintightening #chemicalpeel
  #prphairtreatment #fatfreezing #venusviva
Geo: #lahore #dhalahore #gulberglahore #johartown #islamabad #f7islamabad #karachi #faisalabad
Brand: #venusaesthetics   Concern: #pigmentation #acnescars #hairfall #openpores #hyperhidrosis
BANNED: #laserhairremoval as a claim, #permanenthairremoval, #skinwhitening, #botox, any superlative,
#sale #discount #offer, and broad global tags like #skincare or #beauty.

=== THE PILLARS ===
THE FULL PASS (Monday, Reel 25 to 45 seconds, goal reach)
  This is a TREATMENT FILM, not a clip. The source footage runs 24 to 67 seconds and it has a real
  arc: prep, the pass itself, the reaction, the finish. USE THAT ARC. Do not reduce a 50 second film
  to 8 seconds, that throws the asset away and it is the single thing the client most objects to.
  Frame 1 is the device or handpiece ALREADY IN MOTION on skin. No logo, no face, no title card,
  nothing branded in the first 3 seconds. Burned-in English text carries the hook at frame 1 and then
  one short line per beat as the pass progresses. Cut on sensation and on visible change. Hold the
  final frame on the finished area with no CTA card.
  EVERY Full Pass post also banks a SECOND, SHORTER CUT from the same source, 8 to 12 seconds, built
  from the single strongest beat. Name that beat precisely in the spec, with its timecode range if you
  can infer it, and say it is banked for Stories and for reuse. One shoot, three uses: the film, the
  short cut, and the still frames for a later carousel.
  When the row says subPillar "The Men's Room", the same format but male-directed: beard line and neck,
  back and chest, body. Direct and unfussy, no floral language. This audience is two thirds of the
  platform in Pakistan and Venus has never addressed it.

THE DECISION TABLE (Tuesday, Carousel 8 to 10 slides, goal saves)
  Slide 1 a text hook frame naming a decision, music attached. Slides 2 to 7 one variable per slide,
  one fact per slide, under 25 words each. Slide 8 or 9 is the DECISION RULE, never a verdict, because
  Venus sells both sides. Final slide the consultation ask.

THE HONEST NUMBER (Wednesday, Reel, goal trust)
  One specific number or one refusal is the whole post. Declining business is the least fakeable trust
  signal available. When the row says subPillar "The Tray": a 15 to 20 second single take of the
  treatment tray being set up. Sealed packaging opened on camera, disposables unwrapped, tip or needle
  gauge visible, device screen showing the parameter set, batch or expiry label held to lens, surfaces
  wiped. NO PATIENT IN FRAME. One on-screen line naming what is single use and what is sterilised.

MATCHED FRAME (Thursday, goal proof)
  Identical lighting, camera distance, angle, background, posture. Only the treated area differs. No
  filter or grading on either frame and never on one only. Three fixed on-screen fields: treatment name,
  sessions completed, and how long after the last session. Fixed line "Result shown is this patient only."
  Faceless by default. PREFER MID-COURSE: "Session 3 of 6" with visibly partial progress is more credible.

ASKED AND ANSWERED (Friday, Reel from the existing Dr. Uzair FAQ library, goal authority)
  The question is the title, the subject and frame 1. Frame 1 is large English on-screen text carrying
  the question verbatim over device or process b-roll, NEVER over the doctor's face. His answer runs as
  audio with the existing burned-in English subtitles. Cut away to hands, the machine screen, the tray.
  NOTE ON THE SOURCE FILES: they are 4K vertical, he speaks English, and the existing word-level English
  subtitles are already burned in. Their one weakness is the opening card, which is small low-contrast
  serif type on pale grey. Every edit note must say to replace that card with large high-contrast text.

THE ROOM (Saturday, Reel, goal comment or send) === THIS IS THE ENGAGEMENT DAY ===
  The single most important slot in the week for this client, because Venus's own best-performing
  organic posts have always been the team being human, never a treatment film.
  It is humour, culture, team, behind the scenes and relatable clinic life. The treatment is the
  punchline or the backdrop, never the lecture.
  THE PRODUCTION RULE THAT MATTERS: the highest engagement rates in the entire competitor audit came
  from the SMALLEST productions. One staff member, one line, deadpan, shot on a phone in a treatment
  room, 4.46% engagement. Venus's problem is the opposite: high production, huge paid reach, no response.
  So every Room post must be shootable in under fifteen minutes with a phone and no crew.
  EVERY Room post MUST carry BOTH:
    - reference: the content reference, a real reel that proves the format
    - editReference: a second real link showing the EDITING and pacing to copy, plus a written
      description of exactly what to copy about the cut, the text style, the timing and the sound
  Where existing footage is supplied, the editNote must be surgical and must fix any defect named in
  the row. Where no footage is supplied, write a full recordGuide: who, where, kit, the beat by beat,
  the direction, and the total time on set.

BIOLOGY COUNTDOWN (Sunday in October and December, Carousel, goal sends)
  Urgency from biology instead of a discount. A dated card. Frame 1 a specific function date. Each line
  one treatment with its real lead time and one of three verdicts: still possible, last week for this,
  or start now for next season. State A LEAD TIME REQUIRED, never A RESULT GUARANTEED BY A DATE.
  Built to be screenshotted and forwarded to one person, not read.

SMOG DIARY (Sunday in November, Carousel, goal sends)
  Fixed three frame template, only the number changes each week. Frame 1 the week's Lahore AQI reading.
  Frame 2 one named mechanism. Frame 3 one concrete countermeasure. NEVER a mechanism without a
  countermeasure in the same post.

BRANCH DESK (break days, Carousel, goal local intent)
  Pure branch utility. This branch, this address, these hours, this WhatsApp number, this week's
  operational note. Location tag the specific branch, never the city.

=== EVERY POST DECLARES ONE GOAL AND THE CTA IS WRITTEN FOR IT ===
  save -> worth returning to.  send -> name the recipient.  comment -> an easy but meaningful question.
  dm -> a natural next step.   profile -> withhold the specific thing and say where it is answered.
NEVER use a treatment name as a comment trigger. Asking a woman to publicly comment a treatment name is
asking her to disclose in front of her own followers. Route private concerns to saves and DMs.
`

const REFS = `
=== REFERENCE LIBRARY. Every reference MUST MATCH THE POST'S FORMAT. ===
A carousel references a carousel or static post. A reel references a reel. If nothing here fits the
format and the point, set reference to "" and refWhy to "". Never invent a URL.

--- ENGAGING AND HUMOUR REELS, for The Room. These carry the highest engagement rates found anywhere. ---
- https://instagram.com/p/DcO5LR-AqU0 | Sculpt Spa, "No time to gossip". Six words, deadpan, one staff
  member, shot on a phone in the treatment room, no production at all.
  2k plays, 95 likes, 4.46% ER, the best humour result in the whole audit.
- https://instagram.com/p/DZ0ZWodCjuC | Sculpt Spa, "All jokes aside, we are totally fine with being
  your little secret." Plays on the fact that nobody tells anyone they come. 3k plays, 115 likes, 3.60% ER.
- https://instagram.com/p/Da3V-BPDlj9 | Sculpt Spa, "Guess I will try again tomorrow." The failed
  attempt is the entire joke. 4k plays, 83 likes, 2.37% ER.
- https://instagram.com/p/DbWn5UlhfRx | Alchemy 43, two staff, one trending audio, the treatment as the
  punchline rather than the subject. 3k plays, 1.97% ER.
- https://instagram.com/p/DbWQkkDP7uk | LaserAway, a mother teaching her daughter that looking after
  yourself is necessary. 56k plays, 2,444 likes, 4.45% ER, the highest engagement found anywhere.
- https://instagram.com/p/DbdqueMOmLU | Skin Laundry, "between the errands, the emails and everything
  else". The clinic is never mentioned. 10k plays, 0.46% ER.
- https://instagram.com/p/DcBxwo1CCE2 | Pulse Light London, "You are not going to believe this, but we
  think you should wear sunscreen." Personality over information. 3k plays, 1.17% ER.
- https://instagram.com/p/DcZhRGkAMFZ | Milan Laser, nine words, one treatment, no explanation. An
  entire chain runs on this. 6k plays, 0.76% ER.
- https://instagram.com/p/DcBiLzXCXoW | VENUS'S OWN, the team celebrating Independence Day, no treatment
  in sight. 8,900 plays, 87 likes, 0.99% ER, one of their three best ever.
- https://instagram.com/p/DYIP3yWCjc6 | VENUS'S OWN, the team on Mother's Day. 7,682 plays, 70 likes, 0.98% ER.
- https://instagram.com/p/DUDpXQDFTfk | VENUS'S OWN, absurdist penguin. 1,783,781 plays, 2,656 likes.
- https://instagram.com/p/DaddvlVkZyk | VENUS'S OWN, a POV blooper where the balloon had other plans.
  26,766 plays, 118 likes, 0.47%.
- https://instagram.com/p/DQe0j3BCOWI | VENUS'S OWN, "POV: you open something you weren't supposed to".
  55,827 plays, 122 likes, 22 comments.
- https://instagram.com/p/DN7FCmVkvnX | VENUS'S OWN, a pause-the-video game, Stop the Sunblock and Win.
  2,388,358 plays, 206 comments, their highest comment count outside a giveaway.
- https://instagram.com/p/DP0GawgAQSH | VENUS'S OWN, Babar Azam. 6,699,036 plays, 54,026 likes, 0.81% ER,
  the single biggest engagement event in the account's history.

--- EDITING AND PACING REFERENCES, use these as editReference ---
- https://www.instagram.com/p/DctTDGeS6fQ/ | 233,952 plays, 3,554 likes, 10,022 comments. Editing to
  copy: one static camera, face large, no cuts at all, all the work done by overlays. Raw screenshots
  dropped on top rather than designed graphics. Big yellow section-divider cards. 34 seconds.
- https://www.instagram.com/p/DdNliMKI8tx/ | 1,536,752 plays, 27,490 likes, 53,954 comments. The same
  formula scaled. Editing to copy: open on proof of failure in the first 3 seconds, flip to proof of
  success by second 10, then the method as a document, then a one-line close. 31 seconds.
- https://instagram.com/p/DcO5LR-AqU0 | Editing to copy: no cut at all, no music bed, one take, the
  on-screen line appears at frame 1 and never moves. The restraint is the craft.
- https://instagram.com/p/DbWn5UlhfRx | Editing to copy: trending audio drives the cut, two performers
  hit the beat, the text lands on the audio's punch.

--- TREATMENT AND PROOF REELS ---
- https://instagram.com/p/DbdowHqk8H- | Sono Bello, three months on, progress over real elapsed time
  rather than one reveal. 92k plays, 1,930 likes, 2.16% ER.
- https://instagram.com/p/DcByqkjFjzn | Sono Bello, completed treatment, the patient speaks for herself
  with no brand voiceover. 78k plays, 2,003 likes, 2.69% ER.
- https://instagram.com/p/DboqG0evGyt | LaserAway, a male patient filmed plainly on his own terms.
  38k plays, 700 likes, 1.86% ER. Use for The Men's Room.
- https://instagram.com/p/DbIZKAIFRJK | Pulse Light London, what the treatment actually feels like,
  narrated while it happens, including the uncomfortable parts.
- https://instagram.com/p/DbYJ9SjCpZe | Pulse Light London, part two of a numbered series. The part
  number is what brings people back.
- https://instagram.com/p/DQ7tEOBD9a4 | Ideal Image, a named practitioner answers one specific question.
  Their single best performing post. 14k plays, 162 likes, 1.30% ER. Use for Asked and Answered.
- https://www.instagram.com/p/DdWx_IIlPpl/ | VENUS'S OWN best ever engagement rate, 1.03%. A doctor
  answering a pre-event worry with the question as the subject. 4,553 plays, 41 likes.
- https://www.instagram.com/p/DP8oCpqDsQm/ | VENUS'S OWN, a wedding-timed treatment question.
  104,989 plays, 276 likes, 37 comments, 0.30% ER.
- https://instagram.com/p/DcOsYaChl8J | Skin Laundry, the hero treatment filmed and named in the caption
  every time. 9k plays, 0.57% ER.

--- CAROUSELS. Every one crawled with real engagement. A carousel post MUST use one of these. ---
- https://instagram.com/p/DbCGcx9DwhK | SkinSpirit, 4 slides. "Things that hurt more than microneedling."
  Turns the pain question into a joke then answers it honestly. Slide 1 is the joke, the middle slides
  are the comparisons, the last slide reassures. 766 likes, 35 comments.
- https://instagram.com/p/DcNiQjIiFpi | Dr Rashmi Shetty, 7 slides. Why two patients having the same
  treatment get different results. Sequential, and it explicitly continues a previous post so people go
  back and look. 1,787 likes, 28 comments.
- https://instagram.com/p/DaSKpcYAeZD | Dr Jaishree Sharad, 3 slides. Skin boosters, lasers or
  regenerative treatments, which pre-wedding treatments are worth the money. A comparison that helps
  someone choose rather than pushing one option. 390 likes, 15 comments.
- https://instagram.com/p/DbhObcpGpyU | SkinSpirit, 3 slides. One appointment does not always mean the
  final result. Sets expectations before the booking. 496 likes, 21 comments.
- https://instagram.com/p/DbhxnXFkfgr | Dr Rashmi Shetty, 5 slides. One session, maybe two, but never
  the under eye alone. Explains why a concern cannot be treated in isolation. Persuasive because it
  sounds like a caution. 423 likes, 20 comments.
- https://instagram.com/p/DFwKaBjNXTC | SkinSpirit, 3 slides. New to medical aesthetics, a first-timer
  entry point that assumes nothing. 544 likes, 25 comments.
- https://instagram.com/p/DFtgsFSMdtd | SkinSpirit, 3 slides. "Our team trains the trainers." Authority
  stated as fact rather than boast. 542 likes, 36 comments.
- https://instagram.com/p/DF1GC74OC5S | SkinSpirit, 3 slides. Step into the space, the clinic sold as an
  experience rather than a facility. 746 likes, 70 comments. Use for Branch Desk.
- https://instagram.com/p/DbyWRuTlLx8 | SkinSpirit, 3 slides. A new location announced as news, with a
  countdown feel and no discount attached. 533 likes, 39 comments.
- https://instagram.com/p/DbGU_X7CGaQ | Dr Rashmi Shetty, 7 slides. The aesthetics industry has a
  marketing problem and it is costing patients. Taking a position against your own category is the
  strongest trust play available. 465 likes, 16 comments. Use for The Honest Number as a carousel.
- https://www.instagram.com/sonobello/p/C30amLssmwL/ | Sono Bello, a results post with a six field spec
  block where the practitioner is one line of data, not a face. Use for Matched Frame.
- https://www.instagram.com/p/DdIvEhsoN6J/ | Clinic Dermatech, "Not Wedding-Ready. Life-Ready." and
  "Your wedding is for 1 day. Your skin stays with you for 1000 days." Refuses the panic frame.
- https://www.instagram.com/p/DdB3R1BE8bB/ | Oliva, a concern-led hook that stays on behaviour.
- https://www.instagram.com/olivaclinics/p/DdboieCE7N8/ | Oliva, the bracketed keyword block replacing a
  hashtag wall. Strip their superlatives.
- https://instagram.com/p/Da3Vg47xYUq | Face Haus, a new place filmed as a destination. 91k plays,
  2,011 likes, 2.29% ER. Use for Branch Desk.
`

const POST = {
  type: 'object',
  properties: {
    id: { type: 'integer' },
    date: { type: 'string' },
    hook: { type: 'string', description: 'The on-screen first line or slide 1 text. Short, concrete, numeric where possible.' },
    caption: { type: 'string', description: 'Full caption following the architecture exactly, with real line breaks.' },
    hashtags: { type: 'string' },
    keywordBlock: { type: 'string', description: '5 to 7 plain search phrases inside square brackets' },
    goal: { type: 'string', enum: ['save', 'send', 'comment', 'dm', 'profile'] },
    cta: { type: 'string' },
    spec: { type: 'string', description: 'Carousel: SLIDE 1..N each with Background, Heading, Body, Footer, plus a DESIGNER NOTE. Reel: SHOT 1..N with timings, what is on screen, the burned-in text, and an EDITOR NOTE. A designer or editor must work from this with no further questions.' },
    script: { type: 'string', description: 'Word for word script ONLY if someone speaks to camera, else empty string.' },
    recordGuide: { type: 'string', description: 'Who, where, kit, beat by beat, direction, total time on set. ONLY if this needs shooting, else empty string.' },
    editNote: { type: 'string', description: 'Exact edit instruction for the supplied footage, including fixing any defect named in the row. ONLY if a Drive asset is supplied, else empty string.' },
    reference: { type: 'string', description: 'A format-matched URL from the library, or empty string' },
    refWhy: { type: 'string', description: 'One line on what to copy from it, or empty string' },
    editReference: { type: 'string', description: 'REQUIRED on every The Room post: a second URL showing the editing and pacing to copy. Empty string elsewhere.' },
    editRefWhy: { type: 'string', description: 'REQUIRED on every The Room post: exactly what to copy about the cut, text style, timing and sound. Empty string elsewhere.' },
  },
  required: ['id','date','hook','caption','hashtags','keywordBlock','goal','cta','spec','script','recordGuide','editNote','reference','refWhy','editReference','editRefWhy'],
}
const WEEK = { type: 'object', properties: { posts: { type: 'array', items: POST } }, required: ['posts'] }
const VERDICT = {
  type: 'object',
  properties: {
    week: { type: 'integer' },
    violations: { type: 'array', items: { type: 'object', properties: {
      postId: { type: 'integer' }, rule: { type: 'string' }, quote: { type: 'string' }, fix: { type: 'string' },
    }, required: ['postId','rule','quote','fix'] } },
    clean: { type: 'boolean' },
  },
  required: ['week','violations','clean'],
}

const WEEKS = [{"week": 1, "theme": "The season opens", "themeNote": "Wedding season opens in October and a course started now finishes in time. Set the arithmetic up.", "rows": [{"id": 1, "date": "2026-09-28", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "the whole pass, start to finish", "source": "DRIVE_EDIT", "bankSecondCut": true, "asset": {"driveName": "Nellum_Viva.mp4", "treat": "viva", "model": "Neelum 2nd Visit", "dur": 66.9}}, {"id": 2, "date": "2026-09-29", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "this or that, after six sessions", "source": "DESIGN", "frameSource": "Assbeah_Laser.mp4 (52s)"}, {"id": 3, "date": "2026-09-30", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "the real session arithmetic", "source": "DRIVE_READY", "asset": {"driveName": "Is aftercare is Imp_Subtitling.mp4", "treat": "other", "model": "", "dur": 39.5}}, {"id": 4, "date": "2026-10-01", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "session 3 of 6, partial on purpose", "source": "DRIVE_EDIT", "asset": {"driveName": "Fat freeze Mehwish_02.mp4", "treat": "fatfreeze", "model": "Mehwish", "dur": 33.3}}, {"id": 5, "date": "2026-10-02", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "do you offer fat freezing treatment-_Subtitling.mp4", "treat": "fatfreeze", "model": "", "dur": 17.7}}, {"id": 6, "date": "2026-10-03", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "source": "DRIVE_EDIT", "watchedDesc": "The whole team stands looking at their phones, then all look up and point at the lens. Text asks who our dream patient is, answer YOU.", "defect": "DEFECT: the burned-in text reads PATENT, not PATIENT. The text must be re-rendered.", "variant": "the whole team points at the lens", "asset": {"driveName": "WHO'S YOUR DREAM PATENT.mp4", "treat": "engaging", "model": "Engaging Content", "dur": 6.0}}, {"id": 7, "date": "2026-10-04", "dayFull": "Sunday", "pillar": "Biology Countdown", "creative": "Carousel", "variant": "a dated card for a December function", "source": "DESIGN", "frameSource": "Ayesha Kakani Testimonial.mp4 (19s)"}]}, {"week": 2, "theme": "How many sessions, really", "themeNote": "The published average is close to nine sessions, not three. Spend the week on honest numbers.", "rows": [{"id": 8, "date": "2026-10-05", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "what it actually feels like, narrated on screen", "source": "DRIVE_EDIT", "subPillar": "The Men's Room", "bankSecondCut": true, "asset": {"driveName": "Assbeah_Laser.mp4", "treat": "laser", "model": "Asbeah", "dur": 52.4}}, {"id": 9, "date": "2026-10-06", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "the order to do them in", "source": "DESIGN", "frameSource": "Darma Pen.mp4 (56s)"}, {"id": 10, "date": "2026-10-07", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "three things worth knowing before you book", "source": "DRIVE_READY", "asset": {"driveName": "Is RF Micro Neddling af_Subtitling.mp4", "treat": "other", "model": "", "dur": 7.5}}, {"id": 11, "date": "2026-10-08", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "same light, same angle, months apart", "source": "DRIVE_EDIT", "asset": {"driveName": "Mehwish Laser.mp4", "treat": "laser", "model": "Mehwish", "dur": 38.4}}, {"id": 12, "date": "2026-10-09", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "Does venus use FDA approved.mp4", "treat": "other", "model": "", "dur": 17.4}}, {"id": 13, "date": "2026-10-10", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "source": "DRIVE_EDIT", "watchedDesc": "Gloved hand against the yellow-lit wall. Words on each finger unfold one at a time: Treatment, YOU, NEED, VENUS, AESTHTIC, then the palm turns to show BOOK NOW.", "defect": "DEFECT: the glove reads AESTHTIC, misspelled. Either reshoot the hand or mask and relabel that finger.", "variant": "the gloved hand reveal, one word per finger", "asset": {"driveName": "Engaging content_02.mp4", "treat": "engaging", "model": "Lhr Data", "dur": 7.8}}, {"id": 14, "date": "2026-10-11", "dayFull": "Sunday", "pillar": "Biology Countdown", "creative": "Carousel", "variant": "the March bride's session map", "source": "DESIGN", "frameSource": "Ayesha_face lift.mp4 (39s)"}]}, {"week": 3, "theme": "Before the event", "themeNote": "Peels and glow timed to a function, and what genuinely fits inside three weeks.", "rows": [{"id": 15, "date": "2026-10-12", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "the prep nobody films", "source": "DRIVE_EDIT", "bankSecondCut": true, "asset": {"driveName": "Darma Pen.mp4", "treat": "dermapen", "model": "Ayesha 2nd Visit", "dur": 55.7}}, {"id": 16, "date": "2026-10-13", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "what it costs you in time, not money", "source": "DESIGN", "frameSource": "Ayesha LaserTreatment (1).mp4 (50s)"}, {"id": 17, "date": "2026-10-14", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "who we turn away and why", "source": "DRIVE_READY", "asset": {"driveName": "Sideeffects of RF Micro Neddling_Subtitling.mp4", "treat": "other", "model": "", "dur": 17.3}}, {"id": 18, "date": "2026-10-15", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "the area nobody photographs", "source": "DRIVE_EDIT", "asset": {"driveName": "Laser_Mehwish_3rd Visit.mp4", "treat": "laser", "model": "Mehwish", "dur": 25.0}}, {"id": 19, "date": "2026-10-16", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "DoesRFhave minimal downtime_Subtitling.mp4", "treat": "other", "model": "", "dur": 7.2}}, {"id": 20, "date": "2026-10-17", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "source": "DRIVE_EDIT", "watchedDesc": "POV walk through reception, hand held forward, past the GET THE GLOW neon, ending on a purple brochure reading WE PUT ETHICS IN AESTHETICS.", "defect": "Clean, no text defects.", "variant": "the walk in, POV from the front door", "asset": {"driveName": "Engaging content_04.mp4", "treat": "engaging", "model": "Lhr Data", "dur": 7.0}}, {"id": 21, "date": "2026-10-18", "dayFull": "Sunday", "pillar": "Biology Countdown", "creative": "Carousel", "variant": "what still fits in three weeks", "source": "DESIGN", "frameSource": "Daniah Belly tightning (1).mp4 (38s)"}]}, {"week": 4, "theme": "Hair, honestly", "themeNote": "Seasonal shedding is easing rather than peaking. Say so, then separate it from real hair loss.", "rows": [{"id": 22, "date": "2026-10-19", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "the settings on the screen", "source": "DRIVE_EDIT", "bankSecondCut": true, "asset": {"driveName": "Ayesha LaserTreatment (1).mp4", "treat": "laser", "model": "Ayesha Kamran", "dur": 50.3}}, {"id": 23, "date": "2026-10-20", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "who it will not work on", "source": "DESIGN", "frameSource": "Daniah PRP.mp4 (22s)"}, {"id": 24, "date": "2026-10-21", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "what we will not promise", "source": "DRIVE_READY", "asset": {"driveName": "what should yo avoid_Subtitling.mp4", "treat": "other", "model": "", "dur": 28.5}}, {"id": 25, "date": "2026-10-22", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "progress with the spec block", "source": "DRIVE_EDIT", "asset": {"driveName": "Mehwish4th_Visit_Fatfreezemp4.mp4", "treat": "fatfreeze", "model": "Mehwish", "dur": 26.6}}, {"id": 26, "date": "2026-10-23", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "Future of Glowing Skin_Subtitling.mp4", "treat": "other", "model": "", "dur": 11.1}}, {"id": 27, "date": "2026-10-24", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "source": "DRIVE_EDIT", "watchedDesc": "Rotating cast in one treatment chair. A doctor in a white coat, then staff in black uniforms take turns sitting and posing while the group stands around.", "defect": "Clean.", "variant": "the chair swap, the whole team takes a turn", "asset": {"driveName": "Engaging content_05.mp4", "treat": "engaging", "model": "Lhr Data", "dur": 7.0}}, {"id": 28, "date": "2026-10-25", "dayFull": "Sunday", "pillar": "Biology Countdown", "creative": "Carousel", "variant": "start now for next season", "source": "DESIGN", "frameSource": "Fat tightening_Hafsa.mp4 (24s)"}]}, {"week": 5, "theme": "What is on the tray", "themeNote": "Sterility, provenance and paperwork, in a market where the regulator is sealing clinics weekly.", "rows": [{"id": 29, "date": "2026-10-26", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "the aftercare in the first hour", "source": "DRIVE_EDIT", "subPillar": "The Men's Room", "bankSecondCut": true, "asset": {"driveName": "Kabeer_Laser.mp4", "treat": "laser", "model": "Kabeer", "dur": 50.4}}, {"id": 30, "date": "2026-10-27", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "what each one actually treats", "source": "DESIGN", "frameSource": "Kabeer_Laser.mp4 (50s)"}, {"id": 31, "date": "2026-10-28", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "the thing that goes wrong when you rush it", "source": "SHOOT_BROLL", "subPillar": "The Tray"}, {"id": 32, "date": "2026-10-29", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "what week two really looks like", "source": "DRIVE_EDIT", "asset": {"driveName": "MehwishFatfreeze.mp4", "treat": "fatfreeze", "model": "Mehwish", "dur": 32.1}}, {"id": 33, "date": "2026-10-30", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "how do we Ensure Safety & Effectiveness in our Treatment_Subtitling.mp4", "treat": "other", "model": "", "dur": 36.4}}, {"id": 34, "date": "2026-10-31", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "source": "DRIVE_EDIT", "watchedDesc": "Paper aeroplane POV flying the length of the clinic, past HELLO BEAUTY, the brochure stand, GET THE GLOW and BEYOND SKIN BEYOND BEAUTY.", "defect": "Handheld and shaky, needs stabilising.", "variant": "the paper aeroplane tour of the clinic", "asset": {"driveName": "Engaging content_07.mp4", "treat": "engaging", "model": "Lhr Data", "dur": 22.7}}, {"id": 35, "date": "2026-11-01", "dayFull": "Sunday", "pillar": "Smog Diary", "creative": "Carousel", "variant": "this week's reading and one mechanism", "source": "DESIGN", "frameSource": "Kabeer_PRP.mp4 (50s)"}]}, {"week": 6, "theme": "The air changes", "themeNote": "November opens. The Sunday slot becomes the smog card and holds for five weeks.", "rows": [{"id": 36, "date": "2026-11-02", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "one area, one session, real time", "source": "DRIVE_EDIT", "bankSecondCut": true, "asset": {"driveName": "Rabita_SkinTightning_02.mp4", "treat": "skintighten", "model": "Rabita", "dur": 47.3}}, {"id": 37, "date": "2026-11-03", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "the three questions to ask any clinic", "source": "DESIGN", "frameSource": "Kabeer_SkinTeightenig.mp4 (34s)"}, {"id": 38, "date": "2026-11-04", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "the real session arithmetic", "source": "DRIVE_READY", "asset": {"driveName": "what skin concern can RF Micro Neddling treat_Subtitling.mp4", "treat": "other", "model": "", "dur": 22.2}}, {"id": 39, "date": "2026-11-05", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "session 3 of 6, partial on purpose", "source": "DRIVE_EDIT", "asset": {"driveName": "Laser_Mehwish_6thVisit_02.mp4", "treat": "laser", "model": "Mehwish", "dur": 30.8}}, {"id": 40, "date": "2026-11-06", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "how is PRP for Hair loss Performed.mp4", "treat": "prp", "model": "", "dur": 50.8}}, {"id": 41, "date": "2026-11-07", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "source": "DRIVE_EDIT", "watchedDesc": "A staff member holds up cards to camera: Thank You, then For Visitng, then the Venus logo card.", "defect": "DEFECT: the card reads For Visitng, misspelled. Reprint the card and reshoot the middle beat, it is three seconds of work.", "variant": "cards held to camera, no words spoken", "asset": {"driveName": "Engaging content_11.mp4", "treat": "engaging", "model": "Lhr Data", "dur": 3.3}}, {"id": 42, "date": "2026-11-08", "dayFull": "Sunday", "pillar": "Smog Diary", "creative": "Carousel", "marker": "Diwali, public holiday", "variant": "the barrier one", "source": "DESIGN", "frameSource": "Kurasa_Facelaser.mp4 (5s)"}]}, {"week": 7, "theme": "Barrier week", "themeNote": "Two public holidays back to back. Lead with hours and utility, then barrier science.", "rows": [{"id": 43, "date": "2026-11-09", "dayFull": "Monday", "pillar": "Branch Desk", "creative": "Carousel", "marker": "Iqbal Day, public holiday. Reconfirm with the Cabinet Division in late October.", "variant": "hours and the holiday note", "source": "DESIGN", "frameSource": "Kurasa_HandLaser.mp4 (25s)"}, {"id": 44, "date": "2026-11-10", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "what changes if your skin is deeper", "source": "DESIGN", "frameSource": "Kurasa_PartyPeal.mp4 (30s)"}, {"id": 45, "date": "2026-11-11", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "three things worth knowing before you book", "source": "DRIVE_READY", "asset": {"driveName": "when do you see results_Subtitling.mp4", "treat": "other", "model": "", "dur": 7.7}}, {"id": 46, "date": "2026-11-12", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "same light, same angle, months apart", "source": "DRIVE_EDIT", "asset": {"driveName": "Mehwaish Laser.mp4", "treat": "laser", "model": "Mehwish", "dur": 45.6}}, {"id": 47, "date": "2026-11-13", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "how many sessios are needed for fat freeing_Subtitling.mp4", "treat": "other", "model": "", "dur": 18.6}}, {"id": 48, "date": "2026-11-14", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "source": "DRIVE_EDIT", "watchedDesc": "Two staff in black uniforms and gloves talking across a consultation desk to a seated patient, shot over the patient's shoulder. No burned-in text.", "defect": "Clean. The patient is unidentifiable from behind, which is the point.", "variant": "what actually happens at the consultation desk", "asset": {"driveName": "Engaging content_12.mp4", "treat": "engaging", "model": "Lhr Data", "dur": 8.3}}, {"id": 49, "date": "2026-11-15", "dayFull": "Sunday", "pillar": "Smog Diary", "creative": "Carousel", "variant": "the acne one", "source": "DESIGN", "frameSource": "Ayra_SkinTightning.mp4 (28s)"}]}, {"week": 8, "theme": "The laser window opens", "themeNote": "UV drops to an average daily maximum of 4. The clinically correct season to start laser.", "rows": [{"id": 50, "date": "2026-11-16", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "the handpiece changing over", "source": "DRIVE_EDIT", "subPillar": "The Men's Room", "bankSecondCut": true, "asset": {"driveName": "Kabeer_PRP.mp4", "treat": "prp", "model": "Kabeer", "dur": 50.3}}, {"id": 51, "date": "2026-11-17", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "this or that, after six sessions", "source": "DESIGN", "frameSource": "Fateh_PartyPeel.mp4 (36s)"}, {"id": 52, "date": "2026-11-18", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "who we turn away and why", "source": "DRIVE_READY", "asset": {"driveName": "Will I see immediate results after a fat freezing treatment_Subtitling.mp4", "treat": "fatfreeze", "model": "", "dur": 22.7}}, {"id": 53, "date": "2026-11-19", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "the area nobody photographs", "source": "DRIVE_EDIT", "asset": {"driveName": "Mehwaish_Hydra.mp4", "treat": "hydra", "model": "Mehwish", "dur": 26.8}}, {"id": 54, "date": "2026-11-20", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "How to achieve best best results.mp4", "treat": "other", "model": "", "dur": 47.5}}, {"id": 55, "date": "2026-11-21", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "source": "SHOOT_ENGAGE", "variant": "a deadpan one liner in the treatment room, one staff member, no cuts"}, {"id": 56, "date": "2026-11-22", "dayFull": "Sunday", "pillar": "Smog Diary", "creative": "Carousel", "variant": "the scalp and hair one", "source": "DESIGN", "frameSource": "Fateh_PRP.mp4 (16s)"}]}, {"week": 9, "theme": "Scalp and fall", "themeNote": "Pollution and hair loss evidence, handled carefully, with a countermeasure in every post.", "rows": [{"id": 57, "date": "2026-11-23", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "the whole pass, start to finish", "source": "DRIVE_EDIT", "bankSecondCut": true, "asset": {"driveName": "Pashmina_Laser.mp4", "treat": "laser", "model": "Pashmina", "dur": 46.7}}, {"id": 58, "date": "2026-11-24", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "the order to do them in", "source": "DESIGN", "frameSource": "Hala_Viva.mp4 (36s)"}, {"id": 59, "date": "2026-11-25", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "what we will not promise", "source": "SHOOT_BROLL", "subPillar": "The Tray"}, {"id": 60, "date": "2026-11-26", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "progress with the spec block", "source": "DRIVE_EDIT", "asset": {"driveName": "VenusViva_Nelum_Opt_02.mp4", "treat": "viva", "model": "Neelum", "dur": 38.2}}, {"id": 61, "date": "2026-11-27", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "How to choose proper tretment_Subtitling.mp4", "treat": "other", "model": "", "dur": 32.1}}, {"id": 62, "date": "2026-11-28", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "source": "SHOOT_ENGAGE", "variant": "two staff, one trending sound, the treatment as the punchline"}, {"id": 63, "date": "2026-11-29", "dayFull": "Sunday", "pillar": "Smog Diary", "creative": "Carousel", "variant": "the pigment one", "source": "DESIGN", "frameSource": "MaleModel_Laser.mp4 (48s)"}]}, {"week": 10, "theme": "Choosing a clinic", "themeNote": "December is when the researching patient finally picks. Shift from acquisition to comparison.", "rows": [{"id": 64, "date": "2026-11-30", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "what it actually feels like, narrated on screen", "source": "DRIVE_EDIT", "bankSecondCut": true, "asset": {"driveName": "Mufasira_PRP.mp4", "treat": "prp", "model": "Lhr Data", "dur": 38.9}}, {"id": 65, "date": "2026-12-01", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "what it costs you in time, not money", "source": "DESIGN", "frameSource": "MaleModel_Skinteightening.mp4 (24s)"}, {"id": 66, "date": "2026-12-02", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "the thing that goes wrong when you rush it", "source": "SHOOT_TALK"}, {"id": 67, "date": "2026-12-03", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "what week two really looks like", "source": "DRIVE_EDIT", "asset": {"driveName": "Neelum3rdVisit_ViVa.mp4", "treat": "viva", "model": "Neelum 3rd Visit", "dur": 28.8}}, {"id": 68, "date": "2026-12-04", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "howdoesRfworks__Subtitling.mp4", "treat": "other", "model": "", "dur": 36.2}}, {"id": 69, "date": "2026-12-05", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "source": "SHOOT_ENGAGE", "variant": "the thing patients always say at the front desk"}, {"id": 70, "date": "2026-12-06", "dayFull": "Sunday", "pillar": "Biology Countdown", "creative": "Carousel", "variant": "the Ramadan 2027 window", "source": "DESIGN", "frameSource": "MaleModel_Skinteightening_SHOUTOUT.mp4 (16s)"}]}, {"week": 11, "theme": "Wavelength week", "themeNote": "Wavelength is the one variable most competitors running IPL cannot match. Move the talk off price.", "rows": [{"id": 71, "date": "2026-12-07", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "the prep nobody films", "source": "DRIVE_EDIT", "subPillar": "The Men's Room", "bankSecondCut": true, "asset": {"driveName": "MaleModel_Laser.mp4", "treat": "laser", "model": "Lhr Data", "dur": 48.1}}, {"id": 72, "date": "2026-12-08", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "who it will not work on", "source": "DESIGN", "frameSource": "MaleModel_PartyPeel.mp4 (34s)"}, {"id": 73, "date": "2026-12-09", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "the real session arithmetic", "source": "SHOOT_TALK"}, {"id": 74, "date": "2026-12-10", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "session 3 of 6, partial on purpose", "source": "DRIVE_EDIT", "asset": {"driveName": "NeelumShoutOut.mp4", "treat": "other", "model": "Neelum 3rd Visit", "dur": 26.9}}, {"id": 75, "date": "2026-12-11", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "Is fat Freezing is Painful_Subtitling.mp4", "treat": "fatfreeze", "model": "", "dur": 20.1}}, {"id": 76, "date": "2026-12-12", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "source": "SHOOT_ENGAGE", "variant": "a failed attempt, kept in, because the fail is the joke"}, {"id": 77, "date": "2026-12-13", "dayFull": "Sunday", "pillar": "Biology Countdown", "creative": "Carousel", "variant": "a dated card for a December function", "source": "DESIGN", "frameSource": "MaleModel_PRP.mp4 (26s)"}]}, {"week": 12, "theme": "The December bride", "themeNote": "Be honest about what no longer fits before a December function and what still moves in three weeks.", "rows": [{"id": 78, "date": "2026-12-14", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "the settings on the screen", "source": "DRIVE_EDIT", "bankSecondCut": true, "asset": {"driveName": "Ayesha_face lift.mp4", "treat": "other", "model": "Ayesha kakani", "dur": 38.8}}, {"id": 79, "date": "2026-12-15", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "what each one actually treats", "source": "DESIGN", "frameSource": "Maliha Fat Freeze.mp4 (34s)"}, {"id": 80, "date": "2026-12-16", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "three things worth knowing before you book", "source": "SHOOT_TALK"}, {"id": 81, "date": "2026-12-17", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "same light, same angle, months apart", "source": "DRIVE_EDIT", "asset": {"driveName": "Kurasa_Facelaser.mp4", "treat": "laser", "model": "Khurasa", "dur": 4.9}}, {"id": 82, "date": "2026-12-18", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "Is laser removal painful.mp4", "treat": "laser", "model": "", "dur": 46.8}}, {"id": 83, "date": "2026-12-19", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "source": "SHOOT_ENGAGE", "variant": "the clinic at 9am before anyone arrives"}, {"id": 84, "date": "2026-12-20", "dayFull": "Sunday", "pillar": "Biology Countdown", "creative": "Carousel", "variant": "the March bride's session map", "source": "DESIGN", "frameSource": "Mufasira_PRP.mp4 (39s)"}]}, {"week": 13, "theme": "Quiet days", "themeNote": "Quaid-e-Azam Day and Christmas. Hours, aftercare, low effort, high utility.", "rows": [{"id": 85, "date": "2026-12-21", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "the aftercare in the first hour", "source": "DRIVE_EDIT", "bankSecondCut": true, "asset": {"driveName": "Daniah Belly tightning (1).mp4", "treat": "skintighten", "model": "Daniah", "dur": 37.5}}, {"id": 86, "date": "2026-12-22", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "the three questions to ask any clinic", "source": "DESIGN", "frameSource": "MufasiraSkinteightening.mp4 (29s)"}, {"id": 87, "date": "2026-12-23", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "who we turn away and why", "source": "SHOOT_BROLL", "subPillar": "The Tray"}, {"id": 88, "date": "2026-12-24", "dayFull": "Thursday", "pillar": "Branch Desk", "creative": "Carousel", "variant": "which branch for which treatment", "source": "DESIGN", "frameSource": "Rabia_DarkCircle_ShoutOut.mp4 (17s)"}, {"id": 89, "date": "2026-12-25", "dayFull": "Friday", "pillar": "Asked and Answered", "creative": "Reel", "marker": "Quaid-e-Azam Day and Christmas, public holiday", "variant": "the question as the whole first frame", "source": "DRIVE_READY", "asset": {"driveName": "What make Venus Different_Subtitling.mp4", "treat": "other", "model": "", "dur": 3.8}}, {"id": 90, "date": "2026-12-26", "dayFull": "Saturday", "pillar": "The Room", "creative": "Reel", "marker": "Holiday for Christians only", "source": "SHOOT_ENGAGE", "variant": "the gossip chain, re-cut around a real announcement"}, {"id": 91, "date": "2026-12-27", "dayFull": "Sunday", "pillar": "Biology Countdown", "creative": "Carousel", "variant": "what still fits in three weeks", "source": "DESIGN", "frameSource": "Rabia_SkinTeightening.mp4 (33s)"}]}, {"week": 14, "theme": "What next year needs", "themeNote": "Four days. Year end, January course planning, and the Ramadan 2027 window.", "rows": [{"id": 92, "date": "2026-12-28", "dayFull": "Monday", "pillar": "The Full Pass", "creative": "Reel", "variant": "one area, one session, real time", "source": "DRIVE_EDIT", "subPillar": "The Men's Room", "bankSecondCut": true, "asset": {"driveName": "Kabeer_SkinTeightenig.mp4", "treat": "skintighten", "model": "Kabeer", "dur": 33.6}}, {"id": 93, "date": "2026-12-29", "dayFull": "Tuesday", "pillar": "The Decision Table", "creative": "Carousel", "variant": "what changes if your skin is deeper", "source": "DESIGN", "frameSource": "Mahnoor_Lazer.mp4 (22s)"}, {"id": 94, "date": "2026-12-30", "dayFull": "Wednesday", "pillar": "The Honest Number", "creative": "Reel", "variant": "what we will not promise", "source": "SHOOT_TALK"}, {"id": 95, "date": "2026-12-31", "dayFull": "Thursday", "pillar": "Matched Frame", "creative": "Carousel", "variant": "the area nobody photographs", "source": "DRIVE_EDIT", "asset": {"driveName": "Kurasa_HandLaser.mp4", "treat": "laser", "model": "Khurasa", "dur": 24.9}}]}]
const weeks = (args && args.weeks) || WEEKS
phase('Write')
log(`Writing ${weeks.length} themed weeks, ${weeks.reduce((n, w) => n + w.rows.length, 0)} posts`)

const done = await pipeline(
  weeks,
  w => agent(`${RULES}\n${REFS}\n\n=== YOUR ASSIGNMENT ===
WEEK ${w.week} of 14. THEME: "${w.theme}".
${w.themeNote}
Season: ${w.rows[0].season || ''}

Write one post per row below, in order, using these exact ids and dates.
 - source DRIVE_READY or DRIVE_EDIT: the footage EXISTS. Write an editNote, not a recordGuide.
 - source SHOOT_TALK, SHOOT_BROLL or SHOOT_ENGAGE: write a recordGuide, and a full script if anyone speaks.
 - source DESIGN: a carousel or card to design. Write a slide by slide spec, no recordGuide. Where a
   frameSource is given, the designer pulls the still frames from THAT real Venus clip, never from stock.
 - Any row whose pillar is "The Room" MUST have both reference and editReference filled in.
 - Where a row carries watchedDesc, that is a frame by frame description of the actual footage. Write to
   what is really in the clip and fix any defect it names.

${w.rows.map(r => `ROW id=${r.id} date=${r.date} (${r.dayFull}) pillar=${r.pillar}${r.subPillar ? ' / ' + r.subPillar : ''} format=${r.creative} source=${r.source}${r.variant ? `\n   VARIANT, the exact shape this post must take: ${r.variant}` : ''}${r.marker ? '\n   MARKER: ' + r.marker : ''}${r.asset ? `\n   ASSET: ${r.asset.driveName} (treatment=${r.asset.treat}${r.asset.model ? ', model=' + r.asset.model : ''}${r.asset.dur ? `, REAL LENGTH ${r.asset.dur} SECONDS` : ''})` : ''}${r.bankSecondCut ? '\n   BANK A SECOND CUT: this source is long enough to yield an 8 to 12 second cut as well. Name the beat it comes from.' : ''}${r.frameSource ? `\n   FRAME SOURCE for the slides: ${r.frameSource}` : ''}${r.watchedDesc ? `\n   WHAT IS ACTUALLY IN THE CLIP: ${r.watchedDesc}` : ''}${r.defect ? `\n   DEFECT TO FIX IN THE EDIT: ${r.defect}` : ''}`).join('\n')}

Write all ${w.rows.length}.

THE TWO THINGS THE CLIENT WILL JUDGE THIS ON:
1. REPETITION. He is worried the audience will get bored seeing the same thing week after week. Each
   row carries a VARIANT, which is the specific shape that post must take. Honour it. A Decision Table
   that is "the order to do them in" must not read like one that is "this or that after six sessions".
   Every hook must differ from every other hook this week, and none may reuse a structure you can
   already see in the row list. Tie the week to its theme without repeating the theme phrase.
2. WASTED FOOTAGE. Where an asset carries a duration, that is how much real footage exists. Build an
   edit that uses it. A 47 second clip supports a 30 to 40 second film. Say in the editNote exactly
   which seconds carry which beat, and where the banked short cut comes from.

Vary the goal across the week, do not make everything a dm. This client rejected three previous
calendars for being generic, so every line must earn its place.`,
    { label: `w${w.week} ${w.theme}`, phase: 'Write', schema: WEEK }),
  (out, w) => {
    if (!out || !out.posts) return null
    const body = out.posts.map(p => `--- POST ${p.id} (${p.date}) ---\nHOOK: ${p.hook}\nCAPTION:\n${p.caption}\nHASHTAGS: ${p.hashtags}\nKEYWORDS: ${p.keywordBlock}\nCTA: ${p.cta}\nSPEC:\n${p.spec}\nSCRIPT:\n${p.script}\nGUIDE:\n${p.recordGuide}\nEDIT:\n${p.editNote}\nREF: ${p.reference}\nEDITREF: ${p.editReference}`).join('\n\n')
    return agent(`You are a strict compliance checker for a Pakistani medical aesthetic clinic's Instagram calendar.
Find every violation below. Be literal. Quote the exact offending text.

1. Roman Urdu anywhere (Urdu in Latin letters: "ka", "ki", "hai", "aap", "kya", "bilkul", "ye", "mein").
2. Em dashes.
3. Banned words: permanent, painless, safe, guaranteed, cure, flawless, best, number one, magic, miracle,
   "best version of yourself", "say goodbye to".
4. "hair removal" as a Venus claim outside the bracketed keyword block.
5. Any discount, sale, percentage off, limited time offer, bundle or price.
6. Botox or any botulinum brand name.
7. Engagement bait: "comment YES", "tag a friend", "tag someone", "double tap", "share if you agree".
8. Dr. Uzair named in a hook, in the first caption line, or placed in frame 1.
9. Any invented number, statistic, patient quote, review or result NOT in this whitelist:
   laser 8.9 mean treatments, range 4 to 22, 54.3% mean reduction, sessions 4 to 6 weeks apart, patch
   test at 48 hours, Fitzpatrick IV to V common in Pakistan, 1064 nm Nd:YAG, cryolipolysis 3 weeks to
   2 months to 15-28% at 4 months, no repeat before 6 to 8 weeks, Lahore AQI 331 on 29 Oct 2025,
   PM2.5 48.1x WHO, AQI 527 on 13 Dec 2025, Nov 2024 peaks 1067, Lahore UV 6 Oct / 4 Nov / 3 Dec,
   the named pollution mechanisms, the Korean cohort of 5,591,500 over 12.5 years linking pollution to
   hair loss risk, telogen shedding highest Aug to Oct, PHC 6,380 raids and 1,415 sealed and 1,153
   illegal, SHCC 18 sealed in Karachi and 10 in DHA, 26 registered vs about 10,000 practitioners,
   wedding season Oct to March, Sunday peak function day, three month venue lead, Ramadan 2027 from
   about 8 Feb 2027, the four Q4 2026 public holidays, Venus 8 branches since 2018 with 10,000+ reviews.
10. Quoted speech attributed to a patient.
11. A claim any treatment reverses or prevents pollution damage, or that particles penetrate intact skin.
12. Exosome regrowth claims.
13. A named competitor, or implying a specific rival is illegal.
14. More than 5 hashtags, or a banned tag.
15. More than one emoji in a caption, or an emoji in line 1.
16. A reference URL that does not match the post's format, or any URL not in the supplied library.
17. Any post whose pillar is The Room that is missing either reference or editReference.
18. A reel caption over 70 words or a carousel caption over 150 words.

WEEK ${w.week} POSTS:
${body}

Report every violation with post id, rule name, exact quote and a concrete fix. Return clean=true with an
empty array only if the week is genuinely spotless. Do not be lenient.`,
      { label: `verify w${w.week}`, phase: 'Verify', schema: VERDICT, effort: 'high' })
      .then(v => ({ week: w.week, posts: out.posts, verdict: v }))
  }
)

const ok = done.filter(Boolean)
const posts = ok.reduce((n, w) => n + w.posts.length, 0)
const viol = ok.reduce((n, w) => n + ((w.verdict && w.verdict.violations) || []).length, 0)
log(`${ok.length} weeks, ${posts} posts, ${viol} violations flagged`)

return {
  weeks: ok.map(w => ({ week: w.week, posts: w.posts })),
  violations: ok.flatMap(w => ((w.verdict && w.verdict.violations) || []).map(v => ({ week: w.week, ...v }))),
  stats: { weeks: ok.length, posts, violations: viol },
}
