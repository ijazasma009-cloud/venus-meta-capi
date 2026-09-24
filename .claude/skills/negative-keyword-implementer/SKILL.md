---
name: negative-keyword-implementer
description: Implements negative keywords directly to Google Ads using MCP write actions. Takes output from search-term-gold-miner or manual lists and adds negatives at campaign or ad group level. Triggers when user wants to add negatives, implement search term recommendations, or block irrelevant traffic. Uses add_negative_keywords MCP action.
---

# Negative Keyword Implementer

Stop talking about negatives. Start adding them. This skill takes your negative keyword lists and implements them directly in Google Ads.

## Core Philosophy

**Analysis without action is waste.** You've identified the garbage search terms. Now block them before they cost you more money.

**The Implementation Questions:**
1. Which negatives should be added at campaign vs ad group level?
2. What match type should each negative use?
3. Are there any conflicts to check?
4. How do we confirm the changes worked?

---

## MCP Integration

### Write Action Used

This skill uses the Google Ads MCP `add_negative_keywords` action:

```json
{
  "platform": "google-ads",
  "workspace_id": "<WORKSPACE_ID>",
  "brand_id": "<BRAND_ID>",
  "account_id": "XXXXXXXXXX",
  "action": "add_negative_keywords",
  "campaign_id": "123456789",
  "keywords": ["free", "cheap", "discount"],
  "match_type": "BROAD"
}
```

### Action Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| workspace_id | Yes | Workspace ID from accounts |
| brand_id | Yes | Brand ID within workspace |
| account_id | Yes | Google Ads customer ID |
| action | Yes | Must be "add_negative_keywords" |
| campaign_id | Conditional | Campaign ID (for campaign-level) |
| ad_group_id | Conditional | Ad group ID (for ad group-level) |
| keywords | Yes | Array of negative keyword texts |
| match_type | No | BROAD (default), PHRASE, or EXACT |

**Note:** Either campaign_id OR ad_group_id is required, not both.

---

## Input Requirements

### Option 1: From search-term-gold-miner Output

If you've run `search-term-gold-miner`, provide its output:

```json
{
  "immediate_negatives": [
    {"search_term": "free bags", "spend": 150, "conversions": 0},
    {"search_term": "bag repair", "spend": 85, "conversions": 0}
  ],
  "pattern_negatives": [
    {"pattern": "free", "match_type": "PHRASE"},
    {"pattern": "repair", "match_type": "PHRASE"}
  ]
}
```

### Option 2: Manual Negative List

Provide a list of negatives to add:

```
free
cheap
diy
how to
jobs
careers
repair
used
```

### Option 3: Copy from Google Ads

Paste your negative keyword list from Google Ads for cross-campaign implementation.

---

## Analysis Framework

### Step 1: Pre-Implementation Validation

**Before adding negatives, check:**

1. **Conflict Check**
   - Does the negative match any existing keywords?
   - Will it block high-performing search terms?

2. **Level Determination**
   - Campaign-level: Applies to ALL ad groups (broader protection)
   - Ad group-level: Applies to specific ad group only (surgical precision)

3. **Match Type Selection**
   - **EXACT**: Block only this exact query (most conservative)
   - **PHRASE**: Block queries containing this phrase (balanced)
   - **BROAD**: Block queries with these words in any order (most aggressive)

---

### Step 2: Match Type Strategy

**Match Type Decision Matrix:**

| Scenario | Recommended Match | Reason |
|----------|-------------------|--------|
| Specific irrelevant query | EXACT | Surgical, preserves variations |
| Bad intent pattern | PHRASE | Blocks phrase anywhere in query |
| Irrelevant word | BROAD | Blocks all variations |
| One-word disaster | PHRASE or EXACT | Avoid accidental blocking |
| Multi-word pattern | PHRASE | Natural phrase blocking |

**Examples:**

| Negative | Match Type | What It Blocks |
|----------|------------|----------------|
| [free bags] | EXACT | Only "free bags" |
| "free bags" | PHRASE | "free bags online", "get free bags" |
| free bags | BROAD | "bags for free", "free designer bags" |

---

### Step 3: Level Strategy

**When to Use Campaign-Level:**
- Universal negatives (jobs, careers, free, DIY)
- Brand protection across all ad groups
- Terms never relevant to any product/service

**When to Use Ad Group-Level:**
- Product-specific exclusions
- Terms relevant in some contexts but not others
- Precise control for different offerings

---

## Implementation Process

### Phase 1: Review & Confirm

**Present negatives for user approval:**

```
PROPOSED NEGATIVE KEYWORDS
Campaign: [Campaign Name]
Level: Campaign-wide

EXACT MATCH:
- [term 1]
- [term 2]

PHRASE MATCH:
- [term 3]
- [term 4]

BROAD MATCH:
- [term 5]

Estimated Monthly Savings: $XXX
Proceed with implementation? (yes/no)
```

