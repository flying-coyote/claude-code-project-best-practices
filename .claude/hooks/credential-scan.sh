#!/bin/bash
# PreToolUse hook: Block writes containing hardcoded credentials
# Matches: Bash, Write, Edit tools
# Based on CodeGuard mandatory rule #1 (secure-code-generation.md)
# No jq dependency — scans raw JSON input with grep

read -r input

[ -z "$input" ] && exit 0

# Credential patterns (OWASP / CodeGuard)
FOUND=""

# AWS Access Keys (20-char alphanumeric after AKIA/ASIA prefix)
if echo "$input" | grep -qE '(AKIA|ASIA)[A-Z0-9]{16}'; then
  FOUND="AWS Access Key"
fi

# Stripe keys
if echo "$input" | grep -qE 'sk_live_[a-zA-Z0-9]{20,}'; then
  FOUND="${FOUND:+$FOUND, }Stripe Secret Key"
fi
if echo "$input" | grep -qE 'pk_live_[a-zA-Z0-9]{20,}'; then
  FOUND="${FOUND:+$FOUND, }Stripe Publishable Key"
fi

# GitHub tokens
if echo "$input" | grep -qE 'gh[ps]_[a-zA-Z0-9]{36,}'; then
  FOUND="${FOUND:+$FOUND, }GitHub Token"
fi

# Private keys
if echo "$input" | grep -qE 'BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY'; then
  FOUND="${FOUND:+$FOUND, }Private Key"
fi

# Google API keys
if echo "$input" | grep -qE 'AIza[a-zA-Z0-9_-]{35}'; then
  FOUND="${FOUND:+$FOUND, }Google API Key"
fi

# Slack tokens
if echo "$input" | grep -qE 'xox[bpras]-[a-zA-Z0-9-]{10,}'; then
  FOUND="${FOUND:+$FOUND, }Slack Token"
fi

# Generic high-entropy secrets in assignment patterns
if echo "$input" | grep -qiE '(api_key|api_secret|access_token|secret_key)["\x27]*\s*[=:]\s*["\x27][a-zA-Z0-9+/=_-]{32,}["\x27]'; then
  FOUND="${FOUND:+$FOUND, }Possible API Key/Secret"
fi

if [ -n "$FOUND" ]; then
  echo "BLOCKED: Potential hardcoded credential detected: $FOUND"
  echo ""
  echo "Use environment variables or a secrets manager instead:"
  echo "  export SECRET_NAME=value  # in shell"
  echo "  os.environ['SECRET_NAME']  # in Python"
  echo "  process.env.SECRET_NAME  # in Node.js"
  exit 2
fi

exit 0
