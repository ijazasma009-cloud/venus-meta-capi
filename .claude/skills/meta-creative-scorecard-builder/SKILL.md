---
name: meta-creative-scorecard-builder
description: Scores every active Meta ad from 1 to 100 using a weighted composite of CTR, conversion rate, ROAS, cost efficiency and longevity, then bands them into star performer, solid, underperformer and cut. Use when the user wants a Meta creative ranking, an objective scorecard for a creative review, or to decide which ads to scale or pause.
---

# Creative Scorecard Builder (Meta Ads)

Gives creative teams a single number to rally around, which makes creative review meetings data-driven instead of opinion-driven.

## Required data

Ad-level performance data: ad name, format, days active, impressions, CTR, conversion rate, CPA, ROAS, spend. The account average for CTR, CVR and CPA, plus the ROAS target.

## Analysis instructions

Act as a Meta Ads creative performance analyst. Score every active ad on a 1 to 100 scale using this weighted framework:

- CTR vs. account average: 25% weight
- Conversion rate vs. account average: 25% weight
- ROAS vs. target: 20% weight
- Cost efficiency, meaning CPA vs. account average: 15% weight
- Longevity, meaning days active without fatigue: 15% weight

Scoring bands:

- **80 to 100, Star Performer**: scale budget, create iterations
- **60 to 79, Solid**: maintain, monitor for fatigue
- **40 to 59, Underperformer**: test new variants
- **0 to 39, Cut**: pause immediately, reallocate budget

Output:

- Scorecard table: `Ad Name | Format | Score | CTR Score | CVR Score | ROAS Score | Efficiency Score | Longevity Score | Action`
- Top 3 learnings from the star performers, meaning what makes them work
- Bottom 3 patterns from the underperformers, meaning what to avoid
- Creative mix recommendation: ratio of static, video, carousel and UGC

## Operating notes

- Show the component sub-scores, not just the composite. A 55 driven by weak CTR needs a different fix than a 55 driven by weak CVR, which is usually a landing page problem rather than a creative one.
- Ads with very low impressions do not have a meaningful score. Exclude them and say why.
- Share the scorecard with the creative team weekly. When designers see UGC-style video score 78 while polished brand video scores 42, creative direction shifts fast.

Source: get-ryze.ai, "15 Claude Skills for Meta Ads".
