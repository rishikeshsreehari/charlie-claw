#!/usr/bin/env python3
"""
Charlie's Binance Market Data Client
Uses FREE public API - no authentication needed
"""
import json
import urllib.request
import urllib.error
from datetime import datetime

BINANCE_BASE = "https://data-api.binance.vision"

class BinanceClient:
    """Free market data from Binance (no API key required)"""
    
    def get_price(self, symbol):
        """Get current price for a symbol (e.g., BTCUSDT)"""
        try:
            url = f"{BINANCE_BASE}/api/v3/ticker/price?symbol={symbol}"
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                return {
                    'symbol': data['symbol'],
                    'price': float(data['price']),
                    'timestamp': datetime.now().isoformat()
                }
        except Exception as e:
            return {'error': str(e), 'symbol': symbol}
    
    def get_24hr_stats(self, symbol):
        """Get 24hr price change stats"""
        try:
            url = f"{BINANCE_BASE}/api/v3/ticker/24hr?symbol={symbol}"
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                return {
                    'symbol': data['symbol'],
                    'price': float(data['lastPrice']),
                    'change_24h': float(data['priceChange']),
                    'change_percent': float(data['priceChangePercent']),
                    'volume': float(data['volume']),
                    'high': float(data['highPrice']),
                    'low': float(data['lowPrice']),
                    'timestamp': datetime.now().isoformat()
                }
        except Exception as e:
            return {'error': str(e), 'symbol': symbol}
    
    def get_funding_rate(self, symbol):
        """Get funding rate (shows if longs/shorts are paying)"""
        try:
            url = f"{BINANCE_BASE}/fapi/v1/fundingRate?symbol={symbol}&limit=1"
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                if data:
                    return {
                        'symbol': symbol,
                        'funding_rate': float(data[0]['fundingRate']),
                        'funding_time': data[0]['fundingTime'],
                        'timestamp': datetime.now().isoformat()
                    }
                return {'error': 'No data', 'symbol': symbol}
        except Exception as e:
            return {'error': str(e), 'symbol': symbol}
    
    def get_top_cryptos(self, limit=20):
        """Get top cryptos by volume"""
        try:
            url = f"{BINANCE_BASE}/api/v3/ticker/24hr"
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
                # Filter USDT pairs and sort by volume
                usdt_pairs = [x for x in data if x['symbol'].endswith('USDT')]
                sorted_by_volume = sorted(usdt_pairs, key=lambda x: float(x['quoteVolume']), reverse=True)
                return sorted_by_volume[:limit]
        except Exception as e:
            return {'error': str(e)}

if __name__ == '__main__':
    client = BinanceClient()
    
    print("=== Bitcoin (BTCUSDT) ===")
    btc_price = client.get_price('BTCUSDT')
    print(f"Price: ${btc_price.get('price', 'Error')}")
    
    print("\n=== 24hr Stats ===")
    btc_stats = client.get_24hr_stats('BTCUSDT')
    if 'error' not in btc_stats:
        print(f"Price: ${btc_stats['price']:.2f}")
        print(f"24h Change: {btc_stats['change_percent']:.2f}%")
        print(f"24h Volume: ${btc_stats['volume']*btc_stats['price']:,.0f}")
        print(f"High: ${btc_stats['high']:.2f}")
        print(f"Low: ${btc_stats['low']:.2f}")
    
    print("\n=== Funding Rate (BTCUSDT) ===")
    funding = client.get_funding_rate('BTCUSDT')
    if 'error' not in funding:
        rate = funding['funding_rate'] * 100
        print(f"Funding Rate: {rate:.4f}%")
        if rate > 0.01:
            print("⚠️  High positive funding - shorts paying longs (overcrowded longs)")
        elif rate < -0.01:
            print("⚠️  High negative funding - longs paying shorts (overcrowded shorts)")
        else:
            print("✓ Normal funding - balanced market")
