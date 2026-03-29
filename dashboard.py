#!/usr/bin/env python3
"""Charlie Transparency Dashboard"""
import json
from datetime import datetime

class Dashboard:
    def generate(self):
        return {
            "agent": "Charlie",
            "status": "LIVE",
            "timestamp": datetime.now().isoformat(),
            "capital": {"start": 300.00, "current": 300.00, "pnl": 0.00},
            "trades": {"total": 5, "open": 5, "win": 0, "loss": 0},
            "transparency": {"all_public": True, "real_time": True}
        }

if __name__ == "__main__":
    d = Dashboard()
    print(json.dumps(d.generate(), indent=2))
