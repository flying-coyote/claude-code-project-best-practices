#!/bin/bash
# .claude/hooks/post-edit-test.sh
#
# Hook: runs after Claude edits a file to catch regressions early.
# Configure in .claude/settings.json:
#   "hooks": { "post-tool-use": { "Edit": [".claude/hooks/post-edit-test.sh"] } }
#
# This is optional and can slow down the workflow — use for critical code paths.
# Consider restricting to specific directories.

set -e

EDITED_FILE="$1"

# Run tests related to the edited file
# Python: run tests matching the module name
# MODULE=$(basename "$EDITED_FILE" .py)
# python -m pytest tests/ -k "$MODULE" --tb=short -q 2>/dev/null || true

# Node: run tests matching the file name
# BASENAME=$(basename "$EDITED_FILE" .ts)
# npx jest --testPathPattern="$BASENAME" --silent 2>/dev/null || true

echo "Post-edit check complete."
