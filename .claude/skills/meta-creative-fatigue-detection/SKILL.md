---
name: meta-creative-fatigue-detection
description: Detects Meta Ads creative fatigue by analyzing CTR trajectory, frequency accumulation, engagement decay and CPM trend across active ads, then categorizes each ad as urgent, warning or healthy with a replacement order. Use when the user asks why Meta ad performance is dropping, which Facebook or Instagram ads to replace, or wants a creative rotation schedule.
---

# Creative Fatigue Detection (Meta Ads)

The average Meta ad starts decaying after 3 to 5 days of delivery. Most advertisers catch fatigue only after CTR has already dropped 40% or more and CPA has spiked. This skill catches it earlier.

## Required data

Meta Ads Manager export at ad level, broken down by day, with columns: ad name, impressions, CTR, frequency, CPM, spend, date range. If a Meta Ads MCP connector is available, pull the last 30 days live instead of asking for an export.

## Analysis instructions

Act as a Meta Ads creative analyst. For each ad in the supplied performance data, analyze:

1. CTR trend over the last 7, 14 and 30 days
2. Current frequency vs. the frequency when CTR peaked
3. Engagement rate decay (likes, comments, shares per impression)
4. CPM trend, to judge whether the algorithm is deprioritizing this ad

Categorize each ad:

- **URGENT**: CTR dropped more than 20% from peak AND frequency above 3.0. Replace immediately.
- **WARNING**: CTR dropped 10 to 20% from peak OR frequency between 2.0 and 3.0. Plan replacement.
- **HEALTHY**: CTR stable or improving, frequency below 2.0.

Output a table with these columns:

`Ad Name | Status | Days Active | Peak CTR | Current CTR | CTR Drop % | Frequency | Recommended Action`

Then list the top 3 ads to replace first, with specific notes on why each one is fatigued.

## Operating notes

- Run weekly, and always after scaling budgets. Higher spend burns through creative faster.
- Frequency spikes in the last 3 days predict tomorrow's performance drop better than the all-time number.
- When ads are flagged for replacement, hand off to `meta-creative-brief-generator` to produce the replacements.

Source: get-ryze.ai, "15 Claude Skills for Meta Ads".
