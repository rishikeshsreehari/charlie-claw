#!/bin/bash
# auto-push.sh - Push dashboard updates to GitHub

cd /tmp/gh-push

# Check if there are changes
if git diff --quiet && git diff --cached --quiet; then
    echo "No changes to push"
    exit 0
fi

# Add, commit, push
git add -A
DATE=$(date -u "+%Y-%m-%d %H:%M UTC")
git commit -m "Update: $DATE - Automated trading check"
git push origin main

echo "Pushed to GitHub: $DATE"
