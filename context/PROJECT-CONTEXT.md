# Venus Meta CAPI: full project context

Written 24 September 2026 for a cloud session picking this up cold.

Everything below is either verified from the account, computed from the client's
own data, or explicitly marked as unknown. Where a value is unknown, it says so
rather than guessing. **Do not invent tab names, IDs or numbers that are marked
unknown here.**

---

## 1. What this project is

Venus Aesthetics is a Pakistani aesthetic clinic chain, 8 branches, an Arrax
Marketing client. Meta lead ads fill a Google Sheet. The sales team calls those
leads, books appointments, and the clinic system (Pabau) records whether the
patient actually arrived.

Meta currently only knows that a form was filled. It does not know who arrived.
So it optimises toward cheap form fills, which is why the account produces a lot
of leads and few patients.

This project sends the real outcome back through the Conversions API, so Meta
can learn to find people who walk into a clinic.

---

## 2. Deployment status

| Thing | Status |
|---|---|
| Script written and tested | **Done.** 104 assertions pass. |
| Sandbox rehearsal on a separate Meta account | **Done and passed.** |
| Installed on the live Venus sheet | **Not done.** |
| `Meta Stage Sent` column added to live tabs | **Not done.** |
| Live access token regenerated | **Not done. Blocking.** |
| First live dry run | **Not done.** |
| Hourly trigger | **Not done.** |
| Five custom conversions | **Not done.** |
| Arrived-patients audience and lookalike | **Not done.** |
| Conversion Leads switched on any ad set | **Not done.** |

**Nothing is live.** No event has ever been sent to the Venus dataset from this
build. The only real sends went to the sandbox dataset.

---

## 3. IDs and accounts

### Verified

| What | Value | Source |
|---|---|---|
| Venus CAPI dataset ID | `726819547675464` | Events Manager, confirmed in session |
| Venus main ad account | `578304653670501` | Venus Aesthetics PKR, business "Sanabel Ventures" |
| Venus skincare ad account | `277355218676285` | Venus Skin Shop PK, same business. Separate brand, not this project. |
| Venus Health ad account | `269987068047063` | Listed, not used in this work |
| Graph API version in use | `v26.0` | Matches Meta's current Explorer output |
| Endpoint | `POST https://graph.facebook.com/v26.0/726819547675464/events` | |
| `lead_event_source` value | `Venus Lead Flow` | Set in the script as `CRM_NAME` |
| Instagram account | `@venusaestheticspk` | 4,978 posts, 148K followers |

> `@venusaesthetics` without the `pk` is a **different clinic in another country**.
> It has been crawled by mistake before. Always use `@venusaestheticspk`.

### Sandbox account, used for the rehearsal only

| What | Value |
|---|---|
| Test dataset ID | `1612027523775772`, named "test run best" |
| Test ad account | `2245795282843197` |
| Portfolio | `staleks_uk_official` |

This is a completely unrelated business. It was used so that nothing on Venus
could break during the rehearsal. It has no lead ads, so match quality there was
meaningless by design.

### Unknown, needs looking up

- **Venus pixel ID**, if it is separate from the dataset ID. Never confirmed.
- **Which Meta Page** the lead forms sit on. Needed for Conversion Leads.
- **Whether a system user exists** on the Venus business for the token.

---

## 4. Credentials, and where they live

**There is no credential in this repository and there must never be one.**

| Secret | Where it lives |
|---|---|
| Meta access token | Apps Script, **Project Settings, Script Properties, key `META_TOKEN`**. Not in the script body, not in the sheet, not here. |
| Google Sheets access | Implicit. The script is bound to the spreadsheet, so it inherits the editor's access. No service account needed. |

### Standing security issue, still open

A Meta Page access token was pasted into a chat window during an earlier
session. **It must be treated as public and revoked.** Generating a replacement
automatically invalidates the old one. This has not been done yet and it blocks
go-live.

If "Generate token" is greyed out on the system user screen, it is because no
app is attached to the business portfolio. The workaround that does not need an
app: Events Manager, select the dataset, **Settings**, **Conversions API**,
**Generate access token**.

---

## 5. The lead sheet

Source file seen in analysis: `Venus Lead Flow 2.0 (9).xlsx`, 14,283 visible lead
rows at the time of the diagnostic.

### Known tab

Only one tab name is confirmed: **`Islamabad Logic`**. That is what the script is
currently configured for.

### Unknown tabs

