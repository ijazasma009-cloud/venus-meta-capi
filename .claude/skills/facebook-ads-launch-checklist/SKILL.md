---
name: facebook-ads-launch-checklist
description: Provides comprehensive pre-launch verification for Meta Ads campaigns covering pixel tracking, conversion API, audience setup, creative specs, and campaign settings. Prevents common launch mistakes. Use before launching new campaigns or accounts.
---

# Facebook Ads Launch Checklist

Launch right the first time. Fixing mistakes post-launch wastes time and money.

## Core Philosophy

**Every dollar spent with broken tracking is a dollar wasted.**

The first 7 days of a campaign are critical. The algorithm is learning. First impressions are being made. Data is being collected. If your tracking is broken, your audiences are wrong, or your creative is disapproved—you're not just losing money, you're teaching the algorithm the wrong things.

**90% of launch problems are preventable.** Wrong pixel, missing CAPI, ads that violate policies, landing pages that don't load on mobile—all of these can be caught before you spend a single dollar.

**This checklist is your insurance policy.** Take 30 minutes before launch to verify everything. Save yourself days of debugging and wasted spend.

---

## The Launch Checklist

### Tier 1: Critical (Must Pass Before Launch)

These items will cause immediate problems if not addressed.

#### 1.1 Pixel & Tracking

| Check | How to Verify | Pass/Fail |
|-------|---------------|-----------|
| Pixel installed on all pages | Use Facebook Pixel Helper extension | ☐ |
| Pixel ID matches ad account | Events Manager → Settings → Pixel ID | ☐ |
| PageView fires on all pages | Browse site with Pixel Helper active | ☐ |
| Conversion event fires correctly | Complete a test conversion | ☐ |
| Conversion event fires ONCE per conversion | Check for duplicate events | ☐ |
| Event parameters populated | View event details in Events Manager | ☐ |

**Common Pixel Problems:**
- Pixel installed but wrong ID
- PageView fires, but conversion events don't
- Conversion event fires multiple times
- Event fires on page load, not on action
- Missing value/currency for Purchase events

#### 1.2 Conversions API (CAPI)

| Check | How to Verify | Pass/Fail |
|-------|---------------|-----------|
| CAPI enabled | Events Manager → Settings → Conversions API | ☐ |
| Server events appearing | Events Manager → Test Events | ☐ |
| Event deduplication working | Check for duplicate events | ☐ |
| Event match quality >6 | Events Manager → Overview | ☐ |

**Why CAPI Matters:**
- iOS 14.5+ blocks significant browser tracking
- Without CAPI, you lose 30-40% of conversion data
- Lower data = worse optimization

#### 1.3 Conversion Event Selection

| Check | How to Verify | Pass/Fail |
|-------|---------------|-----------|
| Optimizing for correct event | Campaign settings → Optimization | ☐ |
| Event has sufficient volume (50+/week ideal) | Events Manager → Event history | ☐ |
| Event represents actual business value | Confirm with stakeholder | ☐ |

**Conversion Event Hierarchy:**
1. Purchase (if e-commerce)
2. Lead/Submit Form (if lead gen)
3. Complete Registration (if app/signup)
4. Add to Cart (only if Purchase volume too low)

**Never Optimize For:** PageView, ViewContent (too broad, no purchase intent)

---

### Tier 2: Important (Should Pass Before Launch)

These items affect performance but may not cause immediate failure.

#### 2.1 Ad Creative Compliance

| Check | How to Verify | Pass/Fail |
|-------|---------------|-----------|
| Images follow 20% text guideline | Facebook Text Overlay Tool | ☐ |
| No prohibited content | Review Meta Advertising Policies | ☐ |
| No misleading claims | Review ad copy objectively | ☐ |
| Video meets specs (15s, 9:16/1:1) | Check file properties | ☐ |
| Thumbnails are high quality | Preview in Ads Manager | ☐ |
| Landing page matches ad promise | Click through and verify | ☐ |

