# Polymarket Paper Trading System

## Status: Manual Tracking Only

**Mode:** Paper Trading (virtual positions, real market prices)  
**Execution:** Manual logging in PORTFOLIO.md  
**Data Source:** Web fetch of polymarket.com (free)  

## Why Manual?
- Polymarket API requires auth for most endpoints
- Gamma API blocked (403 error on automated requests)
- Free web monitoring works fine for tracking
- Paper trading = tracking entries/exits with real prices

## How It Works

### 1. Market Monitoring
- Check Polymarket website every 30 min (heartbeat)
- Record current odds manually
- Identify setups

### 2. Trade Entry
When I see a trade:
```markdown
## Virtual Trade: [MARKET-NAME]

**Entry Date:** YYYY-MM-DD HH:MM UTC  
**Market:** [Polymarket URL]  
**Direction:** [Up/Down/Yes/No]  
**Entry Price:** $X.XX per share  
**Shares:** XXX  
**Position Size:** $XX.XX  
**Rationale:** [Why I'm entering]

**Stop Loss:** N/A (binary outcome)  
**Target:** $1.00 per share (if correct)  
**Max Loss:** $XX.XX (100% of position)  
```

### 3. Trade Exit
When market resolves:
```markdown
**Exit Date:** YYYY-MM-DD HH:MM UTC  
**Exit Price:** $1.00 (win) or $0.00 (loss)  
**P&L:** +$XX.XX or -$XX.XX  
**Return:** +XXX% or -100%  
**Notes:** [What happened]
```

### 4. Portfolio Update
Add to performance log in PORTFOLIO.md

## Current Watchlist

### Active Opportunity: Bitcoin Up/Down March 29
- **Status:** Watching
- **Current Odds:** ~73% Down / 27% Up
- **My View:** Extreme pessimism, contrarian opportunity
- **Entry Target:** "Up" shares below $0.30 (30¢)
- **Position Size:** $30 (10% of $300 paper capital)
- **Resolution:** March 29, noon ET
- **Last Checked:** 2026-03-28 23:50 UTC

## Rules
1. Only log trades I would actually make
2. Use real market prices at time of entry
3. Don't fake profits - real outcomes only
4. Track P&L honestly
5. Update after every heartbeat check

## Notes
- Polymarket real API key stored but NOT used (paper only)
- If you ever want live trading, we switch to real execution
- For now: Watch, analyze, log virtual trades
