---
name: meta-placement-performance-analyzer
description: Breaks down Meta Ads CPA, ROAS and conversion rate by placement across Feed, Stories, Reels, Audience Network, Messenger and Explore, identifies placements where spend share far exceeds conversion share, and recommends exclusions. Use when the user asks where Meta budget is actually going, about Advantage+ placements, or about Audience Network waste.
---

# Placement Performance Analyzer (Meta Ads)

Most advertisers use Advantage+ placements and never check where the money actually goes. It is common to find 60 to 70% of spend in the top 2 placements while the rest burn budget at 3 to 5 times higher CPA.

## Required data

Ads Manager: Breakdowns > By Delivery > Placement. At least 14 days for statistical significance. Include spend, impressions, conversions, CPA, revenue or ROAS, split by prospecting and retargeting where possible.

## Analysis instructions

Act as a Meta Ads placement optimization specialist. Analyze the placement-level performance data and:

1. Rank all placements by ROAS, or by CPA if no revenue data is available
2. Calculate each placement's share of total spend vs. share of total conversions
3. Identify placements where spend share exceeds conversion share by 2x or more. These are money pits.
4. Flag placements with fewer than 50 impressions as insufficient data to judge

Output:

- Table: `Placement | Spend | Spend % | Conversions | Conv % | CPA | ROAS | Verdict`
- Verdict options: Scale (ROAS above target), Maintain, Reduce, Exclude
- Estimated monthly savings if underperforming placements are excluded
- Recommendation: keep Advantage+ with exclusions, or switch to manual placements

Break this down separately for prospecting campaigns and retargeting campaigns, because they have very different placement economics.

## Operating notes

- Audience Network is the most common offender: cheap impressions, near-zero conversions.
- Do not judge Stories and Reels on last-click alone. For revenue attribution across placements, use `meta-roas-by-placement-breakdown` instead.

Source: get-ryze.ai, "15 Claude Skills for Meta Ads".
