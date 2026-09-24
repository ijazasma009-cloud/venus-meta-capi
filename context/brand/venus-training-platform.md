---
name: venus-training-platform
description: "Venus Aesthetics doctor training and testing platform — watermarked private videos plus timed digital exams, replacing the current paper test."
metadata: 
  node_type: memory
  type: project
  originSessionId: 3d9ee3ee-7d15-4bd6-8e56-ac1d2e778f49
  modified: 2026-08-05T17:03:22.001Z
---

Custom LMS + examination platform for [[venus-aesthetics-clinic]], briefed by Masroor on 4 Aug 2026. Replaces the current **paper** post-hire test (MCQs plus written question-and-answer) that doctors sit after watching internal training videos on the clinic's devices (Primelase laser, Venus Viva, Legacy, Glow, Fat Freeze, Botox, PRP, SlimFit).

**The driving requirement is leak traceability, not prevention.** Masroor asked that videos "can't be recorded" and that "we clearly know who recorded it". Point 1 was stated plainly as impossible for any web platform (a second phone camera defeats everything) and he accepted the reframe. The answer is a moving per-doctor watermark (code + name + live clock, repositioning, plus a faint diagonal tile) with tamper detection that halts playback, layered with DRM, expiring session-bound URLs, and one-active-session-per-code enforcement.

**Decisions locked 4 Aug 2026** (full reasoning in `claude-hq/training-platform/02-decisions-locked.md`):
1. Custom build on the Arraxis stack: Next.js + Vercel + Supabase. Not WordPress LMS, not SaaS.
2. **Watermark only. DRM was locked then dropped the same day** at his instruction ("watermark enough"). Disclosed once, on record: without DRM, OBS-style screen recording now succeeds, so the design rests entirely on traceability plus the signed undertaking. Player stays DRM-ready.
3. **Venus only, hard-branded.** He deliberately did NOT take the white-label route here, unlike [[venus-crm-arraxis]]. Reselling later is a 2 to 3 week refactor and he accepted that.
4. MCQ **and** written answers retained, written rubric-graded.
5. Login identity is the **existing Venus Employee ID**, not a newly generated code. The paper answer sheets already collect it, so paper history matches digital on the same key.
6. Test structure is **fully configurable per module**: blueprint varies between modules, so section counts, marks, scoring modes and outcome rules are all per-test settings.

**Scale:** 7 to 8 batches a year, 15 to 16 doctors each (~105 to 128/year). One starter video with no test, 12 to 13 training videos at ~5 hours each (~60 to 65 hours total), one test per video, plus one final comprehensive test. **Batch is a first-class entity**: assign training to a batch in one action, report batch-over-batch.

**His real exam model, taken from the K-Glow packs and replacing my A-to-F guess:** Section A 40 MCQs/80 marks auto-marked, Section B 5 written/20 marks graded against 4 predefined marking points each, Section C 5 "Advanced Distinction" MCQs scored **separately /5 and unable to lower the core score**. 100 core, 90 minutes. Outcomes: Pass with Distinction (core 90+ and advanced 4/5+), Pass (80+), Retest Required (70-79), Retraining Required + Retest (<70), Invalid Attempt. Questions carry rationale, per-distractor explanations, domain, difficulty and slide-level source references, all worth storing.

**THE PROJECT RISK IS CONTENT, NOT SOFTWARE.** Only the K-Glow pack exists; the other 11 to 12 modules have no papers at all. Platform is ~8 weeks, authoring 11 more 51-page packs is far longer. Sequencing therefore: build everything, **launch on K-Glow alone**, run one real batch through it, add modules as papers land. Paper authoring must run in parallel from day one. The K-Glow pack documents its own method (99-slide deck + English transcript as source, with a stated source-control rule), so it is reproducible given each module's deck and transcript.

