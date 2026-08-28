#!/bin/bash
# PreToolUse hook: guard against committing live credentials (Bash, Write, Edit).
# Based on CodeGuard mandatory rule #1 (secure-code-generation.md). No jq dependency.
#
# Two deliberate tiers (this is the clarified hard-block):
#
#   HARD BLOCK  (exit 2): unambiguous live-secret FORMATS — AWS / Stripe / GitHub /
#     Slack / Google keys and PEM private keys. These carry distinctive prefixes, so
#     false positives are near-zero and a real hit is high-impact. The tool call is
#     stopped and the reason is returned to the model.
#
#   ADVISORY    (exit 0 + warning): the single generic "secret-ish assignment"
#     heuristic, which fires on ANY 32+ char value assigned to a field named
#     api_key / secret / token. It false-positives on hashes, IDs, and documented
#     examples, so it WARNS and lets the call proceed rather than killing the turn.

# Read the ENTIRE stdin payload, not just the first line. `read -r input` stops at
# the first newline, so a secret sitting on line 2+ of a multi-line Write/Edit body
# would slip past every grep below and leak through the hard block. `cat` slurps it all.
input=$(cat)

[ -z "$input" ] && exit 0

# ── Tier 1: unambiguous live-secret formats → HARD BLOCK ──────────────────────
HARD=""
add_hard() { HARD="${HARD:+$HARD, }$1"; }

echo "$input" | grep -qE '(AKIA|ASIA)[A-Z0-9]{16}'                 && add_hard "AWS Access Key"
echo "$input" | grep -qE 'sk_live_[a-zA-Z0-9]{20,}'               && add_hard "Stripe Secret Key"
echo "$input" | grep -qE 'pk_live_[a-zA-Z0-9]{20,}'               && add_hard "Stripe Publishable Key"
echo "$input" | grep -qE 'gh[ps]_[a-zA-Z0-9]{36,}'                && add_hard "GitHub Token"
echo "$input" | grep -qE 'BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY' && add_hard "Private Key"
echo "$input" | grep -qE 'AIza[a-zA-Z0-9_-]{35}'                  && add_hard "Google API Key"
echo "$input" | grep -qE 'xox[bpras]-[a-zA-Z0-9-]{10,}'           && add_hard "Slack Token"

if [ -n "$HARD" ]; then
  echo "BLOCKED — live secret format detected: $HARD"
  echo ""
  echo "This is a HARD block: the value matches a real credential format."
  echo "Use an environment variable or a secrets manager instead:"
  echo "  export SECRET_NAME=value        # shell"
  echo "  os.environ['SECRET_NAME']       # Python"
  echo "  process.env.SECRET_NAME         # Node.js"
  echo "If this is a documented placeholder, redact the realistic-looking value first."
  exit 2
fi

# ── Tier 2: generic high-entropy assignment → ADVISORY (warn, do not block) ───
if echo "$input" | grep -qiE '(api_key|api_secret|access_token|secret_key)["\x27]*\s*[=:]\s*["\x27][a-zA-Z0-9+/=_-]{32,}["\x27]'; then
  echo "NOTE (cred-scan heuristic): a 32+ char value is assigned to a secret-named field."
  echo "Allowed — this check is ADVISORY (it false-positives on hashes, IDs, and examples)."
  echo "If it is in fact a live secret, move it to an environment variable."
fi

exit 0
