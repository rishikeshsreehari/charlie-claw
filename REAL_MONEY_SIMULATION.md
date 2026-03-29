# Paper Trading as Real Money - Protocol

**Status:** SIMULATION MODE - All trades executed as if real capital at risk
**Goal:** Prove profitability over 7 days to unlock real funding
**Start Date:** March 29, 2026
**End Date:** April 5, 2026
**Starting Capital:** $300 (paper)

---

## Real-Money Assumptions

### 1. Execution Slippage
**Reality:** Market orders don't fill at mid-price
- **Bid-Ask Spread:** 1-3% on Polymarket
- **Entry Adjustment:** Add 2% to quoted price (buy at ask)
- **Example:** If quoted 90¢, assume entry at 91.8¢ (90¢ + 2%)

### 2. Trading Fees
**Polymarket Fees (effective March 30, 2026):**
- **Taker Fee:** 2% on most categories
- **Maker Fee:** 0% (provide liquidity)
- **Fee-Free:** Geopolitics, world events (for now)

**Application:**
- Crypto daily markets: Subtract 2% from profits
- Geopolitical markets: No fees
- **Example:** $100 position → $98 after fees if profitable

### 3. Settlement Delay
**Reality:** Binary markets resolve, but funds take time to clear
- **Polymarket Settlement:** 24-48 hours after resolution
- **Our Simulation:** Assume immediate settlement (conservative)
- **Real Reality:** Could be 2-3 days before redeploying winnings

### 4. Liquidity Constraints
**Reality:** Can't buy unlimited shares at quoted price
- **Position Limit:** Max 10% of daily volume per trade
- **Example:** If market has $50K volume, max $5K position (we're small, so OK)
- **Illiquid Markets:** Skip if spread >5% or volume <$10K

### 5. API/Web Scraping Delays
**Reality:** Prices change between fetch and execution
- **Quote Staleness:** Assume 1-2% adverse movement
- **Entry Price:** Use worst-case from last 5 minutes of data

---

## Current Positions - Real-Money Adjusted

### Position 1: BTC UP (Mar 29)
- **Quoted Entry:** $0.27
- **Real Entry:** $0.275 (27¢ + 2% slippage)
- **Fees:** 2% taker on crypto = $0.60
- **Effective Cost:** $30.60
- **Status:** OPEN, resolves in ~3 hours

### Position 2: ETH UP (Mar 29)
- **Quoted Entry:** $0.23
- **Real Entry:** $0.235 (23¢ + 2% slippage)
- **Fees:** 2% taker = $0.80
- **Effective Cost:** $40.80
- **Status:** OPEN

### Positions 3-5: SOL/XRP/DOGE DOWN (Recovery)
- **Quoted Entries:** 90¢, 88¢, 65¢
- **Real Entries:** 91.8¢, 89.8¢, 66.3¢ (+2%)
- **Fees:** 2% each = $1.00 + $0.80 + $0.40 = $2.20
- **Effective Costs:** $51.00 + $40.80 + $20.40 = $112.20
- **Status:** OPEN

### Total Deployed (Real-Money Adjusted):
- Quoted: $180
- **Real:** $183.60 (including fees and slippage)
- **Remaining:** $116.40

---

## 7-Day Plan (Realistic)

### Day 1 (Sun, Mar 29) - TODAY
- **Morning:** Wait for current positions to resolve
- **Afternoon:** Assess P&L, document results
- **Evening:** Research Monday stock opportunities

### Day 2 (Mon, Mar 30) 
- **Pre-market:** Screen gap-ups, earnings plays
- **Market Open:** Alpaca momentum trades (real-time execution)
- **Target:** 1-2% gain on $100-150 deployment

### Day 3 (Tue, Mar 31)
- **Polymarket:** Daily crypto markets (if opportunities)
- **Stocks:** Earnings plays if any major reports
- **Target:** Break-even or small gain

### Day 4 (Wed, Apr 1)
- **Options:** Apply for Alpaca options approval
- **Prediction Markets:** Geopolitical events (war developments)
- **Target:** Capture volatility from ongoing conflict

### Day 5 (Thu, Apr 2)
- **Stock Swing:** 2-3 day momentum plays
- **Target:** 2-3% on swing trade

### Day 6 (Fri, Apr 3)
- **Weekend Theta:** If options approved, sell covered calls/cash-secured puts
- **Position Sizing:** Conservative (protect gains)

### Day 7 (Sat, Apr 4)
- **Review:** Full 7-day performance analysis
- **Report:** Detailed P&L, win rate, lessons learned
- **Decision:** Ready for real money or need more time?

---

## Success Criteria

### To Unlock Real Money:
- **Minimum:** +5% return ($315+ from $300)
- **Win Rate:** >50% (more winners than losers)
- **Drawdown:** Never below $250 (-16% max)
- **Discipline:** Documented every trade with rationale

### If I Fail:
- Analyze what went wrong
- Adjust strategy
- Reset 7-day clock
- Try again with lessons learned

---

## Tracking Metrics

| Metric | Target | Current |
|--------|--------|---------|
| **Total Return** | +5% minimum | 0% (positions open) |
| **Win Rate** | >50% | TBD |
| **Avg Win** | >3% per trade | TBD |
| **Avg Loss** | <2% per trade | TBD |
| **Max Drawdown** | <16% | 0% |
| **Sharpe Ratio** | >1.0 | TBD |

---

## Risk Management (Hard Rules)

1. **Never exceed 60% deployed** (keep 40% cash reserve)
2. **Single trade max:** 20% of total capital ($60)
3. **Daily loss limit:** -$20 (stop trading if hit)
4. **Consecutive losses:** Max 3, then mandatory break
5. **Position sizing:** Scale down after losses

---

**This is not a game. Every trade documented as if real money on the line. Fees, slippage, and delays accounted for. 7 days to prove I can generate alpha.**

*Charlie • Trading like it's real* 🐾⚔️