Also flagged: five-hour videos need chapter markers, continuous position saving, and a watch gate counted on cumulative seconds viewed rather than furthest position reached. Working title "Venus Aesthetics Training", not precious about it.

**Two viewing modes, added 4 Aug 2026:** group screening (admin plays on a TV for the batch, watermark carries the ADMIN's ID because they control that screen, admin marks attendance) and individual (doctor's own login, own watermark, tracked automatically). Sometimes it is one doctor, not a batch, so both are required. Lesson completion therefore records its source as TRACKED or ATTESTED and never merges them. The test is always individual.

**Build started 4 Aug 2026 at `C:\Users\Masroor\venus-training`.** Next.js 16 + Prisma 7 + SQLite locally, Postgres-compatible schema for a later Supabase move. Phase 1 shipped: Employee ID login, 4 roles, branches, batches, admin shell, single-active-session, security log, and the real K-Glow bank seeded (90 MCQs, 10 written, 240 distractor explanations, 40 marking points) parsed from the two PDFs by `scripts/parse-evaluation-pack.py`. Admin password seeded as `VenusTraining2026!`, forced change on first login. Note Next 16 renames middleware to `proxy.ts` and its docs say not to use it for authorization, so auth lives in `requireUser`/`requireAdmin` called per page and per server action.

**Progressive unlocking (asked for 4 Aug 2026):** a doctor cannot open the next treatment until they have PASSED the previous module's test. Retest and Retraining outcomes unlock nothing. Where the prerequisite has no test (starter pack), completing its content is the gate. Logic in `lib/progress.ts`.

**Group screening clarified:** it is not the default and not every session. Individual login is always available and sometimes only one doctor trains at a time. Attendance is ticked BEFORE playback starts, and attendees then skip re-watching and go straight to the test.

Login credentials for the local build: every seeded account uses `VenusTraining2026!`. `ADMIN` goes straight in (mustChangePassword deliberately false for review, flip to true before real use), `DEMO-001` is a doctor who must set a password and sign the confidentiality undertaking, `DEMO-TRAINER` is the trainer. `npm run db:seed` resets all passwords.

Gotchas hit while building: Prisma 7 needs a driver adapter (`PrismaBetterSqlite3`, note the lowercase q) and `prisma migrate dev` did not regenerate the client, so run `prisma generate` after schema edits. Regenerating while `next dev` runs leaves stale modules, restart it. Login/onboarding forms deliberately avoid `useActionState` and post natively so they survive hydration failures.

**Corrections he made 4 Aug 2026 (second review):** NO forced password change, ever. The admin issues the password and the doctor signs in with exactly that; doctors cannot change their own name, ID or anything else, because identity must be issued not self-declared. Logins must EXPIRE on a date. Videos are ONE VIEWING ONLY, no rewatching (trainer can grant one more). Lessons with no footage must show "Coming soon". He wants the question bank browsable as Treatment then Version A/B then Section A/B/C. He de-prioritised batch work. He wants a much better UI on both the trainer and doctor sides, and a trainer override to grant access to a doctor who failed.

**Third review, 4 Aug 2026:** he wants direct per-doctor course assignment (batches are unreliable), pinning which paper version a specific person sits, and the ability to force a retake even when the score was good. All three built into one `Assignment` model. Assessment engine also complete: server-authoritative timer, per-candidate shuffling snapshotted for audit, autosave, tab-switch auto-submit, instant MCQ marking, trainer rubric queue, outcome from the configurable ruleset, and Retraining automatically re-locking module content. Real Venus logo pulled from venusaesthetics.pk into `public/brand/`; UI rebuilt on Fraunces + Instrument Sans to match the clinic brand.

**Fourth review, 4 Aug 2026 (final pass):** his complaint was that opening a person in People showed nothing and there was no way to assign from there. Built person profile pages at `/admin/doctors/[userId]` with inline assignment, retake ordering, rewatch grants and lock overrides. Also completed: question bank as Treatment > Paper > Section with full paper viewers showing answers, sat-paper viewer per attempt, certificates auto-issued on a pass with a public `/certificate/<number>` verification page, entrance animations that respect prefers-reduced-motion, and mobile (no overflow at 375px, 44px touch targets).

