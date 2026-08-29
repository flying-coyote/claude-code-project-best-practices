#!/bin/bash
# .claude/hooks/post-tool-use.sh
# PostToolUse hook (settings.json matcher: "Write|Bash|NotebookEdit").
# Keeps INDEX.md in sync with the markdown inventory by re-running
# automation/generate_index.py after every matched tool call.
#
# Rewritten 2026-08-29. The previous version parsed a payload schema Claude Code
# does not send: it read `.tool` and `.parameters.*`, where the real payload
# carries `tool_name` and `tool_input.*` (first-party docs, and the schema
# analysis/safety-and-sandboxing.md already documented correctly). So TOOL was
# always "unknown", every branch that discriminated on it was dead, and the case
# statement fell through to an unconditional regenerate. It "worked" only by
# accident, through its own fallback arm.
#
# There is deliberately NO "did this call change the file structure?" test now.
# Restoring one would be worse than deleting it:
#
#   - Structure-changing Bash is unbounded — heredocs, `>` redirection, `git mv`,
#     `git checkout`, any script this repo runs — so no prefix allowlist can
#     enumerate it, and each command it fails to recognise is a silently stale
#     INDEX.md that no check catches.
#   - generate_index.py IS the exact check, and a cheap one: measured 34 ms on
#     this corpus, and it rewrites INDEX.md only when the inventory actually
#     differs (verified: consecutive runs leave the file byte-identical).
#     Guessing in front of an exact, idempotent check buys 34 ms and can only be
#     wrong.
#
# Code formatting used to live here too (prettier/black/gofmt/rustfmt on
# Write|Edit). Removed rather than repaired, because repairing it would have been
# the harmful option: it had never executed once (same parsing bug), yet all four
# formatters ARE on PATH here, so correcting the schema alone would have switched
# it on. This repo holds 0 .go and 0 .rs files, its markdown is linted by
# markdownlint-cli2 instead, and 17 of the 32 .py/.json/.js targets outside
# archive/ sit under research/artifacts/ — frozen measurement evidence that must
# not be reformatted to whatever formatter version happens to be installed.
# It was a latent hazard, not a dormant feature.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$PROJECT_ROOT" || exit 0

# Drain the JSON payload even though nothing is parsed out of it, so the caller
# is never left writing into a pipe with no reader. `cat`, not `read -r input`:
# credential-scan.sh:17-19 records why — `read` stops at the first newline and
# returns non-zero on a payload with no trailing newline, so the old
# `read -r input || input=""` truncated a pretty-printed payload and discarded a
# compact one outright. The `[ -t 0 ]` guard keeps an interactive debugging run
# from blocking on the terminal.
[ -t 0 ] || cat > /dev/null

[ -f "automation/generate_index.py" ] || exit 0

OLD_HASH=$(md5sum INDEX.md 2>/dev/null | cut -d' ' -f1)
python3 automation/generate_index.py > /dev/null 2>&1
NEW_HASH=$(md5sum INDEX.md 2>/dev/null | cut -d' ' -f1)

if [ "$OLD_HASH" != "$NEW_HASH" ]; then
    echo "INDEX.md automatically regenerated"
fi

exit 0  # Non-blocking: this hook never fails a tool call.
