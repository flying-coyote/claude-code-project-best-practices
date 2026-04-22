# Audit Context: Signal → Advisory Routing Map

**Purpose**: This file is fetched by the [adaptive routing audit prompt](ONE-LINE-PROMPT.md) to route other projects to the analysis docs that apply to what they actually have, not all 28 at once. Each row states a verifiable signal, the docs to fetch, and the reason for the fetch.

**Design principles**:

- Routing is **inclusive** (multiple signals can trigger overlapping fetches) but **deduplicated** (fetch each doc only once even if multiple signals match).
- Signals are phrased as **observable facts** an agent can verify with a concrete command — not subjective judgments.
- **Always Fetch** rows fetch unconditionally, regardless of observed signals. They are non-negotiable baselines.
- Every analysis doc has a machine-readable `applies-to-signals` frontmatter field using the **signal vocabulary** in the rightmost column below. Routing rows and doc frontmatter must stay in sync.

**Evidence-tier reminder**: Tier A = Anthropic / primary observation. Tier B = expert practitioner / production validation. Tier C = community. See [analysis/evidence-tiers.md](analysis/evidence-tiers.md). Authority-weighted source list: [SOURCES-QUICK-REFERENCE.md](SOURCES-QUICK-REFERENCE.md).

---

## Signal Collection Commands (run before routing)

The audit prompt collects these signals. Each routing row below is phrased to match one or more of these outputs:

```bash
# Project identity and layout
ls -la .claude/ 2>/dev/null
ls -la .claude/hooks/ .claude/rules/ .claude/skills/ .claude/agents/ .claude/commands/ 2>/dev/null
cat .claude/settings.json 2>/dev/null

# CLAUDE.md state
wc -l CLAUDE.md .claude/CLAUDE.md 2>/dev/null
grep -nEi "\b(best practices|idiomatic|robust|proper|clean code)\b" CLAUDE.md .claude/CLAUDE.md 2>/dev/null
grep -nEi "\b(where applicable|as needed|if relevant|consider edge cases)\b" CLAUDE.md .claude/CLAUDE.md 2>/dev/null
grep -nE "see (rules/|\.claude/|[A-Z])" CLAUDE.md .claude/CLAUDE.md 2>/dev/null

# Model version detection
grep -REi "opus-4-?[567]|sonnet-4-?[567]|claude-[0-9]" .claude/settings.json .github/workflows/ 2>/dev/null

# Commit patterns (assumes git repo)
git log --since="90 days ago" --oneline 2>/dev/null | wc -l
git log --since="90 days ago" --pretty=format:'%s' 2>/dev/null | grep -cE "(Claude|claude|Co-Authored)"

# Session diagnostics
npx -y claude-doctor 2>/dev/null
```

**Edge cases handled explicitly in the prompt**: no `.claude/` → treat as "no harness" signal; no git → skip commit-pattern rows; `settings.json` without model field → "model unknown" signal; `claude-doctor` unavailable → skip session rows.

---

## Always Fetch (every audit, signal-independent)

| Fetch | Signal key | Why |
|---|---|---|
| `analysis/evidence-tiers.md` | `audit-always-fetch` | You need the tier definitions to cite recommendations correctly. |
| `analysis/behavioral-insights.md` | `audit-always-fetch` | Quantified behavioral thresholds (80% CLAUDE.md adherence, 60% context quality threshold, prompt-sensitivity table across model versions) apply to every project. |
| `analysis/evidence-based-revalidation.md` | `audit-always-fetch` | Every claim has a half-life; any audit should surface stale-claim risk. |

## Fetch on Model Version Signal

| Signal (verifiable) | Signal key | Fetch | Why |
|---|---|---|---|
| `settings.json` or recent config references `opus-4-7` or `claude-opus-4-7` | `model-version-4-7` | `analysis/model-migration-anti-patterns.md` | Six prompt anti-patterns that silently no-op on 4.7. Audit CLAUDE.md/skills for vague descriptors, edge-case gestures, unanchored triggers, implicit subagent dispatch, missing verbosity directives, references without read-enforcement. |
| References `opus-4-6` with no 4.7 reference | `model-version-4-6` | `analysis/model-migration-anti-patterns.md` | Open revalidation trigger before upgrade. |
| References `opus-4-5` with no 4.6/4.7 reference | `model-version-4-5` | `analysis/model-migration-anti-patterns.md` | Two-version gap; compound revalidation risk. |
| Mixed versions across agents / settings / CI | `model-version-migration` | `analysis/model-migration-anti-patterns.md` + `analysis/evidence-based-revalidation.md` | Cross-version matrix; revalidation trigger. |
| No model field found anywhere | `model-version-unknown` | `analysis/model-migration-anti-patterns.md` | Default-model behavior shifts across releases; doc surfaces latest defaults. |