---

### Phase 2: Execute

**Call MCP action for each batch:**

```json
{
  "platform": "google-ads",
  "workspace_id": 101,
  "brand_id": 69,
  "account_id": "9382431689",
  "action": "add_negative_keywords",
  "campaign_id": "123456789",
  "keywords": ["free", "cheap", "diy", "how to"],
  "match_type": "PHRASE"
}
```

**Batch by match type** (separate call for each):
1. Add EXACT negatives
2. Add PHRASE negatives
3. Add BROAD negatives

---

### Phase 3: Confirm & Report

**After implementation:**

```
IMPLEMENTATION COMPLETE

Campaign: [Campaign Name]
Negatives Added: XX

EXACT MATCH: X keywords
PHRASE MATCH: X keywords
BROAD MATCH: X keywords

Status: SUCCESS / PARTIAL / FAILED

Next Steps:
- Monitor search term report in 7 days
- Verify blocked terms no longer appearing
- Track spend reduction vs baseline
```

---

## Output Format

### Pre-Implementation Summary

```
NEGATIVE KEYWORD IMPLEMENTATION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Account: [Account Name]
Source: search-term-gold-miner / manual list

CAMPAIGN-LEVEL NEGATIVES:
Campaign: [Campaign Name] (ID: XXXXXXX)

  EXACT MATCH (X keywords):
  ─────────────────────────
  [free bags]
  [bag repair near me]

  PHRASE MATCH (X keywords):
  ─────────────────────────
  "free"
  "repair"
  "jobs"

  BROAD MATCH (X keywords):
  ─────────────────────────
  careers hiring

CONFLICT CHECK:
⚠️ "free" may conflict with keyword "free shipping promo"
   → Recommendation: Use EXACT [free bags] instead
✓ No other conflicts detected

ESTIMATED IMPACT:
Monthly wasted spend blocked: ~$XXX
Search terms affected: ~XXX

Ready to implement? (yes/no/modify)
```

---

### Post-Implementation Report

```
IMPLEMENTATION REPORT
━━━━━━━━━━━━━━━━━━━━━

Account: [Account Name]
Timestamp: [datetime]

RESULTS:
────────
Campaign: [Campaign Name]
  ✓ EXACT negatives added: X
  ✓ PHRASE negatives added: X
  ✓ BROAD negatives added: X

Total Negatives Added: XX
Status: SUCCESS

MCP RESPONSE:
{
  "status": "success",
  "negative_keywords_added": XX,
  "level": "campaign",
  "target_id": "XXXXXXX"
}

NEXT STEPS:
1. Check search term report in 7 days
2. Verify wasted spend reduction
3. Run search-term-gold-miner again in 14 days
```

---

## Composability

**Chains from:**
- `search-term-gold-miner` - Primary input source for negatives
- Manual lists or spreadsheets

**Chains to:**
- `spend-pacing-monitor` - Verify spend reduction
- Re-run `search-term-gold-miner` - Validate blocked terms

**Workflow Example:**
```
search-term-gold-miner (identify waste)
         ↓
negative-keyword-implementer (add negatives)
         ↓
Wait 7-14 days
         ↓
search-term-gold-miner (verify improvement)
```

---

## Safety Features

### Automatic Protections

1. **Always require user confirmation before adding**
2. **Conflict detection against existing keywords**
3. **Match type recommendations to prevent over-blocking**
4. **Batch limits to prevent accidents**
5. **Full rollback instructions if needed**

### Rollback Process

If negatives were added incorrectly:

1. Go to Google Ads → Keywords → Negative Keywords
2. Filter by date added
3. Select and remove incorrect negatives

**Note:** MCP does not currently support negative keyword removal - must be done in UI.

---

## Limitations

**I can do:**
- Add negative keywords at campaign or ad group level
- Use BROAD, PHRASE, or EXACT match types
- Batch multiple keywords per call
- Validate against conflicts

**I cannot do:**
- Remove existing negative keywords (UI only)
- Add shared negative keyword lists (API limitation)
- Add negatives to Performance Max campaigns
- Guarantee zero over-blocking (user must validate)

**Best Practices:**
- Start with EXACT match for uncertain negatives
- Review search terms 7 days post-implementation
- Keep a log of negatives added with dates

---

## Quality Checklist

Before implementation:
- [ ] Negatives reviewed for conflicts
- [ ] Match types assigned appropriately
- [ ] Level (campaign vs ad group) determined
- [ ] User confirmation received
- [ ] Estimated savings calculated

After implementation:
- [ ] MCP response confirmed success
- [ ] Count of negatives matches expected
- [ ] Post-implementation report generated
- [ ] Follow-up date scheduled
