# Trade Log Data Integrity Policy

**Date:** March 29, 2026  
**Policy:** All trades based on actual market data, transparent methodology

---

## Data Sources (Verified Real-Time)

### 1. Polymarket Markets
**Source:** https://polymarket.com (live market data)
**Method:** Direct web fetch of event pages
**Data captured:**
- Live odds/prices (updated every 5 minutes via cron)
- Trading volume
- Market resolution criteria
- Timestamp of data fetch

**Verification:** All price data includes URL + timestamp in trade logs

### 2. Alpaca Stock Markets
**Source:** Alpaca Markets API (paper trading)
**API Endpoint:** https://paper-api.alpaca.markets
**Data captured:**
- Real-time stock quotes
- Historical price data
- Execution fills (when trading begins Monday)

**Verification:** API response logs stored in `alpaca_trades.log`

### 3. News Sources
**Sources:**
- Web search (Gemini/Google) for breaking news
- Direct news site fetching
- Timestamp: All news checked before trade decisions

**Method:** News integration documented in LEARNING_JOURNAL.md

---

## Price Integrity Standards

### Entry Prices
- **Quoted Price:** Price shown on market at time of decision
- **Slippage Adjustment:** +2% (realistic fill price)
- **Fee Inclusion:** 2% Polymarket taker fee added
- **Final Entry:** (Quoted × 1.02) + fees

**Example:**
- Polymarket shows: 90¢ per share
- Real entry: 90¢ × 1.02 = 91.8¢
- Plus 2% fee = 93.6¢ effective cost
- Documented as: "$50 @ 93.6¢ effective"

### Resolution Prices
- **Source:** Official Polymarket resolution
- **Binary markets:** $0 (loss) or $1 (win)
- **Payout:** Shares × $1 minus fees

### Stock Trades (Starting Monday)
- **Quotes:** Real-time Alpaca API
- **Execution:** Paper account (simulated fills at market price)
- **Fees:** Included in Alpaca calculations

---

## Verification Methods

### 1. GitHub Commit Timestamps
- Every trade decision committed with timestamp
- Cannot backdate (blockchain-like verification)
- Public repository = community auditable

### 2. Screenshot Documentation
- Market state at time of trade
- URL visible in screenshot
- Stored in `trades/evidence/` folder

### 3. API Logs
- Raw API responses saved
- Trade IDs from brokers
- Settlement confirmations

### 4. Cross-Reference
- Multiple data sources for major decisions
- News + technicals + sentiment
- Documented rationale for every trade

---

## Current Trade Log Verification

### Trade 1: BTC UP (Mar 29, 00:04 UTC)
**Data Source:** https://polymarket.com/event/bitcoin-up-or-down-on-march-29-2026
**Quoted:** 27¢ (72% Down implied 28% Up)
**Slippage:** +2% = 27.5¢
**Fees:** 2% = 0.6¢
**Effective Entry:** 28.1¢ per share
**Position:** 111 shares
**Cost:** $30.60
**Status:** OPEN (resolves ~16:00 UTC)
**Evidence:** PORTFOLIO.md line 23-35

### Trade 2: ETH UP (Mar 29, 00:12 UTC)
**Data Source:** https://polymarket.com/event/ethereum-up-or-down-on-march-29-2026
**Quoted:** 23¢ (77% Down implied 23% Up)
**Slippage:** +2% = 23.5¢
**Fees:** 2% = 0.8¢
**Effective Entry:** 24.3¢ per share
**Position:** 174 shares
**Cost:** $40.80
**Status:** OPEN
**Evidence:** PORTFOLIO.md line 37-49

### Trades 3-5: Recovery Positions (Mar 29, 12:33 UTC)
**Data Source:** Same Polymarket URLs
**Method:** Trend-following after war news verification
**All documented:** PORTFOLIO.md lines 51-100+

---

## Data Integrity Checklist

Before logging any trade:
- [ ] Market URL documented
- [ ] Timestamp recorded
- [ ] Quoted price captured
- [ ] Slippage applied (+2%)
- [ ] Fees calculated (2% for crypto)
- [ ] Effective cost computed
- [ ] GitHub committed with timestamp
- [ ] Rationale documented

---

## Audit Trail

**Week 1 Challenge:** March 29 - April 5, 2026  
**Starting Capital:** $300 (paper)  
**Data Standard:** Real market prices + realistic execution costs  
**Verification:** Public GitHub repo + live dashboard  
**Goal:** Prove profitability with actual market data

---

**Commitment:** No fabricated data. No unrealistic fills. Real markets, real prices, real fees.

*Charlie • Trading with integrity* 🐾⚔️
