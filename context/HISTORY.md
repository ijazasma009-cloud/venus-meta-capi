# How this work unfolded

A summary of the Venus sessions, in order, so a cloud session knows what was
already tried, what was ruled out, and what got corrected.

---

## Phase 1: the diagnostic

**Starting point.** The owner said the month was running at half of the previous
month, the sheet was full of "Call Later", and leads were not landing at the
clinic. A lead export was handed over for analysis.

**What was found.** 14,283 visible leads produced 2,098 bookings and about 154
visible arrivals. Booking rate 14.7%, attend rate 9.2%, contact reach 42.4%.
Show rate was halving week on week, from 15.8% down to 7.0%.

The dominant driver was **booking lead time decay**: the longer between the lead
arriving and the call, the less likely the patient ever showed. Two branches
already proved the ceiling was reachable, Lake City at 16.2% attend and Dorris at
54.4% reach.

**The conclusion that mattered:** 30 landed consultations per clinic needs zero
extra spend. They already book around 217 per branch per month. At a 16% attend
rate that is 188 arrivals. The problem was never lead volume.

**A major error I made and withdrew.** I reported roughly 7,055 leads missing
from the sheet. The client corrected me: two sheets were in use at the time, so
those leads did reach the sales team and were booked. I withdrew the finding
entirely and restated the numbers. True landed is about 230, not 154, and cost
per patient about PKR 16,740, not PKR 25,001. Those corrected figures are what
everything since is built on.

---

## Phase 2: the account and the plan

Connected the Meta ad account, added real spend, ran competitor research, and
produced a scorecard and a scaling plan.

**The client rejected the first plan** for leaning too heavily on sales-team
fixes. What was wanted was the marketing side: a complete campaign and ad account
plan, a named kill list, CAPI, and brand building toward being the top aesthetic
clinic brand in the market.

**Creative economics found.** Hair video produced patients at PKR 5,985 each.
Laser produced them at PKR 52,179. Fisher exact p = 3.33e-08, so not noise. Male
laser CPL was PKR 74 against female at PKR 337 to 1,076, an uncontested segment.

**Two arguments I lost, and should not re-open.**

*Campaign structure.* I recommended consolidating the city by treatment
structure. The client pushed back on four grounds: device utilisation differs per
branch, creatives starve in merged ad sets, new treatments need their own launch
surface, and audiences genuinely differ per treatment. I tested it and conceded.
The budget supports 103 ad sets and they run 68. The problem is distribution, not
structure. The client's strongest point was about CAPI signal quality per ad set,
and it was right.

*The cost cap.* I expected the minimum cost per lead cap to be throttling
delivery. I tested it. Cost-cap and highest-volume ad sets produce statistically
identical landing rates, 1.14% against 1.15%, at roughly half the cost per lead.
I told them to keep the cap.

---

## Phase 3: building the CAPI feed

The client wanted outcomes fed back to Meta so delivery would chase arrivals
rather than form fills.

**Route chosen.** Google Apps Script bound to the lead sheet, posting directly to
the Conversions API on an hourly trigger. Considered and set aside: Pabbly and
Zapier as the sender. The client has an unlimited Pabbly plan, so the honest cons
were laid out, but a script gives exact control over the payload and the
deduplication state.

**The blocker that stalled it.** The first version only sent final stages.
Meta requires a trigger for **every** stage including the raw `Lead` stage. It
was rebuilt as a stage machine with a forward-only rank guard.

**Errors the client caught from screenshots**, all fixed:
- `custom_data` with `event_source` and `lead_event_source` was missing
- `em` and `ph` were sent as bare strings instead of arrays
- API version was v21 while Meta's own Explorer was on v26

**Form ID versus Lead ID.** The client asked whether the form ID they were
receiving was the same as a lead ID. It is not. Proof: the form ID column had
only 2 distinct values across 14,293 rows, while a lead ID is unique per person.
The client then asked for `lead_id` to be the primary key, which is correct, it
is deterministic where email and phone are probabilistic.

**A live access token was pasted into chat.** It must be treated as compromised
and regenerated. This is still outstanding and it blocks go-live.

