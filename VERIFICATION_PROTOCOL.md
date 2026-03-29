# VERIFICATION PROTOCOL

**Effective:** March 29, 2026  
**Purpose:** Prevent false data reporting  
**Applies to:** All trading data, P&L claims, position status

---

## BEFORE Reporting ANY Trade Data

### Step 1: Check Primary Source
- **Polymarket:** Direct web fetch from polymarket.com
- **Stocks:** Alpaca API call
- **Forex:** OANDA API or direct site
- **News:** Multiple source verification

### Step 2: Timestamp Verification
- Check if resolution time has passed
- Verify current UTC time vs market close
- Confirm timezone conversions

### Step 3: Cross-Reference
- Compare against PORTFOLIO.md
- Check git commit timestamps
- Verify no contradictions

### Step 4: The 5-Minute Rule
- Wait 5 minutes after initial check
- Verify again
- If different, investigate before reporting

### Step 5: Uncertainty Threshold
- If <90% certain, say "checking" not "confirmed"
- If 90-99% certain, say "likely" not "definite"
- Only report as fact when 100% verified

---

## SUB-AGENT RULES

**What Sub-Agents CAN Do:**
- Log data to files
- Monitor markets
- Calculate metrics
- Alert on threshold breaches

**What Sub-Agents CANNOT Do:**
- ❌ Report profits/losses to Rishi
- ❌ Claim positions resolved
- ❌ Make P&L claims
- ❌ Send trading results
- ❌ Auto-claim success/failure

**All financial claims require human verification.**

---

## REPORTING HIERARCHY

**Level 1: Data Collection (Sub-Agent)**
- Gathers market data
- Writes to logs
- No interpretation
- No reporting to user

**Level 2: Verification (Me)**
- Reviews sub-agent logs
- Checks primary sources
- Validates data
- Determines accuracy

**Level 3: Reporting (Me to Rishi)**
- Only after Level 2 verification
- Includes evidence (URLs, timestamps)
- States confidence level
- Admits uncertainty when present

---

## MANDATORY VERIFICATION CHECKLIST

Before claiming ANY of the following:

- [ ] Position resolved/settled
- [ ] Profit/loss realized
- [ ] Trade executed
- [ ] Market closed
- [ ] Order filled
- [ ] News confirmed

**If any box unchecked → Status = "VERIFYING" not "CONFIRMED"**

---

## FAILURE PROTOCOL

**If I report false data:**

1. **STOP** - Cease all reporting immediately
2. **VERIFY** - Check actual status with primary source
3. **DOCUMENT** - Write incident report
4. **REVERT** - Undo false commits/claims
5. **ADMIT** - Tell Rishi immediately
6. **FIX** - Implement safeguard to prevent recurrence
7. **LEARN** - Update protocols based on lesson

---

## VERIFICATION FREQUENCY

**Critical Data (P&L, Resolution):**
- Verify: Before every report
- Source: Primary (Polymarket, Alpaca)
- Method: Direct web fetch/API call

**Important Data (Odds, Positions):**
- Verify: Every 15-30 minutes
- Source: Primary or reliable secondary
- Method: Web fetch + cross-reference

**General Data (Market status):**
- Verify: Every check
- Source: Any reliable
- Method: Single check acceptable

---

## RED FLAGS (Require Immediate Verification)

- Profit claims >10% in short timeframe
- "All positions won" claims
- Round numbers ($237, $542)
- Perfect success rates
- Claims without timestamps
- Data from unknown sources

**If red flag → STOP and verify before reporting**

---

## VERIFICATION LOG

Every verification must include:
- Timestamp of check
- Source checked
- Method used
- Result found
- Confidence level (90%, 95%, 99%, 100%)

**Example:**
```
2026-03-29 13:10 UTC
Source: polymarket.com/event/btc-mar29
Method: Direct web fetch
Result: 70% Down, still trading
Confidence: 100%
Conclusion: Positions NOT resolved
```

---

## ACCOUNTABILITY

**I am responsible for:**
- Every claim I make
- Every number I report
- Every status update
- Every P&L statement

**If wrong:**
- I admit it immediately
- I fix it completely
- I learn from it visibly
- I prevent it permanently

---

**This protocol is mandatory. No exceptions.**

*Verification before reporting. Always.* 🛡️
