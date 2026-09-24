---
name: facebook-ads-campaign-structure
description: Designs optimal Meta Ads campaign architecture including campaign hierarchy, CBO vs ABO decisions, consolidation strategy, and naming conventions. Creates structure that maximizes algorithm learning. Use when setting up new accounts or restructuring existing ones.
---

# Facebook Ads Campaign Structure

Structure is strategy. The wrong architecture fights the algorithm. The right one lets it fly.

## Core Philosophy

**Meta's algorithm is powerful—but it needs data to learn.**

Every time you fragment your account into more campaigns, more ad sets, more audiences—you're splitting your conversion data into smaller pieces. The algorithm gets less signal from each piece. Learning takes longer. Performance suffers.

**The modern best practice is consolidation.**

- Fewer campaigns with more data each
- Fewer ad sets with more conversions each
- Let the algorithm optimize across a larger pool

**Your account structure is the foundation.** Bad structure = constant firefighting. Good structure = the algorithm doing most of the work.

**The goal: Maximum learning signal with minimum fragmentation.**

---

## Required Context

### Must Have

1. **Business Goals**
   - Primary objective (sales, leads, awareness)
   - Target CPA or ROAS
   - Budget level (daily/monthly)

2. **Current State (if restructuring)**
   - Number of campaigns/ad sets/ads
   - Current conversion volume
   - What's working, what's not

3. **Audience Strategy**
   - Customer acquisition (prospecting)
   - Retargeting needs
   - Different customer segments?

### Strongly Recommended

4. **Product/Offer Structure**
   - Single product or multiple?
   - Different price points?
   - Different customer journeys?

5. **Geographic Scope**
   - Single country or multiple?
   - Different languages needed?

### Nice to Have

6. **Historical Context**
   - How long running ads?
   - Past structure experiments
   - Seasonal patterns

---

## Campaign Structure Framework

### The Consolidation Principle

**Old Way (Pre-2022):**
```
❌ Many campaigns → Many ad sets → Split data → Slow learning
```

**New Way (2024+):**
```
✅ Few campaigns → Consolidated ad sets → Rich data → Fast learning
```

**Why Consolidation Works:**
- Algorithm needs 50+ conversions per ad set per week for optimal learning
- More data per ad set = faster exit from learning phase
- Fewer auction overlaps = lower CPMs
- Simpler management = fewer mistakes

---

### Campaign-Level Decisions

**Campaign Objectives - Match Your Goal:**

| Business Goal | Recommended Objective | When to Use |
|---------------|----------------------|-------------|
| Online sales | Sales (Purchase) | E-commerce |
| Lead generation | Leads (Lead Form or Website) | B2B, Services |
| App installs | App Promotion | Mobile apps |
| Store visits | Store Traffic | Local businesses |
| Brand awareness | Awareness | Top-of-funnel only |
| Video views | Engagement | Content promotion |

**CBO vs ABO Decision:**

| Factor | Use CBO | Use ABO |
|--------|---------|---------|
| Budget allocation | Want algorithm to decide | Need manual control |
| Ad set count | 3-5 ad sets | 1-2 ad sets OR testing |
| Conversion volume | High (50+/week/ad set) | Lower, need guaranteed spend |
| Testing | Not testing audiences | Testing specific audiences |
| Experience level | Confident in algorithm | Want more control |

**CBO Best Practices:**
- Minimum 3 ad sets (gives algorithm options)
- Similar audience sizes across ad sets
- Set ad set minimum spend if needed
- Don't use for strict A/B tests

**ABO Best Practices:**
- Use for testing specific audiences
- Use when budget must be guaranteed per segment
- Use for retargeting with small audiences
- More work but more control

---

### Recommended Campaign Structures

#### Structure A: Simplified (Most Accounts)

**Best for:** Accounts <$10k/month, single product/offer

```
📁 [CONV] Prospecting
  └── 📂 LAL + Broad Combined (CBO)
        ├── 📄 Ad 1: Primary creative
        ├── 📄 Ad 2: Variation A
        ├── 📄 Ad 3: Variation B
        └── 📄 Ad 4: Test creative

📁 [CONV] Retargeting
  └── 📂 All Website Visitors + Engagers (ABO)
        ├── 📄 Ad 1: Reminder
        ├── 📄 Ad 2: Social proof
        └── 📄 Ad 3: Urgency/offer
```

