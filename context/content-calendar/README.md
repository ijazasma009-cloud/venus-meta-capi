# Venus content calendar and the video library

Copied from `Desktop\Venus-Aesthetics\05-content-calendar-2026` on 24 Sep 2026.

This is adjacent to the CAPI work, not part of it. It is here because the same
brand rules apply and because the video library is what the calendar is built
from.

---

## The live board

**https://venus-content-calendar-production.up.railway.app**

Railway project `venus-content-calendar`, workspace "Asma Ijaz's Projects".
Admins: Masroor, sameed, uzair. Staff: usman, Abubaker.
Two shared fallback logins exist. Values deliberately not recorded here, ask Masroor.

---

## What `calendar.json` actually contains

Read straight out of the file, not from memory:

| Field | Value |
|---|---|
| Title | 8 Week Content Calendar |
| Period | Monday 28 September to Sunday 22 November 2026 |
| Weeks | 8 |
| Posts | **56** |
| Generated | 2026-09-24 |
| Blocks | September, October, November |
| Reference library | 18 references |

Of the 56 posts: **40 are video**, **26 pull an existing clip from Drive**, and
**14 still need production**.

Owners assigned across posts: Editor, Designer, Social, Production.

The seven themes in use:

```
Treatment  · Treatment Film
Treatment  · The Results
Educational · Skin School
Educational · Ask Venus
Engaging   · Real Talk
Engaging   · The Team
Conversion · Your Glow Plan
```

### A discrepancy worth knowing about

My session memory records the calendar as **95 posts running to 31 December**.
The `calendar.json` actually on disk is **56 posts running to 22 November**.

Both may be true at different moments. There are three workbooks in this folder,
named `8-Weeks`, `Q4-2026` and `Sep-Dec-2026`, so more than one version exists.
`calendar.json` is the 8-week one and it was regenerated on 24 September.

**Check the Railway board before acting on either number.** Do not assume.

---

## The video library

Two files describe it, and they do not cover the same set.

### `research/drive_inventory.json`

A full crawl of the Google Drive folder. 900 entries: 76 folders and 824 files.

| Type | Count |
|---|---|
| Video files (mp4/mov/m4v) | **201** |
| Image files | 335 |
| Other files | 288 |

Videos by top level group:

| Count | Group |
|---|---|
| 119 | Models Videos |
| 81 | Sir Uzair Info Videos |
| 1 | Sir Uzair Music Video |

There is also a `Sir Uzair Stills` group holding images.

Each entry carries its Drive file `id`, so a clip can be resolved to a Drive URL
directly.

### `research/durations_clean.json`

Measured runtimes, but only for a **subset**: 66 clips.

| Metric | Value |
|---|---|
| Clips measured | 66 |
| Total runtime | 23.6 minutes |
| Median | 20.94 s |
| Shortest | 2.08 s |
| Longest | 59.98 s |
| Under 10 s | 25 |
| 10 to 30 s | 22 |
| 30 to 60 s | 19 |
| 60 s and over | 0 |

### Second discrepancy

Memory records the library as **95 clips totalling 45.7 minutes, median 28.5 s**.
The measured file says **66 clips, 23.6 minutes, median 20.94 s**, and the Drive
crawl says **201 video files exist**.

So there are three different numbers in play: 201 videos on Drive, 66 with a
measured duration, and a remembered figure of 95 that matches neither. Most
likely 95 was a curated shortlist at some point, and durations were only ever
measured for part of it.

**If clip counts matter for a decision, re-measure rather than trusting any of
these three.**

---

## The build pipeline

`build/` holds the generators. The rule from previous sessions:

> **Never hand-edit `calendar.json`.**

The flow, for the v4 line which is the current one:

```
v4_spine3.py       builds the slots
v4_write_final.js  the writing workflow, week data embedded
v4_export2.py      emits calendar.json
v4_validate.py     independent mechanical rule check
v4_workbook.py     emits the xlsx
```

`v2_*` and `v3_*` are superseded. `v5_*` and `v6_*` exist and are later
experiments. Check which one actually produced the current board before editing.

---

## Content rules, learned through five rejections

These are not suggestions. Each one came from work being sent back.

- **Treatment-led, never doctor-led.** Dr. Uzair answers a question but is never
  in a hook, a first caption line, or frame one. He speaks English in the FAQ
  videos, so the Roman Urdu ban does not block those.
- **English only.** No Roman Urdu in captions, on-screen text or scripts.
- **Zero discount posts.** Urgency comes from biology and the wedding calendar.
- **Never write what a person said unless the audio was verified.**
- **References must be format-matched**, and an engaging post needs two: one for
  content and one for editing.
- **Do not cut 8 seconds out of a 40 second film.** Monday is a 25 to 45 second
  film plus a banked short cut plus stills.
- **Weeks must not feel repetitive.** 14 named themes plus a named variant on
  every post.

---

## The number that drives the strategy

Across 207 reels the median was 511,299 plays and 67 likes. Across the last eight
weeks, after boosting was scaled back, the median was 17,546 plays and 41 likes.

**Organic reach is 5,000 to 25,000 plays. Everything above that was bought.**

The category benchmark for Health and Beauty is 0.06% engagement per post, so
Venus is at par, not broken. Their three best organic posts ever were the team
being human, not treatment films.

---

## Instagram account

**`@venusaestheticspk`** is correct. 4,978 posts, 148K followers.

`@venusaesthetics` without the `pk` is a **different, verified clinic in another
country**. It has been crawled by mistake before.

---

## Files in this folder

| File | What it is |
|---|---|
| `data/calendar.json` | The 56 post calendar. Generated, never hand-edit. |
| `research/drive_inventory.json` | Full Drive crawl, 900 entries with file IDs |
| `research/durations_clean.json` | Measured runtimes for 66 clips |
| `research/v4-research-dims.json` | Research dimensions behind v4 |
| `research/v4-primary-data.md` | Primary data gathered for v4 |
| `research/v4-playbook.md` | The v4 playbook |
| `research/v4-critique.md` | Critique of v4 |
| `research/v6-creative-ideas.md` | Creative idea bank, the largest note here |
| `research/instagram-audit-and-references.md` | IG audit and the reference accounts |
| `research/paid-performance-90d.md` | 90 day paid performance |
| `research/clinic-chain-playbook.md` | Clinic chain playbook |
| `build/*.py`, `build/*.js` | The generator pipeline, v2 through v6 |
| `Venus-Content-Calendar-*.xlsx` | Three workbook versions: 8 Weeks, Q4 2026, Sep to Dec 2026 |

---

## A note on names in these files

`drive_inventory.json` and `durations_clean.json` contain folder and file names
from the client's own content Drive, and some of those include the names of
models and talent who appear in published Venus marketing videos.

They are kept as-is because stripping them would make the inventory useless, you
could no longer match a calendar slot to a clip. This repository is private.

**If that is not acceptable, say so and both files can be re-keyed to opaque IDs
with the mapping held outside the repo.**
