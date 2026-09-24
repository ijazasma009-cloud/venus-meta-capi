---
name: spend-pacing-monitor
description: Tracks Google Ads spend against budget targets, predicts month-end totals, and alerts on pacing anomalies. Triggers when user asks about spend pacing, budget tracking, "am I on track?", or "will I hit my budget?" Provides daily/weekly analysis, identifies over/underspend patterns, and recommends adjustments to hit targets.
---

# Spend Pacing Monitor

Know exactly where you'll land before the month ends.

## Core Philosophy

**Budget surprises are management failures.** Whether you overspend by the 20th or scramble to spend on the 30th, poor pacing wastes money and opportunity.

**The Goal:** At any point in the month, know:
1. Where you are vs. where you should be
2. Where you'll end up if nothing changes
3. What adjustments to make to hit target

---

## Required Context

### Must Have

**1. Budget Information**
- Monthly budget target
- Budget period (calendar month or custom)

**2. Spend Data**
- Current month-to-date spend
- Current date (day of month)
- Days remaining in period

### Strongly Recommended

**3. Daily Spend History**
- Daily spend for current month (enables trend analysis)
- Or: weekly totals if daily not available

**4. Campaign Breakdown**
- Spend by campaign
- Budget by campaign (if set at campaign level)

### Nice to Have

- Historical monthly spend patterns
- Seasonality context
- Known upcoming changes (promotions, pauses)
- Conversion data (efficiency check)

---

## Pacing Analysis Framework

### Step 1: Basic Pacing Calculation

**Linear Pacing (Simplest):**
```
Expected spend to date = (Monthly budget / Days in month) × Days elapsed
Pacing % = (Actual spend / Expected spend) × 100

Under 90%: Underpacing
90-110%: On pace
Over 110%: Overpacing
```

**Example:**
```
Monthly budget: $30,000
Days in month: 30
Today: Day 15
Expected spend: ($30,000 / 30) × 15 = $15,000

Actual spend: $12,000
Pacing: $12,000 / $15,000 = 80%
Status: Underpacing by 20%
```

---

### Step 2: Projection Calculation

**Simple Projection (Current Run Rate):**
```
Daily run rate = Month-to-date spend / Days elapsed
Projected month-end = Daily run rate × Days in month
```

**Weighted Projection (Recent Trend):**
```
Recent daily average (last 7 days) = Last 7 days spend / 7
Projected remaining = Recent daily average × Days remaining
Projected month-end = MTD spend + Projected remaining
```

**Which to Use:**
- Early month (Day 1-10): Use simple projection with caution
- Mid month (Day 11-20): Use weighted projection
- Late month (Day 21+): Weighted projection is most accurate

---

### Step 3: Variance Analysis

**Identify Patterns:**
- Consistent underspend: Systematic issue (budgets too high, targeting too narrow)
- Consistent overspend: Demand exceeds expectations or budgets too low
- Volatile spend: External factors or campaign issues

**Day-of-Week Patterns:**
- B2B: Often lower weekend spend
- B2C: Often higher weekend spend
- Retail: Day patterns vary by product

**Early vs Late Month:**
- Early month low: Could be learning period, will accelerate
- Early month high: Might burn out before month end
- Late month spike: Often indicates scramble to spend

---

### Step 4: Adjustment Recommendations

**If Underpacing:**

| Underpace Level | Likely Cause | Recommended Action |
|-----------------|--------------|-------------------|
| 5-15% under | Minor variance | Monitor, may self-correct |
| 15-25% under | Targeting/budget issue | Expand targeting or increase campaign budgets |
| 25%+ under | Structural problem | Audit account—something's blocking spend |

**If Overpacing:**

| Overpace Level | Likely Cause | Recommended Action |
|----------------|--------------|-------------------|
| 5-15% over | Normal variance | Monitor, slight budget reduction if needed |
| 15-25% over | Higher demand | Reduce budgets or tighten targeting |
| 25%+ over | Campaign issue | Immediate intervention—check for anomalies |

---

## Output Format

### Pacing Dashboard

```
═══════════════════════════════════════════════════════════════
SPEND PACING REPORT
Period: [Month Year]
As of: [Date] (Day [X] of [Y])
═══════════════════════════════════════════════════════════════

PACING STATUS: 🟢 On Track / 🟡 Warning / 🔴 Alert

Budget:     $XX,XXX
MTD Spend:  $XX,XXX (XX% of budget)
Expected:   $XX,XXX (XX% of budget)
Variance:   +/-$X,XXX (+/-XX%)
```

---

### 📊 Current Status

**Month Overview:**
```
Day of Month:     [X] of [Y]
Days Remaining:   [X]
% of Month:       [XX]%
```

**Spend Status:**
```
Monthly Budget:   $[XX,XXX]
MTD Spend:        $[XX,XXX]
Expected MTD:     $[XX,XXX]
Variance:         $[+/-X,XXX] ([+/-XX]%)
Pacing:           [XX]% of expected
```

**Status Assessment:** [On Track / Slightly Under / Significantly Under / Slightly Over / Significantly Over]

---

### 📈 Projections

**Month-End Forecast:**

| Method | Projected Spend | vs Budget | Confidence |
|--------|-----------------|-----------|------------|
| Run Rate | $XX,XXX | +/-XX% | [Low/Med/High] |
| Trend-Based | $XX,XXX | +/-XX% | [Low/Med/High] |
| Best Estimate | $XX,XXX | +/-XX% | — |