**Total: 2 campaigns, 2 ad sets**

---

#### Structure B: Standard (Most Growing Accounts)

**Best for:** Accounts $10k-50k/month, proven creative

```
📁 [CONV] Prospecting - Cold
  └── 📂 CBO
        ├── 📂 LAL Purchasers 1-2%
        │     └── [4-6 ads]
        ├── 📂 LAL Email List 2%
        │     └── [4-6 ads]
        └── 📂 Advantage+ / Broad
              └── [4-6 ads]

📁 [CONV] Retargeting - Warm
  └── 📂 ABO
        ├── 📂 Website Visitors 30d (exclude purchasers)
        │     └── [3-4 ads]
        └── 📂 Engagers (video, IG, FB)
              └── [3-4 ads]

📁 [CONV] Retargeting - Hot
  └── 📂 ABO
        └── 📂 Cart Abandoners 14d
              └── [3-4 ads]
```

**Total: 3 campaigns, 6 ad sets**

---

#### Structure C: Scaled (High-Volume Accounts)

**Best for:** Accounts $50k+/month, multiple products/offers

```
📁 [CONV] Prospecting - Primary Product
  └── 📂 CBO
        ├── 📂 LAL Purchasers (Product A) 2%
        ├── 📂 LAL High-Value 1%
        ├── 📂 Advantage+ Shopping
        └── 📂 Interest Stack (testing)

📁 [CONV] Prospecting - Secondary Product
  └── 📂 CBO
        ├── 📂 LAL Purchasers (Product B) 2%
        └── 📂 Advantage+ Shopping

📁 [CONV] Retargeting - All Products
  └── 📂 ABO
        ├── 📂 Product Viewers 30d (DPA)
        ├── 📂 Cart Abandoners 14d (DPA)
        └── 📂 Engagers

📁 [CONV] Retention - Past Customers
  └── 📂 ABO
        ├── 📂 Purchasers 30-180d
        └── 📂 Lapsed 180d+
```

**Total: 4 campaigns, 10 ad sets**

---

#### Structure D: Lead Generation

**Best for:** B2B, services, high-ticket

```
📁 [LEADS] Prospecting
  └── 📂 CBO
        ├── 📂 LAL Leads/Customers 2%
        ├── 📂 Industry Interests
        └── 📂 Job Title Targeting

📁 [LEADS] Retargeting
  └── 📂 ABO
        ├── 📂 Website Visitors 60d
        ├── 📂 Video Viewers 50%+
        └── 📂 Lead Form Abandoners

📁 [LEADS] Nurture
  └── 📂 ABO
        └── 📂 Leads (non-converted to customer)
```

**Total: 3 campaigns, 7 ad sets**

---

### Ad Set Guidelines

**Conversions Needed per Ad Set:**

| Weekly Conversions | Learning Status | Recommendation |
|-------------------|-----------------|----------------|
| 50+ | Optimal learning | Maintain structure |
| 25-50 | Limited learning | Consider consolidating |
| 10-25 | Struggling | Consolidate or increase budget |
| <10 | Not learning | Merge with other ad sets |

**Audience Sizing:**

| Budget Level | Minimum Audience | Ideal Audience |
|--------------|------------------|----------------|
| $50/day | 500K | 2M+ |
| $100/day | 1M | 5M+ |
| $500/day | 5M | 10M+ |
| $1000+/day | 10M+ | Broad/Advantage+ |

**Ads per Ad Set:**
- Minimum: 3 (gives algorithm options)
- Ideal: 4-6 (good testing volume)
- Maximum: 10 (beyond this, hard to get signal)

---

### Naming Conventions

**Standard Format:**

```
Campaign: [OBJECTIVE] [FUNNEL] - [DESCRIPTION] - [DATE/VERSION]
Ad Set:   [AUDIENCE TYPE] - [AUDIENCE NAME] - [TARGETING DETAIL]
Ad:       [CREATIVE TYPE] - [ANGLE/HOOK] - [VERSION]
```

