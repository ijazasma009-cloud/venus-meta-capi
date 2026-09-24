# How to Use This Skill

Hey Claude—I just added the "negative-keyword-implementer" skill. Can you add these negative keywords to my Google Ads campaign?

## Example Invocations

**Example 1: From search-term-gold-miner Output**
Hey Claude—I just added the "negative-keyword-implementer" skill. I ran search-term-gold-miner and got a list of negatives. Can you add them to my Brand Campaign?

**Example 2: Manual List**
Hey Claude—I just added the "negative-keyword-implementer" skill. Add these negative keywords to campaign ID 123456789:
- free
- jobs
- careers
- how to
- diy

**Example 3: With Match Type Specification**
Hey Claude—I just added the "negative-keyword-implementer" skill. Add "free shipping competitor" as an EXACT match negative and "free" as a PHRASE match negative to my Brand Campaign.

**Example 4: Ad Group Level**
Hey Claude—I just added the "negative-keyword-implementer" skill. Add these negatives only to the "Generic Terms" ad group, not the whole campaign: cheap, discount, budget

## What to Provide

- Account and campaign/ad group to target
- List of negative keywords to add
- Match type preferences (EXACT, PHRASE, BROAD)
- Level preference (campaign or ad group)
- Or: Output from search-term-gold-miner skill

## What You'll Get

- Pre-implementation plan with conflict check
- Confirmation prompt before adding
- MCP execution with actual negative addition
- Post-implementation report
- Follow-up recommendations

## MCP Action Used

This skill uses the **write action** `add_negative_keywords`:
- Adds negatives directly to your Google Ads account
- Supports campaign-level or ad group-level
- Supports BROAD, PHRASE, or EXACT match types

## Safety Features

- Always asks for confirmation before adding
- Checks for conflicts with existing keywords
- Provides rollback instructions
- Batches by match type for clarity

## Workflow

Recommended workflow:
1. Run `search-term-gold-miner` to identify waste
2. Review the negative recommendations
3. Use this skill to implement the negatives
4. Wait 7-14 days
5. Re-run `search-term-gold-miner` to verify improvement
