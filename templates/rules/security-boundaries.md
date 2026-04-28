<!-- .claude/rules/security-boundaries.md
     Critical for repos handling credentials, PII, or customer data.
     Load this globally (no path restriction) via settings. -->

# Security Boundaries

## Never Commit
- `.env` files, API keys, tokens, passwords, certificates
- Customer data, PII, or data that could identify individuals
- Hardcoded credentials (use environment variables)

## Data Handling
<!-- Customize for your domain -->
- {{PII rule: e.g., "All customer identifiers must be tokenized before LLM processing"}}
- {{Data classification: e.g., "Production data never leaves the secure environment"}}
- {{Logging rule: e.g., "Never log request bodies that may contain credentials"}}

## External Services
- {{API rule: e.g., "All external API calls must use the client in lib/api_client.py"}}
- {{Auth rule: e.g., "OAuth tokens are managed by the auth middleware, never manually"}}
