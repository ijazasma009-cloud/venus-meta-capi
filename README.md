# Venus Meta CAPI

Sends patient-arrival outcomes from the Venus lead sheet back to Meta through the
Conversions API, so Meta learns to buy patients who actually walk into a clinic
rather than phone numbers that never answer.

Google Apps Script, bound to the lead spreadsheet, on an hourly trigger.

## Why this exists

Meta optimises toward whatever you report. Report a form fill and it finds people
who fill forms. Reporting the real end of the funnel is what changes who it shows
the ads to.

The funnel being reported:

| Event | Sheet condition |
|---|---|
| `Lead` | a row exists with a Meta lead ID and no outcome yet |
| `ScheduledAppointment` | Booked Status is `Booked` |
| `ShowedUp` | Pabau Status is `Complete`, `Arrived` or `Running Late` |
| `NoShow` | Pabau Status is `No Show` or `Not Show` |
| `Disqualified` | Booked Status is `Not Interested` |

Meta needs **every** rung reported, including the raw `Lead` stage. A funnel that
only reports its ending is meaningless to the ranking system.

## Layout

```
apps-script/venus-script.js     the live build, multi-tab, batched writes
apps-script/sandbox-script.js   single-tab rehearsal build for a throwaway account
test/units.cjs                  52 unit tests on the pure functions
test/harness.cjs                52 end-to-end tests, fakes the whole Apps Script runtime
tools/make-demo-sheet.cjs       regenerates the demo CSV with in-window dates
demo/demo-sheet.csv             12 rows that trip every branch
```

## Running the tests

No dependencies. Node 18 or newer.

```bash
node test/units.cjs
node test/harness.cjs
```

The harness fakes `SpreadsheetApp`, `UrlFetchApp`, `PropertiesService` and
`Logger`, then runs the real `sendStagesToMeta` against simulated sheets. It
covers batching past 100 events, the runaway cap, a failed batch leaving rows
unmarked so they retry, a tab missing its column, a tab name that does not
exist, and the one-write-per-tab behaviour that keeps 14,000 rows inside the
six minute execution limit.

## Setup, short version

The full step-by-step lives in the guides linked at the bottom. In brief:

1. Add a `Meta Stage Sent` column to every lead tab. `addStageColumnEverywhere()` does this.
2. Run `listTabs()` and copy the tabs marked `READY` into `SHEET_NAMES`.
3. Put the Meta access token in **Project Settings, Script Properties**, named `META_TOKEN`.
4. Run with `DRY_RUN = true` and read the counters.
5. Set `DRY_RUN = false`, run once, check the write-back.
6. Add an hourly time-driven trigger on `sendStagesToMeta`.

## Things that are easy to get wrong

- **The token never goes in the code.** It lives in Script Properties so it is not
  in any copy, export or version history of the sheet. There is no credential in
  this repository and there never should be.
- **Hashes are arrays.** `em`, `ph`, `fn`, `ln` and `country` are arrays of SHA-256
  hex. A bare string is rejected.
- **`lead_id` is a string and is not hashed.** Meta needs it readable to match the
  lead deterministically.
- **`lead_id` is not the form ID.** They look identical. A lead ID is unique per
  person; a form ID repeats across thousands of rows. Swapping them silently
  destroys match quality.
- **Apps Script returns signed bytes** from `computeDigest`, so `sha256()` masks
  with `& 0xFF`. Without that mask every hash is wrong and nothing matches.
- **Seven day limit.** Meta rejects events older than that. History cannot be
  backfilled; only the future can be captured.
- **Never use an on-edit trigger.** Edit triggers only fire for a human typing in
  the browser. When an automation writes a row through the API, no edit trigger
  fires at all. Time-driven is the only correct choice.
- **Column `Meta Stage Sent` is the memory.** A row is marked only after Meta
  returns 200, so a failed batch simply retries next run. There is no queue.

## Guides

Published separately as artifacts:

- Sandbox rehearsal, 29 steps: <https://claude.ai/code/artifact/c4d95c2c-9536-45e5-a97d-b2c9891ddc75>
- Venus live cutover, 32 steps: <https://claude.ai/code/artifact/64ea9202-06f0-4945-b22f-c393ff6d72b2>

## Status

Not yet deployed to the live sheet. Outstanding before go-live:

- [ ] Revoke and regenerate the Meta access token
- [ ] Add `Meta Stage Sent` to every branch tab
- [ ] Install and dry run against the real sheet
- [ ] Hourly trigger
- [ ] Five custom conversions in Events Manager
- [ ] Arrived-patients customer list and 1% lookalike
