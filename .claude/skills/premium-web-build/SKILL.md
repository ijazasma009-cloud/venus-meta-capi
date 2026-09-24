---
name: premium-web-build
description: "Universal method for designing and building a website that looks like a senior designer made it, not an AI. Works for ANY brand and ANY stack (WordPress theme, Shopify, Next.js, static HTML). Orchestrates the installed design skills (taste, Emil Kowalski, Apple design, avoid-ai-design, Vercel web guidelines, DESIGN.md, Playwright self-review) into one pipeline: brief read, reference study, design tokens, real media sourcing, build, screenshot review loop, anti-slop audit, motion pass, launch gate. Use for 'build a website', 'redesign this site', 'make it look premium', 'make it like Apple', 'it looks AI generated', 'world class site', 'Awwwards level', or any new page, theme or landing page."
---

# Premium Web Build

One pipeline, nine gates. Do not skip a gate because the previous one "went fine".
This file is the conductor. The detailed craft lives in the skills it calls.

## 0. Rules of precedence

1. **The owner's standing rules win.** Check memory and any CLAUDE.md or brand file first. Typical owner rules that override third-party skills: no em-dashes, real brand imagery only (no AI images, no stock), never invent metrics, conversion first.
2. Then the brand's existing assets (logo, colour, type, photography).
3. Then the third-party skills below. Where they conflict with 1 or 2, they lose.

Known conflicts, found when these skills were security reviewed before install. Override them every time:
- `design-taste-frontend` and `redesign-existing-projects` say to use "organic, messy data" such as `47.2%`, invented names and randomised dates. On a real site that is fabricated evidence. Use only real, sourced figures, or a clearly labelled mock that is removed before launch.
- `design-taste-frontend` says "use an image-generation tool first" and to hotlink `picsum.photos`. Go to gate 4 of this file instead. Ask before spending image credits. Never ship a placeholder hotlink.
- `design-taste-frontend` says to build "Trusted by" walls from Simple Icons logos. Only real clients, with permission, from files the brand supplied.
- `avoid-ai-design` defaults to rewrite mode and will edit files without asking when run as a sub-task. On a live site run it in audit mode first and show the owner the findings.
- `web-interface-guidelines`, `vercel-react-best-practices` and the code skeletons in the taste skill are React, Next.js and Tailwind flavoured. On WordPress or Shopify apply the principle, not the syntax.
- Several process skills (from superpowers and agent-skills) push autonomous execution. The owner's rule still stands: confirm before anything destructive, outward-facing or costly.

Brand design references: 74 reverse-engineered `DESIGN.md` files (Apple, Stripe, Linear, Nike and others) live in `~/claude-hq/references/design-md/<brand>/DESIGN.md`. They are for studying structure and vocabulary. Never copy a brand's identity or use its proprietary typeface.

## 1. Brief read (before any code)

State one line: **"Reading this as: <page kind> for <audience>, with a <vibe> language, leaning toward <system or aesthetic>."**
Then set the three dials from `design-taste-frontend`: DESIGN_VARIANCE, MOTION_INTENSITY, VISUAL_DENSITY.
"Like Apple" or "like Rolex" means: variance 7-8, motion 8-9 (scroll choreography, slow and deliberate), density 2-3 (huge breathing room, one idea per screen).
If the owner gave a positioning order (for example "marketing first, AI second, software third"), write it down here. Every headline, nav order and section order must follow it.

## 2. Reference study

Open the references the owner named and 3 to 5 category leaders. For each, record: hero paradigm, scroll devices, type pairing, section rhythm, how imagery is used, what is absent. Name patterns with the vocabulary in `design-taste-frontend` section 10 and `animation-vocabulary`. Take ideas, never copy layouts or assets.

## 3. Design tokens in a DESIGN.md

