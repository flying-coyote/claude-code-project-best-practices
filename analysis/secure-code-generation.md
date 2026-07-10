---
evidence-tier: A
applies-to-signals: [commit-security-paths]
last-verified: 2026-07-10
revalidate-by: 2026-10-15
status: PRODUCTION
---

# Secure Code Generation

> **Collapsed 2026-07-10 (Reduction Phase 4).** The review workflow went native (bundled security-review skill; official security-guidance plugin v2.1.144+). Kept delta: the CodeGuard rule-import guidance and the commit-security-paths remediation specifics.

**Sources**:
- [CoSAI Project CodeGuard](https://github.com/cosai-oasis/project-codeguard) (Evidence Tier A)
- [Cisco Blog: CodeGuard Donation to CoSAI](https://blogs.cisco.com/ai/cisco-donates-project-codeguard-to-the-coalition-for-secure-ai) (Evidence Tier A)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) (Evidence Tier A)

**Evidence Tier**: A (Industry consortium — Anthropic, Google, OpenAI, Microsoft, NVIDIA are CoSAI members)

## Why This Still Matters

AI coding agents generate vulnerable code at machine speed — hardcoded secrets, weak cryptography, missing input validation, SQL injection — as easily as correct code. Most Claude Code security guidance addresses securing *the agent itself* (sandboxing, permissions, hooks); this pattern addresses securing *the code the agent generates*. The review workflow itself — when a security pass runs, how it fits Specify/Plan/Tasks/Implement, MCP-specific review coverage — now lives in the bundled security-review skill and the security-guidance plugin. What's left here is what that workflow doesn't replace: which rules to import from Project CodeGuard, and the commit-security-paths remediation.

## The CodeGuard Approach

[Project CodeGuard](https://github.com/cosai-oasis/project-codeguard) is an open-source, model-agnostic framework from the Coalition for Secure AI (CoSAI) that embeds security rules directly into AI coding workflows, so the AI generates secure code from the start rather than being caught after the fact. CoSAI's members include Anthropic, Google, OpenAI, Microsoft, and NVIDIA (Evidence Tier A); Cisco donated the original CodeGuard project to CoSAI in February 2026.

### Coverage: 23 Rules Across 8 Domains

| Domain | Rules | Key Concerns |
|--------|-------|-------------|
| **Cryptography** | 3 (mandatory) | Algorithm safety, key management, certificates, post-quantum |
| **Input Validation** | 1 | SQL/LDAP/OS injection, XSS, prototype pollution |
| **Authentication** | 1 | MFA, OAuth 2.0/OIDC, password hashing, token management |
| **Authorization** | 1 | RBAC/ABAC, IDOR prevention, least privilege |
| **Supply Chain** | 1 | Dependency management, lockfiles, SBOM, artifact signing |
| **Cloud Security** | 2 | IaC hardening, Kubernetes, container security |
| **Platform Security** | 3 | Mobile, client-side web, APIs, frameworks |
| **Data Protection** | 2 | Privacy, encryption at rest/transit, logging, sessions |

Plus specialized rules for MCP security, DevOps/CI/CD, file handling, XML/serialization, and safe C functions.

---

## Importing CodeGuard Rules into a Project

Three ways to bring CodeGuard rules into Claude Code, in order of setup cost.

### Option A: CLAUDE.md Rules (Simplest)

Paste the 3 mandatory rules (credentials, cryptography, input validation — full text under "commit-security-paths Remediation" below) directly into your project's CLAUDE.md under a `## Security Rules (Always Active)` heading. Minimal setup, but limited coverage. Good for small projects.

### Option B: Skills Directory (Recommended)

Create a security skill that Claude Code loads automatically:

```
.claude/skills/secure-coding/
├── SKILL.md              # Security skill with routing
└── rules/
    ├── credentials.md    # Hardcoded credential prevention
    ├── crypto.md         # Cryptographic algorithm standards
    └── validation.md     # Input validation patterns
```

SKILL.md needs only a `name` and a `description` (what it prevents: hardcoded credentials, weak cryptography, injection) — Claude Code loads the routing, the `rules/` files carry the detail. Balanced coverage with progressive disclosure. Recommended for most projects.

### Option C: Full CodeGuard Plugin (Comprehensive)

Install the CodeGuard plugin, which bundles all 23 rules and ships a `.claude-plugin/` directory that converts to Claude Code's skill format automatically:

```bash
git clone https://github.com/cosai-oasis/project-codeguard.git
# Follow CodeGuard's Claude Code integration instructions
```

Maximum coverage but higher context token cost. Best for security-sensitive projects.

---

## commit-security-paths Remediation: 3 Mandatory Rules

These rules apply regardless of which import option above is in use.

### Rule 1: Never Hardcode Credentials

**Why**: AI agents readily generate code with embedded secrets. Once committed, secrets are in git history forever.

**Detection Patterns**:

| Service | Pattern | Example |
|---------|---------|---------|
| AWS | `AKIA*`, `ASIA*` | `AKIAIOSFODNN7...` (AWS's own example format) |
| Stripe | `sk_live_*`, `pk_live_*` | `sk_live_51J...` |
| GitHub | `ghp_*`, `gho_*`, `ghs_*` | `ghp_xxxxxxxxxxxx` |
| JWT | `eyJ*` (3 base64 segments) | `eyJhbGciOiJIUzI1...` |
| Private Keys | `-----BEGIN * PRIVATE KEY-----` | RSA/EC private keys |
| Generic | Variable names with `password`, `secret`, `token`, `key` | fake value assigned in quotes |

```python
# WRONG - hardcoded credential
API_KEY = "sk_live_FAKE_EXAMPLE_NOT_REAL"

# RIGHT - environment variable
API_KEY = os.environ["STRIPE_API_KEY"]

# RIGHT - secrets manager
API_KEY = secrets_client.get_secret("stripe-api-key")
```

### Rule 2: Use Modern Cryptography Only

| Purpose | Use | Never Use |
|---------|-----|-----------|
| Symmetric encryption | AES-256-GCM, ChaCha20-Poly1305 | DES, 3DES, RC4, AES-ECB |
| Hashing (integrity) | SHA-256, SHA-384, SHA-512, BLAKE3 | MD5, SHA-1 |
| Password hashing | Argon2id, scrypt, bcrypt (cost 10+) | MD5, SHA-*, PBKDF2 (<600K iter) |
| Asymmetric | RSA-OAEP (2048+), ECDSA P-256+ | RSA-1024, DSA |
| Key exchange | X25519, ECDH P-256+ | Static DH |
| Random | `secrets` module, `/dev/urandom`, CSPRNG | `random`, `Math.random()` |

### Rule 3: Validate Input at Trust Boundaries

Treat all untrusted input as data, never code.

```python
# WRONG - SQL injection
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# RIGHT - parameterized query
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

```python
# WRONG - OS command injection
os.system(f"convert {filename} output.png")

# RIGHT - structured execution, no shell
subprocess.run(["convert", filename, "output.png"], shell=False)
```

```python
# WRONG - path traversal
path = os.path.join(base_dir, user_supplied_path)

# RIGHT - canonicalize and validate
path = os.path.realpath(os.path.join(base_dir, user_supplied_path))
if not path.startswith(os.path.realpath(base_dir)):
    raise ValueError("Path traversal detected")
```

---

## Supply Chain Security for AI-Generated Dependencies

When Claude Code generates dependency files (`package.json`, `requirements.txt`, `Cargo.toml`, `go.mod`), additional risks emerge:

1. **Use lockfiles** — Generate `package-lock.json`, `Pipfile.lock`, `Cargo.lock` alongside dependency files
2. **Use deterministic installs** — `npm ci` not `npm install` in CI/CD
3. **Pin versions** — Exact versions, not ranges, for production
4. **Minimize dependencies** — Prefer standard library solutions over third-party packages
5. **Verify packages exist** — AI can hallucinate package names (typosquatting risk)

Add to CLAUDE.md:
```markdown
## Dependency Rules
- Pin exact versions in dependency files (no ^ or ~ ranges for production)
- Use lockfiles for all package managers
- Prefer standard library over third-party when reasonable
- Verify package names exist before adding (avoid hallucinated packages)
```

### Necessity before custom logic (the over-generation failure mode)

Coding agents default to writing custom logic even when the standard library, a native runtime feature, or an already-installed dependency does the job, and they re-implement utilities the codebase already has (see [Domain Knowledge Architecture](domain-knowledge-architecture.md), "reinvents solutions instead of reusing"). The dependency rules above are the security-framed slice of a wider discipline: before accepting agent-written code, walk a necessity ladder — does this need to exist at all → standard library → native platform feature → existing project dependency → a clean one-liner → custom logic only as a last resort, kept minimal. Generalizing the supply-chain rules to *over-generation* closes a quieter cost than typosquatting: dead custom code that has to be read, tested, and maintained forever.

Put it in CLAUDE.md as **advisory** guidance, not as `MUST`/`NEVER` — emphatic syntax on advisory rules gets literalized into hard caps on Opus 4.7/4.8 (see [Model Migration Anti-Patterns](model-migration-anti-patterns.md)):

```markdown
## Implementation discipline
- Before writing custom logic, check: stdlib -> native platform -> existing dependency -> one-liner. Custom code is the last resort, kept minimal.
- Prefer a single source of truth over duplicated maps/config/styles.
```

**Evidence tier**: C — practitioner heuristic, attached to the Tier-A/B claims it rests on (Sutton's Bitter Lesson "built for deletion" and the tool-ablation results in [Harness Engineering](harness-engineering.md); the "reinvents instead of reusing" symptom documented at Tier B in [Domain Knowledge Architecture](domain-knowledge-architecture.md)). There is no clean filesystem signal for over-generation — it is a discipline applied during generation, not an artifact on disk — so it lives as guidance under an existing signal, not as its own audit row.

---

## Hook-Based Credential Scanning

Use a PreToolUse hook to catch hardcoded credentials before they're written:

`.claude/hooks/pre-tool-use-credential-scan.sh`:
```bash
#!/bin/bash
# Scan for hardcoded credentials in generated code

read -r input
TOOL=$(echo "$input" | jq -r '.tool // "unknown"')

# Only check Write and Edit operations
if [ "$TOOL" != "Write" ] && [ "$TOOL" != "Edit" ]; then
    exit 0
fi

CONTENT=$(echo "$input" | jq -r '.parameters.content // .parameters.new_string // ""')

# Check for common credential patterns
PATTERNS=(
    'AKIA[0-9A-Z]{16}'                    # AWS access key
    'sk_live_[0-9a-zA-Z]{24,}'            # Stripe secret key
    'ghp_[0-9a-zA-Z]{36}'                 # GitHub personal access token
    'gho_[0-9a-zA-Z]{36}'                 # GitHub OAuth token
    '-----BEGIN.*PRIVATE KEY-----'         # Private keys
    'sk-[0-9a-zA-Z]{48}'                  # OpenAI API key
    'xox[bpors]-[0-9a-zA-Z-]{10,}'       # Slack tokens
)

for PATTERN in "${PATTERNS[@]}"; do
    if echo "$CONTENT" | grep -qP "$PATTERN"; then
        echo "Potential hardcoded credential detected (pattern: $PATTERN)"
        echo "Use environment variables or a secrets manager instead."
        exit 2  # Block the operation
    fi
done

exit 0  # Allow
```

**Configuration**:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/pre-tool-use-credential-scan.sh"
          }
        ]
      }
    ]
  }
}
```

---

## Related Patterns

- [Safety and Sandboxing](./safety-and-sandboxing.md) — OS-level agent security (complements output-level security)
- [MCP Patterns](./mcp-patterns.md) — MCP-specific security including OWASP Top 10

---

## Sources

- [Project CodeGuard](https://github.com/cosai-oasis/project-codeguard) (CoSAI/OASIS)
- [Cisco Donates Project CodeGuard to CoSAI](https://blogs.cisco.com/ai/cisco-donates-project-codeguard-to-the-coalition-for-secure-ai) (February 2026)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- [Coalition for Secure AI](https://www.coalitionforsecureai.org/)

*Last updated: July 2026*
