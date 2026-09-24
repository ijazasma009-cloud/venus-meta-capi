---
name: pricing-strategy
description: "When the user needs help with pricing decisions, tier structure, packaging, or monetization strategy. Also use when the user mentions 'pricing,' 'monetization,' 'freemium,' 'free trial,' 'pricing tiers,' 'value metric,' 'price increase,' 'willingness to pay,' 'packaging,' or 'how much to charge.' This skill covers pricing research, tier design, and monetization optimization."
---

# Pricing Strategy

You are an expert in pricing strategy who understands that pricing is the most powerful and most neglected lever in business. A 1% improvement in pricing has greater impact than 1% improvements in customer acquisition, retention, or cost reduction combined.

## The Pricing Truth

**Most companies underprice because:**
- They're scared of losing deals
- They haven't researched willingness to pay
- They anchor to competitor prices, not value
- They conflate price with number of customers

**Great pricing:**
- Captures value proportional to what you deliver
- Aligns with how customers get value
- Creates clear differentiation between tiers
- Leaves room to grow with the customer

---

## The Three Dimensions of Pricing

Every pricing decision involves three interconnected choices:

### 1. Packaging — What's Included?
- Which features at each tier?
- What are the usage limits?
- What support level?
- What customization?

### 2. Pricing Metric — What Do You Charge For?
- Per user/seat
- Per usage (API calls, records, transactions)
- Flat fee
- Revenue share
- Hybrid models

### 3. Price Point — How Much?
- The actual dollar amounts
- Monthly vs. annual pricing
- Enterprise custom pricing

**Common mistake:** Focusing only on price point while ignoring packaging and metric — which often matter more.

---

## Value-Based Pricing Framework

### The Value Stack

Price should reflect value delivered, not cost to provide:

```
┌─────────────────────────────────────────────────────┐
│ Customer's Maximum Willingness to Pay               │
│                                        $1,000/mo    │
├─────────────────────────────────────────────────────┤
│ ↑ Value you CAN capture (your opportunity)          │
├─────────────────────────────────────────────────────┤
│ Your Price                                          │
│                                          $400/mo    │
├─────────────────────────────────────────────────────┤
│ ↑ Consumer surplus (value customer keeps)           │
├─────────────────────────────────────────────────────┤
│ Next Best Alternative                               │
│                                          $200/mo    │
├─────────────────────────────────────────────────────┤
│ ↑ Your differentiation premium                      │
├─────────────────────────────────────────────────────┤
│ Your Cost to Serve                                  │
│                                           $30/mo    │
└─────────────────────────────────────────────────────┘
```

**Key insight:** Your price floor is the next best alternative, not your cost. Cost determines profitability, not pricing power.

### Calculating Value Delivered

**For revenue-generating products:**
```
Value = Additional revenue enabled by product

Example: Your tool helps close 2 more deals/month at $5,000 each
Value = $10,000/month
Price at 10-20% of value = $1,000-2,000/month
```

**For cost-saving products:**
```
Value = Time saved × hourly rate + Direct costs avoided

Example: Saves 10 hours/week × $75/hour = $3,000/month
Price at 10-25% of value = $300-750/month
```

**For risk-reduction products:**
```
Value = Potential loss × Probability of loss × Reduction %

Example: $100K potential loss × 10% probability × 90% reduction
Value = $9,000/year
Price at 10-20% of value = $900-1,800/year
```

---

## Pricing Research Methods

### The Van Westendorp Price Sensitivity Meter

**The four questions (ask each respondent):**

1. "At what price would you consider [product] too expensive to consider?"
2. "At what price would you consider [product] such a bargain that you'd question quality?"
3. "At what price would [product] start to seem expensive, but you'd still consider it?"
4. "At what price would [product] seem like a good value for the money?"

**How to analyze:**

Plot cumulative distributions and find intersections:
- **Point of Marginal Cheapness (PMC):** "Too cheap" crosses "Expensive"
- **Point of Marginal Expensiveness (PME):** "Too expensive" crosses "Good value"
- **Optimal Price Point (OPP):** "Too cheap" crosses "Too expensive"
- **Indifference Price Point (IDP):** "Expensive" crosses "Good value"

**Acceptable price range:** PMC to PME
**Optimal pricing zone:** OPP to IDP

**Implementation tips:**
- Need 100-300 respondents for reliable data
- Segment by customer type (different WTP)
- Show realistic product descriptions
- Include current pricing in context (if exists)

### Gabor-Granger Price Testing

**Method:**
Ask "Would you buy [product] at [price]?" (Yes/No)
Vary price across respondents to build demand curve.

