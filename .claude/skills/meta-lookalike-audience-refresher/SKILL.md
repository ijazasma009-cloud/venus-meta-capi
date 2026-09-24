---
name: meta-lookalike-audience-refresher
description: Audits Meta lookalike audience performance decay across 30, 60 and 90 day windows, identifies which seed lists are stale, and recommends refresh timing, new seed criteria and lookalike percentages to test. Use when the user asks about lookalike performance, stale audiences, seed list refresh, or rising lookalike CPA.
---

# Lookalike Audience Refresher (Meta Ads)

Lookalike audiences degrade every 60 to 90 days as the customer base evolves and Meta's modeling goes stale.

## Required data

Lookalike audience performance over the last 90 days: audience name, lookalike percentage, seed list source and last update date, audience size at creation and now, spend, CPA, CTR, ROAS split into 30, 60 and 90 day windows.

## Analysis instructions

Act as a Meta Ads audience strategist specializing in lookalike audiences. For each lookalike audience, analyze:

1. CPA trend over 30, 60 and 90 day windows. Is it rising?
2. CTR trend. Declining CTR signals audience model staleness.
3. Age of seed list. When was the source audience last updated?
4. Current size vs. size when it was created
5. Lookalike percentage (1%, 2%, 5% and so on) vs. performance

Categorize each lookalike:

- **REFRESH NOW**: CPA increased more than 25% from the first 30 days, seed list older than 90 days
- **MONITOR**: CPA increased 10 to 25%, or seed list 60 to 90 days old
- **HEALTHY**: Performance stable, seed list under 60 days old

For each lookalike marked REFRESH NOW, recommend:

- Updated seed list criteria (purchase-based, high-LTV, recent 30/60/90 day customers)
- Suggested lookalike percentages to test, typically 1%, 2 to 3%, and 5%
- Whether to expand to new countries or keep the existing geography

## Operating notes

- Update seed lists quarterly at minimum.
- The best-performing seed lists are usually the top 25% LTV customers from the last 90 days, not all purchasers.
- A 1% lookalike on a bad seed list beats nothing, but a 5% lookalike on a high-LTV seed list usually beats both.

Source: get-ryze.ai, "15 Claude Skills for Meta Ads".
