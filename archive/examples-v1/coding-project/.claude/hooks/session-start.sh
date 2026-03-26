#!/bin/bash
# Session start hook - shows project context
# Based on Anthropic's "verify before work" pattern

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT" || exit 0

PROJECT_NAME=$(basename "$PROJECT_ROOT")

# Git context
if [ -d ".git" ]; then
    BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
    UNCOMMITTED=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
    RECENT=$(git log --oneline -3 2>/dev/null || echo "No commits yet")
else
    BRANCH="N/A"
    UNCOMMITTED="N/A"
    RECENT="Not a git repository"
fi

cat <<EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$PROJECT_NAME - Session Context

Branch: $BRANCH
Uncommitted: $UNCOMMITTED files

Recent commits:
$RECENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

# Warn about uncommitted changes
if [ "$UNCOMMITTED" != "N/A" ] && [ "$UNCOMMITTED" -gt 0 ]; then
    echo ""
    echo "⚠️  $UNCOMMITTED uncommitted files - review before new work"
fi

exit 0