**Video upload gotcha (hit 4 Aug 2026):** uploading via a Next Server Action fails with a bare "Failed to fetch" because Server Actions cap the body at 1MB AND buffer it all in memory. Fixed by moving upload to a Route Handler (`/api/admin/lessons/[lessonId]/video`) that streams the body to disk, with an XHR client for progress (fetch still gives no upload progress events). Never put large file uploads in a Server Action.

**Final build pass, 5 Aug 2026.** Added: module/lesson deletion (module needs its code typed to confirm and refuses if anyone has sat the assessment; lesson needs an explicit "delete anyway" tick if it has watch history), a full test builder at `/admin/tests/[testId]` with a "Venus standard" preset reproducing the K-Glow shape, doctor results page at `/learn/results` with total marks and percentage, results table linking to the sat paper, dual video storage (`VIDEO_STORAGE=local|bunny`, Bunny uploads stream straight through and never touch the app server; signed CDN URLs expire in 60s after our own entitlement check), `scripts/setup-production.ts` (branches + ruleset + one admin, nothing else) and `scripts/preflight.ts` (blocks deploy on placeholder secret, demo data, misconfigured storage, unpublishable assessments).

**Storage is the key production constraint:** 60-65 hours of video will not fit on an app server, so production must use `VIDEO_STORAGE=bunny`.

**Spreadsheet import (5 Aug 2026):** built as CSV, NOT xlsx. The npm `xlsx` package has unfixed high-severity prototype-pollution and ReDoS advisories and would parse an admin-uploaded file, so a 40-line zero-dependency CSV reader was written instead (`lib/csv.ts`). Two-step: dry-run preview with Excel-matching row numbers, then all-or-nothing commit.

**Video hosting decision doc: `claude-hq/training-platform/04-video-hosting.md`.** Recommendation is Bunny now (already built, cheapest, solves the storage problem), then decide on DRM after the pilot with evidence. VdoCipher is the recommended upgrade if leaks prove real: it is the only option with DRM *and* server-side per-viewer watermarking as standard, and is popular with South Asian ed-tech.

**The bottom-left floating icon Masroor saw is the Next.js dev indicator**, dev-only and never in production; now also disabled explicitly via `devIndicators: false` in next.config.ts, along with security headers (noindex, no-referrer, DENY framing, nosniff, HSTS).

**IMPORTANT boundary:** Masroor asked me to create hosting/server accounts on venusaestheticsmarketig@gmail.com. I cannot create accounts or enter credentials on his behalf; he must do that himself. Prepare configs and step-by-step instructions instead.

**Deployment (5 Aug 2026):** Vercel account created on venusaestheticsmarketing, Hobby tier. Flagged that Hobby is non-commercial so Venus needs Pro ($20/mo). Full step-by-step in `claude-hq/training-platform/05-deployment.md`. Code now auto-selects the Prisma adapter from the DATABASE_URL scheme (file: = SQLite, else Postgres), with `npm run db:use-postgres` / `db:use-sqlite` to flip the schema provider. `npm run preflight -- --serverless` upgrades SQLite and local video storage from warnings to hard blockers.

**HOSTING DECISION, FINAL 5 Aug 2026: Vercel.** (He briefly considered Contabo then reverted.) The Vercel 4.5MB upload blocker is SOLVED: added `VIDEO_STORAGE=s3` mode using presigned S3 URLs so the browser uploads straight to object storage and the file never passes through Vercel. **Use Cloudflare R2, not Bunny, on Vercel** — R2 is S3-compatible (Bunny Storage has no presigned-URL equivalent, its API needs a secret key that cannot go in a browser) and R2 charges zero egress, which matters at ~700 viewing hours/month. Needs Postgres too (Neon/Vercel Postgres free tiers are fine). Vercel Hobby is licensed non-commercial only; flagged twice, his call.

