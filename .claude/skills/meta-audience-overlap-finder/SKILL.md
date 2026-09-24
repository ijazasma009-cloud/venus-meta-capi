---
name: meta-audience-overlap-finder
description: Finds where Meta ad set audiences compete against each other, estimates overlap severity and the CPM premium caused by self-competition, and recommends consolidate, exclude or differentiate actions. Use when the user asks why Meta CPMs are rising, whether ad sets are cannibalizing each other, or wants an exclusion strategy.
---

# Audience Overlap Finder (Meta Ads)

When two ad sets target similar people, you bid against yourself in Meta's auction. CPMs inflate 15 to 30% and neither ad set wins.

## Required data

Targeting details for all active ad sets: interests, behaviors, custom audiences, lookalike sources and seed lists, geography, age and gender. Meta's own Audience Overlap tool in Ads Manager exports actual overlap percentages. If the user has those numbers, use them instead of estimating.

## Analysis instructions

Act as a Meta Ads audience strategist. For each pair of ad sets, evaluate:

1. Interest and behavior targeting overlap (shared interests)
2. Custom audience overlap, for example website visitors appearing in both
3. Lookalike source similarity, if both use similar seed lists
4. Geographic and demographic overlap

For each overlap found:

- Estimate overlap percentage: Low is under 15%, Medium is 15 to 40%, High is above 40%
- Calculate the CPM premium caused by self-competition
- Recommend one of: consolidate, exclude, or differentiate targeting

Output a matrix showing every ad set pair with its overlap severity. Then provide 3 specific actions to reduce CPM waste, ranked by estimated savings.

## Operating notes

- Real overlap percentages from Ads Manager produce far better recommendations than estimates. Ask for them when they are not supplied.
- Consolidation usually beats exclusion when both ad sets are small, because it also helps the algorithm exit the learning phase.

Source: get-ryze.ai, "15 Claude Skills for Meta Ads".
