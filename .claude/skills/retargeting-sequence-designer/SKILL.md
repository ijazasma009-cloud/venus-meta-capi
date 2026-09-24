---
name: retargeting-sequence-designer
description: Designs strategic retargeting ad sequences based on user behavior and funnel stage. Triggers when user asks about retargeting strategy, remarketing ads, or "how do I bring back visitors?" Creates segmented audience sequences with messaging, creative direction, frequency caps, and platform recommendations. Outputs ready-to-implement retargeting playbooks.
---

# Retargeting Sequence Designer

Bring back lost visitors with the right message at the right time.

## Core Philosophy

**Retargeting is a conversation, not a chase.** Just showing the same ad repeatedly isn't retargeting—it's stalking. Strategic retargeting delivers relevant messages based on where users dropped off.

**The Goal:** Design retargeting sequences that feel helpful, not annoying, and convert abandoners into customers.

**The Principle:** Segment by behavior → Message to intent → Time appropriately → Respect frequency limits.

---

## Required Context

### Must Have

**1. Business Type**
- E-commerce / SaaS / Lead Gen / Content
- Average order value or customer value
- Purchase/conversion cycle length

**2. User Behavior Points**
What actions can you track:
- Page views (which pages)
- Product views
- Add to cart
- Checkout start
- Form starts
- Content engagement
- Previous purchases

**3. Conversion Goal**
- Primary action (purchase, signup, lead)
- Value of conversion

### Strongly Recommended

**4. Available Platforms**
Where you can run retargeting:
- Google Display/YouTube
- Meta (Facebook/Instagram)
- LinkedIn
- Programmatic
- Email

**5. Current Setup**
- Existing retargeting campaigns
- Current frequency caps
- What's working/not working

### Nice to Have

- Conversion window data (time to convert)
- Customer lifetime value segments
- Seasonal patterns
- Creative assets available
- Budget constraints

---

## Sequence Design Framework

### Step 1: Audience Segmentation

**Behavior-Based Segments:**

| Segment | Definition | Intent Level | Priority |
|---------|------------|--------------|----------|
| **Hot** | Cart abandoners, checkout started | Very High | Highest |
| **Warm** | Product viewers, engaged visitors | High | High |
| **Cool** | Category/page viewers | Medium | Medium |
| **Cold** | Bounced visitors | Low | Low |
| **Customers** | Past purchasers | Varies | Depends |

**Standard Retargeting Segments:**

```
SEGMENT HIERARCHY:

HOT AUDIENCES (Highest intent)
├── Cart Abandoners (1-3 days)
├── Cart Abandoners (4-7 days)
├── Cart Abandoners (8-14 days)
├── Checkout Abandoners
└── Pricing Page Visitors

WARM AUDIENCES (Demonstrated interest)
├── Product Viewers (1-7 days)
├── Product Viewers (8-30 days)
├── Multiple Product Viewers
├── High-Time-on-Site Visitors
└── Form Starters (Lead Gen)

COOL AUDIENCES (General interest)
├── Category Browsers
├── Blog/Content Readers
├── Homepage Visitors
└── Search/Resource Page Visitors

CUSTOMER AUDIENCES (Post-purchase)
├── Recent Customers (1-30 days)
├── Repeat Customers
├── Lapsed Customers (90+ days)
└── High-Value Customers
```

---

### Step 2: Timing Strategy

**Recency Windows:**

| Time Since Visit | User State | Messaging Approach |
|------------------|------------|-------------------|
| 0-24 hours | High intent | Reminder, urgency |
| 1-3 days | Still considering | Value reinforcement |
| 4-7 days | Cooling off | Re-engage, new angle |
| 8-14 days | May have forgotten | Brand recall, offer |
| 15-30 days | Likely moved on | Strong incentive |
| 30-60 days | Last chance | Win-back offer |
| 60+ days | Very cold | Exclude or minimal |

**Optimal Duration by Segment:**