The other branch tabs are **not known**. The guide uses `Lahore Logic`, `Dorris`
and `Lake City` as illustrative examples only. **Those are branch names, not
confirmed tab names. Do not put them in `SHEET_NAMES` without checking.**

Run `listTabs()` from the script. It prints every tab, its row count, and whether
it has the required columns. Copy the ones marked `READY`.

Confirmed branch list for the business (not necessarily tab names): Lahore has MM
Alam, Faisal Town, DHA and Lake City. Karachi has Shaheed-e-Millat. Then
Islamabad F7, Faisalabad, Gujranwala. **There is no Multan branch**, this has been
corrected repeatedly.

See `sheet-structure.md` for the column layout.

---

## 6. Funnel numbers from the diagnostic

All computed from the client's own sheet and spend, not benchmarks.

| Stage | Count | Rate |
|---|---|---|
| Leads visible in the sheet | 14,283 | |
| Booked | 2,098 | 14.7% of leads |
| Appointments matured | 1,675 | |
| Landed, visible in sheet | 154 | |
| **Landed, true figure** | **~230** | see correction below |

Derived economics, on roughly PKR 3.85M of spend across the analysed period:

| Metric | Value |
|---|---|
| Cost per lead | ~PKR 270 |
| Cost per booking | ~PKR 1,835 |
| **Cost per arrived patient** | **~PKR 16,740** |
| Attend rate, of booked | 9.2% |
| Contact reach rate | 42.4% |

Internally proven ceilings, both achieved by the business already:
- **Lake City reaches 16.2% attend rate.**
- **Dorris reaches 54.4% contact rate.**

These are targets that are operational, not aspirational, because a branch in the
same business already hits them.

### Creative economics

| Creative | Cost per arrived patient |
|---|---|
| Hair video | PKR 5,985 |
| Laser | PKR 52,179 |

Fisher exact p = 3.33e-08. This is not noise. Laser is the thing to fix.

Male laser CPL is PKR 74 against female PKR 337 to 1,076. That is an uncontested
segment nobody is bidding on.

### Capacity

Clinic capacity is 100 clients per day per branch. Target is 30 landed
consultations per clinic. The business already books around 217 per branch per
month, so hitting 30 landed needs no extra spend, only a better attend rate.

---

## 7. Decisions made, and why

**Keep the city by treatment campaign structure.**
I initially recommended consolidating. The client pushed back with four arguments:
device utilisation differs per branch, creatives get starved in merged ad sets,
new treatments need their own launch surface, and audiences genuinely differ per
treatment. I tested it and conceded. The budget supports 103 ad sets and they run
68, so the problem is distribution, not structure. **Do not re-open this.**

**Keep the minimum cost per lead cap.**
I expected the cap to be throttling delivery. Tested it: cost-cap and
highest-volume ad sets produce statistically identical landing rates, 1.14%
against 1.15%, at roughly half the cost per lead. The cap is not the problem.
If an ad set cannot spend after a change, raise the cap rather than remove it.

**Optimise on `ScheduledAppointment`, not `ShowedUp`.**
The client specifically wants ShowedUp as the optimisation event. Meta will let
you select it. The maths says do not:

| Optimise on | Cost per one | 50/week costs | Per ad set per day |
|---|---|---|---|
| Lead | PKR 270 | PKR 13,500 | PKR 1,930 |
| ScheduledAppointment | PKR 1,835 | PKR 91,750 | PKR 13,110 |
| ShowedUp | PKR 16,740 | PKR 837,000 | **PKR 119,570** |

An ad set needs roughly 50 of the optimisation event per week to leave learning.
No ad set can support PKR 119,570 a day. An ad set stuck in learning delivers
worse than one never switched. So ShowedUp earns its value three other ways
instead: the reporting column, the lookalike audience, and weekly manual budget
moves. Switch an ad set to ShowedUp only once it alone produces ~40 arrivals a
week.

**Send the whole funnel, not just the ending.**
Meta requires a trigger for every stage including the raw `Lead` stage. A funnel
that only reports its ending is meaningless to the ranking system. This was the
actual blocker that stalled the build for a while.

**`lead_id` is the primary key.**
Email and phone are probabilistic. The Meta lead ID is deterministic, it is
Meta's own record of the person who filled the form on the ad. Sent as an
unhashed string.

**No value field on the events.**
There is no rule requiring one, and a made-up value poisons every ROAS figure
the account will ever show. If real revenue is wanted later, take it from Pabau
after treatment, not from an estimate at booking.

---

## 8. Things that were tried and were wrong

