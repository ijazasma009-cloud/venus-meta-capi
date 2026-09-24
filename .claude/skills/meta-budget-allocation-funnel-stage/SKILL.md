---
name: meta-budget-allocation-funnel-stage
description: Categorizes Meta campaigns into TOFU, MOFU and BOFU, analyzes spend split, conversion rate and saturation at each stage, and recommends dollar reallocation against business-type benchmarks. Use when the user asks how to split Meta budget, whether they are over-investing in prospecting or retargeting, or about funnel stage spend.
---

# Budget Allocation by Funnel Stage (Meta Ads)

Most Meta accounts over-invest in prospecting and under-invest in mid-funnel.

## Required data

Campaign performance data plus two inputs from the user: business type (e-commerce, lead gen, or high-ticket B2B) and monthly Meta Ads budget. Campaign data should include spend, conversions, CPA, ROAS, frequency and reach.

## Analysis instructions

Act as a Meta Ads funnel strategist. Categorize each campaign into a funnel stage:

- **TOFU**: cold prospecting, lookalike audiences, interest-based targeting
- **MOFU**: video viewers, page engagers, content interacters. Warm but not yet on site.
- **BOFU**: website visitors, add-to-cart, initiated checkout, customer lists

Then analyze:

1. Current spend split across TOFU, MOFU and BOFU as actual percentages
2. Conversion rate and CPA at each stage
3. Audience saturation at each stage: frequency plus reach as a percentage of total addressable
4. ROAS by funnel stage

Compare to benchmarks:

- E-commerce: 60% TOFU / 20% MOFU / 20% BOFU
- Lead gen: 50% TOFU / 30% MOFU / 20% BOFU
- High-ticket B2B: 40% TOFU / 35% MOFU / 25% BOFU

Output:

- Current allocation vs. recommended allocation
- Dollar amounts to shift between stages
- Expected ROAS impact of the reallocation
- A warning if any stage is saturated: frequency above 3 at TOFU, above 5 at MOFU, above 8 at BOFU

## Operating notes

- If BOFU retargeting frequency is above 8, the account does not need more retargeting budget. It needs more TOFU to fill the funnel. This is the most common budget mistake on Meta.
- Benchmarks are starting points, not targets. An account with an unusually strong MOFU should keep what works.

Source: get-ryze.ai, "15 Claude Skills for Meta Ads".
