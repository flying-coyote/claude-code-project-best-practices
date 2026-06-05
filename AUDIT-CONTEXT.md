# Audit Context: Signal → Advisory Routing Map

**Purpose**: This file is fetched by the [adaptive routing audit prompt](ONE-LINE-PROMPT.md) to route other projects to the analysis docs that apply to what they actually have, not all 41 at once. Each row states a verifiable signal, the docs to fetch, and the reason for the fetch.

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
cat .claude/mcp.json .mcp.json 2>/dev/null              # MCP servers commonly live here, not only in settings.json
ls .claude/agents/*.md 2>/dev/null | grep -vi readme    # custom-agent definitions only (a README-only agents/ dir is not a custom agent)

# CLAUDE.md state
wc -l CLAUDE.md .claude/CLAUDE.md 2>/dev/null
grep -nEi "\b(best practices|idiomatic|robust|proper|clean code)\b" CLAUDE.md .claude/CLAUDE.md 2>/dev/null
grep -nEi "\b(where applicable|as needed|if relevant|consider edge cases)\b" CLAUDE.md .claude/CLAUDE.md 2>/dev/null
grep -nE "see (rules/|\.claude/|[A-Z])" CLAUDE.md .claude/CLAUDE.md 2>/dev/null

# Model version detection
grep -REi "opus-4-?[5678]|sonnet-4-?[5678]|claude-[0-9]" .claude/settings.json .github/workflows/ 2>/dev/null

# Commit patterns (assumes git repo)
git log --since="90 days ago" --oneline 2>/dev/null | wc -l
git log --since="90 days ago" --pretty=format:'%s' 2>/dev/null | grep -cE "(Claude|claude|Co-Authored)"

# Session diagnostics
npx -y claude-doctor 2>/dev/null

# Memory & knowledge corpus signals
find . -name '*.md' -not -path '*/node_modules/*' -not -path '*/.git/*' -not -path '*/archive/*' 2>/dev/null | wc -l
ls -d .obsidian/ 2>/dev/null
ls index.md raw log.md 2>/dev/null                      # Karpathy layout at root (lowercase)
ls wiki/index.md wiki/raw wiki/log.md 2>/dev/null       # Karpathy layout under wiki/
ls -d secrets/ private/ confidential/ 2>/dev/null
ls -a .env .env.* 2>/dev/null | head -3
```

### Edge Cases — handle silently, do not fail the audit

- **No `.claude/` directory**: signal = `harness-minimal` (if CLAUDE.md exists at repo root) or `claude-md-missing` (if not).
- **No git history or bare repo**: skip commit-pattern rows; note in output.
- **`settings.json` has no model field**: signal = `model-version-unknown`.
- **`claude-doctor` unavailable**: skip session-diagnostic rows; note in output.
- **WSL or non-POSIX paths**: commands still work; treat any command failure as "signal not observed."
- **Any command times out or errors**: treat as signal not observed; do not fail the audit.
- **Markdown count returns 0**: no `md-corpus-*` signal triggers; the project is not a knowledge corpus.
- **Karpathy layout partially present** (e.g., `index.md` exists but no `raw/`): `vault-karpathy` does NOT match; the Lum1104 `/understand-knowledge` skill requires the full triple. Fall back to `/understand-anything:understand` recommendation in archetype-A.

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
| `settings.json` or recent config references `opus-4-8` or `claude-opus-4-8` (incl. the `[1m]` 1M-context variant) | `model-version-4-8` | `analysis/model-migration-anti-patterns.md` + `analysis/safety-and-sandboxing.md` | 4.8 (2026-05-28) keeps 4.7's literal-interpretation posture (prompt anti-patterns still apply) and recovers the 4.7 harness-stressing failure modes — but it **regressed on prompt-injection robustness** (system card §5.2) and any harness passing `thinking: {budget_tokens: N}` now hard-fails with a 400. Audit for: extended-thinking-budget usage, injection exposure on tool-use/computer-use agents, and the carried-forward prompt anti-patterns. |
| `settings.json` or recent config references `opus-4-7` or `claude-opus-4-7` | `model-version-4-7` | `analysis/model-migration-anti-patterns.md` | Six prompt anti-patterns that silently no-op on 4.7. Audit CLAUDE.md/skills for vague descriptors, edge-case gestures, unanchored triggers, implicit subagent dispatch, missing verbosity directives, references without read-enforcement. |
| References `opus-4-6` with no 4.7/4.8 reference | `model-version-4-6` | `analysis/model-migration-anti-patterns.md` | Open revalidation trigger before upgrade. |
| References `opus-4-5` with no 4.6/4.7 reference | `model-version-4-5` | `analysis/model-migration-anti-patterns.md` | Two-version gap; compound revalidation risk. |
| Mixed versions across agents / settings / CI | `model-version-migration` | `analysis/model-migration-anti-patterns.md` + `analysis/evidence-based-revalidation.md` | Cross-version matrix; revalidation trigger. |
| No model field found anywhere | `model-version-unknown` | `analysis/model-migration-anti-patterns.md` | Default-model behavior shifts across releases; doc surfaces latest defaults. |

## Fetch on CLAUDE.md Signal

| Signal (verifiable) | Signal key | Fetch | Why |
|---|---|---|---|
| `wc -l` of CLAUDE.md > 150 | `claude-md-size` | `analysis/claude-md-progressive-disclosure.md` | ~150 instruction budget is a convergent behavioral boundary; progressive disclosure is the remediation. |
| `grep -nE "see (rules/\|\\.claude/\|[A-Z])"` returns matches in CLAUDE.md | `claude-md-references` | `analysis/claude-md-progressive-disclosure.md` | 4.7 no longer infers that referenced files should be read. Mechanical enforcement (PreToolUse hook, explicit Read step, inline block) required. |
| No CLAUDE.md found at root or in `.claude/` | `claude-md-missing` | `analysis/claude-md-progressive-disclosure.md` | 3-tier evolution model provides a calibrated starting point. |
| `grep -nEi "\b(best practices\|idiomatic\|robust\|proper\|clean code)\b"` matches in CLAUDE.md | `claude-md-vague-descriptors` | `analysis/model-migration-anti-patterns.md` | Anti-pattern #1 — silent no-ops on 4.7 (carries to 4.8). |
| `grep -nE "MUST\|NEVER\|ALWAYS\|\bmax\b\|cap (at\|of)"` matches on *advisory* (non-safety) guidance in CLAUDE.md | `claude-md-emphatic-constraints` | `analysis/model-migration-anti-patterns.md` | Soft-guideline literalization (first-class anti-pattern): 4.7/4.8 hard-cap emphatic syntax on guidance the author meant as a heuristic. Reserve MUST/NEVER/hard caps for genuine invariants; write heuristics in advisory syntax. |

## Fetch on Harness Layout

| Signal (verifiable) | Signal key | Fetch | Why |
|---|---|---|---|
| `.claude/hooks/` directory present | `harness-hooks` | `analysis/harness-engineering.md` + `analysis/safety-and-sandboxing.md` | Hook-based enforcement is the 100%-adherence boundary; sandboxing is the defense-in-depth layer. |
| `ls .claude/skills/ \| wc -l` returns >5 | `harness-skills` | `analysis/plugins-and-extensions.md` + `analysis/mcp-vs-skills-economics.md` | Skills use ~2% context each; economics comparison applies at this scale. |
| `.claude/agents/` contains one or more agent-definition `.md` files (a README-only `agents/` dir does NOT match — exclude `README.md`) | `harness-custom-agents` | `analysis/agent-principles.md` + `analysis/orchestration-comparison.md` + `analysis/agent-evaluation.md` | Custom-subagent gatekeeping is a documented anti-pattern; 4.7 spawns fewer subagents by default. |
| an `mcpServers` key with ≥1 entry in `settings.json`, `.claude/mcp.json`, or root `.mcp.json` | `harness-mcp` | `analysis/mcp-patterns.md` + `analysis/mcp-daily-essentials.md` + `analysis/mcp-client-integration.md` | MCP context budget, OWASP failure modes, 4-plugin + 2-MCP sweet spot. |
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

## Fetch on Session Diagnostic Signal

**First-party deference (2026-06-04):** Anthropic's `/insights` command (GA Feb 2026) natively analyzes session history and auto-generates CLAUDE.md rules from repeated instructions — it supersedes the session-pattern analysis `claude-doctor` was used for. For session diagnostics, **recommend the audited project run `/insights` first**; `session-quality-tools.md` is now `RETIRING` (status in its frontmatter) and is fetched only for what `/insights` does not do: the static check that a repeated instruction is actually committed to CLAUDE.md, and the evidence-assessment of why composite friction scores are uncalibrated. `claude-doctor` remains an optional fallback when `/insights` is unavailable.

| Signal (verifiable) | Signal key | Fetch | Why |
|---|---|---|---|
| `claude-doctor` produced any output, OR `/insights` is available | `session-diagnostics-run` | `analysis/session-quality-tools.md` | Prefer `/insights` (first-party) for session-pattern analysis; use this doc for the signal-reliability hierarchy and the uncalibrated-score caveat. |
| `edit-thrashing` count > 5 | `session-edit-thrashing` | `analysis/session-quality-tools.md` + `analysis/claude-md-progressive-disclosure.md` | Missing file-pattern knowledge; CLAUDE.md or rules file gap. |
| `error-loop` count > 3 | `session-error-loop` | `analysis/session-quality-tools.md` + `analysis/harness-engineering.md` | No error recovery; harness-level remediation. |
| `repeated-instructions` count > 2 | `session-repeated-instructions` | `analysis/claude-md-progressive-disclosure.md` | The repeated thing belongs in CLAUDE.md — `/insights` will auto-draft the rule; verify it is committed, not just suggested. |

## Fetch on Project Type

| Signal (verifiable) | Signal key | Fetch | Why |
|---|---|---|---|
| README mentions "documentation," "knowledge base," or "notes" in title/first paragraph | `project-type-docs` | `analysis/memory-system-patterns.md` + `analysis/memory-systems-archetype-recommendations.md` + `analysis/claude-md-progressive-disclosure.md` | Auto-memory sizing; archetype index for picking a stack; progressive disclosure for reference-heavy work. The archetype-recommendations index then routes to the per-archetype doc that fits the corpus. |
| Repo contains `*.parquet`, `*.iceberg`, Zeek / Suricata configs, OCSF mappings | `project-type-data-pipeline` | `analysis/security-data-pipeline.md` + `analysis/federated-query-architecture.md` | Zeek→OCSF patterns; federated vs centralized cost analysis. |
| Repo contains MLX, Ollama, or local-model integration alongside cloud API client | `project-type-hybrid-llm` | `analysis/local-cloud-llm-orchestration.md` | Tokenization boundary, hallucination scrubbing, supply-chain hardening. |
| Repo uses "hypothesis," "H-{label}," or `confidence` tracking in commit messages or files | `project-type-research` | `analysis/evidence-based-revalidation.md` + `analysis/confidence-scoring.md` | Confidence scoring with explicit gap statements; revalidation cadence. |
| Repo contains baseline/deviation/compliance tooling | `project-type-config-assessment` | `analysis/automated-config-assessment.md` | Baseline-deviation-remediation pattern. |
| Commits reference ≥3 sibling repos in the same workspace | `project-type-multi-repo` | `analysis/cross-project-synchronization.md` + `analysis/agent-driven-development.md` | Cross-repo coordination and infrastructure maturity. |
| User explicitly asks "which framework should I use" or repo is pre-scaffold | `project-type-framework-selection` | `analysis/framework-selection-guide.md` + `analysis/tool-ecosystem.md` | Decision matrix; Specification Gap framework. |
| Repo ships its own rule language, DSL, or vendor-specific configs | `project-type-domain-heavy` | `analysis/domain-knowledge-architecture.md` | Making expertise findable without overwhelming context. |
| Repo uses an agent-infrastructure runtime — Dapr (`dapr.yaml`/`dapr.yml`, `components/`, `dapr_agents`/`dapr` imports, `dapr init`/`dapr run`), or hand-rolled durability/identity/secrets/observability wrapped around agent code | `project-type-agent-infra` | `analysis/dapr-durable-agents.md` | Infrastructure-as-runtime question: is agent durability, SPIFFE identity, secrets, and OTel observability custom-coded, or delegated to a runtime? Complementary to MCP (tool-exposure layer), not a substitute. |

## Fetch on Memory & Knowledge System

The recommendations in archetype A (curated analytical KB) and C (personal second brain) bend sharply with corpus scale and vault layout. These signals route to the right archetype + the methodology's scale-band guidance, and gate Pass-2-LLM-egress recommendations on observed sensitivity markers.

| Signal (verifiable) | Signal key | Fetch | Why |
|---|---|---|---|
| Markdown count is 50–200 (excluding `archive/`, `node_modules/`, `.git/`) | `md-corpus-small` | `analysis/memory-systems-archetype-a-curated-kb.md` + `analysis/memory-systems-recommendation-methodology.md` | "Below ~200" branch — manual cross-refs work; Lum1104 over wikilinks if a graph view is wanted; no graphify Pass 2. |
| Markdown count is 200–1500 | `md-corpus-design-target` | `analysis/memory-systems-archetype-a-curated-kb.md` + `analysis/memory-systems-archetype-recommendations.md` + `analysis/memory-systems-graphify-vs-understand-anything.md` | Archetype-A primary stack territory. Sample-verification discipline required: ~25% of graphify EXTRACTED edges hallucinated in this repo's Pass 2 testbed (n=8 spot-check, 2026-04-28). |
| Markdown count is 1500–6000 | `md-corpus-large` | `analysis/memory-systems-archetype-a-curated-kb.md` + `analysis/memory-systems-recommendation-methodology.md` + `analysis/memory-systems-graphify-vs-understand-anything.md` | Full archetype-A stack + reviewer pass. At this scale 25% hallucinated EXTRACTED edges = thousands of wrong "verified" relations; hallucination-mitigation is load-bearing, not optional. |
| Markdown count > 6000 | `md-corpus-very-large` | `analysis/memory-systems-recommendation-methodology.md` (read "far-larger projects" section) + `analysis/memory-systems-archetype-g-team-shared-memory.md` | Generic recommendations don't calibrate at 12×–40× the design target. Custom domain-specific stack required (e.g., Postgres + pgvector + MCP shim, or domain-specific extractors). |
| `.obsidian/` directory present | `vault-obsidian` | `analysis/memory-systems-archetype-c-personal-second-brain.md` + `analysis/memory-systems-archetype-recommendations.md` | Cross-domain personal-vault layout (archetype-C). The vault's built-in graph view typically substitutes for an external graph-builder; recommendations should bias toward "use what the vault already gives you" before adding tooling. |
| Lowercase `index.md` + `raw/` directory + `log.md` ALL present at repo root or under `wiki/` | `vault-karpathy` | `analysis/memory-systems-archetype-a-curated-kb.md` | Lum1104 `/understand-knowledge` will pass detection. Without all three, the skill falls back to `/understand-anything:understand` (no Karpathy gate, file-level + tour). |
| `secrets/`, `private/`, or `confidential/` dirs present, OR `.env`/`.env.*` files at root, OR user explicitly flags corpus as sensitive | `corpus-sensitive` | `analysis/memory-systems-recommendation-methodology.md` (assumption #5 + assumption #8) | LLM egress unacceptable. graphify Pass 2 and understand-anything both ship full document content to the invoking session's LLM — not reversible. Stack collapses to "wikilinks + grep + local graph view"; no LLM-driven graph layer. |

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

*Last updated: 2026-06-04 (added `project-type-agent-infra` routing for `dapr-durable-agents.md` so it is reachable; deferred the session-diagnostic rows to first-party `/insights` as `session-quality-tools.md` enters the RETIRING lane; corrected the routable-corpus count 28 → 41; broadened the `harness-mcp` signal to also detect `mcpServers` in `.claude/mcp.json` or root `.mcp.json` (not only `settings.json`), with the `cat` added to Signal Collection; tightened `harness-custom-agents` to require an agent-definition `.md` beyond `README.md`). Prior: 2026-05-30 (added `model-version-4-8` and `claude-md-emphatic-constraints` signals for the Opus 4.8 release; model-version grep extended to `4-8`). Signal vocabulary in the Signal key column is authoritative — every `applies-to-signals` value in `analysis/*.md` frontmatter must appear here, and vice versa.*