**Best Estimate Breakdown:**
```
Current MTD:      $[XX,XXX]
Projected Remaining: $[XX,XXX] (based on [method])
Projected Total:  $[XX,XXX]
vs Budget:        [+/-$X,XXX] ([+/-XX]%)
```

---

### 📅 Daily Breakdown (If Provided)

| Date | Spend | Cumulative | vs Linear Pace | Notes |
|------|-------|------------|----------------|-------|
| [Date] | $X,XXX | $X,XXX | +/-X% | [Any anomaly] |
| [Date] | $X,XXX | $X,XXX | +/-X% | |
| ... | | | | |

**Pattern Observations:**
- [Observation about daily patterns]
- [Observation about trends]

---

### 🏢 Campaign Breakdown (If Provided)

| Campaign | Budget | MTD Spend | Pacing | Projection | Status |
|----------|--------|-----------|--------|------------|--------|
| [Name] | $X,XXX | $X,XXX | XX% | $X,XXX | 🟢/🟡/🔴 |
| [Name] | $X,XXX | $X,XXX | XX% | $X,XXX | 🟢/🟡/🔴 |
| **Total** | **$XX,XXX** | **$XX,XXX** | **XX%** | **$XX,XXX** | |

**Campaign-Level Issues:**
- [Campaign]: [Issue and recommendation]

---

### ⚠️ Alerts & Anomalies

**Active Alerts:**
- 🔴 [Critical alert if any]
- 🟡 [Warning if any]

**Anomalies Detected:**
- [Date/period]: [Unusual spend pattern and likely cause]

---

### 💡 Recommendations

**To Hit Budget Target:**

**If Underpacing:**
```
Current daily run rate:  $[X,XXX]
Required daily rate:     $[X,XXX]
Gap:                     $[X,XXX]/day (+XX%)

Action: [Specific recommendation]
```

**If Overpacing:**
```
Current daily run rate:  $[X,XXX]
Required daily rate:     $[X,XXX]
Excess:                  $[X,XXX]/day (-XX%)

Action: [Specific recommendation]
```

**Specific Adjustments:**
1. [Campaign]: [Increase/decrease] budget by $[X] to [achieve outcome]
2. [Campaign]: [Specific action]

---

### 📋 Pacing Scenarios

**Scenario A: If Spend Continues at Current Rate**
- Month-end spend: $[X]
- vs Budget: [+/-X%]
- Outcome: [Assessment]

**Scenario B: If We Adjust to Target**
- Required daily spend: $[X]
- Adjustment needed: [+/-X%] from current
- Feasibility: [Easy / Moderate / Difficult]

**Scenario C: If [Specific Change]**
- Impact: [Projected outcome]

---

## Pacing Benchmarks

### Acceptable Variance by Month Stage

| Stage | Days | Acceptable Variance |
|-------|------|-------------------|
| Early | 1-7 | ±25% (limited data) |
| Early-Mid | 8-14 | ±15% |
| Mid | 15-21 | ±10% |
| Late | 22-28 | ±5% |
| Final | 29-31 | ±3% |

### Intervention Triggers

| Variance | Early Month | Mid Month | Late Month |
|----------|-------------|-----------|------------|
| ±5% | Monitor | Monitor | Monitor |
| ±10% | Monitor | Investigate | Adjust |
| ±15% | Investigate | Adjust | Urgent |
| ±25%+ | Investigate | Urgent | Critical |

---

## Common Pacing Issues

### Issue 1: Consistent Underspend
**Symptoms:** Pacing under 85% every week
**Causes:**
- Campaign budgets set too high
- Targeting too narrow
- Low impression share not from budget
- Bid strategy too conservative

**Solutions:**
- Audit targeting breadth
- Check impression share reasons
- Increase bids or switch bid strategy
- Expand keywords/audiences

### Issue 2: Early Month Overspend
**Symptoms:** 80% of budget spent by day 20
**Causes:**
- Daily budgets not aligned with monthly
- Unexpected demand spike
- Campaign settings issue

**Solutions:**
- Reduce daily budgets
- Add budget caps at campaign level
- Implement shared budgets
- Enable accelerated spend at month end only

### Issue 3: Month-End Scramble
**Symptoms:** Need to spend 30% of budget in last week
**Causes:**
- Poor pacing management
- Overly conservative early month
- Budget increases not implemented

**Solutions:**
- Increase daily budgets significantly
- Expand targeting temporarily
- Add campaigns/keywords
- Accept potential efficiency loss

### Issue 4: Volatile Daily Spend
**Symptoms:** Days ranging from $500 to $2,000
**Causes:**
- Smart Bidding volatility
- Day-of-week patterns
- Competitive fluctuations

**Solutions:**
- Use shared budgets for smoothing
- Account for known patterns
- Set tighter budget controls
- Review bid strategy settings

---

## Limitations

**I can provide:**
- Accurate pacing calculations
- Reasonable projections based on data
- Anomaly identification
- Adjustment recommendations

**I cannot provide:**
- Future demand predictions
- Competitive landscape changes
- External factor impacts
- Guaranteed projection accuracy

**For better monitoring:**
- Provide daily spend history (enables trend analysis)
- Include campaign-level data (identifies specific issues)
- Note known events (promotions, seasonality)
- Share historical patterns (improves projections)

---

## Quality Checklist

Before delivering pacing report:
- [ ] Basic pacing calculation verified
- [ ] Projection method appropriate for month stage
- [ ] Anomalies flagged with context
- [ ] Recommendations are specific and actionable
- [ ] Campaign-level issues identified (if data provided)
- [ ] Scenarios help decision-making
- [ ] Intervention urgency appropriate to variance level
