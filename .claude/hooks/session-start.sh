#!/bin/bash

# Session Start Hook for claude-code-project-best-practices
# Displays project context and git status at the start of each session

echo "📊 Claude Code Best Practices — Analytical Layer"
echo "=========================================="
echo ""

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "⚠️  Not in a git repository"
    exit 0
fi

# Current branch
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
echo "📍 Branch: $BRANCH"
echo ""

# Git status summary
STAGED=$(git diff --cached --numstat | wc -l | tr -d ' ')
MODIFIED=$(git diff --numstat | wc -l | tr -d ' ')
UNTRACKED=$(git ls-files --others --exclude-standard | wc -l | tr -d ' ')

echo "📊 Status:"
echo "   Staged files: $STAGED"
echo "   Modified files: $MODIFIED"
echo "   Untracked files: $UNTRACKED"
echo ""

# Content summary
ANALYSIS_COUNT=$(ls -1 analysis/*.md 2>/dev/null | wc -l | tr -d ' ')
echo "📚 Content: $ANALYSIS_COUNT analysis documents"
echo ""

# Recent file changes
if [ "$MODIFIED" -gt 0 ] || [ "$STAGED" -gt 0 ]; then
    echo "📝 Recent Changes:"
    git status --short | head -10
    echo ""
fi

# Recent commits
COMMIT_COUNT=$(git rev-list --count HEAD 2>/dev/null || echo "0")
echo "📈 Repository: $COMMIT_COUNT commits"
echo ""

if [ "$COMMIT_COUNT" -gt 0 ]; then
    echo "🕒 Recent Commits:"
    git log --oneline --decorate --max-count=5
    echo ""
fi

echo "Phase: v2.1 — Production Evidence Integration"
echo "=========================================="
