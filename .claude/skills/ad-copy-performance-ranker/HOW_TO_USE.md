# How to Use This Skill

Hey Claude—I just added the "ad-copy-performance-ranker" skill. Can you analyze my RSA ads and tell me which headlines and descriptions are working?

## Example Invocations

**Example 1: Full Ad Copy Audit**
Hey Claude—I just added the "ad-copy-performance-ranker" skill. Pull my RSA ad data and rank them by performance. Show me winning headlines and patterns.

**Example 2: Find Weak Ads**
Hey Claude—I just added the "ad-copy-performance-ranker" skill. Which ads are underperforming and need new creative?

**Example 3: Headline Ideas**
Hey Claude—I just added the "ad-copy-performance-ranker" skill. Based on my top performing ads, suggest new headlines I should test.

**Example 4: Ad Strength Reality Check**
Hey Claude—I just added the "ad-copy-performance-ranker" skill. Are my "Excellent" ad strength ads actually performing well, or is it misleading?

## What to Provide

- Account to analyze (or I'll list available accounts)
- Date range (default: last 30 days)
- CTR/CVR benchmarks if known (optional)
- Industry/vertical for context (optional)

## What You'll Get

- Ads ranked by CTR and conversion rate
- Top performing headlines and patterns
- Underperforming ads with specific issues
- Ad strength vs actual performance comparison
- Headline gaps and suggestions
- Description audit and recommendations
- Pinning strategy recommendations

## MCP Data Used

This skill pulls live data from Google Ads via:
- `ad_group_ad` action with GAQL query
- Fields: RSA headlines, descriptions, ad strength, metrics
- Filters for RESPONSIVE_SEARCH_AD type only

## Limitation Note

Google Ads API provides **ad-level** metrics, not individual headline/description performance. For asset-level data:
- Use Google Ads UI → Assets → "View asset details"
- Export and provide that data for deeper analysis
