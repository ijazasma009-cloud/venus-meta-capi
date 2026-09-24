# Working rules for this repo

## Read this first

Start with `context/PROJECT-CONTEXT.md`. It says what is deployed, what is not,
what was already tried and ruled out, and which facts are unknown. Then
`context/sheet-structure.md` before touching anything that reads the sheet.

## Hard rules

- **No em-dashes** in anything written for this client. Use a comma, a full stop
  or a colon.
- **Never fabricate data.** If a number, tab name or ID is not known, say it is
  not known. `context/PROJECT-CONTEXT.md` marks the unknowns explicitly. Several
  names in the guides are illustrative examples, not confirmed values.
- **No AI-generated images of people.**
- **Conversion first.** Not decoration.

## Security

- **No credential ever enters this repo.** The Meta access token lives only in
  Apps Script, Project Settings, Script Properties, key `META_TOKEN`.
- **No patient data ever enters this repo.** No real names, emails, phone
  numbers, lead IDs or sheet rows. `demo/demo-sheet.csv` is entirely fabricated
  and is the only sample data allowed.
- `.gitignore` blocks `.pkl`, `.xlsx` outside the calendar folder, exports and
  credential files. Do not weaken those rules.
- A token was leaked into a chat window in an earlier session. It must be revoked
  and regenerated before go-live. Assume it is public.

## Before you change the Apps Script

Run both suites. They are fast and need no dependencies:

```bash
npm test
```

52 unit assertions plus 52 end to end assertions. The end to end harness fakes
`SpreadsheetApp`, `UrlFetchApp`, `PropertiesService` and `Logger`, then runs the
real `sendStagesToMeta`. If you change behaviour, update the harness in the same
commit.

## Things that look like bugs and are not

- Column A of the sheet starts with a **leading space**: `" Date"`.
- Column E spells it **`CONSULATION`**, one L missing. That is the live header.
- `TEST_EVENT_CODE` is empty on purpose. **CRM events have no test code.** Only
  the Website channel issues one.
- Most rows are skipped as older than seven days. That is Meta's hard limit, not
  a fault. History cannot be backfilled.
- `sha256()` masks with `& 0xFF` because Apps Script `computeDigest` returns
  signed bytes. Remove the mask and every hash is wrong.

## Decisions that are closed

Do not re-open these without new evidence. The reasoning is in
`context/PROJECT-CONTEXT.md` section 7.

- The city by treatment campaign structure stays.
- The minimum cost per lead cap stays.
- Optimise on `ScheduledAppointment`, not `ShowedUp`. The maths is in the same
  section and it is not close.
