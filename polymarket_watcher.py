#!/usr/bin/env python3
"""
Charlie's Polymarket Watcher
Uses FREE Gamma API - no authentication needed for market data
Paper trading: Manual tracking only (no real execution)
"""
import json
import urllib.request
from datetime import datetime

GAMMA_API = "https://gamma-api.polymarket.com"

class PolymarketWatcher:
    """Watch Polymarket markets - paper trading only (manual tracking)"""
    
    def get_market(self, market_slug):
        """Get market details by slug (e.g., 'bitcoin-up-or-down-on-march-29-2026')"""
        try:
            url = f"{GAMMA_API}/markets?slug={market_slug}"
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                if data and len(data) > 0:
                    market = data[0]
                    return {
                        'id': market.get('id'),
                        'title': market.get('question'),
                        'slug': market.get('slug'),
                        'volume': market.get('volume'),
                        'liquidity': market.get('liquidity'),
                        'end_date': market.get('endDate'),
                        'status': market.get('active'),
                        'outcomes': market.get('outcomes', []),
                        'timestamp': datetime.now().isoformat()
                    }
                return {'error': 'Market not found', 'slug': market_slug}
        except Exception as e:
            return {'error': str(e), 'slug': market_slug}
    
    def get_orderbook(self, market_id):
        """Get orderbook for a market (shows current prices)"""
        try:
            url = f"{GAMMA_API}/order-books?market_id={market_id}"
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                return {
                    'orderbook': data,
                    'timestamp': datetime.now().isoformat()
                }
        except Exception as e:
            return {'error': str(e)}
    
    def search_markets(self, query, limit=10):
        """Search for markets"""
        try:
            url = f"{GAMMA_API}/markets?search={query}&limit={limit}"
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                markets = []
                for m in data:
                    markets.append({
                        'id': m.get('id'),
                        'title': m.get('question'),
                        'slug': m.get('slug'),
                        'volume': m.get('volume'),
                        'end_date': m.get('endDate')
                    })
                return markets
        except Exception as e:
            return {'error': str(e)}

if __name__ == '__main__':
    watcher = PolymarketWatcher()
    
    print("=== Polymarket Watcher (Paper Trading Mode) ===\n")
    
    # Watch BTC Up/Down March 29
    print("Checking: Bitcoin Up or Down on March 29?")
    market = watcher.get_market('bitcoin-up-or-down-on-march-29-2026')
    
    if 'error' not in market:
        print(f"Market: {market['title']}")
        print(f"Volume: ${market.get('volume', 'N/A')}")
        print(f"Status: {'Active' if market['status'] else 'Closed'}")
        print(f"End Date: {market.get('end_date', 'N/A')}")
        
        if market.get('outcomes'):
            print("\nOutcomes:")
            for outcome in market['outcomes']:
                print(f"  - {outcome.get('name', 'N/A')}: {outcome.get('probability', 'N/A')}")
    else:
        print(f"Error: {market['error']}")
    
    print("\n=== Paper Trading Note ===")
    print("I will track trades manually in PORTFOLIO.md")
    print("No real execution - just realistic tracking with actual market prices")
