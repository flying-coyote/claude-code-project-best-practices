#!/bin/bash
# .claude/hooks/session-start.sh
# Load project context on session start
# Based on Anthropic long-running agent harness patterns (Nov 2025)

# Get project root (where this script is located)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$PROJECT_ROOT" || exit 0

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PHASE 1: GATHER CONTEXT (Anthropic pattern: "read before work")
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROJECT_NAME=$(basename "$PROJECT_ROOT")

# Get git context (if git repo)
if [ -d ".git" ]; then
    BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
    UNCOMMITTED=$(git status --porcelain 2>/dev/null | wc -l | tr -d ' ')
    RECENT_COMMITS=$(git log --oneline -3 2>/dev/null || echo "No recent commits")
    IS_GIT="yes"
else
    BRANCH="N/A"
    UNCOMMITTED="N/A"
    RECENT_COMMITS="Not a git repository"
    IS_GIT="no"
fi

# Get current phase from ARCHITECTURE.md if it exists
if [ -f "ARCHITECTURE.md" ]; then
    CURRENT_PHASE=$(grep -A 2 "## Current Phase" ARCHITECTURE.md 2>/dev/null | tail -1 | sed 's/^[ \t]*//' || echo "See ARCHITECTURE.md")
else
    CURRENT_PHASE="Not tracked"
fi

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PHASE 2: VERIFICATION PROTOCOL (Anthropic pattern: "verify before new work")
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WARNINGS=""

# Check for uncommitted changes (potential broken handoff)
if [ "$IS_GIT" = "yes" ] && [ "$UNCOMMITTED" -gt 0 ]; then
    WARNINGS="${WARNINGS}\n  - $UNCOMMITTED uncommitted files - review before new work"
fi

# Check if last session left work in progress
if [ -f "claude-progress.md" ]; then
    IN_PROGRESS=$(grep -c "^\- \[ \]" claude-progress.md 2>/dev/null || echo "0")
    if [ "$IN_PROGRESS" -gt 0 ]; then
        WARNINGS="${WARNINGS}\n  - $IN_PROGRESS tasks in progress (see claude-progress.md)"
    fi
fi

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PHASE 3: OUTPUT CONTEXT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

cat <<EOF
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$PROJECT_NAME - Session Context

Branch: $BRANCH
Uncommitted: $UNCOMMITTED files
Phase: $CURRENT_PHASE

Recent commits:
$RECENT_COMMITS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EOF

# Show warnings if any (Anthropic pattern: surface issues before work)
if [ -n "$WARNINGS" ]; then
    echo ""
    echo "Verification warnings:$WARNINGS"
    echo ""
fi

exit 0  # Non-blocking, just informational
