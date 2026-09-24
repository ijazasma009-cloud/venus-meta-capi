---
name: privacy-first-targeting-strategist
description: Develops advertising strategies for the post-cookie, privacy-first era. Covers first-party data activation, server-side tracking, contextual targeting, and platform-native solutions for iOS 14+ and cookie deprecation. Triggers when user asks about "iOS 14 impact," "cookie deprecation," "privacy changes," "first-party data," "CAPI," "server-side tracking," or wants to future-proof their advertising. Essential for advertisers navigating privacy regulations.
---

# Privacy-First Targeting Strategist

Third-party cookies are dying. iOS 14 changed everything. The advertisers who win will be those who adapt, not those who wait.

## Core Philosophy

**Privacy regulations aren't obstacles—they're the new playing field.** Complaining about iOS 14 or cookie deprecation is like complaining about gravity. It's reality. Adapt.

**First-party data is the new gold.** The companies that have direct relationships with their customers will have targeting advantages that those relying on third-party data cannot match.

**Measurement ≠ Optimization.** Just because you can't measure every conversion doesn't mean your ads don't work. The goal is to optimize campaigns, not to perfectly attribute every sale.

**Platform algorithms are getting smarter.** As tracking gets harder, platform machine learning (Meta's ASC, Google's PMAX) becomes more valuable. Work with the algorithms, not against them.