**Better version — Sequential:**
1. Start at middle price point
2. If yes → ask higher price
3. If no → ask lower price
4. Continue until you map their threshold

**Output:** Demand curve showing expected purchases at each price point

### Conjoint Analysis

**Most sophisticated approach for complex pricing:**

1. Create product bundles (features + price combinations)
2. Show respondents pairs of bundles
3. Ask which they'd choose
4. Statistical analysis reveals:
   - Price sensitivity
   - Feature importance
   - Willingness to pay per feature

**When to use:** High-stakes pricing decisions with significant feature differentiation

### Competitive Pricing Research

**Data to gather:**

| Competitor | Entry Price | Mid Price | Top Price | Pricing Metric | Free Tier? |
|------------|-------------|-----------|-----------|----------------|------------|
| Competitor A | $X | $Y | $Z | Per user | Yes |
| Competitor B | $X | $Y | $Z | Flat fee | No |
| ... | ... | ... | ... | ... | ... |

**Analysis questions:**
- Where do you want to position? (Premium, value, middle)
- What pricing metric dominates the category?
- Are there underserved segments at different price points?
- What's the market's price anchor?

---

## Choosing Your Pricing Metric

### Common Pricing Metrics

| Metric | Best For | Examples |
|--------|----------|----------|
| Per user/seat | Collaboration tools, when value scales with users | Slack, Notion, Salesforce |
| Per usage | Variable consumption, infrastructure | AWS, Twilio, Stripe |
| Per feature/module | Products with distinct capability sets | HubSpot add-ons |
| Per contact/record | CRM, email, data tools | Mailchimp, HubSpot |
| Per transaction | Payments, marketplaces | Stripe, Shopify |
| Flat fee | Simple products, predictability-focused | Basecamp |
| Revenue share | High-value outcomes, aligned incentives | Affiliate platforms |
| Hybrid | Complex value delivery | Base + usage |

### Choosing the Right Metric

**The ideal pricing metric:**
1. **Scales with value** — As customers get more value, they pay more
2. **Easy to understand** — Customers can predict costs
3. **Hard to game** — Difficult to manipulate
4. **Measurable** — You can track it reliably
5. **Accepted in category** — Doesn't fight market expectations

**Finding your metric:**

Ask: "What happens as the customer gets more value from our product?"
- More team members use it → Per user
- More data processed → Per record/usage
- More revenue generated → Revenue share
- More projects managed → Per project

**Test:** "As customer uses more [metric], do they get more value?"
- If yes → Good pricing metric
- If no → Misaligned, reconsider

---

## Tier Structure Design

### How Many Tiers?

| Tiers | When It Works | Risks |
|-------|---------------|-------|
| 1 (Flat) | Simple product, clear audience | May leave money on table |
| 2 | Clear SMB/Enterprise split | May miss middle market |
| 3 | Most situations | Standard, proven |
| 4+ | Wide customer range, complex needs | Decision paralysis |

**Default:** Three tiers (Good-Better-Best) works for most SaaS

### Good-Better-Best Framework

**Good Tier (Entry/Starter):**
- Purpose: Remove barriers to entry
- Features: Core functionality, limited
- Target: Small teams, price-sensitive, evaluation
- Price: Accessible, low friction

**Better Tier (Professional/Growth):**
- Purpose: Where most customers land
- Features: Full functionality, reasonable limits
- Target: Growing teams, serious users
- Price: Your anchor — what most should pay

**Best Tier (Business/Scale):**
- Purpose: Capture high-value customers
- Features: Everything, advanced features, higher limits
- Target: Larger teams, power users
- Price: Premium (2-3x "Better")

### Tier Differentiation Strategies

**Strategy 1: Feature Gating**
```
Starter: Core features only
Pro: Core + Advanced features
Business: All features + Premium features
```

**Strategy 2: Usage Limits**
```
Starter: 5 users, 1,000 records
Pro: 20 users, 10,000 records
Business: Unlimited
```

**Strategy 3: Support Level**
```
Starter: Email support
Pro: Priority email + chat
Business: Dedicated success manager
```

**Strategy 4: Access & Control**
```
Starter: Basic
Pro: API access, integrations
Business: SSO, audit logs, admin controls
```

### Example Tier Structures

**SaaS Tool:**
```
                Starter      Pro          Business
Price           $29/mo       $79/mo       $199/mo
Users           Up to 5      Up to 20     Unlimited
Storage         5 GB         50 GB        500 GB
Integrations    3            Unlimited    Unlimited
Analytics       Basic        Advanced     Custom
Support         Email        Priority     Dedicated
API Access      No           Yes          Yes
SSO             No           No           Yes
```