| Segment | Recommended Window | Max Window |
|---------|-------------------|------------|
| Cart Abandoners | 14 days | 30 days |
| Product Viewers | 30 days | 60 days |
| General Visitors | 30 days | 45 days |
| Customers (upsell) | 90 days | 180 days |
| Customers (replenishment) | Based on cycle | Varies |

---

### Step 3: Frequency Strategy

**Frequency Caps by Segment:**

| Segment | Daily Cap | Weekly Cap | Total Campaign |
|---------|-----------|------------|----------------|
| Cart Abandoners | 3 | 10-15 | 30 |
| Product Viewers | 2 | 7-10 | 20 |
| General Visitors | 1-2 | 5-7 | 15 |
| Past Customers | 1 | 3-5 | 10 |

**Frequency by Platform:**

| Platform | Recommended Daily | Notes |
|----------|-------------------|-------|
| Facebook/Instagram | 1-2 per platform | Users on multiple times |
| Google Display | 3-5 across network | Lower attention |
| YouTube | 1-2 | High attention |
| LinkedIn | 1 | Professional context |
| Email | N/A | Separate cadence |

---

### Step 4: Messaging Strategy

**Message Progression Framework:**

| Stage | Day Range | Message Type | Goal |
|-------|-----------|--------------|------|
| Stage 1 | Day 1-3 | Reminder | Complete action |
| Stage 2 | Day 4-7 | Value/Benefit | Reinforce why |
| Stage 3 | Day 8-14 | Social Proof | Build trust |
| Stage 4 | Day 15-21 | Incentive | Overcome hesitation |
| Stage 5 | Day 22-30 | Urgency/Scarcity | Final push |

**Messaging by Segment:**

| Segment | Primary Message | Secondary Message | CTA |
|---------|-----------------|-------------------|-----|
| Cart Abandoners | "Still thinking?" | "Complete your order" | Return to Cart |
| Product Viewers | "Like what you saw?" | Product benefits | View Product |
| Form Abandoners | "We saved your progress" | Offer value reminder | Complete Form |
| General Visitors | "Looking for X?" | Brand value prop | Learn More |
| Customers | "Based on your purchase" | Related products | Shop Now |

---

### Step 5: Creative Direction

**Ad Format by Stage:**

| Stage | Best Formats | Creative Focus |
|-------|--------------|----------------|
| Reminder (Day 1-3) | Carousel, Dynamic | Product they viewed |
| Value (Day 4-7) | Single image, Video | Benefits, features |
| Social Proof (Day 8-14) | Testimonial, UGC | Reviews, results |
| Incentive (Day 15-21) | Single image | Offer-focused |
| Urgency (Day 22-30) | Single image | Deadline, scarcity |

**Dynamic vs. Static:**

| Use Dynamic | Use Static |
|-------------|------------|
| Multiple products viewed | Single product interest |
| E-commerce with catalog | SaaS/Services |
| Personalization needed | Brand awareness focus |
| Large product range | Limited SKUs |

---

## Output Format

### Executive Summary

```
RETARGETING SEQUENCE DESIGN

Business Type: [E-commerce/SaaS/Lead Gen]
Conversion Goal: [Action]
Platforms: [Where to run]
Total Segments: X audiences
Duration: X days total

SEQUENCE OVERVIEW:
Hot Audiences:  Day 1-14  | X creatives | X frequency cap
Warm Audiences: Day 1-30  | X creatives | X frequency cap
Cool Audiences: Day 1-30  | X creatives | X frequency cap
Customers:      Day 1-90  | X creatives | X frequency cap
```

---

### Audience Segment Definitions

**Segment 1: [Segment Name]**

```
AUDIENCE: [Name]
DEFINITION: Users who [behavior] but did not [goal]
WINDOW: Last [X] days
EXCLUSIONS: [What to exclude]
ESTIMATED SIZE: [If known]
PLATFORM: [Where to target]
```

**Targeting Setup:**
| Platform | Targeting Method |
|----------|-----------------|
| Meta | Custom Audience: [Event/Page] |
| Google | Remarketing List: [Definition] |
| LinkedIn | Website Retargeting: [Pages] |

