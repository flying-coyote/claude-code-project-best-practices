# Secure Code Generation

**Sources**:
- [CoSAI Project CodeGuard](https://github.com/cosai-oasis/project-codeguard) (Evidence Tier A)
- [Cisco Blog: CodeGuard Donation to CoSAI](https://blogs.cisco.com/ai/cisco-donates-project-codeguard-to-the-coalition-for-secure-ai) (Evidence Tier A)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/) (Evidence Tier A)

**Evidence Tier**: A (Industry consortium — Anthropic, Google, OpenAI, Microsoft, NVIDIA are CoSAI members)

**SDD Phase**: Cross-phase (security applies to all phases)

## The Core Problem

AI coding agents generate vulnerable code at machine speed. Hardcoded secrets, weak cryptography, missing input validation, SQL injection — all produced as effortlessly as correct code. Traditional post-hoc security review can't keep pace with AI-generated output volume.

**The gap**: Most Claude Code security guidance (sandboxing, permissions, hooks) focuses on securing *the agent itself*. This pattern addresses securing *the code the agent generates*.

---

## The CodeGuard Approach

[Project CodeGuard](https://github.com/cosai-oasis/project-codeguard) is an open-source, model-agnostic framework from the Coalition for Secure AI (CoSAI) that embeds security rules directly into AI coding workflows. Rather than catching vulnerabilities after code is written, security rules guide the AI to generate secure code from the start.

### How It Works

```
┌─────────────────────────────────────────────────┐
│ Pre-Generation (Specify/Plan)                   │
│ Security rules loaded as persistent context     │
│ → Agent understands security constraints        │
├─────────────────────────────────────────────────┤
│ During Generation (Implement)                   │
│ Rules actively guide code generation            │
│ → Parameterized queries, not string concat      │
│ → Env vars, not hardcoded secrets               │
│ → Modern crypto, not deprecated algorithms      │
├─────────────────────────────────────────────────┤
│ Post-Generation (Verification)                  │
│ Rules enable security-aware review              │
│ → Hook-based credential scanning                │
│ → Automated security checks                     │
└─────────────────────────────────────────────────┘
```

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

## Integration with Claude Code

### Option A: CLAUDE.md Rules (Simplest)

Add the 3 mandatory rules directly to your project's CLAUDE.md:

```markdown
## Security Rules (Always Active)

### Never Hardcode Credentials
- Never embed secrets, API keys, tokens, or passwords in source code
- Use environment variables, secrets managers, or config files excluded from git
- Detect patterns: AKIA* (AWS), sk_live_* (Stripe), ghp_* (GitHub), eyJ* (JWT)

### Use Modern Cryptography Only
- AES-256-GCM or ChaCha20-Poly1305 for symmetric encryption
- RSA-OAEP (2048+ bit) or ECDSA (P-256+) for asymmetric
- Argon2id, scrypt, or bcrypt (cost 10+) for password hashing
- Never: MD5, SHA1, DES, 3DES, RC4, ECB mode

### Input Validation at Trust Boundaries
- Use parameterized queries for all database access (never concatenate)
- Validate with allow-lists, not deny-lists
- Escape output context-specifically (HTML, SQL, shell)
```

**Tradeoff**: Minimal setup, but limited coverage. Good for small projects.

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

**SKILL.md**:
```yaml
---
name: secure-coding
description: >
  Enforce secure coding practices for all generated code.
  Prevents hardcoded credentials, weak cryptography, and
  injection vulnerabilities.
---
```

```markdown
# Secure Coding Standards

Apply these rules to ALL generated code. These are non-negotiable.

## Mandatory Rules (Always Apply)

1. **Credentials**: See rules/credentials.md
2. **Cryptography**: See rules/crypto.md
3. **Input Validation**: See rules/validation.md

## When Generating Database Code
- Always use parameterized queries
- Never concatenate user input into SQL strings
- Grant least-privilege database access

## When Generating Authentication Code
- Use slow, memory-hard password hashing (Argon2id preferred)
- Return generic error messages ("Invalid credentials")
- Enforce TLS for all auth endpoints

## When Generating API Endpoints
- Validate all inputs at trust boundaries
- Apply rate limiting
- Use allow-list validation, not deny-list
```

**Tradeoff**: Balanced coverage with progressive disclosure. Recommended for most projects.

### Option C: Full CodeGuard Plugin (Comprehensive)

Install the CodeGuard plugin which bundles all 23 rules:

```bash
# Clone CodeGuard and symlink as a plugin
git clone https://github.com/cosai-oasis/project-codeguard.git
# Follow CodeGuard's Claude Code integration instructions
```

CodeGuard includes a `.claude-plugin/` directory with pre-configured rules that convert to Claude Code's skill format automatically.

**Tradeoff**: Maximum coverage but higher context token cost. Best for security-sensitive projects.

---

## 3 Mandatory Rules (Always Active)

These rules apply to every project regardless of integration method.

### Rule 1: Never Hardcode Credentials

**Why**: AI agents readily generate code with embedded secrets. Once committed, secrets are in git history forever.

**Detection Patterns**:

| Service | Pattern | Example |
|---------|---------|---------|
| AWS | `AKIA*`, `ASIA*` | `AKIAIOSFODNN7EXAMPLE` |
| Stripe | `sk_live_*`, `pk_live_*` | `sk_live_51J...` |
| GitHub | `ghp_*`, `gho_*`, `ghs_*` | `ghp_xxxxxxxxxxxx` |
| JWT | `eyJ*` (3 base64 segments) | `eyJhbGciOiJIUzI1...` |
| Private Keys | `-----BEGIN * PRIVATE KEY-----` | RSA/EC private keys |
| Generic | Variable names with `password`, `secret`, `token`, `key` | `API_SECRET = "..."` |

**Correct Pattern**:
```python
# WRONG - hardcoded credential
API_KEY = "sk_live_EXAMPLE_PLACEHOLDER_NOT_A_REAL_KEY"

# RIGHT - environment variable
API_KEY = os.environ["STRIPE_API_KEY"]

# RIGHT - secrets manager
API_KEY = secrets_client.get_secret("stripe-api-key")
```

### Rule 2: Use Modern Cryptography Only

**Secure Choices**:

| Purpose | Use | Never Use |
|---------|-----|-----------|
| Symmetric encryption | AES-256-GCM, ChaCha20-Poly1305 | DES, 3DES, RC4, AES-ECB |
| Hashing (integrity) | SHA-256, SHA-384, SHA-512, BLAKE3 | MD5, SHA-1 |
| Password hashing | Argon2id, scrypt, bcrypt (cost 10+) | MD5, SHA-*, PBKDF2 (<600K iter) |
| Asymmetric | RSA-OAEP (2048+), ECDSA P-256+ | RSA-1024, DSA |
| Key exchange | X25519, ECDH P-256+ | Static DH |
| Random | `secrets` module, `/dev/urandom`, CSPRNG | `random`, `Math.random()` |

### Rule 3: Validate Input at Trust Boundaries

**Core Principle**: Treat all untrusted input as data, never code.

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

### Rules

1. **Use lockfiles** — Generate `package-lock.json`, `Pipfile.lock`, `Cargo.lock` alongside dependency files
2. **Use deterministic installs** — `npm ci` not `npm install` in CI/CD
3. **Pin versions** — Exact versions, not ranges, for production
4. **Minimize dependencies** — Prefer standard library solutions over third-party packages
5. **Verify packages exist** — AI can hallucinate package names (typosquatting risk)

### Configuration

Add to CLAUDE.md:
```markdown
## Dependency Rules
- Pin exact versions in dependency files (no ^ or ~ ranges for production)
- Use lockfiles for all package managers
- Prefer standard library over third-party when reasonable
- Verify package names exist before adding (avoid hallucinated packages)
```

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
        echo "🛑 Potential hardcoded credential detected (pattern: $PATTERN)"
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

## SDD Phase Mapping

| SDD Phase | Security Application | CodeGuard Alignment |
|-----------|---------------------|---------------------|
| **Specify** | Define security requirements in specs; list allowed crypto, auth patterns | Pre-generation rules |
| **Plan** | Include security constraints in architecture; threat model | Pre-generation rules |
| **Tasks** | Add security verification steps to task breakdowns | Post-generation review |
| **Implement** | CodeGuard rules active during code generation; hook-based scanning | During-generation rules |

---

## MCP Security Extensions

CodeGuard includes an MCP-specific security rule that complements our existing [MCP Patterns](./mcp-patterns.md):

| CodeGuard MCP Addition | Our Existing Coverage |
|------------------------|----------------------|
| SPIFFE/SPIRE workload identity | Not covered — new |
| Transport security (stdio vs HTTP SSE) | Partially covered |
| Tool design (single-purpose, two-stage commits) | Covered in 7 failure modes |
| LLM-generated code sandboxing (gVisor, SELinux) | Covered in safety-and-sandboxing |
| Cryptographic signatures + SBOM for servers | Not covered — new |
| OpenTelemetry observability | Not covered — new |

---

## Anti-Patterns

### 1. Security Rules as Afterthought

**Problem**: Adding security review only after code is generated
**Symptom**: Catch-and-fix cycles, vulnerabilities in production
**Solution**: Embed rules as persistent context so the AI generates secure code by default

### 2. Over-Relying on AI Security Knowledge

**Problem**: Assuming the AI knows current best practices without explicit rules
**Symptom**: Outdated algorithms (MD5, SHA-1), deprecated patterns
**Solution**: Provide explicit rules with approved algorithms and patterns

### 3. Broad Permission Grants to Skip Security

**Problem**: Disabling credential scanning hooks because they "slow things down"
**Symptom**: Secrets in git history, credential exposure
**Solution**: Tune hook patterns to reduce false positives rather than disabling

### 4. Ignoring Supply Chain in Generated Dependencies

**Problem**: Accepting AI-generated `package.json` without verifying packages exist
**Symptom**: Typosquatting attacks, hallucinated package names
**Solution**: Verify packages before installing; pin exact versions; use lockfiles

### 5. One-Size-Fits-All Security Rules

**Problem**: Loading all 23 CodeGuard rules for every project
**Symptom**: Excessive context consumption, irrelevant warnings
**Solution**: Start with the 3 mandatory rules; add domain-specific rules as needed

---

## Related Patterns

- [Safety and Sandboxing](./safety-and-sandboxing.md) — OS-level agent security (complements output-level security)
- [MCP Patterns](./mcp-patterns.md) — MCP-specific security including OWASP Top 10
- [Advanced Hooks](./advanced-hooks.md) — Hook patterns for credential scanning and security gates
- [Plugins and Extensions](./plugins-and-extensions.md) — CodeGuard as a recommended security plugin
- [Skills Domain Knowledge](./skills-domain-knowledge.md) — Embedding security expertise as a skill

---

## Sources

- [Project CodeGuard](https://github.com/cosai-oasis/project-codeguard) (CoSAI/OASIS)
- [Cisco Donates Project CodeGuard to CoSAI](https://blogs.cisco.com/ai/cisco-donates-project-codeguard-to-the-coalition-for-secure-ai) (February 2026)
- [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/)
- [Coalition for Secure AI](https://www.coalitionforsecureai.org/)

*Last updated: February 2026*