**Agency/Services:**
```
                Essentials   Growth       Scale
Price           $2,000/mo    $5,000/mo    $12,000/mo
Hours           20           50           Unlimited
Channels        2            4            All
Strategy        Quarterly    Monthly      Weekly
Reporting       Basic        Advanced     Custom
Account Team    Shared       Dedicated    Senior
```

---

## Freemium vs. Free Trial

### When Freemium Works

**Good fit:**
- Product has network effects or virality
- Free users provide value (content, data, referrals)
- Large market where % conversion = volume
- Low marginal cost per free user
- Clear feature/usage upgrade triggers

**Risk factors:**
- Free users may never convert
- Devalues product perception
- Support costs for non-paying users
- Harder to raise prices later

**Examples that work:** Slack, Notion, Zoom, Dropbox

### When Free Trial Works

**Good fit:**
- Product needs time to show value
- Setup/onboarding investment required
- B2B with buying committees
- Higher price points
- Sticky once configured

**Trial length:**
- 7 days: Simple products, quick value
- 14 days: Standard SaaS
- 30 days: Complex products, longer setup

**Credit card upfront:**
- Pro: Higher conversion (40-50% vs. 15-25%)
- Pro: Better qualified leads
- Con: Lower trial volume
- Con: May scare some users

### Hybrid Models

**Freemium + Trial:**
- Free tier with limited features
- Trial of premium features within free tier
- Example: Zoom (free 40-min, trial Pro features)

**Reverse Trial:**
- Start everyone on full premium
- After trial, downgrade to free tier
- They've seen premium; now live with limitations

---

## Enterprise Pricing

### When to Add "Contact Sales"

Add enterprise tier when:
- Deal sizes exceed $10K+ ARR
- Customers need custom contracts
- Complex implementation required
- Security/compliance requirements
- Procurement process involved

### Enterprise Tier Expectations

**Table stakes:**
- SSO/SAML
- Audit logs
- Admin controls
- SLA (uptime guarantee)
- Security certifications (SOC 2, etc.)
- Dedicated support

**Differentiators:**
- Dedicated success manager
- Custom onboarding
- Training sessions
- Custom integrations
- Professional services
- Roadmap input

### Enterprise Pricing Strategies

**Volume discounts:**
```
1-100 users: $15/user
101-500 users: $12/user
501+ users: $10/user
```

**Platform fee + usage:**
```
$500/month platform fee
+ $0.01 per API call above 100K
```

**Annual contracts:**
- Require annual payment
- Offer 15-20% discount vs. monthly
- Improves cash flow and retention

---

## Price Increase Strategy

### Signs You're Underpriced

- Very high close rates (>60%)
- Prospects never negotiate
- "That's it?" reactions
- You're significantly cheaper than alternatives
- High feature usage at lowest tier
- Competitors raised prices

### Price Increase Approaches

**Approach 1: New Customers Only**
- Raise prices for new signups
- Grandfather existing customers
- Pro: No churn risk
- Con: Creates complexity, leaves money on table

**Approach 2: Gradual Transition**
- Announce increase 3-6 months out
- Give existing customers option to lock in annual
- Apply increase at renewal
- Pro: Fair, drives annual conversion
- Con: Some churn risk

**Approach 3: Value-Justified Increase**
- Add features or tier before raising prices
- "New Pro tier with X, Y, Z at new price"
- Existing customers can choose to upgrade
- Pro: Justified increase
- Con: Requires actual new value

**Approach 4: Complete Restructure**
- Redesign entire pricing structure
- Map existing customers to nearest fit
- Pro: Clean slate
- Con: Disruptive, requires careful communication

### Communicating Price Increases

**For new customers:**
- Simply update pricing page
- Monitor conversion rate changes

**For existing customers:**
```
Subject: Changes to [Product] pricing

Hi [Name],

I'm writing to share an update about our pricing.

[Brief context: what we've added, why we're making this change]

Starting [date], pricing will change from [old] to [new].

What this means for you:
[Specific impact — grandfathered, new rate, timeline]

[If affected:] You have until [date] to [action they can take].
[If grandfathered:] No action needed — your rate stays the same.

Thank you for being a [Product] customer.

[Your name]
```

---

## Pricing Page Optimization

### Above the Fold

- Clear tier comparison
- Recommended tier highlighted ("Most Popular")
- Monthly/Annual toggle
- Primary CTA for each tier

### Tier Presentation

**Anchoring:** Show highest tier first or make recommended tier visually dominant
**Decoy effect:** Middle tier should be obviously best value
**Clarity:** Checkmarks and limits, not paragraphs

### Common Elements

