# How to Use This Skill

Hey Claude—I just added the "keyword-performance-analyzer" skill. Can you analyze my keyword performance and find Quality Score issues?

## Example Invocations

**Example 1: Full Keyword Audit**
Hey Claude—I just added the "keyword-performance-analyzer" skill. Can you pull keyword data from my Google Ads account and identify which keywords have QS problems costing me money?

**Example 2: Specific Account**
Hey Claude—I just added the "keyword-performance-analyzer" skill. For the Atlanta Luxury Bags account, analyze keyword performance for the last 30 days. My target CPA is $50.

**Example 3: Find Bleeders**
Hey Claude—I just added the "keyword-performance-analyzer" skill. Which keywords are wasting money with no conversions?

**Example 4: Bid Recommendations**
Hey Claude—I just added the "keyword-performance-analyzer" skill. Which keywords should I increase or decrease bids on based on performance?

## What to Provide

- Account to analyze (or I'll list available accounts)
- Target CPA or ROAS
- Date range (default: last 30 days)
- Any specific campaigns to focus on (optional)

## What You'll Get

- Quality Score distribution and penalty estimates
- Keywords segmented by performance tier (Stars, Bleeders, QS Victims)
- Match type health analysis
- Specific bid adjustment recommendations
- Quick wins with estimated impact

## MCP Data Used

This skill pulls live data from Google Ads via:
- `keyword_view` action with GAQL query
- Metrics: impressions, clicks, cost, conversions, CTR, historical QS
