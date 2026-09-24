export const meta = {
  name: 'venus-calendar-repair',
  description: 'Repair 56 Venus posts against the check findings and the client bans',
  phases: [{ title: 'Repair', detail: 'one agent per week, fixes findings and re-verifies its own output' }],
}

const RULES = `
You are repairing a finished week of Instagram posts for Venus Aesthetics, a premium 8-branch
aesthetic clinic chain in Pakistan. The writing is good. Do not rewrite what works. Fix what is broken
and return the whole week, corrected.

=== THE SEVEN REPAIRS, APPLY TO EVERY POST ===

1. REMOVE EVERY PERSONAL NAME FROM THE CAPTION.
   Names currently used: Ayesha, Mehwish, Mehwaish, Rabita, Neelum, Nellum, Kurasa, Khurasa, Mahnoor,
   Daniah, Hafsa, Quratulain, Ayra, Mufasira, Naba, Pashmina, Fateh, Hala, Maliha, Asbeah, Kabeer.
   Replace with "our client", "one of our clients", "this client". The person is visible in the video,
   so nothing is lost. This client has previously rejected work for attributing things to named people,
   so this is absolute. Names may stay in the SPEC where they identify the source file. Never in a caption.

2. NEVER STATE AN OUTCOME YOU CANNOT SEE IN THE FOOTAGE.
   Delete any claim about how many sessions someone had, how long a result lasted, what a person felt,
   or what changed for them, unless the footage plainly shows it. Describe what is on screen, nothing more.
   No invented durations. No "six months later". No made up game results or diary entries.

3. REMOVE EVERY PEEL, CHEMICAL PEEL, PARTY PEEL, HYDRAFACIAL AND VENUS GLOW REFERENCE.
   The client banned facials outright. Where a post is built on a peel, rebuild it on one of:
   laser hair reduction, skin tightening, fat freezing, PRP for hair, Venus Viva resurfacing, dermapen.
   Pick whichever suits the concept. Change the caption, the on-screen text, the slide copy and the
   hashtags together so nothing is left behind.

4. THE HASHTAG #GlowWithVenus IS BANNED because it welds Glow to the brand.
   Replace it with #VenusAesthetics or #SkinCarePakistan.

5. NO EM DASHES ANYWHERE, including inside slide headings in the spec. Use a comma or a full stop.
   Slide headings should read "Slide 2, HOW OFTEN" not "Slide 2 — HOW OFTEN".

6. THE CAPTION AND THE SPEC MUST AGREE.
   If the caption promises a split screen, the spec must build a split screen with no fallback option.
   If the caption says five things, the spec must contain five. If the caption states a runtime, the
   spec's own timings must add up to it. Fix whichever side is wrong, usually the caption.

7. THE CONCEPT MUST BE VISIBLE IN THE CAPTION.
   If the caption would read exactly the same with the creative concept deleted, rewrite the caption
   so the idea is the thing the reader notices first.

=== ALSO STILL TRUE ===
English only, no Roman Urdu anywhere including prop names in shoot guides.
No discounts, prices, percentages or offers. No Botox or any drug brand name.
Never say permanent, painless, guaranteed or flawless. Say hair reduction, not hair removal, and never
burn "hair removal" into a frame. No statistics, studies, regulators or AQI readings in a caption.
Dr. Uzair never appears in a hook or a first caption line. No engagement bait, but a real open question
is fine. 3 to 5 hashtags. 2 to 4 emojis, never in line 1.

=== THE VOICE, UNCHANGED ===
WARM for treatment and conversion. USEFUL for educational. PLAYFUL for engaging.
Caption shape: a short hook line with one emoji, then 2 or 3 warm plain sentences, then a three beat
rhythm line, then one soft question or invitation, then:
  📍 Lahore · Karachi · Islamabad · Faisalabad · Gujranwala
  🕚 Mon to Sat, 11 AM to 8 PM
  📞 Call or WhatsApp on the number in bio
then 3 to 5 hashtags. Body 40 to 65 words, not counting the location block.

=== THE BRIEF FORMAT, UNCHANGED ===
Numbered pointers. Slide by slide for designed posts, step by step for edits. Exact colours, positions,
on-screen words and timings. Never prose paragraphs. Shoot guides list who, where, kit, props, the beat,
direction and time on set.

=== REFERENCES, use only these ===
Reels: DcO5LR-AqU0 Sculpt Spa deadpan 4.46% · DZ0ZWodCjuC Sculpt Spa secret 3.60% · Da3V-BPDlj9 Sculpt Spa
fail 2.37% · DbWn5UlhfRx Alchemy 43 trending audio · DbWQkkDP7uk LaserAway mother daughter 4.45% ·
DcBxwo1CCE2 Pulse Light personality · DcZhRGkAMFZ Milan Laser nine words · DbdqueMOmLU Skin Laundry life
context · DcBiLzXCXoW Venus own team 0.99% · DYIP3yWCjc6 Venus own team 0.98% · DN7FCmVkvnX Venus own
pause game 206 comments · DQe0j3BCOWI Venus own POV · DUDpXQDFTfk Venus own penguin · DP0GawgAQSH Venus own
Babar Azam · DcOsYaChl8J Skin Laundry treatment filmed plainly · DbIZKAIFRJK Pulse Light what it feels
like · DbdowHqk8H- Sono Bello progress over time 2.16% · DcByqkjFjzn Sono Bello client speaks 2.69% ·
DboqG0evGyt LaserAway male client 1.86% · DbYJ9SjCpZe Pulse Light numbered series · DQ7tEOBD9a4 Ideal
Image one question 1.30% · DdWx_IIlPpl Venus own best ever 1.03% · DP8oCpqDsQm Venus own wedding question
Carousels: DbCGcx9DwhK SkinSpirit pain joke · DcNiQjIiFpi Dr Rashmi why results differ · DaSKpcYAeZD
Dr Jaishree pre wedding · DbhObcpGpyU SkinSpirit expectations · DbhxnXFkfgr Dr Rashmi one session ·
DFwKaBjNXTC SkinSpirit first timer · DFtgsFSMdtd SkinSpirit authority · DF1GC74OC5S SkinSpirit the space ·
DbyWRuTlLx8 SkinSpirit new location · DbGU_X7CGaQ Dr Rashmi industry honesty · DdIvEhsoN6J Clinic
Dermatech wedding · DdB3R1BE8bB Oliva concern hook · DdboieCE7N8 Oliva keyword block · C30amLssmwL Sono
Bello spec block · Da3Vg47xYUq Face Haus destination
Format as https://instagram.com/p/CODE . A reel references a reel, a carousel references a carousel.
`

