# The Venus lead sheet: structure

What the script reads, and what is actually known about the live workbook.

---

## Confirmed column layout

These eleven headers are what the script maps. The spelling below is exact and
two of them look wrong but are not.

| Col | Header | Required | Used for |
|---|---|---|---|
| A | `␣Date` | optional | Lead creation time. Timestamp for the `Lead` stage. **Begins with a space.** |
| B | `Full Name` | **required** | Split into first and last, then hashed |
| C | `Booked Status` | **required** | Drives `ScheduledAppointment` and `Disqualified` |
| D | `Pabau Status` | **required** | Drives `ShowedUp` and `NoShow` |
| E | `CONSULATION STATUS UPDATED AT` | **required** | Timestamp for the arrival stages |
| F | `Meta Lead ID` | optional | The strongest identifier. Sent unhashed. |
| G | `Lead Phone` | optional | Normalised then hashed |
| H | `Lead Email` | optional | Lowercased then hashed |
| I | `Pabau Client Mobile` | optional | Fallback, used only when G is empty |
| J | `Pabau Client Email` | optional | Fallback, used only when H is empty |
| K | `Meta Stage Sent` | **required** | **The script writes here.** This is what stops double sending. |

### The two headers that look like typos and are not

- **Column A starts with a leading space.** `" Date"`, not `"Date"`. The script
  trims headers before matching, so it works either way, but leave it alone.
- **Column E spells it `CONSULATION`**, with one L missing. That is how it is in
  the live sheet. Do not correct it, the match is exact.

### Column K does not exist yet on the live sheet

`Meta Stage Sent` has to be added before the first run. Without it the script
stops on the first line and does nothing, which is safe but looks like a failure.

Run `addStageColumnEverywhere()`. It adds the header in the first free column of
every tab that already has the other four required columns, and leaves summary
and pivot tabs alone. Or type it by hand into each lead tab. The spelling and the
capitals must match exactly and the column must be empty below the header.

---

## Tabs

### Confirmed

**`Islamabad Logic`** is the only tab name that has been verified. It is what
`SHEET_NAMES` is currently set to.

### Not confirmed

**The other tab names are unknown.** The live guide uses `Lahore Logic`, `Dorris`
and `Lake City` as worked examples. Those are real branch names but they have
**not** been confirmed as tab names. Do not paste them into `SHEET_NAMES`.

### How to find them

Run `listTabs()` from the script editor. It sends nothing. Output looks like:

```
"Islamabad Logic"  rows: 2841  READY
"<some tab>"       rows: 4102  MISSING -> Meta Stage Sent
"Summary"          rows: 14    MISSING -> Booked Status | Pabau Status | ...
```

A tab missing **only** `Meta Stage Sent` is a lead tab that needs the column.
A tab missing several columns is a summary or pivot tab, leave it alone.

Copy every `READY` tab into `SHEET_NAMES`, exactly as printed.

### Branches in the business

For orientation only. These are branch names, not tab names.

Lahore: MM Alam, Faisal Town, DHA, Lake City.
Karachi: Shaheed-e-Millat.
Islamabad: F7. Plus Faisalabad and Gujranwala.

**There is no Multan branch.** This has been corrected more than once.

---

## How a row becomes an event

```
Pabau Status = Complete | Arrived | Running Late   ->  ShowedUp
Pabau Status = No Show  | Not Show                 ->  NoShow
Booked Status = Booked                             ->  ScheduledAppointment
Booked Status = Not Interested                     ->  Disqualified
none of the above, but a Meta Lead ID exists       ->  Lead
no outcome and no lead ID                          ->  skipped entirely
```

Matching is case-insensitive and trims whitespace, so `"  COMPLETE  "` works.

Statuses seen in the live sheet that fall through to `ScheduledAppointment`:
`Waiting`, `Manual Review`. Statuses that fall through to the raw `Lead` stage:
`No Contact`, `Call Later`.

### Forward only

`Meta Stage Sent` holds the last stage sent. A row is only sent again if the new
stage ranks higher:

```
Lead 1  <  ScheduledAppointment 2  <  Disqualified 3 = NoShow 3  <  ShowedUp 4
```

So a status edited backwards by hand cannot un-send an arrival, and the hourly
trigger can run all day without ever double reporting a patient.

### Only after a 200

A row is marked in column K **only after Meta returns 200 for its batch**. A
failed batch leaves those rows unmarked and they retry on the next run. There is
no queue and no state to lose. The spreadsheet is the memory.

---

## What to expect on the first live dry run

Most of the sheet will be skipped. Meta rejects any event older than seven days
and the sheet holds months of history. A first dry run on 14,000 rows looks
roughly like:

```
to send: 640  {"Lead":410,"ScheduledAppointment":96,"ShowedUp":31,"NoShow":44,"Disqualified":59}
   | with lead_id: 601 | stage unchanged: 0 | no identity: 812 | older than 7 days: 12780
```

Reading the counters:

| Counter | Healthy | If it looks wrong |
|---|---|---|
| `to send` | about one week of leads plus a week of status changes | Zero means column K already has values, or every date is old |
| `with lead_id` | 90% or better of `to send` | Far below means `Meta Lead ID` is not being mapped by the automation. Fix before go-live. |
| `stage unchanged` | zero on the very first run | Above zero means column K was not empty |
| `no identity` | some | A large share means the automation is dropping fields. Every one of these is a patient Meta will never learn from. |
| `older than 7 days` | very large | Correct. History cannot be backfilled. |

**The sanity check:** take average leads per week. `to send` should be in that
neighbourhood. Wildly bigger means a date column is being read wrong. Wildly
smaller means a tab is missing from `SHEET_NAMES`.

---

## Sample rows

`demo/demo-sheet.csv` in the repo root holds twelve **fabricated** rows using the
same eleven headers. Every value in it is invented. It exercises every branch:

- 2 raw leads, 2 booked, 3 arrivals, 1 no-show, 1 disqualified
- 1 row with no identity at all, which must be skipped
- 1 row already at `ShowedUp`, which must be refused
- 1 row at `ScheduledAppointment` that must climb to `ShowedUp`
- 1 row twenty days old, which must be rejected by the seven day limit

Expected dry run against it: `to send: 9`, three skipped.

Regenerate it with `node tools/make-demo-sheet.cjs` so the dates stay inside the
seven day window.

**No real patient rows are in this repository.**