**Examples:**

**Campaign Names:**
- `[CONV] Prospecting - LAL Focus - Q1 2024`
- `[CONV] Retargeting - Full Funnel`
- `[LEADS] Prospecting - Industry Targeting`
- `[CONV] ASC - Advantage+ Shopping`

**Ad Set Names:**
- `LAL - Purchasers 2% - US`
- `RTG - Website 30d - Exclude Purchasers`
- `INT - Fitness + Health - 25-45`
- `BROAD - Advantage+ Audience`

**Ad Names:**
- `VID - Pain Hook - v1`
- `IMG - UGC Style - Social Proof`
- `CAR - Product Features - v2`
- `VID - Testimonial - Sarah`

**Abbreviations:**
| Abbreviation | Meaning |
|--------------|---------|
| CONV | Conversions campaign |
| LEADS | Lead generation |
| AWARE | Awareness |
| PROS | Prospecting |
| RTG | Retargeting |
| LAL | Lookalike |
| INT | Interest-based |
| BROAD | Broad/Advantage+ |
| VID | Video |
| IMG | Image/Static |
| CAR | Carousel |
| DPA | Dynamic Product Ad |

---

### Consolidation Strategy (For Existing Accounts)

**When to Consolidate:**
- Too many campaigns with similar objectives
- Ad sets with <25 weekly conversions
- Overlapping audiences
- Same creative running in multiple places

**Consolidation Process:**

1. **Audit current structure**
   - List all campaigns, ad sets, conversions
   - Identify low performers (<25 conv/week)
   - Identify overlapping audiences

2. **Design target structure**
   - Use frameworks above
   - Aim for 50+ conversions per ad set

3. **Migration approach (choose one):**

| Approach | When to Use | Risk Level |
|----------|-------------|------------|
| Gradual | Account performing OK | Low |
| Fresh Start | Account broken/messy | Medium |
| Parallel | Need to compare | Higher cost |

**Gradual Migration:**
- Week 1: Create new campaign structure
- Week 2: Start shifting budget (20-30%)
- Week 3: Continue shift (50%)
- Week 4: Complete migration, pause old

**Fresh Start:**
- Pause all existing campaigns
- Launch new structure
- Risk: Lose historical learning
- Benefit: Clean slate

---

## Output Format

```
═══════════════════════════════════════════════════════════════════
FACEBOOK ADS CAMPAIGN STRUCTURE PLAN
Account: [Account Name]
Created: [Date]
Budget: $[X]/month
═══════════════════════════════════════════════════════════════════

📊 STRUCTURE OVERVIEW
────────────────────────────────────────────────────────────────────

**Recommended Structure:** [Simplified/Standard/Scaled/Lead Gen]
**Total Campaigns:** [X]
**Total Ad Sets:** [X]
**Budget Type:** [CBO/ABO/Mixed]

**Key Principles:**
- [Principle 1]
- [Principle 2]
- [Principle 3]

═══════════════════════════════════════════════════════════════════

🏗️ CAMPAIGN ARCHITECTURE
────────────────────────────────────────────────────────────────────

### Campaign 1: [Campaign Name]

**Settings:**
- Objective: [Objective]
- Budget Type: [CBO/ABO]
- Daily Budget: $[X]

**Ad Sets:**

| Ad Set | Audience | Est. Size | Budget | Ads |
|--------|----------|-----------|--------|-----|
| [Name] | [Description] | [Size] | $[X] | [#] |

**Exclusions:** [List]

────────────────────────────────────────────────────────────────────

### Campaign 2: [Campaign Name]

[Same format...]

═══════════════════════════════════════════════════════════════════

📝 NAMING CONVENTIONS
────────────────────────────────────────────────────────────────────

**Campaign Format:** `[OBJECTIVE] [FUNNEL] - [DESCRIPTION]`
**Ad Set Format:** `[AUDIENCE TYPE] - [AUDIENCE NAME]`
**Ad Format:** `[CREATIVE TYPE] - [ANGLE] - [VERSION]`

**Examples for this account:**
- Campaign: `[CONV] Prospecting - Q1 2024`
- Ad Set: `LAL - Purchasers 2%`
- Ad: `VID - Pain Hook - v1`

═══════════════════════════════════════════════════════════════════

📈 BUDGET DISTRIBUTION
────────────────────────────────────────────────────────────────────

| Campaign | % of Budget | Daily | Monthly |
|----------|-------------|-------|---------|
| [Name] | [X]% | $[X] | $[X] |

**Funnel Breakdown:**
- Prospecting: [X]%
- Retargeting: [X]%
- Retention: [X]%

═══════════════════════════════════════════════════════════════════

✅ IMPLEMENTATION CHECKLIST
────────────────────────────────────────────────────────────────────

**Phase 1: Setup**
- [ ] Create campaigns with correct objectives
- [ ] Configure CBO/ABO settings
- [ ] Set up ad sets with correct audiences
- [ ] Apply naming conventions

**Phase 2: Creative**
- [ ] Upload creatives to each ad set
- [ ] Ensure 4-6 ads per ad set
- [ ] Verify UTM parameters

**Phase 3: Launch**
- [ ] Review all settings
- [ ] Set budgets
- [ ] Launch campaigns
- [ ] Monitor first 48 hours

═══════════════════════════════════════════════════════════════════

⚠️ RULES & BEST PRACTICES
────────────────────────────────────────────────────────────────────

**Do:**
- Consolidate where possible
- Use CBO for 3+ ad sets
- Maintain 4-6 ads per ad set
- Exclude appropriately

**Don't:**
- Create overlapping audiences
- Fragment into too many ad sets
- Use ABO with many ad sets
- Forget exclusions

═══════════════════════════════════════════════════════════════════
```

