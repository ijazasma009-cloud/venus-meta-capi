---
name: venus-crm-arraxis
description: "Arraxis — the white-label lead/analytics CRM built for Venus Aesthetics, designed to be resold by Arrax Marketing."
metadata: 
  node_type: memory
  type: project
  originSessionId: 06e44eb3-b9e9-4853-a20d-3b8b6719e18f
  modified: 2026-08-03T09:47:34.488Z
---

**Arraxis** is the custom CRM built for [[venus-aesthetics-clinic]], deliberately architected white-label so [[arrax-marketing-agency]] can duplicate and sell it to other companies. Name = Arrax + Axis, "the axis where every lead converges". Login screen reads "Powered by Arrax Marketing".

**Pipeline:** NEW → CALLING (5 attempts) → BOOKED → LANDED → PURCHASED. Exit statuses: Not Interested, Invalid Number, Query Solved, Existing Client, Lost. Key definitions from Masroor: **Booking** = customer agrees on a call; **Landing** = customer physically arrives at the clinic. Cost-per-booking and cost-per-landing are the metrics that matter, not cost-per-lead.

**Added on top of his spec:** callback scheduling that forces a date/time, duplicate detection by phone, speed-to-first-call tracking, round-robin auto-assignment with admin quota sliders, no-show tracking.

**Two distinct treatment fields:** treatment stated on the form vs treatment confirmed by the agent. These are different columns and he corrected this explicitly.

**Roles:** Admin (everything), Manager (reports + all leads, no settings), Agent (only their own leads, no spend/revenue/reports), Reception (branch booking schedule, marks Landed + purchase amount).

**Reports tab must look like Meta Ads Manager**: real date-range picker (not 7/14/30/90 buttons), Campaign → Ad Set → Ad drill-down, columns for results, CPL, bookings, cost/booking, cost/landing, impressions, reach, frequency, CPM, link clicks, CTR, purchase amount, plus campaign created/scheduled dates and last-lead-received. Custom columns and custom formula builder required.

**Data sources:** Meta webhook for instant leads, Meta API for spend, **Pabau** (clinic software, transcribed as "Pobao") for landed + purchase amounts, plus manual/website/WhatsApp/walk-in leads. Phase 2 sends Conversions API events back to Meta so campaigns optimise for bookings, not cheap leads.

Stack chosen: Next.js on Vercel + Supabase. Built locally first, UI/UX signed off before wiring integrations. Real seed data came from his Meta ad account and a 7,004-row lead sheet (real agents: Merry, Farwa, Rabia, Asma).