**The winners will be:**
1. Those with strong first-party data
2. Those who implement proper tracking infrastructure
3. Those who embrace probabilistic measurement
4. Those who build brand (which doesn't require precise tracking)

---

## Required Context

### Must Have

**1. Current Tracking Setup**
- Pixel implementation (client-side only or CAPI/server-side?)
- Conversion events tracked
- Cookie consent implementation
- iOS 14 opt-in rates (if Meta)

**2. Business Model**
- E-commerce, lead gen, SaaS, etc.
- Typical customer journey length
- Primary conversion events

**3. Data Assets**
- Customer email list size
- Purchase history availability
- CRM system in use
- Newsletter/engagement data

### Strongly Recommended

**4. Current Performance Context**
- How much has performance declined post-iOS 14?
- Which channels/campaigns most affected?
- Attribution window used

**5. Technical Capabilities**
- Development resources available
- CDPs or data platforms in use
- Marketing automation tools

### Nice to Have

- Marketing mix model data
- Incrementality test history
- Competitive intelligence on their tracking

---

## Privacy Landscape Overview

### The Key Privacy Changes

**iOS 14+ (ATT Framework):**
- Users must opt-in to tracking
- Opt-in rates typically 15-25%
- Meta most affected (lost cross-app tracking)
- Google less affected (owns the browser)
- Impact: 30-50% drop in attributed conversions

**Third-Party Cookie Deprecation:**
- Chrome phasing out (timeline shifting)
- Safari/Firefox already blocked
- Affects: Retargeting, conversion tracking, audience building
- Expected impact: Significant for those relying on 3P data

**GDPR/CCPA/Privacy Regulations:**
- Consent required for tracking
- Data minimization principles
- Right to deletion
- Affects: Data collection, retention, usage

### Channel-by-Channel Impact

| Channel | iOS 14 Impact | Cookie Deprecation Impact | Adaptation Difficulty |
|---------|---------------|---------------------------|----------------------|
| Meta | 🔴 Severe | 🔴 Severe | High |
| Google Search | 🟢 Low | 🟡 Moderate | Low |
| Google Display | 🟡 Moderate | 🔴 Severe | High |
| TikTok | 🔴 Severe | 🔴 Severe | High |
| LinkedIn | 🟡 Moderate | 🟡 Moderate | Medium |
| Programmatic | 🟡 Moderate | 🔴 Severe | High |
| Email/SMS | 🟢 None | 🟢 None | N/A |

---

## Strategy Framework

### Pillar 1: First-Party Data Activation

**What is First-Party Data?**
Data you collect directly from customers with their consent:
- Email addresses
- Purchase history
- Website behavior (with consent)
- Survey responses
- Loyalty program data

**First-Party Data Sources:**

| Source | Data Type | Use Cases |
|--------|-----------|-----------|
| Email signups | Email, preferences | Custom audiences, lookalikes |
| Purchases | Email, products, value | Segmentation, LTV-based targeting |
| Account creation | Email, profile data | Personalization, audiences |
| Surveys/quizzes | Preferences, intent | Segmentation |
| Loyalty programs | Engagement, value | VIP targeting |
| App users | In-app behavior | Re-engagement |

**Activation Strategies:**

**1. Customer Match / Custom Audiences**
- Upload customer emails to platforms
- Target directly or create lookalikes
- Refresh regularly (weekly minimum)

| Platform | Feature Name | Match Rate |
|----------|--------------|------------|
| Google | Customer Match | 30-60% |
| Meta | Custom Audiences | 40-70% |
| LinkedIn | Matched Audiences | 20-40% |
| TikTok | Custom Audiences | 30-50% |

**2. Segmentation for Targeting**

| Segment | Definition | Use Case |
|---------|------------|----------|
| High LTV | Top 20% by revenue | Lookalike source |
| Recent purchasers | Bought in last 30 days | Exclude from prospecting |
| Lapsed customers | No purchase in 90+ days | Win-back campaigns |
| High intent | Cart abandoners, frequent visitors | Retargeting priority |
| Email engaged | Opens/clicks emails | Warm audience |

**3. Value-Based Audiences**
- Upload customer list with LTV/purchase value
- Platforms optimize for high-value lookalikes
- Available on Meta, Google

---

### Pillar 2: Server-Side Tracking Implementation

**Why Server-Side?**
- More reliable than client-side (ad blockers, browser restrictions)
- Better data quality
- Required for full Conversions API functionality
- Preparation for cookie deprecation

**Platform-Specific Implementation:**

**Meta Conversions API (CAPI):**

| Implementation | Complexity | Coverage |
|----------------|------------|----------|
| Partner integration (Shopify, etc.) | Low | Good |
| Google Tag Manager Server | Medium | Better |
| Direct API integration | High | Best |

**Key Events to Send:**
- PageView
- ViewContent
- AddToCart
- InitiateCheckout
- Purchase (with value)
- Lead/CompleteRegistration

**Event Match Quality Score:**
- Target: 6.0+ (out of 10)
- Improve with: email, phone, external_id, fbp, fbc

**Google Enhanced Conversions:**

| Type | What It Does |
|------|--------------|
| Enhanced Conversions for Web | Sends hashed user data with conversions |
| Enhanced Conversions for Leads | Matches offline conversions to ads |

**Implementation:**
1. Enable in Google Ads settings
2. Collect user-provided data (email, phone, address)
3. Send with conversion tags or via API

**TikTok Events API:**
- Similar to Meta CAPI
- Partner integrations available
- Direct API for custom implementation

---

### Pillar 3: Measurement Adaptation

**The New Measurement Stack:**

| Method | What It Measures | Confidence |
|--------|------------------|------------|
| Platform attribution | Last-touch within platform | Low-Medium |
| Server-side tracking | More complete conversion data | Medium |
| Conversion lift studies | Incremental impact | High |
| Marketing mix modeling | Channel contribution | Medium-High |
| Holdout tests | True incrementality | High |

**Attribution Window Strategy:**

| Platform | Recommended Window | Why |
|----------|-------------------|-----|
| Meta | 7-day click, 1-day view | Standard post-iOS 14 |
| Google | Data-driven or 30-day | More first-party data |
| TikTok | 7-day click, 1-day view | Similar to Meta |

**Modeled Conversions:**
- Platforms now use statistical modeling
- Accept that reported conversions are estimates
- Focus on directional trends, not exact numbers
- Compare to server-side data for calibration

**Cross-Channel Measurement Approaches:**

| Approach | Complexity | Cost | Accuracy |
|----------|------------|------|----------|
| Last-touch attribution | Low | Free | Low |
| Multi-touch attribution | Medium | Medium | Medium |
| Marketing mix modeling | High | High | Medium-High |
| Incrementality testing | High | Medium | High |
| Unified measurement | Very High | Very High | Highest |

---

### Pillar 4: Platform-Native Solutions

**Leverage Platform ML:**

| Platform | Solution | Benefit |
|----------|----------|---------|
| Meta | Advantage+ Shopping | Broader targeting, ML optimization |
| Meta | Broad audiences | Let algorithm find converters |
| Google | Performance Max | Automated cross-channel |
| Google | Smart Bidding | Conversion prediction |
| TikTok | Smart Performance | Automated optimization |

**Why Platform ML Helps:**
- Platforms have more data than any one advertiser
- Aggregated learning across millions of conversions
- Probabilistic modeling fills tracking gaps
- Works better with less targeting input

**Broad Targeting Best Practices:**

| Old Approach | New Approach |
|--------------|--------------|
| Narrow interest targeting | Broad or no interest targeting |
| Multiple small audiences | Fewer larger audiences |
| Heavy exclusions | Minimal exclusions |
| Detailed demographic filters | Wide demographics, let ML optimize |

---

### Pillar 5: Contextual & Cohort-Based Targeting

**Contextual Targeting:**
Show ads based on content being consumed, not user behavior.

| Type | How It Works | Best For |
|------|--------------|----------|
| Keyword contextual | Target pages with keywords | Google Display |
| Topic targeting | Target content categories | Display, YouTube |
| Publisher direct | Buy inventory on specific sites | Brand safety |
| Content adjacency | Appear near relevant content | All display |

**Cohort-Based Approaches:**

| Method | Description | Platform |
|--------|-------------|----------|
| Topics API | Google's cookie replacement | Chrome/Google |
| FLEDGE | On-device auction | Chrome |
| Seller-defined audiences | Publisher segments | Programmatic |
| Contextual segments | Behavior-based without cookies | Various DSPs |

---

### Pillar 6: Building Brand (Tracking-Independent)

**Brand Advertising Benefits:**
- Works without precise tracking
- Creates demand that search captures
- Builds long-term business value
- Less affected by privacy changes

**Brand Measurement Approaches:**

| Metric | How to Measure | Platform |
|--------|----------------|----------|
| Brand search lift | Search volume for brand terms | Google Trends, Search Console |
| Direct traffic | Direct visits increase | Google Analytics |
| Brand awareness | Survey-based studies | Platform brand lift |
| Share of voice | Competitive impression share | Platform tools |
| Social listening | Brand mention volume | Social tools |

---

## Output Format

### Privacy-First Strategy Document

```
═══════════════════════════════════════════════════════════════════
PRIVACY-FIRST ADVERTISING STRATEGY
═══════════════════════════════════════════════════════════════════
Brand: [Brand Name]
Prepared: [Date]
Current State: [Pre-adaptation / In-progress / Advanced]
═══════════════════════════════════════════════════════════════════

📊 CURRENT ASSESSMENT
────────────────────────────────────────────────────────────────────

TRACKING INFRASTRUCTURE:

| Component | Status | Priority |
|-----------|--------|----------|
| Client-side pixels | ✅/⚠️/❌ | [P0/P1/P2] |
| Meta CAPI | ✅/⚠️/❌ | [P0/P1/P2] |
| Google Enhanced Conversions | ✅/⚠️/❌ | [P0/P1/P2] |
| TikTok Events API | ✅/⚠️/❌ | [P0/P1/P2] |
| Cookie consent | ✅/⚠️/❌ | [P0/P1/P2] |
| Server-side GTM | ✅/⚠️/❌ | [P0/P1/P2] |

FIRST-PARTY DATA:

| Asset | Size | Quality | Activation |
|-------|------|---------|------------|
| Customer emails | [X] | [Good/Fair/Poor] | [Active/Inactive] |
| Purchase history | [X] transactions | [Quality] | [Active/Inactive] |
| Website behavior | [X] users | [Quality] | [Active/Inactive] |
| Email engagement | [X]% open rate | [Quality] | [Active/Inactive] |

CURRENT IMPACT:
- Estimated attribution loss: [X]%
- Channels most affected: [List]
- Measurement confidence: [High/Medium/Low]

═══════════════════════════════════════════════════════════════════

🔧 TRACKING INFRASTRUCTURE ROADMAP
────────────────────────────────────────────────────────────────────

PHASE 1: Foundation (Weeks 1-2)

1. [ ] META CONVERSIONS API
   - Implementation method: [Partner/GTM Server/Direct]
   - Events to send: [List]
   - Target event match quality: 6.0+
   - Technical resource: [Required/Not required]

2. [ ] GOOGLE ENHANCED CONVERSIONS
   - Enable enhanced conversions for web
   - Enable enhanced conversions for leads (if B2B)
   - Technical setup: [Steps]

3. [ ] COOKIE CONSENT OPTIMIZATION
   - Current opt-in rate: [X]%
   - Target opt-in rate: [X]%
   - Optimization: [Recommendations]

PHASE 2: Optimization (Weeks 3-4)

1. [ ] Server-side GTM implementation (if applicable)
2. [ ] Event quality score optimization
3. [ ] Data deduplication setup
4. [ ] Testing and validation

═══════════════════════════════════════════════════════════════════

📧 FIRST-PARTY DATA STRATEGY
────────────────────────────────────────────────────────────────────

DATA COLLECTION IMPROVEMENTS:

| Opportunity | Current | Target | Method |
|-------------|---------|--------|--------|
| Email capture rate | [X]% | [X]% | [Method] |
| Account creation rate | [X]% | [X]% | [Method] |
| Consent opt-in rate | [X]% | [X]% | [Method] |

AUDIENCE ACTIVATION PLAN:

| Audience | Size | Platform | Use |
|----------|------|----------|-----|
| All customers | [X] | Meta, Google | Exclusion, lookalike |
| High LTV (top 20%) | [X] | Meta, Google | Lookalike source |
| Recent purchasers | [X] | All | Exclusion |
| Lapsed (90+ days) | [X] | Meta, Email | Win-back |
| Email engaged | [X] | Meta | Warm prospecting |
| Cart abandoners | [X] | Meta, Google | Retargeting |

LOOKALIKE STRATEGY:

| Source Audience | Platform | Expansion |
|-----------------|----------|-----------|
| [Source 1] | Meta | 1-3% (test) |
| [Source 2] | Google | Similar audiences |
| [Source 3] | TikTok | Lookalikes |

═══════════════════════════════════════════════════════════════════

📈 CAMPAIGN STRATEGY ADAPTATION
────────────────────────────────────────────────────────────────────

TARGETING CHANGES:

| Before | After |
|--------|-------|
| [Old approach] | [New approach] |
| [Old approach] | [New approach] |
| [Old approach] | [New approach] |

PLATFORM-SPECIFIC RECOMMENDATIONS:

META:
- Campaign type: [Advantage+ Shopping / Broad manual / etc.]
- Targeting: [Broad / Lookalikes / Custom audiences]
- Attribution: 7-day click, 1-day view
- Creative strategy: [Recommendations]

GOOGLE:
- Campaign type: [PMAX / Standard Shopping / Search]
- Targeting: [Recommendations]
- Bidding: [Smart bidding type]
- Enhanced conversions: Required

TIKTOK:
- Events API: [Status and recommendations]
- Targeting: [Recommendations]
- Creative: [Recommendations]

═══════════════════════════════════════════════════════════════════

📊 MEASUREMENT FRAMEWORK
────────────────────────────────────────────────────────────────────

MEASUREMENT STACK:

| Method | Frequency | Purpose |
|--------|-----------|---------|
| Platform reporting | Daily | Operational optimization |
| Server-side data | Weekly | Calibration, true conversion count |
| Blended ROAS/CAC | Weekly | Overall efficiency |
| Incrementality tests | Quarterly | Channel validation |
| MMM | Annually | Budget allocation |

KEY METRICS TO TRACK:

| Metric | Source | Target |
|--------|--------|--------|
| Blended CAC | Finance + Marketing | $[X] |
| Server-side conversion rate | Server data | [X]% |
| Event match quality | Meta | 6.0+ |
| Brand search volume | GSC | +[X]% YoY |

═══════════════════════════════════════════════════════════════════

🎯 IMPLEMENTATION TIMELINE
────────────────────────────────────────────────────────────────────

WEEK 1:
- [ ] [Task]
- [ ] [Task]

WEEK 2:
- [ ] [Task]
- [ ] [Task]

WEEK 3-4:
- [ ] [Task]
- [ ] [Task]

MONTH 2:
- [ ] [Task]
- [ ] [Task]

ONGOING:
- [ ] [Process]
- [ ] [Process]

═══════════════════════════════════════════════════════════════════
```

---

## Common Scenarios

### Scenario 1: "Meta performance dropped 40% after iOS 14"
**Immediate Actions:**
1. Implement CAPI if not done (biggest single fix)
2. Consolidate campaigns (fewer ad sets = more learning)
3. Broaden targeting (let algorithm optimize)
4. Extend attribution window consideration
5. Add UTM parameters for backup tracking

**Strategic Shifts:**
1. Upload customer lists for targeting
2. Use value-based custom audiences
3. Shift to Advantage+ Shopping campaigns
4. Invest more in first-party data collection

### Scenario 2: "How do I prepare for cookie deprecation?"
**Priority Actions:**
1. Audit current cookie dependency
2. Implement server-side tracking
3. Build first-party data assets
4. Test contextual targeting now
5. Increase platform-native campaign usage

**What Changes:**
- Retargeting pools will shrink
- Conversion tracking will be modeled
- Lookalikes based on platform data
- Contextual becomes more important

### Scenario 3: "My attribution is unreliable"
**Build Multi-Source View:**
1. Platform reported conversions
2. Server-side tracked conversions
3. UTM/last-click in Google Analytics
4. Actual revenue from finance systems

**Reconciliation:**
- Compare all sources weekly
- Use server-side as "source of truth"
- Apply calibration factors to platform data
- Track blended CAC from finance

### Scenario 4: "I don't have a lot of first-party data"
**Collection Strategies:**
1. Email capture optimization (pop-ups, content offers)
2. Account creation incentives
3. Loyalty program launch
4. Quiz/survey for preferences
5. App with login

**Quick Wins:**
- Optimize existing email pop-up (design, timing, offer)
- Add exit-intent capture
- Offer value for email (discount, content)

### Scenario 5: "Should I invest in a CDP?"
**Decision Framework:**

| Factor | CDP Worth It | Skip CDP |
|--------|--------------|----------|
| Customer list size | >100K | <50K |
| Data sources | 5+ systems | 1-2 systems |
| Budget | Can afford $30K+/year | Under $30K/year |
| Team | Dedicated data team | No data resources |
| Use cases | Complex segmentation | Basic custom audiences |

**Alternatives to Full CDP:**
- Platform-native audience tools
- Email platform segments
- Manual customer match uploads
- Simple data warehouse + uploads

---

## Limitations

**I can provide:**
- Strategic framework for privacy adaptation
- Platform-specific recommendations
- Implementation prioritization
- Measurement framework
- Best practices and benchmarks

**I cannot provide:**
- Technical implementation steps (CAPI code, GTM setup)
- Legal compliance advice (GDPR, CCPA specifics)
- Platform-specific real-time policy changes
- CDP selection or configuration

**For implementation, involve:**
- Development team (tracking implementation)
- Legal/compliance (privacy policy, consent)
- Data team (CDP, data infrastructure)
- Platform specialists (complex setups)

---

## Quality Checklist

Before delivering strategy:
- [ ] Current tracking infrastructure assessed
- [ ] First-party data assets inventoried
- [ ] CAPI/server-side tracking addressed
- [ ] Platform-specific recommendations included
- [ ] Measurement framework defined
- [ ] Implementation prioritized by impact
- [ ] Technical resource requirements noted
- [ ] Timeline realistic for capabilities
- [ ] Ongoing processes defined
