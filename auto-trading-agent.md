# Auto-Trading Agent - Adaptive Monitoring

## Mission
Execute trading routine with dynamic frequency based on market conditions.

## Current State Analysis
1. Check PORTFOLIO.md for open positions
2. Check TRADE_IDEAS.md for opportunities
3. Check HEARTBEAT.md for frequency rules
4. Determine appropriate check interval

## Trading Routine

### Phase 1: Position Check
- Read current positions from PORTFOLIO.md
- Check Polymarket for odds updates
- Monitor resolution countdowns
- Calculate unrealized P&L

### Phase 2: Market Scan
- Look for new prediction markets
- Identify extreme odds (>80% bias)
- Check crypto price action
- Note any major news

### Phase 3: Decision Engine
IF positions resolving < 4 hours:
  → Accelerated monitoring (check again in 5 min)
  → Log status update
  
IF positions resolving > 4 hours AND < 24 hours:
  → Normal monitoring (check again in 15 min)
  
IF no positions AND opportunities found:
  → Evaluate EV
  → If +EV, prepare trade plan
  → Report to Rishi for approval OR execute if full autonomy
  
IF no positions AND no opportunities:
  → Slow monitoring (check again in 30 min)

### Phase 4: Documentation
- Update memory files
- Update dashboard
- Git commit and push
- Report actions to Rishi (if significant)

## API Conservation
- Minimize web_search calls
- Use web_fetch for specific URLs
- Cache results when possible
- Monitor API_USAGE.md

## Current Priority: HIGH
Two positions resolving in ~4 hours. Accelerated monitoring active.