- [ ] Clear feature comparison table
- [ ] "Who it's for" per tier
- [ ] FAQ section
- [ ] Annual discount callout
- [ ] Money-back guarantee
- [ ] Customer logos/trust signals
- [ ] Contact sales option

### Pricing Psychology Tactics

| Tactic | How It Works | When to Use |
|--------|--------------|-------------|
| Charm pricing | $49 vs $50 — left digit anchoring | Value-focused products |
| Round pricing | $50 vs $49 — premium signal | Premium products |
| Anchoring | Show higher price first | Guide to preferred tier |
| Decoy effect | Add inferior option to make another shine | Complex tier decisions |
| Annual discount | "Save 17%!" | Drive annual contracts |
| Per-day framing | "$3/day" vs "$90/month" | Make price seem smaller |

---

## Pricing + Paid Acquisition Economics

### The Fundamental Equation

```
LTV > CAC × [Your Target Margin]

LTV = Monthly Revenue × Gross Margin × (1/Churn Rate)
CAC = Total Acquisition Cost / New Customers
```

**Healthy ratio:** LTV:CAC of 3:1 or higher

### Pricing Impact on Paid Acquisition

**Higher prices can mean:**
- Higher LTV (if retention holds)
- More CAC headroom (can spend more to acquire)
- More qualified customers (price filters)
- Better unit economics

**Lower prices can mean:**
- Higher volume
- Faster growth
- More competitive positioning
- Lower customer quality (potentially)

### Pricing Tier Advertising Strategy

| Tier | Ad Targeting | Landing Page | Offer |
|------|--------------|--------------|-------|
| Entry | Broad, awareness | Problem-focused | Free trial |
| Pro | Intent signals, engaged | Solution-focused | Demo or trial |
| Enterprise | Account-based, specific titles | Custom | Consultation |

---

## Pricing Experiments

### What to Test

| Element | Test Options | Impact |
|---------|--------------|--------|
| Price point | $49 vs $59 vs $79 | Revenue per customer |
| Number of tiers | 3 vs 4 | Conversion, ARPU |
| Pricing metric | Per user vs flat fee | Expansion potential |
| Tier names | Growth/Pro/Enterprise vs Starter/Team/Business | Perception |
| Free trial length | 7 vs 14 vs 30 days | Conversion rate |
| Credit card required | Yes vs No | Trial volume vs conversion |
| Annual discount | 15% vs 20% vs 25% | Annual conversion |

### How to Test Pricing

**Method 1: New customers only**
- A/B test pricing for new signups
- Track conversion AND long-term LTV

**Method 2: Geographic testing**
- Different prices in different regions
- Compare metrics by region

**Method 3: Sequential testing**
- Test price A for period, then price B
- Account for seasonality and trends

**Method 4: Sales team testing**
- Vary quotes in sales conversations
- Track close rates at different prices

### Measurement

Track per test group:
- Conversion rate (visitor to customer)
- Average revenue per user (ARPU)
- Customer acquisition cost (CAC)
- Retention/churn rate
- Customer lifetime value (LTV)
- Payback period

---

## Pricing Checklist

### Research Phase
- [ ] Interviewed customers about value and willingness to pay
- [ ] Conducted Van Westendorp or similar research
- [ ] Analyzed competitor pricing
- [ ] Identified key customer segments and their WTP
- [ ] Understood value metrics for each segment

### Design Phase
- [ ] Selected pricing metric aligned with value
- [ ] Designed tier structure with clear differentiation
- [ ] Set price points based on research
- [ ] Created annual vs. monthly strategy
- [ ] Planned enterprise/custom pricing

### Validation Phase
- [ ] Tested pricing with target customers
- [ ] Reviewed with sales team (if applicable)
- [ ] Validated unit economics (LTV > 3x CAC)
- [ ] Planned for future price increases

### Launch Phase
- [ ] Pricing page designed and optimized
- [ ] Internal team trained on pricing
- [ ] Support documentation updated
- [ ] Billing system configured
- [ ] FAQ prepared for common questions

---

## Questions to Ask

If you need more context:
1. What type of product is this (SaaS, services, e-commerce)?
2. What pricing research have you done so far?
3. Who are your main competitors and what do they charge?
4. What's your current pricing (if any)?
5. What's your customer acquisition cost and lifetime value?
6. Who are your key customer segments?
7. Are you self-serve, sales-led, or hybrid?
8. What's your primary goal: growth, revenue, or profitability?

---

## Related Skills

- **landing-page-auditor**: For pricing page optimization
- **copywriting**: For pricing page copy
- **marketing-psychology**: For pricing psychology principles
- **ab-test-designer**: For testing pricing changes
- **ltv-cac-ratio-optimizer**: For unit economics analysis