**Common Policy Violations:**
- Before/after images (health, weight loss)
- Personal attributes ("Are you...?")
- Misleading buttons ("Download" that aren't downloads)
- Prohibited products (weapons, drugs, etc.)
- Adult content or suggestive imagery

#### 2.2 Landing Page Quality

| Check | How to Verify | Pass/Fail |
|-------|---------------|-----------|
| Page loads <3 seconds | Google PageSpeed Insights | ☐ |
| Mobile-friendly | Test on actual mobile device | ☐ |
| CTA visible above fold | Check on mobile and desktop | ☐ |
| No broken links/images | Click all links on page | ☐ |
| Form works correctly | Submit test form | ☐ |
| SSL certificate valid (HTTPS) | Check browser security | ☐ |
| No pop-ups blocking content | Test user experience | ☐ |

**Landing Page Impact:**
- 1 second delay = 7% conversion loss
- 40% abandon pages that take >3 seconds
- Mobile traffic is typically 70%+ of Facebook traffic

#### 2.3 Audience Setup

| Check | How to Verify | Pass/Fail |
|-------|---------------|-----------|
| Audience size appropriate | Check estimated reach | ☐ |
| No overlapping audiences | Use Audience Overlap tool | ☐ |
| Exclusions set correctly | Review exclusions in ad set | ☐ |
| Location targeting correct | Check included/excluded areas | ☐ |
| Age/gender targeting intentional | Confirm with strategy | ☐ |

**Audience Size Guidelines:**

| Budget | Minimum Audience | Ideal Audience |
|--------|------------------|----------------|
| $50/day | 100,000 | 500,000+ |
| $200/day | 500,000 | 2,000,000+ |
| $500/day | 1,000,000 | 5,000,000+ |

---

### Tier 3: Optimization (Nice to Have)

These items maximize performance but aren't blockers.

#### 3.1 Campaign Structure

| Check | How to Verify | Pass/Fail |
|-------|---------------|-----------|
| Campaign objective matches goal | Campaign settings | ☐ |
| Budget level appropriate (CBO vs ABO) | Campaign settings | ☐ |
| Ad sets not competing | Check audience overlap | ☐ |
| Naming conventions clear | Review campaign/ad set/ad names | ☐ |
| UTM parameters added | Check URL parameters | ☐ |

**Naming Convention Template:**
```
Campaign: [Objective] - [Audience Type] - [Date]
Ad Set: [Audience Name] - [Placement]
Ad: [Creative Type] - [Hook/Angle] - [Version]

Example:
Campaign: CONV - Prospecting - Jan24
Ad Set: LAL Purchasers 1% - Auto
Ad: Video - Pain Hook - v1
```

#### 3.2 Ad Variations

| Check | How to Verify | Pass/Fail |
|-------|---------------|-----------|
| Multiple ads per ad set (3-6) | Count ads in ad set | ☐ |
| Creative diversity (formats, angles) | Review ad creative | ☐ |
| Copy variations tested | Review primary text | ☐ |
| Headlines/CTAs varied | Review ad components | ☐ |

#### 3.3 Advanced Settings

| Check | How to Verify | Pass/Fail |
|-------|---------------|-----------|
| Attribution window appropriate | Ad set settings | ☐ |
| Placement selection intentional | Ad set placement settings | ☐ |
| Scheduling set (if needed) | Ad set schedule | ☐ |
| Bid strategy matches goal | Campaign bid settings | ☐ |

**Attribution Window Recommendations:**

| Business Type | Click Window | View Window |
|---------------|--------------|-------------|
| E-commerce (impulse) | 7-day | 1-day |
| E-commerce (considered) | 7-day | 1-day |
| Lead Gen (B2C) | 7-day | 1-day |
| Lead Gen (B2B) | 7-day | 1-day |
| High-ticket | 7-day | 1-day |

---

## Pre-Launch Verification Process

### Step 1: Tracking Verification (15 minutes)

1. Open Facebook Pixel Helper (Chrome extension)
2. Browse your website:
   - Home page → Verify PageView fires
   - Product page → Verify ViewContent fires
   - Add to cart → Verify AddToCart fires
   - Complete purchase/lead → Verify conversion fires
3. Check Events Manager:
   - Test Events tab → Verify events appearing
   - Event Match Quality → Should be 6+ (good) or 8+ (great)
4. Complete one test conversion:
   - Verify it appears in Events Manager
   - Verify only ONE event fired (no duplicates)

### Step 2: Creative & Landing Page (10 minutes)

1. Preview all ads on mobile AND desktop
2. Click through each ad to landing page
3. Verify:
   - Page loads quickly
   - Content matches ad promise
   - CTA is clear and works
   - Forms submit successfully
4. Run landing page through PageSpeed Insights

### Step 3: Campaign Settings Review (5 minutes)

1. Confirm campaign objective
2. Verify optimization event
3. Check budget and schedule
4. Review audience targeting
5. Confirm exclusions are set
6. Verify naming conventions

### Step 4: Final Approval

| Checklist Section | Status | Notes |
|-------------------|--------|-------|
| Tier 1: Critical | ☐ All Pass | |
| Tier 2: Important | ☐ All Pass | |
| Tier 3: Optimization | ☐ Reviewed | |
| Test conversion completed | ☐ Yes | |

**Launch Decision:**
- All Tier 1 Pass + Most Tier 2 Pass → ✅ Launch
- Any Tier 1 Fail → ❌ Do Not Launch (fix first)
- Multiple Tier 2 Fail → ⚠️ Launch with caution, fix ASAP

---

## Output Format

```
═══════════════════════════════════════════════════════════════════
FACEBOOK ADS LAUNCH CHECKLIST
Account: [Account Name]
Campaign: [Campaign Name]
Verified By: [Name]
Date: [Date]
═══════════════════════════════════════════════════════════════════

📊 SUMMARY
────────────────────────────────────────────────────────────────────

| Section | Status | Pass | Fail | Notes |
|---------|--------|------|------|-------|
| Tier 1: Critical | [✅/❌] | [#] | [#] | [Notes] |
| Tier 2: Important | [✅/⚠️/❌] | [#] | [#] | [Notes] |
| Tier 3: Optimization | [✅/⚠️] | [#] | [#] | [Notes] |

**Launch Decision:** [✅ Ready to Launch / ⚠️ Launch with Caution / ❌ Do Not Launch]

═══════════════════════════════════════════════════════════════════

🔴 TIER 1: CRITICAL CHECKS
────────────────────────────────────────────────────────────────────

### 1.1 Pixel & Tracking

| Check | Status | Notes |
|-------|--------|-------|
| Pixel installed on all pages | [✅/❌] | [Notes] |
| Pixel ID matches ad account | [✅/❌] | [Notes] |
| PageView fires correctly | [✅/❌] | [Notes] |
| Conversion event fires correctly | [✅/❌] | [Notes] |
| No duplicate events | [✅/❌] | [Notes] |
| Event parameters populated | [✅/❌] | [Notes] |

### 1.2 Conversions API

| Check | Status | Notes |
|-------|--------|-------|
| CAPI enabled | [✅/❌] | [Notes] |
| Server events appearing | [✅/❌] | [Notes] |
| Deduplication working | [✅/❌] | [Notes] |
| Event match quality | [Score] | [Good/Needs improvement] |

### 1.3 Conversion Event

| Check | Status | Notes |
|-------|--------|-------|
| Correct optimization event | [✅/❌] | Event: [Name] |
| Sufficient volume | [✅/❌] | [X]/week |
| Represents business value | [✅/❌] | [Notes] |

═══════════════════════════════════════════════════════════════════

🟡 TIER 2: IMPORTANT CHECKS
────────────────────────────────────────────────────────────────────

### 2.1 Ad Creative Compliance

| Check | Status | Notes |
|-------|--------|-------|
| Text <20% of image | [✅/❌] | [Notes] |
| No prohibited content | [✅/❌] | [Notes] |
| No misleading claims | [✅/❌] | [Notes] |
| Video specs met | [✅/❌/N/A] | [Notes] |
| LP matches ad promise | [✅/❌] | [Notes] |

### 2.2 Landing Page

| Check | Status | Notes |
|-------|--------|-------|
| Load time <3s | [✅/❌] | [X.X seconds] |
| Mobile-friendly | [✅/❌] | [Notes] |
| CTA above fold | [✅/❌] | [Notes] |
| Form works | [✅/❌] | [Notes] |
| HTTPS enabled | [✅/❌] | [Notes] |

### 2.3 Audience Setup

| Check | Status | Notes |
|-------|--------|-------|
| Audience size appropriate | [✅/❌] | [Size] |
| No overlap issues | [✅/❌] | [Notes] |
| Exclusions correct | [✅/❌] | [Notes] |
| Geo-targeting correct | [✅/❌] | [Notes] |

═══════════════════════════════════════════════════════════════════

🟢 TIER 3: OPTIMIZATION CHECKS
────────────────────────────────────────────────────────────────────

### 3.1 Campaign Structure

| Check | Status | Notes |
|-------|--------|-------|
| Objective correct | [✅/❌] | [Objective] |
| Budget level appropriate | [✅/❌] | [CBO/ABO] |
| Naming conventions | [✅/❌] | [Notes] |
| UTM parameters | [✅/❌] | [Notes] |

### 3.2 Ad Variations

| Check | Status | Notes |
|-------|--------|-------|
| Multiple ads per ad set | [✅/❌] | [#] ads |
| Creative diversity | [✅/❌] | [Notes] |
| Copy variations | [✅/❌] | [Notes] |

═══════════════════════════════════════════════════════════════════

⚠️ ISSUES REQUIRING ATTENTION
────────────────────────────────────────────────────────────────────

### Critical Issues (Must Fix Before Launch)
1. [Issue description and fix]
2. [Issue description and fix]

### Important Issues (Fix ASAP After Launch)
1. [Issue description and fix]
2. [Issue description and fix]

### Optimization Opportunities
1. [Opportunity description]
2. [Opportunity description]

═══════════════════════════════════════════════════════════════════

✅ LAUNCH APPROVAL
────────────────────────────────────────────────────────────────────

**Launch Status:** [Ready / Not Ready]

**If Not Ready, Required Actions:**
- [ ] [Action 1]
- [ ] [Action 2]

**Post-Launch Monitoring Plan:**
- Day 1: Check tracking firing correctly
- Day 2-3: Verify conversions appearing
- Day 7: First performance review

═══════════════════════════════════════════════════════════════════
```

---

## Common Launch Mistakes

### Mistake 1: "Pixel says it's installed but no conversions tracked"
**Cause:** Pixel fires on page load, not on conversion action
**Fix:** Implement event-based pixel firing (on form submit, on purchase complete)
**Prevention:** Always complete a test conversion before launch

### Mistake 2: "Ad got disapproved after launch"
**Cause:** Policy violation in copy, image, or landing page
**Common Violations:** Before/after images, personal attributes, prohibited products
**Fix:** Review Meta Advertising Policies, update creative
**Prevention:** Use the Ad Policy Checker before launch

### Mistake 3: "Landing page loads slow on mobile"
**Cause:** Large images, too many scripts, slow hosting
**Fix:** Optimize images, reduce scripts, improve hosting
**Prevention:** Run PageSpeed Insights, test on real mobile device

### Mistake 4: "Spending but getting no conversions"
**Causes:**
- Wrong optimization event
- Landing page form broken
- Audience too cold/broad
- Creative doesn't match LP
**Fix:** Verify conversion tracking, test forms, review targeting

### Mistake 5: "Duplicate conversions reported"
**Cause:** Pixel and CAPI both firing without deduplication
**Fix:** Implement event_id matching between pixel and CAPI
**Prevention:** Check Events Manager for duplicate events

---

## Limitations

1. **Cannot access your Ads Manager** - You must perform the checks
2. **Cannot guarantee ad approval** - Meta's policies evolve
3. **Cannot test your actual landing page** - You must verify yourself
4. **Cannot predict performance** - Checklist ensures setup, not results
5. **Policies vary by region/industry** - Some restrictions are context-specific

---

## Quality Checklist

Before signing off:
- [ ] All Tier 1 items verified
- [ ] Tier 2 items reviewed (failures documented)
- [ ] Test conversion completed successfully
- [ ] Landing page tested on mobile
- [ ] Any issues documented with fix plans
- [ ] Launch decision clearly stated
