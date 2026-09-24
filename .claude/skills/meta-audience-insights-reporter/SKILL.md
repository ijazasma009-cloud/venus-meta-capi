---
name: meta-audience-insights-reporter
description: Analyzes Meta Ads breakdown data across age, gender, device, region and time to surface the segments driving results versus the segments draining budget, and builds a data-backed ideal customer profile with a day-parting schedule. Use when the user asks who is actually converting on Meta, about demographic performance, or about wasted audience spend.
---

# Audience Insights Reporter (Meta Ads)

Most accounts find that 70 to 80% of conversions come from 2 or 3 demographic segments while the rest waste money.

## Required data

Ads Manager: Breakdowns > By Demographics and By Time. At least 30 days for reliable patterns. Include spend, impressions, conversions, CPA and ROAS per segment.

## Analysis instructions

Act as a Meta Ads audience analyst. Analyze across these dimensions:

1. **AGE**: which age brackets convert at the lowest CPA, and which waste budget?
2. **GENDER**: performance split with CPA and ROAS by gender
3. **DEVICE**: mobile vs. desktop vs. tablet, comparing conversion rate and CPA
4. **REGION**: top and bottom performing regions or DMAs
5. **TIME**: day of week and hour of day performance patterns

For each dimension:

- Identify the top 20% of segments driving 80% of results
- Flag segments with more than 2x the average CPA as budget drains
- Recommend: scale, maintain, reduce, or exclude

Output:

- Ideal customer profile based on the data: age, gender, device, region, time
- Budget waste estimate, meaning how much is spent on underperforming segments
- 3 targeting recommendations to implement this week
- A day-parting schedule if performance varies significantly by time

## Operating notes

- Segment sample sizes get small fast when slicing five ways. State the conversion count behind any recommendation and do not recommend excluding a segment on a handful of conversions.
- Meta restricts age, gender and location targeting for special ad categories such as housing, employment, credit and social issues. Check the category before recommending demographic exclusions.
- Combine with `meta-budget-allocation-funnel-stage` for the full spend picture.

Source: get-ryze.ai, "15 Claude Skills for Meta Ads".