---

### Sequence Map by Segment

**[Segment Name] Retargeting Sequence:**

```
SEQUENCE: [Name]
DURATION: [X] days
FREQUENCY CAP: [X] per day / [X] per week

DAY 1-3: REMINDER PHASE
├── Message: "[Headline]"
├── Creative: [Format + direction]
├── CTA: [Button text]
└── Offer: [If any]

DAY 4-7: VALUE PHASE
├── Message: "[Headline]"
├── Creative: [Format + direction]
├── CTA: [Button text]
└── Offer: [If any]

DAY 8-14: SOCIAL PROOF PHASE
├── Message: "[Headline]"
├── Creative: [Format + direction]
├── CTA: [Button text]
└── Offer: [If any]

DAY 15-21: INCENTIVE PHASE
├── Message: "[Headline]"
├── Creative: [Format + direction]
├── CTA: [Button text]
└── Offer: [Discount/Bonus]

DAY 22-30: URGENCY PHASE
├── Message: "[Headline]"
├── Creative: [Format + direction]
├── CTA: [Button text]
└── Offer: [Final offer + deadline]
```

---

### Ad Creative Briefs

**Creative Brief 1: [Phase Name]**

| Element | Direction |
|---------|-----------|
| **Objective** | [What this ad should accomplish] |
| **Audience** | [Who sees this] |
| **Format** | [Single image/Carousel/Video/etc.] |
| **Headline** | "[Suggested headline]" |
| **Primary Text** | "[Suggested body copy]" |
| **Visual** | [Description of image/video] |
| **CTA** | [Button text] |
| **Landing Page** | [Where it goes] |

**Example Ad Copy:**

```
HEADLINE: [Headline]

PRIMARY TEXT:
[Body copy with appropriate length for platform]

CTA: [Button]
```

---

### Platform-Specific Setup

**Meta (Facebook/Instagram):**

| Setting | Recommendation |
|---------|----------------|
| Campaign Objective | [Conversions/Traffic/etc.] |
| Optimization | [Event to optimize for] |
| Placements | [Automatic/Manual selection] |
| Bidding | [Strategy] |
| Attribution | [7-day click, 1-day view] |

**Audience Setup:**
```
Custom Audience: [Name]
Source: [Website/App/Customer List]
Event: [Specific event]
Days: [Retention period]
Exclude: [Exclusions]
```

---

**Google Ads:**

| Setting | Recommendation |
|---------|----------------|
| Campaign Type | [Display/YouTube/Performance Max] |
| Bidding | [Target CPA/Maximize Conversions] |
| Targeting Expansion | [On/Off] |
| Frequency Cap | [Setting] |

**Audience Setup:**
```
Audience Name: [Name]
Source: [GA4/Google Ads tag]
Membership: [All visitors/Event-based]
Duration: [Days]
Similar Audiences: [Enable/Disable]
```

---

### Exclusion Rules

**Who to Exclude from Each Segment:**

| Segment | Exclude |
|---------|---------|
| Cart Abandoners | Purchasers (last 30 days) |
| Product Viewers | Cart Abandoners (separate sequence), Purchasers |
| General Visitors | All more engaged segments, Purchasers |
| Customers (Upsell) | Recent purchasers (wait 7 days) |

**Exclusion Setup:**

```
EXCLUSION AUDIENCES TO CREATE:

1. Converters (Last 30 Days)
   - Definition: Completed [conversion event]
   - Use: Exclude from all prospecting/retargeting

2. Recent Purchasers (Last 7 Days)
   - Definition: Completed purchase
   - Use: Exclude from upsell (give time with product)

3. Email Subscribers
   - Definition: Signed up for email
   - Use: Exclude from lead gen retargeting
```

---

### Budget Allocation

**Recommended Budget Split:**