## Fetch on CLAUDE.md Signal

| Signal (verifiable) | Signal key | Fetch | Why |
|---|---|---|---|
| `wc -l` of CLAUDE.md > 150 | `claude-md-size` | `analysis/claude-md-progressive-disclosure.md` | ~150 instruction budget is a convergent behavioral boundary; progressive disclosure is the remediation. |
| `grep -nE "see (rules/\|\\.claude/\|[A-Z])"` returns matches in CLAUDE.md | `claude-md-references` | `analysis/claude-md-progressive-disclosure.md` | 4.7 no longer infers that referenced files should be read. Mechanical enforcement (PreToolUse hook, explicit Read step, inline block) required. |
| No CLAUDE.md found at root or in `.claude/` | `claude-md-missing` | `analysis/claude-md-progressive-disclosure.md` | 3-tier evolution model provides a calibrated starting point. |
| `grep -nEi "\b(best practices\|idiomatic\|robust\|proper\|clean code)\b"` matches in CLAUDE.md | `claude-md-vague-descriptors` | `analysis/model-migration-anti-patterns.md` | Anti-pattern #1 — silent no-ops on 4.7. |

## Fetch on Harness Layout

| Signal (verifiable) | Signal key | Fetch | Why |
|---|---|---|---|
| `.claude/hooks/` directory present | `harness-hooks` | `analysis/harness-engineering.md` + `analysis/safety-and-sandboxing.md` | Hook-based enforcement is the 100%-adherence boundary; sandboxing is the defense-in-depth layer. |
| `ls .claude/skills/ \| wc -l` returns >5 | `harness-skills` | `analysis/plugins-and-extensions.md` + `analysis/mcp-vs-skills-economics.md` | Skills use ~2% context each; economics comparison applies at this scale. |
| `.claude/agents/` contains one or more `.md` files | `harness-custom-agents` | `analysis/agent-principles.md` + `analysis/orchestration-comparison.md` + `analysis/agent-evaluation.md` | Custom-subagent gatekeeping is a documented anti-pattern; 4.7 spawns fewer subagents by default. |
| `settings.json` has `mcpServers` key with ≥1 entry | `harness-mcp` | `analysis/mcp-patterns.md` + `analysis/mcp-daily-essentials.md` + `analysis/mcp-client-integration.md` | MCP context budget, OWASP failure modes, 4-plugin + 2-MCP sweet spot. |
| Only CLAUDE.md exists; no hooks/skills/agents/rules/commands | `harness-minimal` | `analysis/harness-engineering.md` | Start-minimal decision tree; when to add each mechanism. |
| ≥4 of {hooks, skills, agents, rules, commands} directories present | `harness-comprehensive` | `analysis/harness-engineering.md` + `analysis/framework-selection-guide.md` | Bitter Lesson diagnostic — is the harness buying you anything, or accreting complexity? |

## Fetch on Commit Pattern

| Signal (verifiable) | Signal key | Fetch | Why |
|---|---|---|---|
| Co-authored commits / total commits > 0.5 in period | `commit-ai-coauthoring` | `analysis/agent-driven-development.md` | 7-repo infrastructure maturity model; calibrate expectations against production evidence. |
| Any day with ≥15 commits in period | `commit-bursts` | `analysis/agent-driven-development.md` + `analysis/harness-engineering.md` | Burst patterns signal agent-driven work; harness quality determines sustainability. |
| Commits reference other repos in project portfolio | `commit-cross-repo` | `analysis/cross-project-synchronization.md` | Hub-spoke coordination patterns; dependency cascading. |
| Files matching `customer-data/\|secrets/\|credentials/\|.env` touched | `commit-security-paths` | `analysis/safety-and-sandboxing.md` + `analysis/secure-code-generation.md` | OWASP-aware enforcement, PreToolUse blocking for customer data. |
| Total commits in period < 10 | `commit-low-activity` | Extend window to 365 days before routing. No fetch. | Signal collection retry, not a fetch trigger. |

## Fetch on Session Diagnostic Signal (claude-doctor)

| Signal (verifiable) | Signal key | Fetch | Why |
|---|---|---|---|
| `claude-doctor` produced any output | `session-diagnostics-run` | `analysis/session-quality-tools.md` | Signal reliability hierarchy — act on edit-thrashing and error-loop; treat sentiment as directional only. |
| `edit-thrashing` count > 5 | `session-edit-thrashing` | `analysis/session-quality-tools.md` + `analysis/claude-md-progressive-disclosure.md` | Missing file-pattern knowledge; CLAUDE.md or rules file gap. |
| `error-loop` count > 3 | `session-error-loop` | `analysis/session-quality-tools.md` + `analysis/harness-engineering.md` | No error recovery; harness-level remediation. |
| `repeated-instructions` count > 2 | `session-repeated-instructions` | `analysis/claude-md-progressive-disclosure.md` | The repeated thing belongs in CLAUDE.md. |