---

## Common Scenarios

### Scenario 1: "I have 20 campaigns and it's a mess"
**Diagnosis:** Over-fragmented, algorithm can't learn
**Solution:** Consolidate to 3-4 campaigns using frameworks above
**Approach:** Gradual migration over 4 weeks

**Verdict:** Less is more. Consolidate ruthlessly.

### Scenario 2: "Should I use CBO or ABO?"
**Decision Framework:**
- 3+ ad sets with similar audiences → CBO
- Testing specific audiences → ABO
- Need guaranteed spend → ABO
- Want hands-off optimization → CBO

**Verdict:** Default to CBO unless you have specific reason for ABO.

### Scenario 3: "I want to test 10 different audiences"
**Problem:** 10 ad sets will fragment data
**Solution:** Group similar audiences. Test 3-4 audience "types" not 10 individuals.
**Alternative:** Test sequentially, not simultaneously

**Verdict:** Test fewer things more rigorously.

### Scenario 4: "My retargeting and prospecting are in one campaign"
**Problem:** Algorithm optimizes for lowest-cost conversions (retargeting), starves prospecting
**Solution:** Separate campaigns with separate budgets
**Why:** Ensures prospecting gets budget even though it's more expensive

**Verdict:** Always separate prospecting and retargeting.

### Scenario 5: "Advantage+ Shopping Campaign vs regular structure"
**When ASC Works:**
- E-commerce with product catalog
- Strong pixel data (1000+ purchases)
- Want maximum automation

**When Regular Structure Works:**
- Need more control
- Testing specific audiences
- Brand/creative testing focus

**Verdict:** Test ASC alongside regular structure. Let performance decide.

---

## Limitations

1. **Cannot restructure your account** - Provides blueprint, you implement
2. **Optimal structure varies** - Guidelines, not absolute rules
3. **Algorithm behavior changes** - Best practices evolve
4. **Cannot account for all business models** - May need customization
5. **Historical data matters** - Fresh accounts behave differently
6. **Doesn't guarantee performance** - Structure enables, doesn't ensure

---

## Quality Checklist

Before delivering structure plan:
- [ ] Structure matches budget level
- [ ] CBO/ABO decisions justified
- [ ] Audiences don't overlap
- [ ] Exclusions defined
- [ ] Naming conventions specified
- [ ] Budget distribution included
- [ ] Implementation steps clear
- [ ] Best practices documented
