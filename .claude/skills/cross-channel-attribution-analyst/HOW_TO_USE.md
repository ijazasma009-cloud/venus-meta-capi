# How to Use This Skill

Hey Claude—I just added the "cross-channel-attribution-analyst" skill. Can you help me understand which of my marketing channels is actually driving conversions?

## Example Invocations

**Example 1: Full Attribution Analysis**
Hey Claude—I just added the "cross-channel-attribution-analyst" skill. Here's my conversion path data from Google Analytics. I want to understand which channels are undervalued and where I should shift budget.

**Example 2: Model Comparison**
Hey Claude—I just added the "cross-channel-attribution-analyst" skill. I have conversion data across 5 channels. Show me how attribution changes between last-click and position-based models.

**Example 3: Channel Role Analysis**
Hey Claude—I just added the "cross-channel-attribution-analyst" skill. I suspect my Facebook ads are being undervalued because they mostly start journeys. Can you analyze channel roles?

**Example 4: Budget Reallocation**
Hey Claude—I just added the "cross-channel-attribution-analyst" skill. Here's my channel spend and conversion data. Based on true contribution, how should I reallocate my $50K/month budget?

**Example 5: Brand Search Investigation**
Hey Claude—I just added the "cross-channel-attribution-analyst" skill. Brand search gets 60% of our conversions on last-click. Is it really that valuable or are other channels doing the real work?

**Example 6: Journey Pattern Analysis**
Hey Claude—I just added the "cross-channel-attribution-analyst" skill. I want to understand our typical customer journey—how many touchpoints, how long, and which paths lead to the highest-value conversions.

## What to Provide

**Required:**
- Conversion path data (channel sequence for each conversion)
- Channels in your marketing mix
- Time period for analysis

**Strongly Recommended:**
- Spend by channel
- Conversion values (if variable)
- Timestamps per touchpoint

**Optional:**
- Customer lifetime value data
- Device data
- Conversion lag data
- Campaign-level breakdown

## Where to Get Data

**Google Analytics 4:**
- Advertising > Attribution > Conversion paths
- Export path data or use Model comparison report

**Google Ads:**
- Attribution > Path metrics
- Search attribution reports

**Platform Reports:**
- Meta: Attribution settings, assisted conversions
- LinkedIn: Conversion path reports

## What You'll Get

1. **Model Comparison** - See how credit shifts between attribution models
2. **Channel Roles** - Which channels initiate, assist, or close conversions
3. **Assist Analysis** - Find undervalued channels contributing to journeys
4. **True CPA** - Cost per acquisition based on weighted attribution
5. **Reallocation Plan** - Where to shift budget based on true contribution
6. **Journey Insights** - Common paths and high-value patterns
7. **Testing Plan** - How to validate findings with incrementality tests

## Pro Tips

- Export at least 30 days of path data for meaningful patterns
- Separate brand and non-brand paid search—they have very different roles
- "Direct" often masks attribution failures—investigate high direct %
- Multi-touch analysis matters most for considered purchases (B2B, high-value B2C)
- Use this analysis to justify testing, not to make immediate drastic changes
- Run incrementality tests on channels that show big gaps between models