## Fetch on Project Type

| Signal (verifiable) | Signal key | Fetch | Why |
|---|---|---|---|
| README mentions "documentation," "knowledge base," or "notes" in title/first paragraph | `project-type-docs` | `analysis/memory-system-patterns.md` + `analysis/claude-md-progressive-disclosure.md` | Auto-memory sizing; progressive disclosure for reference-heavy work. |
| Repo contains `*.parquet`, `*.iceberg`, Zeek / Suricata configs, OCSF mappings | `project-type-data-pipeline` | `analysis/security-data-pipeline.md` + `analysis/federated-query-architecture.md` | Zeek→OCSF patterns; federated vs centralized cost analysis. |
| Repo contains MLX, Ollama, or local-model integration alongside cloud API client | `project-type-hybrid-llm` | `analysis/local-cloud-llm-orchestration.md` | Tokenization boundary, hallucination scrubbing, supply-chain hardening. |
| Repo uses "hypothesis," "H-{label}," or `confidence` tracking in commit messages or files | `project-type-research` | `analysis/evidence-based-revalidation.md` + `analysis/confidence-scoring.md` | Confidence scoring with explicit gap statements; revalidation cadence. |
| Repo contains baseline/deviation/compliance tooling | `project-type-config-assessment` | `analysis/automated-config-assessment.md` | Baseline-deviation-remediation pattern. |
| Commits reference ≥3 sibling repos in the same workspace | `project-type-multi-repo` | `analysis/cross-project-synchronization.md` + `analysis/agent-driven-development.md` | Cross-repo coordination and infrastructure maturity. |
| User explicitly asks "which framework should I use" or repo is pre-scaffold | `project-type-framework-selection` | `analysis/framework-selection-guide.md` + `analysis/tool-ecosystem.md` | Decision matrix; Specification Gap framework. |
| Repo ships its own rule language, DSL, or vendor-specific configs | `project-type-domain-heavy` | `analysis/domain-knowledge-architecture.md` | Making expertise findable without overwhelming context. |

## Fetch on Revalidation Context

| Signal (verifiable) | Signal key | Fetch | Why |
|---|---|---|---|
| Audit is itself a revalidation (prior audit exists, model version changed, or `revalidate-by` dates in frontmatter have passed) | `revalidation-trigger` | `analysis/evidence-based-revalidation.md` + `analysis/agent-evaluation.md` | Systematic revalidation patterns; per-version eval baselines. |

---

## Anti-Bloat Rule (deterministic)

The router is inclusive, but the audit degrades if too many docs dilute every recommendation. Apply this rule in order:

1. **Count signal-triggered fetches.** Exclude Always Fetch and Always Check docs from the count — they are mandatory.
2. **If count ≤ 8**, fetch all matched docs. Done.
3. **If count > 8**, drop rows in this order until count ≤ 8:
   a. Rows whose signal you are not sure you observed (any uncertainty).
   b. Rows whose signal overlaps another already-matched row (e.g., both `harness-hooks` and `harness-comprehensive` point to `harness-engineering.md` — keep the more specific one).
   c. Rows where the fetched doc is adjacent rather than central to the signal (e.g., `mcp-client-integration.md` for a project with only one MCP server).
4. **Never drop Always Fetch or Always Check docs.**

Target: 4–8 signal-triggered fetches + 3 baseline fetches = 7–11 total docs. Beyond this, the audit becomes a firehose.

---

## Output Requirement

In the final audit, every **Recommendation** must include:

- The analysis doc that supports it (e.g., `analysis/model-migration-anti-patterns.md`)
- The `evidence-tier` of that doc (read from the machine-readable frontmatter field, not from prose)
- The signal key that triggered the match (e.g., `model-version-4-7`)

Example:

```markdown
**Migrate implicit subagent dispatch in `.claude/agents/builder.md:14`**
- Signal: `model-version-4-7` (settings.json targets `claude-opus-4-7`)
- Source: `analysis/model-migration-anti-patterns.md` (evidence-tier: Mixed)
- Action: Replace "dispatch the work" with "Use the Explore subagent to...".
```

The `evidence-tier` is always extractable from the doc's frontmatter — look for the `evidence-tier:` line, not the prose-form tier declaration.

---

*Last updated: 2026-04-22. Signal vocabulary in the Signal key column is authoritative — every `applies-to-signals` value in `analysis/*.md` frontmatter must appear here, and vice versa.*