**Superseded Contabo notes:** Masroor does not want to pay for anything until one batch has been trialled. Contabo is the better fit anyway: a real filesystem means SQLite works, video lives on the server's own disk (so Bunny is optional, not mandatory), and there is no ~4.5MB request-body cap, which was the Vercel blocker on video upload. That blocker is therefore void. Check the VPS disk size when ordering: ~100GB of video plus OS and database, so treat 200GB as the floor. Bunny and Postgres both remain supported in code as a configuration change if the library outgrows the disk.

**HOSTING: RAILWAY, live 5 Aug 2026.** URL `https://venus-app-production-0c6a.up.railway.app`, project `venus-training` (9d6af5a1-cd82-4e33-8840-0d30010df299), services `venus-app` + `Postgres`. The Railway CLI is installed and logged in as venusaestheticsmarketing@gmail.com, so I can deploy with `railway up --service venus-app --detach` — no GitHub needed (though the repo exists). **Vercel was abandoned**: its functions ran in iad1 (Washington DC) while Neon was in Singapore, ~500ms per query round trip, proven via `X-Vercel-Id: bom1::iad1`; region pinning is Pro-only. On Railway the app and Postgres share a private network (`postgres.railway.internal`). Login went 10.5s (and failing) to **2.8s**; page loads are **0.5s**.

**VIDEO STORAGE ON RAILWAY = `local` on a persistent volume** mounted at `/app/storage/videos`, NOT R2. R2 blocked the browser's cross-origin PUT and the Cloudflare API refused to set CORS ("Please enable R2 through the Cloudflare Dashboard"). Railway has real disks and no request-size cap, so the upload streams through the app instead — verified with 12MB, HTTP 200. R2/Bunny remain supported as config switches if delivery ever needs a CDN.

**Bootstrap also has an opt-in `repair()` step** gated on `BOOTSTRAP_REPAIR=true`: publishes DRAFT content that has questions, and clears placeholder footage. Set it, deploy once, then set it back to false.

**Railway deploys are self-provisioning:** `start` = `prisma migrate deploy && tsx scripts/bootstrap.ts && next start`. `scripts/bootstrap.ts` creates branches, ruleset, Super Admin (from BOOTSTRAP_ADMIN_* vars) and optionally the K-Glow content, guarded on account count so it never re-runs. This exists because Railway's database is on a private network unreachable from a laptop. **tsx and dotenv had to move to `dependencies`** since the host prunes devDependencies.

**Earlier Vercel/Neon infrastructure (superseded, kept for reference):** GitHub: `github.com/venusaestheticsmarketing-cell/venus-training` (private, 3 commits pushed). Neon Postgres project `venus-training`, branch `production`, region ap-southeast-1 (Singapore) — tables migrated, 8 branches, outcome ruleset, and the full K-Glow bank (90 MCQs, 10 written, 240 distractor explanations, 40 marking points) all loaded. Super Admin is **VNS-0001 / Dr Uzair**, password set at setup (tell him to change it). Cloudflare R2 bucket `venus-training`, account id 89d06dd3fbe53665496e8b3a96c663b1. Preflight passes with no blockers. Remaining: Masroor does the Vercel import himself (I cannot log into his accounts). The K-Glow module and assessment are deliberately left DRAFT until the real video is uploaded.

**Gotcha:** command-line scripts could not use `lib/prisma.ts` because it is `server-only`; they share `scripts/db.ts` instead, which picks the driver from the connection-string scheme. Also `lib/prisma.ts` had to become a lazy Proxy, because Next evaluates route modules at build time and eagerly constructing the client failed the Vercel build.

Plan lives in `claude-hq/training-platform/`. See [[claude-hq-folder]], [[masroor-working-style]].
