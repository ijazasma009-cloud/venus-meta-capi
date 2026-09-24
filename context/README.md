# Context handoff index

Everything a cloud session needs that is not already in the code. Written
24 September 2026.

## Read in this order

| # | File | What it gives you |
|---|---|---|
| 1 | `PROJECT-CONTEXT.md` | Deployment status, every ID, decisions and why, what failed, open questions, the hard client rules |
| 2 | `sheet-structure.md` | The eleven columns, which tabs are confirmed, how a row becomes an event, what a first dry run should look like |
| 3 | `HISTORY.md` | How the work unfolded across sessions, what was ruled out, what got corrected |

Then `../CLAUDE.md` at the repo root for the working rules, and `../README.md`
for the code itself.

## The short version

Venus lead ads fill a Google Sheet. The sales team books, the clinic system
records who arrived. Meta only ever learns that a form was filled, so it buys
cheap form fills. This project sends the real outcome back through the
Conversions API on an hourly trigger.

**Nothing is live yet.** The script is written and tested, a full rehearsal
passed on a separate Meta account, and the live install has not been done.

**The one blocking item:** a Meta access token was pasted into a chat window and
must be revoked and regenerated before go-live.

## Facts you will want immediately

| What | Value |
|---|---|
| Venus CAPI dataset | `726819547675464` |
| Venus main ad account | `578304653670501` (business "Sanabel Ventures") |
| Graph API version | `v26.0` |
| Only confirmed sheet tab | `Islamabad Logic` |
| Cost per arrived patient | ~PKR 16,740 |
| Cost per lead | ~PKR 270 |
| Instagram | `@venusaestheticspk`, not `@venusaesthetics` |
| Token location | Apps Script, Script Properties, `META_TOKEN` |

**Tab names other than `Islamabad Logic` are unknown.** Run `listTabs()`. The
guides use `Lahore Logic`, `Dorris` and `Lake City` as illustrative examples
only.

## Folders

### `brand/`

Brand and project notes carried over from session memory. These are background,
written at various dates, and reflect what was true when written. Verify before
acting on any specific file path or flag.

| File | Covers |
|---|---|
| `venus-aesthetics-clinic.md` | The clinic, branches, treatments and devices, website rebuild, K-Beauty launch |
| `venus-content-calendar-2026.md` | Calendar, the Railway board, content rules |
| `venus-crm-arraxis.md` | The white label CRM built for Venus |
| `venus-training-platform.md` | Doctor training videos and exams |
| `venus-website-launch.md` | WordPress launch state |
| `venus-google-reviews-milestone.md` | The 10k reviews reel, held because the real count was 9,861 |
| `venus-beauty-skincare.md` | The separate skincare brand. Must not look like the clinic. |
| `meta-ad-accounts.md` | All 24 ad accounts and which brand owns each |
| `masroor-working-style.md` | The client's hard delivery rules |
| `arrax-marketing-agency.md` | The agency that owns the relationship |
| `desktop-folder-readme.md` | The Desktop Venus folder layout |

### `content-calendar/`

The Q4 2026 calendar, the Drive video inventory, the build pipeline and the
research notes. See `content-calendar/README.md`, which also records two
numeric discrepancies between memory and the files on disk, both flagged rather
than resolved.

Headline numbers, read from the files themselves:

- `calendar.json`: **56 posts**, 28 Sep to 22 Nov 2026, 40 of them video,
  26 pulling an existing Drive clip, 14 still needing production
- Drive crawl: **201 video files**, 335 images, across 76 folders
- Measured runtimes: **66 clips**, 23.6 minutes total, median 20.94 s
- Live board: https://venus-content-calendar-production.up.railway.app

## What is deliberately not here

| Not included | Why | Where it is |
|---|---|---|
| The Meta access token | Never in a repo | Apps Script Script Properties |
| The real lead sheet | Patient data | Google Drive, and `Venus Lead Flow 2.0 (9).xlsx` locally |
| Google reviews CSVs | Real reviewer names | `Desktop\Venus-Aesthetics\04-ads-and-campaigns\google-reviews-milestone\01-verification\` |
| Creative assets and ad exports | 874 MB of video and images | `Desktop\Venus-Aesthetics\03-creative-assets` and `04-ads-and-campaigns` |
| `venus-calendar-app` runtime | `node_modules`, rebuildable | `Desktop\Venus-Aesthetics\05-content-calendar-2026\venus-calendar-app` |

## Skills

`.claude/skills/` holds **220 skill folders**, copied from the machine so a cloud
session loads the same toolkit. No local plugins or slash commands were
installed, so nothing to carry there. `.claude/known_marketplaces.json` records
the plugin marketplace that was registered.
