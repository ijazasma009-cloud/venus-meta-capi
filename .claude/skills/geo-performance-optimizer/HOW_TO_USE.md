# How to Use This Skill

Hey Claude—I just added the "geo-performance-optimizer" skill. Can you analyze which locations are performing best and recommend bid adjustments?

## Example Invocations

**Example 1: Full Geo Analysis**
Hey Claude—I just added the "geo-performance-optimizer" skill. Pull location data for my Google Ads account and show me which cities/states are most efficient. My target CPA is $50.

**Example 2: Find Wasted Geo Spend**
Hey Claude—I just added the "geo-performance-optimizer" skill. Which locations are wasting my budget with no conversions?

**Example 3: Bid Adjustment Recommendations**
Hey Claude—I just added the "geo-performance-optimizer" skill. Give me specific geo bid adjustments I should make for each location.

**Example 4: Expansion Analysis**
Hey Claude—I just added the "geo-performance-optimizer" skill. Based on my top performing locations, where else should I consider targeting?

## What to Provide

- Account to analyze (or I'll list available accounts)
- Target CPA or ROAS
- Date range (default: last 30 days)
- Service area constraints (which states/regions you can serve)
- Current geo bid adjustments if known

## What You'll Get

- Locations ranked by efficiency
- Top performers with scale opportunity
- Underperformers and dead zones
- Specific bid adjustment percentages
- Copy-paste format for implementation
- Expansion/exclusion recommendations
- Impact projection

## MCP Data Used

This skill pulls live data from Google Ads via:
- `user_location_view` action - User's actual location performance
- `geographic_view` action (optional) - Geographic targeting view
- Metrics: impressions, clicks, cost, conversions, CPA by location
