---
name: meta-competitor-ad-library-analyzer
description: Analyzes competitor ad data collected from the Meta Ad Library to map format mix, creative lifespan, refresh rate, messaging patterns and testing velocity, then identifies angle and format gaps to exploit. Use when the user asks about competitor Facebook or Instagram ads, Meta Ad Library research, or competitive creative intelligence.
---

# Competitor Ad Library Analyzer (Meta Ads)

Meta's Ad Library shows every active ad from any advertiser. This skill turns that raw list into a competitive brief.

## Required data

Two inputs: a description of the user's brand or product, and Meta Ad Library data for 3 to 5 competitors including ad copy, formats, start dates and active status.

## Analysis instructions

Act as a competitive intelligence analyst for Meta Ads. Analyze:

**1. CREATIVE STRATEGY**
- Format mix: percentage static vs. video vs. carousel vs. UGC
- Average creative lifespan, from start date to today for active ads
- Creative refresh rate, meaning new ads per week or month

**2. MESSAGING PATTERNS**
- Top 3 hooks or angles each competitor uses repeatedly
- Common CTAs across competitors
- Unique value propositions by competitor

**3. TESTING VELOCITY**
- How many active ads does each competitor run?
- How many new ads launched in the last 30 days?
- Are they testing aggressively or running a small set?

**4. GAPS AND OPPORTUNITIES**
- What angles are competitors not covering that the user could own?
- What format is underrepresented across all competitors?
- What messaging could the user differentiate on?

Output a competitive brief with specific creative recommendations for the next sprint.

## Operating notes

- Check the Ad Library monthly. Focus on competitors spending heavily, since many active ads signals significant budget.
- A long creative lifespan usually means the ad is working, not that the competitor is lazy. Treat long-running ads as their proven winners.
- Ad Library data is observational. It shows what competitors run, not what performs. Never present inferred competitor results as fact.
- Use competitor ads for directional insight. Do not copy their copy or creative.

Source: get-ryze.ai, "15 Claude Skills for Meta Ads".
