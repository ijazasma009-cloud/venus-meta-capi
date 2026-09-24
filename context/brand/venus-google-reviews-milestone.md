---
name: venus-google-reviews-milestone
description: "Venus Aesthetics 10,000 Google reviews reel — live total was 9,861 on 24 Aug 2026, so the 10,000+ claim is not yet substantiated; a data-driven re-render pipeline is built and waiting."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5c59591a-a50b-4fbf-af7e-7d72d2ad9cb0
  modified: 2026-08-24T10:57:29.593Z
---

The **"10,000 VOICES. ONE VENUS."** milestone reel for [[venus-aesthetics-clinic]] was built and delivered on **24 August 2026** to `Desktop\Venus-Aesthetics\04-ads-and-campaigns\google-reviews-milestone\`.

**The blocking fact: Venus had 9,861 Google reviews, not 10,000+.** Verified live across all 8 profiles on 24 Aug 2026: MM Alam 1,847 · DHA Phase 5 965 · Faisal Town 1,995 · Lake City 323 · F-7 Markaz 1,232 · D Ground 1,638 · Gujranwala 1,572 · Karachi 289. That is **139 short**. The film was therefore rendered on the real number with an on-screen "ALL COUNTS VERIFIED ON GOOGLE · 24 AUGUST 2026" line, per [[masroor-working-style]] (never fake data) and the playbook's own rule against unsubstantiated claims.

**Counts move daily** — DHA ticked 965→966 and Gujranwala 1,571→1,572 during the single production session. Because counts only rise and the film is dated, 9,861 is a permanently safe conservative claim.

**The re-render is one command.** Every number (counter, branch stack, particle VFX, end frame, cover) is driven from `02-source/data.js`. On the day the total crosses 10,000: `node refresh-counts.js` re-reads all 8 profiles, refuses to write if any branch fails to read, and rewrites data.js; then `node capture.js full` (~10 min) and the ffmpeg mux in the README. The soundtrack does not need regenerating.

**Technical notes worth keeping:** Google Maps serves a *degraded* page to headless Chrome for the MM Alam profile specifically — its review count often will not render. Use `headful` mode for that one. Reels here render as 1020 deterministic canvas frames via puppeteer-core driving the installed Chrome, then ffmpeg; the soundtrack is synthesised in numpy (`audio.py`), including the non-negotiable silence beat before the milestone hit.

**Do not reuse** the `Venus aesthetics .MOV` clip from Downloads for premium work — it is entirely 14-August Independence Day footage (green balloons, flags) and reads as party-template.