**Validation.** The hashing was checked byte for byte against Meta's own Graph
API Explorer output and matched. The Apps Script signed-byte quirk in
`computeDigest` was found and masked with `& 0xFF`.

---

## Phase 4: the sandbox rehearsal

The client asked to test the entire build on a **completely separate Meta
account** first, so nothing on Venus could be disturbed. Dataset
`1612027523775772` on the `staleks_uk_official` portfolio was used.

A twelve row demo sheet was built, designed so every branch of the logic fires,
including three rows that must be skipped for three different reasons. A 29 step
guide was written with the exact expected output at every step.

**Result: it worked.** Everything passed.

**One real discovery.** The Test Events channel dropdown offers Website, CRM and
Offline, and **only Website issues a test code**. CRM does not, and points you at
the API instead. That is deliberate: a website pixel fires inside a browser Meta
cannot see into, so the code is the only way to separate test traffic, whereas a
CRM event is a direct server call that already returns a full confirmation. The
guide was corrected and `TEST_EVENT_CODE` is left empty.

Also hit: "Generate token" greyed out on the system user screen because no app
was attached to the portfolio. Workaround documented, generate from the dataset's
own Conversions API settings instead.

---

## Phase 5: the live build

The script was extended for Venus scale:

- **Multiple tabs.** `SHEET_NAMES` takes a list. `listTabs()` reports which tabs
  are ready. `addStageColumnEverywhere()` adds the tracking column across tabs.
- **Batched writes.** The sandbox wrote one cell at a time. Fine for 12 rows,
  would time out on 14,000. Now one write per tab per batch.
- **A runaway brake.** `MAX_EVENTS_PER_RUN` caps the first send at 2,000.

104 automated assertions were written and all pass: 52 unit tests on the pure
functions, and 52 end to end tests that fake the whole Apps Script runtime and
run the real send function against simulated multi-tab sheets, covering batching
past 100, the cap, a failed batch leaving rows unmarked for retry, a tab missing
its column, and an absent tab name.

**The honest answer on Conversion Leads.** The client specifically wanted
`ShowedUp` as the optimisation event inside lead ads, and called it the most
important part. The maths says do not do it yet: at PKR 16,740 per arrival,
feeding an ad set the ~50 events a week it needs to leave learning would cost
PKR 119,570 per ad set per day. The recommendation is to optimise on
`ScheduledAppointment` on the largest ad sets, which is reachable at about
PKR 13,110 a day, and to spend the ShowedUp signal on reporting, a lookalike
audience, and weekly manual budget moves instead.

---

## Phase 6: the repo

The work had been living in a session scratchpad, which the system cleared. It
was rebuilt into `ijazasma009-cloud/venus-meta-capi`, private.

**Patient data was found in the test fixtures during the pre-commit scan** and
replaced before anything was committed: a real lead ID, a phone number, an email
and two patient names had come from the client's sheet and a pasted payload.
All replaced with synthetic values, tests still pass.

Then this context handoff, so the work can continue in a cloud session.

---

## Adjacent Venus work, not part of this repo

Useful to know about because it shares the brand and the same client rules.

- **Content calendar for Q4 2026.** Rebuilt from scratch 23 September 2026. Live
  board on Railway. See `content-calendar/` in this folder.
- **Arraxis CRM.** A white label lead and analytics CRM built for Venus and
  designed to be resold. Source recovered from Vercel, a move to Railway is
  pending, and a PII leak hotfix is awaiting approval.
- **Venus training platform.** Watermarked doctor training videos plus timed
  digital exams. Venus only, not white label.
- **Venus website.** WordPress, currently on wertually.com, category URLs,
  redirects and mobile fixes deployed 19 to 20 September. The domain switch is
  waiting on a final check.
- **Google reviews milestone.** The live total was 9,861 on 24 August 2026, so
  "10,000+" was not yet true and the reel was held. Re-render pipeline is ready.
- **Venus Beauty** is a separate DTC skincare brand and must never look like the
  clinic. **Xermal** is an anonymous device house brand that must never link to
  Venus.