| Segment | % of Retargeting Budget | Rationale |
|---------|------------------------|-----------|
| Hot (Cart/Checkout) | 40-50% | Highest intent, best ROAS |
| Warm (Product/Engaged) | 30-35% | Good intent, volume |
| Cool (General) | 10-15% | Lower intent, awareness |
| Customers | 10-15% | Retention/upsell value |

**Budget by Phase:**

| Phase | Allocation | Notes |
|-------|------------|-------|
| Day 1-7 | 50% | Strike while intent is hot |
| Day 8-14 | 30% | Maintain presence |
| Day 15-30 | 20% | Final conversion attempts |

---

### KPIs and Benchmarks

**Expected Performance by Segment:**

| Segment | Target CTR | Target Conv Rate | Target ROAS |
|---------|------------|------------------|-------------|
| Cart Abandoners | 1-3% | 5-15% | 5-10x |
| Product Viewers | 0.5-1.5% | 1-5% | 3-5x |
| General Visitors | 0.2-0.8% | 0.5-2% | 2-4x |
| Customers | 0.5-1% | 2-5% | 3-6x |

*Benchmarks vary significantly by industry*

**Metrics to Monitor:**

| Metric | Frequency | Action Threshold |
|--------|-----------|------------------|
| Frequency | Daily | >4/week: Refresh creative |
| CTR | Weekly | <0.2%: New creative/message |
| Conv Rate | Weekly | Declining: Check offer/landing |
| ROAS | Weekly | <2x: Optimize or pause |
| CPM | Weekly | Rising: Audience fatigue |

---

### Implementation Checklist

**Setup Phase:**
- [ ] Create all custom audiences
- [ ] Set up exclusion audiences
- [ ] Configure pixel/tag events
- [ ] Build creative assets for each phase
- [ ] Set frequency caps

**Launch Phase:**
- [ ] Launch hot audiences first
- [ ] Add warm audiences after 3-7 days
- [ ] Monitor frequency closely
- [ ] Check exclusions are working

**Optimization Phase:**
- [ ] Review performance weekly
- [ ] Refresh creative every 2-3 weeks
- [ ] Adjust budgets based on ROAS
- [ ] Test new messages/offers
- [ ] Expand to new platforms if working

---

## Special Scenarios

### Scenario 1: E-commerce with Large Catalog
**Approach:**
- Use dynamic product ads heavily
- Segment by category viewed
- Cross-sell based on viewed products
- Sequence: Exact product → Category → Best sellers

### Scenario 2: SaaS Free Trial
**Approach:**
- Segment by trial status (started, not started, expired)
- Message based on activation milestones
- Focus on value realization, not features
- Sequence: Activation help → Feature benefits → Upgrade CTA

### Scenario 3: Lead Generation
**Approach:**
- Segment by form stage (viewed, started, abandoned)
- Emphasize lead magnet value
- Address objections (privacy, spam)
- Sequence: Remind value → Social proof → Alternative offer

### Scenario 4: High-Value B2B
**Approach:**
- Longer sequences (60-90 days)
- Account-based approach if possible
- More educational content
- Multiple CTAs (demo, case study, guide)
- Lower frequency, higher quality

---

## Limitations

**I can design:**
- Audience segmentation strategy
- Messaging sequences
- Creative direction
- Platform setup guidelines
- Frequency and timing strategy

**I cannot provide:**
- Actual audience sizes (need your data)
- Custom audience creation (need platform access)
- Creative production
- Pixel/tag implementation
- Budget recommendations without data

**For complete implementation, you'll also need:**
- Properly configured tracking pixels
- Creative design resources
- Platform ad accounts
- Budget allocation
- Testing infrastructure

---

## Quality Checklist

Before delivering sequence design:
- [ ] All behavior segments identified
- [ ] Timing windows defined for each segment
- [ ] Frequency caps specified
- [ ] Message progression makes sense
- [ ] Exclusions prevent audience overlap
- [ ] Platform-specific setup included
- [ ] Creative briefs are actionable
- [ ] Budget allocation recommended
- [ ] KPIs and benchmarks provided
- [ ] Implementation checklist included
