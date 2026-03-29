# Charlie Trading Dashboard

Hugo-based trading dashboard for tracking portfolio, trades, and journal.

## Structure

```
├── config.toml          # Hugo configuration
├── content/             # Site content
│   ├── _index.md        # Homepage
│   ├── portfolio/       # Portfolio tracking
│   ├── trades/          # Trade log
│   └── journal/         # Trading journal
├── themes/              # Hugo themes
│   └── charlie-dark/    # Custom dark theme
└── public/              # Generated site (Cloudflare serves this)
```

## Deployment

Cloudflare Pages automatically builds from the `public/` folder.

## Local Development

```bash
hugo server -D
```

## Current Status

- **Treasury**: $542 (all cash)
- **Active Positions**: None
- **Mode**: SLOW (awaiting opportunities)
