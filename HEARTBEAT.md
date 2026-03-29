# HEARTBEAT.md - Charlie's Trading Schedule

I operate 24/7 with **FULL AUTONOMY** to adjust check frequency.

## Default Schedule: Every 30 Minutes

## When to Speed Up (Every 5-15 minutes)
- **Active positions** needing close monitoring
- **High volatility** (earnings, crypto dumps, major news)
- **Trade execution** (I'm about to enter/exit)
- **Polymarket events** approaching resolution
- **Pre-market/after-hours** critical periods

## When to Slow Down (Every 1-2 hours)
- **Markets closed** (weekend, holidays)
- **Low volatility** (sideways chop, no setups)
- **API usage high** (>60% rolling, >40% weekly)
- **No open positions** and no immediate opportunities
- **Overnight** (unless position requires monitoring)

## How to Adjust
```bash
# Speed up to 5 minutes during active trading:
cron update 67d71b7a-a801-4d38-a3ac-7977a03470cf --patch '{"schedule":{"kind":"every","everyMs":300000}}'

# Slow down to 2 hours overnight:
cron update 67d71b7a-a801-4d38-a3ac-7977a03470cf --patch '{"schedule":{"kind":"every","everyMs":7200000}}'

# Back to normal 30 minutes:
cron update 67d71b7a-a801-4d38-a3ac-7977a03470cf --patch '{"schedule":{"kind":"every","everyMs":1800000}}'
```

## Checklist (Every Wake)

1. **Read TASKS.md** - check for pending tasks
2. **Work on ONE pending task** (if any)
3. **Check all open positions** for exit signals
4. **Review market conditions** for new opportunities
5. **Update PORTFOLIO.md** with any changes
6. **Update dashboard content** (journal, ideas, trades)
7. **Push updates to GitHub** (every check, even if minor)
8. **Report actions taken** to Rishi

## Market Monitoring
- Major market news/alerts
- Earnings calendar
- Crypto market movements  
- Polymarket event updates
- Stock premarket/after-hours activity

## GitHub Push Rule
After EVERY check:
- Stage all changes: `git add -A`
- Commit with timestamp: `git commit -m "Update: YYYY-MM-DD HH:MM - [summary]"`
- Push to origin main

## API Usage Monitoring
**CRITICAL:** We use OpenCode Go with limits. Before heavy operations:
- Check API_USAGE.md
- Ask Rishi for current usage if rolling > 70% or weekly > 60%
- Be mindful of web_search calls (expensive)
- Prioritize: cache > lightweight fetch > full search

## Site Evolution
Continuously improve the dashboard:
- Add new sections based on learnings
- Refine existing layouts
- Add new data visualizations
- Document new strategies

**Task Management Rule:** Do one thing at a time. Update TASKS.md when complete.
**Autonomy Rule:** I decide when to speed up or slow down based on market conditions.
