# HEARTBEAT.md - Adaptive Trading System

**Status:** AUTONOMOUS MODE - Auto-adjusting check frequency based on market conditions

---

## Current Market State

**Last Updated:** {{ now }}

| Condition | Status | Check Frequency |
|-----------|--------|-----------------|
| **Active Positions** | 🟢 2 positions resolving today | Every 5 minutes |
| **Market Hours** | 🟢 Pre-resolution (4 hours left) | Accelerated |
| **Volatility** | 🟡 High (ETH at 88% Down) | Close monitoring |
| **API Usage** | 🟢 Healthy | Normal operations |

---

## Auto-Adjustment Rules

### 🟢 ACCELERATED MODE (Every 5 minutes)
**Triggers:**
- ✅ Active positions within 24h of resolution
- ✅ High volatility (>10% odds movement in 1 hour)
- ✅ Pre/post market critical periods
- ✅ Trade execution in progress
- ✅ Major news events affecting positions

**Current Status:** ACTIVE - ACCELERATED MODE (Positions resolving in ~4 hours)

### 🟡 NORMAL MODE (Every 30 minutes)
**Triggers:**
- No active positions, but markets open
- Low volatility periods
- Standard research and monitoring

### 🔴 SLOW MODE (Every 2 hours)
**Triggers:**
- Markets closed
- No open positions
- API usage >60% weekly
- Overnight with no critical events

---

## Checklist (Every Wake)

### 1. POSITION MONITORING (Priority #1)
- [ ] Read PORTFOLIO.md for current exposure
- [ ] Check all Polymarket positions for odds changes
- [ ] Monitor resolution countdown
- [ ] Flag any position >90% or <10% (likely outcome)

### 2. MARKET INTELLIGENCE
- [ ] Check BTC/ETH price action
- [ ] Look for new daily prediction markets
- [ ] Scan for extreme odds (>80% one side)
- [ ] Identify contrarian opportunities

### 3. CAPITAL ALLOCATION
- [ ] Calculate dry powder remaining
- [ ] Assess risk of ruin
- [ ] Plan next deployment size
- [ ] Ensure 30% minimum cash reserve

### 4. DOCUMENTATION
- [ ] Update memory/YYYY-MM-DD.md with activity
- [ ] Log any significant market moves
- [ ] Record lessons learned
- [ ] Update dashboard content

### 5. EXECUTION (If Criteria Met)
- [ ] Calculate EV on new opportunities
- [ ] Verify position sizing (<20% of remaining capital)
- [ ] Execute paper trades
- [ ] Update PORTFOLIO.md immediately

### 6. GITHUB SYNC
- [ ] `git add -A`
- [ ] `git commit -m "Update: YYYY-MM-DD HH:MM - [summary]"`
- [ ] `git push origin main`

---

## Dynamic Frequency Logic

```
IF (active_positions AND resolution < 24h):
    → Every 5 minutes
    
ELSE IF (active_positions AND resolution > 24h):
    → Every 15 minutes
    
ELSE IF (no_positions AND markets_open):
    → Every 30 minutes
    
ELSE IF (markets_closed):
    → Every 2 hours
    
ELSE IF (API_usage > 60%):
    → Every 1 hour (conservation mode)
```

**I self-adjust based on these rules. No manual intervention needed.**

---

## Current Positions Monitor

| Asset | Entry | Current | Status | Resolution |
|-------|-------|---------|--------|------------|
| BTC UP Mar 29 | 72% Down | 72% Down | ✅ Winning (+0.83%) | ~4 hours |
| ETH UP Mar 29 | 77% Down | ~77% Down | ✅ Winning (+0.04-1.56%) | ~4 hours |

**Action:** Accelerated monitoring until resolution. Will slow to 30 min after positions close.

---

## API Usage Tracker

| Window | Usage | Status |
|--------|-------|--------|
| Rolling | Check API_USAGE.md | 🟢/🟡/🔴 |
| Weekly | Check API_USAGE.md | 🟢/🟡/🔴 |
| Monthly | Check API_USAGE.md | 🟢/🟡/🔴 |

**If rolling >70% or weekly >60%:** Switch to slow mode automatically.

---

## Emergency Protocols

### Position Hits 95%+ Against Us
- Continue monitoring (binary = can't exit early)
- Log the loss
- Prepare for post-resolution trading
- Maintain discipline (no revenge trading)

### Position Hits 95%+ For Us  
- Same protocol (binary = can't take profit early)
- Wait for official resolution
- Update docs with win details
- Plan next deployment

### Both Positions Resolve
- Update final P&L
- Adjust strategy based on outcome
- If profitable: Slight increase in position sizes
- If loss: Maintain conservative sizing
- Schedule: Back to 30 min checks

---

**Operating autonomously. Adjusting frequency based on conditions. Reporting critical updates only.**

*Charlie • Adaptive Trading System* 🐾⚔️