Recording these so they are not repeated.

**The "7,055 missing leads" finding was wrong and was withdrawn.**
I reported that thousands of leads were missing from the sheet. The client
corrected it: two sheets were in use at the time, so those leads did reach the
sales team and were booked. The corrected figures are the ones in section 6:
true landed ~230 not 154, cost per patient ~PKR 16,740 not PKR 25,001.

**Form ID is not Lead ID.** The client caught this. A form ID had been assumed to
be a lead ID. Proof: the form ID column had only 2 distinct values across 14,293
rows. A lead ID is unique per person. Swapping them silently destroys matching.
Sort the column to check.

**Three payload errors, all caught by the client's screenshots:**
- `custom_data` with `event_source` and `lead_event_source` was missing entirely
- `em` and `ph` were being sent as bare strings instead of arrays
- API version was v21 when Meta's own Explorer was on v26

**Apps Script `computeDigest` returns signed bytes.** Without masking with
`& 0xFF` every SHA-256 hash comes out wrong and nothing matches. Verified
byte-for-byte against Meta's own Graph API Explorer output.

**On-edit triggers do not work here.** Apps Script edit triggers only fire when a
human types in the browser. When an automation writes a lead row through the API,
no edit trigger fires at all. This was proven from the client's own data. Only a
time-driven trigger works.

**There is no test event code for CRM events.** The Test Events channel dropdown
offers Website, CRM and Offline. Only Website issues a `TEST12345` code. This is
deliberate, not a missing feature. Confirmation for CRM comes from the HTTP 200
response, the Actions tab and the Overview tab. Leave `TEST_EVENT_CODE` empty.

**Writing one cell at a time does not scale.** The first version wrote the stage
column row by row. Fine for 12 demo rows, would time out on 14,000. Now each
tab's column is written in a single call after each successful batch.

---

## 9. The sandbox rehearsal, what it did and did not prove

Run on dataset `1612027523775772`. Everything passed except the test code, which
does not exist for CRM as explained above.

**Proved:** token validity, endpoint and API version, payload acceptance, hashing
correctness, column mapping, all five stage branches, deduplication, sheet write
back, batching, and the hourly trigger firing on its own.

**Could not prove:** event match quality (the demo people are invented), whether
Conversion Leads unlocks (needs real lead ads and a validation period), and
attribution back to a real ad.

---

## 10. Custom conversions, proposed but not yet created

None of these exist yet. Create them in Events Manager, Custom conversions, with
the Venus dataset as the source. Leave the value field empty on all five.

| Name to use | Event |
|---|---|
| Landed Consultation | `ShowedUp` |
| Booked Appointment | `ScheduledAppointment` |
| Did Not Attend | `NoShow` |
| Junk Lead | `Disqualified` |
| CRM Lead | `Lead` |

Then in Ads Manager, Columns, Customise columns, add count and cost per result
for the first three and save the preset as `Venus Funnel`.

This single screen is the point of the whole project. Until cost per Landed
Consultation is visible per ad, the ads that buy cheap phone numbers and no
patients are invisible.

---

## 11. Open questions

1. **What are the real tab names?** Run `listTabs()`. Only `Islamabad Logic` is confirmed.
2. **Is `Meta Lead ID` populated across all tabs?** If the automation is not mapping it, match quality will be weak and this should be fixed before go-live.
3. **Which Meta Page holds the lead forms?** Needed for the Conversion Leads prerequisite.
4. **Is there a separate pixel ID?** Never confirmed.
5. **How long does Conversion Leads validation take?** Unknown. Expect days, not minutes. If nothing appears after two weeks of clean events, raise it with Meta support with fbtrace IDs in hand.
6. **Should the repo move to the `venusaestheticsmarketing-cell` org?** It currently sits under `ijazasma009-cloud`.

---

## 12. Hard rules that apply to all Venus work

From the client's stated preferences, enforced across sessions:

- **No em-dashes** in any deliverable.
- **No AI-generated images of people.**
- **Never fabricate data.** If a number is not known, say so.
- **Conversion first**, not decoration.
- **English only** in content. No Roman Urdu in captions, on-screen text or scripts.
- **Treatment-led, never doctor-led.** Dr. Uzair answers a question but is never in a hook, a first caption line, or frame one.
- **Zero discount posts.** Urgency comes from biology and the wedding calendar.
- **Never write what a person said unless the audio was verified.**
- Lake City is the internal flagship, used for private shoots and influencer days. **Do not label it "luxury" publicly.**
