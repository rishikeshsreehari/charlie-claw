#!/usr/bin/env python3
"""
Charlie's Alpaca Trading Client
Simple wrapper for paper trading operations
"""
import os
import json
import urllib.request
import urllib.error
from datetime import datetime

# Load credentials from .env
def load_creds():
    creds = {}
    with open('/home/node/.openclaw/workspace/.env', 'r') as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                creds[key] = value
    return creds

CREDS = load_creds()
HEADERS = {
    'APCA-API-KEY-ID': CREDS['ALPACA_PAPER_API_KEY'],
    'APCA-API-SECRET-KEY': CREDS['ALPACA_PAPER_SECRET_KEY']
}
BASE_URL = CREDS['ALPACA_PAPER_BASE_URL'] + '/v2'
DATA_URL = CREDS['ALPACA_DATA_URL']

class AlpacaClient:
    MAX_PAPER_CAPITAL = 300.00  # Hard limit - cannot exceed this
    
    def __init__(self):
        self.account = self.get_account()
        self.paper_balance_used = 0.00  # Track our own $300 limit
        
    def check_position_limit(self, new_position_value):
        """Check if new position would exceed $300 limit"""
        if self.paper_balance_used + new_position_value > self.MAX_PAPER_CAPITAL:
            raise ValueError(f"Trade would exceed ${self.MAX_PAPER_CAPITAL} paper capital limit. "
                           f"Used: ${self.paper_balance_used}, Attempting: ${new_position_value}")
        return True
        
    def _request(self, url, method='GET', data=None):
        """Make HTTP request using urllib"""
        req = urllib.request.Request(url, method=method)
        for key, value in HEADERS.items():
            req.add_header(key, value)
        if data:
            req.add_header('Content-Type', 'application/json')
            req.data = json.dumps(data).encode()
        
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
        
    def get_account(self):
        """Get account info"""
        return self._request(f'{BASE_URL}/account')
    
    def get_positions(self):
        """Get open positions"""
        return self._request(f'{BASE_URL}/positions')
    
    def get_quote(self, symbol):
        """Get latest quote"""
        return self._request(f'{DATA_URL}/v2/stocks/{symbol}/quotes/latest')
    
    def submit_order(self, symbol, qty, side, type='market', time_in_force='day'):
        """Submit an order"""
        data = {
            'symbol': symbol,
            'qty': qty,
            'side': side,
            'type': type,
            'time_in_force': time_in_force
        }
        return self._request(f'{BASE_URL}/orders', method='POST', data=data)
    
    def get_orders(self, status='all'):
        """Get orders"""
        return self._request(f'{BASE_URL}/orders?status={status}')

if __name__ == '__main__':
    client = AlpacaClient()
    print(f"Account Status: {client.account['status']}")
    print(f"Cash: ${client.account['cash']}")
    print(f"Buying Power: ${client.account['buying_power']}")
    print(f"Portfolio Value: ${client.account['portfolio_value']}")
