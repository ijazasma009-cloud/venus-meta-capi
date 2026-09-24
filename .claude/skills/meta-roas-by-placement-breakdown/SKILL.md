---
name: meta-roas-by-placement-breakdown
description: Calculates true Meta Ads ROAS by placement accounting for assisted conversions, view-through impact and attribution window sensitivity, and classifies each placement as initiator, influencer or closer. Use when the user asks whether Stories or Reels are really unprofitable, about view-through conversions, or about attribution windows across Meta placements.
---

# ROAS by Placement Breakdown (Meta Ads)

Related to `meta-placement-performance-analyzer`, but focused on revenue attribution rather than raw efficiency. Feed, Stories, Reels and Audience Network each have different attribution patterns.

## Required data

Placement-level performance data with revenue and conversion values, plus the user's attribution window (1-day click, 7-day click, or 7-day click plus 1-day view). Ideally pull the same report under two attribution settings so the comparison is real rather than modeled.

## Analysis instructions

Act as a Meta Ads attribution and placement analyst. Analyze ROAS by placement with these considerations:

1. **Direct ROAS**: revenue attributed directly to each placement
2. **Assisted conversions**: placements that typically initiate but do not close. Stories and Reels often assist, Feed often closes.
3. **View-through impact**: which placements drive view-through conversions?
4. **Attribution window sensitivity**: how does ROAS change across 1-day click, 7-day click, and 7-day click plus 1-day view?

For each placement, provide:

- `Spend | Revenue | Direct ROAS | Estimated True ROAS (accounting for assists)`
- Role in the conversion path: Initiator, Influencer, or Closer
- Recommendation: invest more, maintain, or reduce

Key analysis:

- Which placement has the best true ROAS once assists are accounted for?
- Which placement looks expensive on direct ROAS but is actually an important initiator?
- Estimated revenue impact of cutting the bottom 2 placements entirely

## Operating notes

- Run this with both 1-day click and 7-day click attribution. Stories and Reels often look unprofitable on 1-day click and clearly profitable on 7-day.
- "Estimated True ROAS" is a model, not a measurement. Label it as an estimate, state the assumption behind the assist weighting, and never present it as reported platform data.
- The only way to settle a placement's real contribution is a holdout or lift test. Recommend one before any large budget shift.

Source: get-ryze.ai, "15 Claude Skills for Meta Ads".
