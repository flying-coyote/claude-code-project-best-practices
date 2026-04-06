#!/bin/bash
# .claude/hooks/pre-commit-lint.sh
#
# Hook: runs before git commit to catch style issues.
# Configure in .claude/settings.json:
#   "hooks": { "pre-commit": [".claude/hooks/pre-commit-lint.sh"] }
#
# Customize the lint command for your project.

set -e

# Python projects
# python -m ruff check --fix .
# python -m ruff format .

# Node/TypeScript projects
# npx eslint --fix .
# npx prettier --write .

# Go projects
# go fmt ./...
# go vet ./...

echo "Pre-commit lint passed."
