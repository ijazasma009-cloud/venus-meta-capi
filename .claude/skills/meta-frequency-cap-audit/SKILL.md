---
name: meta-frequency-cap-audit
description: Audits Meta ad sets for frequency violations against objective-specific benchmarks, correlates frequency growth with CTR and CVR decline, and estimates wasted spend on over-exposed users. Use when the user asks about ad frequency, audience saturation, over-exposure, or why conversion rates are falling while reach stays flat.
---

# Frequency Cap Audit (Meta Ads)

Meta's frequency caps are suggestions, not hard limits, especially in Advantage+ campaigns. Ads get shown 5 or more times to the same person while the cap says 3.

## Required data

Ad set level export with daily breakdown covering at least 14 days: ad set name, campaign objective, frequency, reach, impressions, CTR, conversion rate, spend.

## Analysis instructions

Act as a Meta Ads frequency optimization specialist. Analyze the ad set data for frequency violations using these benchmarks:

- Prospecting campaigns: frequency above 2.0 is a warning, above 3.0 is critical
- Retargeting campaigns: frequency above 4.0 is a warning, above 6.0 is critical
- Brand awareness: frequency above 5.0 is a warning, above 8.0 is critical

For each ad set, report:

1. Current frequency vs. recommended max for its objective
2. Frequency trend (increasing, stable, decreasing) over the last 14 days
3. Correlation between frequency increase and CTR or CVR decline
4. Cost of excess frequency, estimating wasted impressions served to already-saturated users

Output:

- Table: `Ad Set | Objective | Current Freq | Max Recommended | Status | Est. Wasted Spend`
- Top 3 ad sets to fix immediately, with specific recommendations
- Account-level frequency health score from 1 to 10

## Operating notes

- The 7-day rolling average matters more than the all-time frequency number.
- High BOFU frequency is usually a funnel problem, not a budget problem. If retargeting frequency is above 8, the fix is more top-of-funnel traffic, not more retargeting spend.

Source: get-ryze.ai, "15 Claude Skills for Meta Ads".
