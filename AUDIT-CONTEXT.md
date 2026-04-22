# Audit Context: Signal → Advisory Routing Map

**Purpose**: This file is fetched by the [one-line audit prompt](ONE-LINE-PROMPT.md) to route other projects to the analysis docs that apply to what they actually have, not all 28 at once.

**How to use (for the auditing agent)**:

1. Collect the project signals listed in the prompt (CLAUDE.md presence, commit patterns, harness layout, session diagnostics, model version in use).
2. For each row in the tables below whose **Signal** matches, fetch the **Fetch** doc(s) from `https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/{path}`.
3. Every recommendation in your final audit must cite the doc and its evidence tier (visible in each doc's header).
4. Do not fetch docs whose signals you did not observe — fewer, more relevant citations beat a firehose.

**Evidence-tier reminder**: Tier A = Anthropic / primary observation. Tier B = expert practitioner / production validation. Tier C = community. See [analysis/evidence-tiers.md](analysis/evidence-tiers.md). Authority-weighted source list: [SOURCES-QUICK-REFERENCE.md](SOURCES-QUICK-REFERENCE.md).

---

## Always Fetch (every audit)

| Fetch | Why |
|---|---|
| `analysis/evidence-tiers.md` | You need the tier definitions to cite recommendations correctly. |
| `analysis/behavioral-insights.md` | Quantified behavioral thresholds (80% CLAUDE.md adherence, 60% context quality threshold, prompt-sensitivity table across model versions) apply to every project. |

## Fetch on Model Version Signal

| Signal observed | Fetch | Why |
|---|---|---|
| Project uses or targets Opus 4.7 (check `settings.json`, recent commits, CI config) | `analysis/model-migration-anti-patterns.md` | Six prompt anti-patterns that silently no-op on 4.7. Audit CLAUDE.md/skills for vague descriptors, edge-case gestures, unanchored triggers, implicit subagent dispatch, missing verbosity directives, references without read-enforcement. |
| Project uses Opus 4.5 or 4.6 and hasn't migrated | `analysis/model-migration-anti-patterns.md` + `analysis/evidence-based-revalidation.md` | Flag as an open revalidation trigger; document which 4.6-tuned prompts should be re-tested before upgrading. |
| Mixed model usage or model version unclear | `analysis/model-migration-anti-patterns.md` | Cross-version matrix helps identify which patterns are version-sensitive. |

## Fetch on CLAUDE.md Signal

| Signal observed | Fetch | Why |
|---|---|---|
| CLAUDE.md exists, >150 lines | `analysis/claude-md-progressive-disclosure.md` | ~150 instruction budget is a convergent behavioral boundary; progressive disclosure into rules/skills/commands is the remediation. |
| CLAUDE.md contains references to other files ("see rules/…", "follow X.md") | `analysis/claude-md-progressive-disclosure.md` | 4.7 no longer infers that referenced files should be read. Mechanical enforcement (PreToolUse hook, explicit Read step, inline block) required. |
| CLAUDE.md missing entirely | `analysis/claude-md-progressive-disclosure.md` | 3-tier evolution model (minimal → resource map → rules+security) gives a calibrated starting point by project maturity. |
| CLAUDE.md contains vague quality descriptors ("best practices," "idiomatic," "robust," "proper") | `analysis/model-migration-anti-patterns.md` | Anti-pattern #1 — silent no-ops on 4.7. |

## Fetch on Harness Layout

| Signal observed | Fetch | Why |
|---|---|---|
| `.claude/hooks/` present | `analysis/harness-engineering.md` + `analysis/safety-and-sandboxing.md` | Hook-based enforcement is the 100%-adherence boundary; sandboxing is the defense-in-depth layer. |
| `.claude/skills/` present, >5 skills | `analysis/plugins-and-extensions.md` + `analysis/mcp-vs-skills-economics.md` | Skills use ~2% context each; economics comparison applies at this scale. |
| `.claude/agents/` with custom subagents | `analysis/agent-principles.md` + `analysis/orchestration-comparison.md` + `analysis/agent-evaluation.md` | Custom-subagent gatekeeping is a documented anti-pattern; 4.7 spawns fewer subagents by default. |
| MCP servers configured (`settings.json` mcpServers) | `analysis/mcp-patterns.md` + `analysis/mcp-daily-essentials.md` + `analysis/mcp-client-integration.md` | MCP context budget, OWASP failure modes, 4-plugin + 2-MCP sweet spot. |
| No harness (just CLAUDE.md or nothing) | `analysis/harness-engineering.md` | Start-minimal decision tree; when to add each mechanism. |
| Comprehensive harness (hooks + skills + agents + rules + commands) | `analysis/harness-engineering.md` + `analysis/framework-selection-guide.md` | Bitter Lesson diagnostic — is the harness buying you anything, or accreting complexity? |

## Fetch on Commit Pattern

| Signal observed | Fetch | Why |
|---|---|---|
| AI co-authoring rate >50% | `analysis/agent-driven-development.md` | 7-repo infrastructure maturity model; calibrate expectations against production evidence. |
| Commit bursts (15+ commits/day) | `analysis/agent-driven-development.md` + `analysis/harness-engineering.md` | Burst patterns signal agent-driven work; harness quality determines sustainability. |
| Multiple repos with cross-references | `analysis/cross-project-synchronization.md` | Hub-spoke coordination patterns; dependency cascading. |
| Security-sensitive data paths in repo | `analysis/safety-and-sandboxing.md` + `analysis/secure-code-generation.md` | OWASP-aware enforcement, PreToolUse blocking for customer data. |
| Low commit volume (<10 in 90 days) | Extend window to 365 days before routing. | |

## Fetch on Session Diagnostic Signal (claude-doctor)

| Signal observed | Fetch | Why |
|---|---|---|
| claude-doctor run at all | `analysis/session-quality-tools.md` | Signal reliability hierarchy — act on edit-thrashing and error-loop; treat sentiment as directional only. Explicit gap statements on threshold calibration. |
| `edit-thrashing` >5 | `analysis/session-quality-tools.md` + `analysis/claude-md-progressive-disclosure.md` | Missing file-pattern knowledge; CLAUDE.md or rules file gap. |
| `error-loop` >3 | `analysis/session-quality-tools.md` + `analysis/harness-engineering.md` | No error recovery; harness-level remediation. |
| `repeated-instructions` >2 | `analysis/claude-md-progressive-disclosure.md` | The repeated thing belongs in CLAUDE.md. |

## Fetch on Project Type

| Signal observed | Fetch | Why |
|---|---|---|
| Documentation / knowledge-management project | `analysis/memory-system-patterns.md` + `analysis/claude-md-progressive-disclosure.md` | Auto-memory sizing; progressive disclosure for reference-heavy work. |
| Data pipeline / security-data project | `analysis/security-data-pipeline.md` + `analysis/federated-query-architecture.md` | Zeek→OCSF patterns; federated vs centralized cost analysis. |
| Hybrid local+cloud LLM | `analysis/local-cloud-llm-orchestration.md` | Tokenization boundary, hallucination scrubbing, supply-chain hardening. |
| Research / hypothesis-driven work | `analysis/evidence-based-revalidation.md` + `analysis/confidence-scoring.md` | Confidence scoring with explicit gap statements; revalidation cadence. |
| Config / compliance assessment | `analysis/automated-config-assessment.md` | Baseline-deviation-remediation pattern. |
| Multi-repo portfolio | `analysis/cross-project-synchronization.md` + `analysis/agent-driven-development.md` | Cross-repo coordination and infrastructure maturity. |
| Tool / framework selection open question | `analysis/framework-selection-guide.md` + `analysis/tool-ecosystem.md` | Decision matrix; Specification Gap framework. |
| Domain-heavy ecosystem (specialized rule languages, vendor tooling) | `analysis/domain-knowledge-architecture.md` | Making expertise findable without overwhelming context. |

## Always Check (even if nothing above matched)

| Fetch | Why |
|---|---|
| `analysis/evidence-based-revalidation.md` | Every claim has a half-life; any audit should surface stale-claim risk. |

---

## Anti-Bloat Rule

If you matched more than 10 analysis docs, you have probably over-routed. Re-read the signal list and drop docs whose trigger you are not sure you observed. The audit is more useful with 5 confidently-applicable docs than 15 speculative ones.

## Output Requirement

In your final audit, the **Recommendations** section must include, per recommendation:

- The analysis doc that supports it (e.g., `analysis/model-migration-anti-patterns.md`)
- The evidence tier of that doc (A / B / C / Mixed — read from the doc's header)
- The project signal that triggered the match

This makes the audit auditable — a reader can verify each recommendation against its source.

---

*Last updated: April 22, 2026. When new analysis docs are added, update this routing map before the next audit run.*