const POST = {
  type: 'object',
  properties: {
    id: { type: 'integer' },
    conceptLine: { type: 'string' },
    hook: { type: 'string' },
    caption: { type: 'string' },
    hashtags: { type: 'string' },
    spec: { type: 'string' },
    recordGuide: { type: 'string' },
    reference: { type: 'string' },
    refWhy: { type: 'string' },
    changed: { type: 'array', items: { type: 'string' }, description: 'One short line per repair you made' },
  },
  required: ['id','conceptLine','hook','caption','hashtags','spec','recordGuide','reference','refWhy','changed'],
}
const WEEK = { type: 'object', properties: { posts: { type: 'array', items: POST } }, required: ['posts'] }

const weeks = WEEKS
phase('Repair')
log(`Repairing ${weeks.length} weeks, ${weeks.reduce((n,w)=>n+w.posts.length,0)} posts`)

const done = await parallel(weeks.map(w => () =>
  agent(`${RULES}

=== WEEK ${w.week}. Repair all ${w.posts.length} posts and return every one. ===

${w.posts.map(p => `
──────── POST ${p.id}  ${p.date}
BUCKET ${p.bucket} / ${p.format}   FORMAT ${p.creative}   VOICE ${p.voice}   SOURCE ${p.source}
CONCEPT: ${p.concept}
${p.asset ? `FOOTAGE: ${p.asset}${p.assetDur ? ', ' + p.assetDur + 's' : ''}${p.assetTreat ? ', ' + p.assetTreat : ''}` : ''}${p.frameSource ? `\nFRAMES FROM: ${p.frameSource}` : ''}
CONCEPT LINE: ${p.conceptLine}
HOOK: ${p.hook}
CAPTION:
${p.caption}
HASHTAGS: ${p.hashtags}
SPEC:
${p.spec}
${p.recordGuide ? 'GUIDE:\n' + p.recordGuide : ''}
REFERENCE: ${p.reference}
${p.findings.length ? 'PROBLEMS FOUND IN THIS POST:\n' + p.findings.map((f,n)=>`  ${n+1}. ${f.issue}\n     quote: ${f.quote}\n     fix: ${f.fix}`).join('\n') : 'No specific problems were flagged, but apply the seven repairs anyway.'}
`).join('\n')}

Return all ${w.posts.length} posts with the same ids. Apply the seven repairs to every one, plus the
specific problems listed. Keep everything that already works, especially the creative ideas and the
detailed briefs. In "changed", list what you actually fixed in one short line each.`,
    { label: `repair w${w.week}`, phase: 'Repair', schema: WEEK, effort: 'high' })
))

const ok = done.filter(Boolean)
log(`${ok.length} weeks repaired, ${ok.reduce((n,w)=>n+w.posts.length,0)} posts`)
return { weeks: ok.map((w,i) => ({ week: weeks[i].week, posts: w.posts })),
         stats: { weeks: ok.length, posts: ok.reduce((n,w)=>n+w.posts.length,0) } }
