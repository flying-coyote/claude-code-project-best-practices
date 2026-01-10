#!/bin/bash
# .claude/hooks/stop-doc-check.sh
# Check documentation currency before session ends

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$PROJECT_ROOT" || exit 0

# Check recent activity
RECENT_COMMITS=$(git log --since="7 days ago" --oneline 2>/dev/null | wc -l | tr -d ' ')

if [ "$RECENT_COMMITS" -eq 0 ]; then
    # No recent activity, documentation likely current
    exit 0
fi

# Check last modification of key docs
WARNINGS=""

if [ -f "ARCHITECTURE.md" ]; then
    ARCH_AGE=$(find ARCHITECTURE.md -mtime +7 2>/dev/null | wc -l)
    if [ "$ARCH_AGE" -gt 0 ]; then
        WARNINGS="${WARNINGS}\n  - ARCHITECTURE.md: >7 days old"
    fi
fi

if [ -f "PLAN.md" ]; then
    PLAN_AGE=$(find PLAN.md -mtime +7 2>/dev/null | wc -l)
    if [ "$PLAN_AGE" -gt 0 ]; then
        WARNINGS="${WARNINGS}\n  - PLAN.md: >7 days old"
    fi
fi

if [ -n "$WARNINGS" ]; then
    echo ""
    echo "Documentation Currency Check"
    echo "Recent commits: $RECENT_COMMITS in past 7 days"
    echo -e "Potentially stale:$WARNINGS"
    echo ""
fi

# Check for uncommitted changes
if ! git diff --quiet 2>/dev/null || ! git diff --cached --quiet 2>/dev/null; then
    UNCOMMITTED=$(git status --short 2>/dev/null | wc -l | tr -d ' ')
    echo "⚠️  $UNCOMMITTED uncommitted change(s) - consider committing before ending"
fi

# Check for unpushed commits
UNPUSHED=$(git log origin/master..HEAD --oneline 2>/dev/null | wc -l | tr -d ' ')
if [ "$UNPUSHED" -gt 0 ]; then
    echo "⚠️  $UNPUSHED unpushed commit(s) - consider: git push origin master"
fi

exit 0  # Non-blocking reminder
