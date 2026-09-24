---
name: meta-creative-brief-generator
description: Analyzes top-performing Meta ads to extract winning formats, hooks, CTAs and visual styles, then produces five new creative briefs that iterate on proven winners while testing new concepts. Use when Meta ads have been flagged for replacement, or the user asks what creative to make next for Facebook or Instagram.
---

# Creative Brief Generator (Meta Ads)

Pairs with `meta-creative-fatigue-detection`. When that skill flags ads for replacement, this one produces what comes next.

## Required data

Ad-level performance data for current and recent ads: ad name, format, primary text, headline, CTR, CVR, spend, ROAS. Brand guidelines and tone of voice if available, since they make the briefs materially more on-brand.

## Analysis instructions

Act as a Meta Ads creative strategist.

**Step 1, analyze the winners:**

- Which ad formats performed best (static, video, carousel, UGC)?
- Which hooks and headlines had the highest CTR?
- Which CTAs had the highest conversion rate?
- Which visual styles got the most engagement?

**Step 2, generate 5 creative briefs for new ads.** Each brief includes:

- Format recommendation (static, video, carousel)
- Hook or headline, meaning the first 3 seconds or the first line of copy
- Key message and value proposition
- CTA text
- Visual direction, 1 to 2 sentences
- Why this brief should work, grounded in the data from Step 1

Rules:

- 3 of 5 briefs iterate on proven winners: same format, different angle
- 2 of 5 briefs test new concepts: different format or an entirely new hook
- All briefs must be platform-native, not repurposed from other channels
- Include aspect ratio recommendations: 9:16 for Stories and Reels, 1:1 for Feed

## Operating notes

- The best Meta creatives feel native to the platform rather than like ads.
- Never invent performance numbers to justify a brief. If the supplied data does not support a claim, say the brief is a hypothesis rather than a data-backed iteration.
- Hand the finished briefs to `meta-ad-copy-ab-variant-writer` when copy variants are needed.

Source: get-ryze.ai, "15 Claude Skills for Meta Ads".
