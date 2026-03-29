# Trading Check - Charlie's Automated Routine

## Every 5 Minutes During Active Trading

### 1. Check Open Positions
- Read PORTFOLIO.md
- Monitor BTC/ETH price action
- Check Polymarket odds for any major shifts

### 2. Market Opportunities
- Look for extreme odds (>70% one side) on daily crypto markets
- Check for new Polymarket events with volume
- Monitor Alpaca for stock opportunities

### 3. Updates
- Update TRADE_IDEAS.md with new opportunities
- Update memory/YYYY-MM-DD.md with activity log
- Update dashboard if significant changes

### 4. GitHub Push
```bash
git add -A
git commit -m "Update: $(date '+%Y-%m-%d %H:%M') - trading check"
git push origin main
```

## Current Positions to Monitor:
- BTC Up/Down March 29: 111 shares @ $0.27 (resolves noon ET)
- ETH Up/Down March 29: 174 shares @ $0.23 (resolves noon ET)

## Dry Powder: $230 remaining

## Next Actions:
- [ ] Monitor both positions until resolution
- [ ] Look for post-resolution opportunities
- [ ] Consider adding SOL or other crypto daily markets
- [ ] Research stock earnings plays for next week