Write a `DESIGN.md` at the project root before building: colours (one accent, locked), type scale and pairing, radius system (one), spacing rhythm, motion curves and durations, component rules. Every page then reads that file, which is what keeps page 12 looking like page 1.
- Borrow structure from the catalogue at getdesign.md (VoltAgent/awesome-design-md) when a known brand's language is the reference.
- Check the palette live with Realtime Colors (realtimecolors.com), which previews colours on a real layout and exports CSS variables.
- Avoid the AI defaults: purple or blue glow accents, cream plus brass, Inter, a serif accent word dropped into a sans headline, Fraunces or Instrument Serif.

## 4. Real media first

A page without real imagery is unfinished, and stock makes a brand invisible.
- **Source from the brand's own world**: its website, its Instagram, its ad library, and any asset folders the owner keeps. For an agency site, source from the **whole client roster**, spread evenly. Two or three over-used clients is a failure; count brands per page and rebalance.
- Instagram history needs the owner signed in to the Browser pane; anonymous access stops at 12 posts. Public single posts and reels download with `yt-dlp`.
- Verify every image: at least 1200px on the long edge for heroes, **no text burned in** for backgrounds, correct brand. Record source URL and date for each asset.
- Video: transcode to H.264 mp4 plus a poster frame, keep hero loops under about 1.5 MB, never autoplay more than what is on screen.
- If the media truly does not exist, leave a labelled slot and tell the owner exactly which shots are missing. Do not fill it with stock or AI.

## 5. Build

Pick components before inventing them:
- 21st.dev for React and Tailwind components, Motion Primitives (motion-primitives.com) for copy-paste animated components, Haikei (haikei.app) for SVG backgrounds (waves, blobs, gradients) when a section needs texture and no photograph fits.
- Follow `design-taste-frontend` section 4.7 hard rules: hero fits the viewport, max 4 text elements in the hero, trust logos under the hero not in it, nav on one line, no layout family used twice, max one marquee per page, max one eyebrow per three sections, one theme per page.
- On WordPress: build a real theme or blocks, keep every word in the initial HTML, no page-builder runtime. Keep the old content reversible.

## 6. Cinematic scroll (when motion is 8 or above)

See `references/cinematic-scroll.md`. Short version: pick ONE scroll system for the whole site. Pin with `start: "top top"`. Scrub image sequences on a canvas, not a `<video>` currentTime hack, for frame accuracy. Smooth scrolling with Lenis. Every scene must say something: one idea, one line of copy, one visual, then move on. Motion is slow and heavy, never bouncy. Always ship a reduced-motion path and keep all copy in the HTML.
If the owner wants a fly-through world rather than product-style scenes, use the `lets-scroll` skill.

## 7. Screenshot review loop (mandatory)

Never judge a design from code. After each meaningful change: open the page in a real browser, screenshot at 1440, 1024 and 375 wide, look at the image, fix what is wrong, repeat. Use the Browser pane tools or `playwright-cli`. Wait for lazy-loaded media before judging, or placeholders will look like bugs. Check: does the hero fit, is anything clipped, do images load, is there a dead zone of empty space, does it look like a template.

## 8. Anti-slop audit

Run `avoid-ai-design` over the result, then the `design-taste-frontend` pre-flight checklist (section 14), then `web-design-guidelines` (Vercel) for accessibility and interaction correctness. Mechanical counts to run every time:
- eyebrows ≤ ceil(sections / 3)
- marquees ≤ 1
- layout families ≥ 4 across 8 sections
- CTA intents: one label per intent, sitewide
- em-dash and en-dash count = 0
- hero text elements ≤ 4
- brands represented in imagery (for agency and portfolio sites)

## 9. Motion pass, then launch gate

Motion pass with `emil-design-eng`, `apple-design` and `review-animations`: custom ease-out curves, UI motion under 300ms, springs for anything draggable, enter and exit on the same path, press feedback on every button, nothing animated "because it looked cool".
Then run `site-launch-gate`. Only then is it done.

## What "finished" means

The owner will rate it. Before showing it, self-rate against the references from gate 2, screen by screen, and fix the weakest screen first. Lead the hand-over with what changed against their last feedback, point by point.
