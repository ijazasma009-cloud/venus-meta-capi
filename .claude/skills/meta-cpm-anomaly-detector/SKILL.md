---
name: meta-cpm-anomaly-detector
description: Compares Meta campaign CPMs against their 14-day rolling average and industry benchmarks, flags spikes by severity, and diagnoses the root cause as audience saturation, competitive pressure, creative decay, auction inflation or narrow targeting. Use when the user asks why Meta CPMs jumped, why costs suddenly increased, or wants CPM benchmarked.
---

# CPM Anomaly Detector (Meta Ads)

CPMs fluctuate daily on Meta, but some spikes signal real problems. This skill separates noise from cause.

## Required data

Campaign level export with daily CPM breakdown, ideally 30 days or more so seasonal patterns are visible. Include: campaign name, date, impressions, CPM, frequency, spend, quality or engagement ranking if available.

## Analysis instructions

Act as a Meta Ads CPM analyst. Analyze CPM trends and flag anomalies:

1. Compare each campaign's current CPM to its 14-day rolling average
2. Flag any campaign where CPM increased more than 20% vs. that average
3. For each anomaly, diagnose the likely cause:
   - Audience saturation (frequency rising alongside CPM)
   - Competitive pressure (CPM up but frequency stable)
   - Creative decay (low quality ranking plus rising CPM)
   - Seasonal or auction inflation (all campaigns affected equally)
   - Targeting too narrow (small audience plus high CPM)

For each flagged campaign, provide:

- Severity: Minor is under 25%, Major is 25 to 50%, Critical is above 50%
- Likely root cause with supporting evidence
- Specific fix with expected CPM reduction

Industry CPM benchmarks for context: B2C $8 to $15, B2B $15 to $35, e-commerce $5 to $12.

## Operating notes

- Q4 CPMs typically run 30 to 50% above baseline. Do not flag seasonal inflation as a fault when every campaign moves together.
- Short data windows miss seasonal patterns. Ask for 30 days when only 7 are supplied.
- Benchmarks above are generic. Substitute vertical-specific numbers when the user has them.

Source: get-ryze.ai, "15 Claude Skills for Meta Ads".
