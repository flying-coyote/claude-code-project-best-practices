---
status: EXECUTED (2026-07-16; wave complete, all five staged items ruled same-day — see §4)
convergence: single-source
---

# Absorption Scan 2026-07 — third-party sweep (first pass)

Sibling of [`REDUCTION-PROPOSAL-2026-07.md`](REDUCTION-PROPOSAL-2026-07.md). That scan asked what **Anthropic first-party** had absorbed; this one extends the same question to **third-party open-source projects and thought-leader canons**, per the owner's standing question (2026-07-16): *which external projects or thought leaders answer parts of this project's best-practices definitions well enough to adapt and follow, so the custom load shrinks?* Owner rulings for this wave: full-wave execution (Decision-11-style reasonable assumptions), seven-lane README repositioning.

Landscape inputs: mid-2026 survey with GitHub-API-verified maturity (2026-07-16) — superpowers v6.1.1 under daily development; ECC (renamed from everything-claude-code); AGENTS.md under Linux Foundation stewardship; ClaudeLog active; awesome-claude-code active; HumanLayer 12-factor frozen since 2025-09; ACE stale since 2025-12; efij/awesome-claude-code-security abandoned same-day-created; multi-project portfolio management with no mature absorber anywhere. Snapshot stats live in SOURCES.md dossiers, not here.

## §1 Verdict table (26 routable docs)

Verdict shape: **15 KEEP-SOLE / 5 FOLLOW-CANON / 2 CANDIDATE-STAGED / 1 RETIRE (partial, gated) / 2 INTERNAL-MERGE / 1 COLLAPSE-ROUND-2.** The pattern the sweep confirmed: this corpus's deltas are *measurements and instruments*; the external landscape ships *implementations and commentary*. Absorption pressure is real in exactly three places — economics (first-party `/usage`), the plugins decision framework (first-party features-overview), and the canon-dense commentary layers.

| Doc | Verdict | Basis (one line) |
|---|---|---|
| agent-driven-development | KEEP-SOLE | measured maturity dataset; nobody publishes measurements. Osmani autonomy-levels crosswalk pointer added |
| agent-evaluation | FOLLOW-CANON + internal collapse | ~70% digests 4 Anthropic posts (escaped Decision 11); Husain/Shankar canon recorded in-doc → legitimate single-source→emerging |
| automated-config-assessment | KEEP-SOLE | ECC ships config, not assessment; candidate-emerging note stays staged for owner ruling |
| behavioral-insights | FOLLOW-CANON (ClaudeLog) | ClaudeLog owns the mechanics-explainer lane; our quantified deltas stay; Fable re-measure remains open |
| claude-md-progressive-disclosure | KEEP-SOLE | AGENTS.md is a format standard, not sizing guidance (Sub ✗); interop note + `repo-has-agents-md` signal proposed |
| confidence-scoring | INTERNAL-MERGE → evidence-tiers | ~60%+ overlap, both gutted by the 1–5 retirement; no external absorber grades evidence at all |
| cross-project-synchronization | KEEP-SOLE (longest runway) | landscape's weakest external coverage; portfolio evidence is the moat |
| domain-knowledge-architecture | KEEP-SOLE | license-watch on the AI-PKM emerging basis (2026-09-30 revalidate) |
| evidence-based-revalidation | KEEP-SOLE (identity) | the corpus's operating system; retires only with the repo |
| evidence-tiers | KEEP-SOLE (identity) + prune | A–D IS the product; dead refs + retired-axis lines pruned in the merge commit |
| framework-selection-guide | INTERNAL-MERGE → orchestration-comparison | ~60% verified overlap; superpowers verified ✗ (member of the compared class) |
| harness-engineering | FOLLOW-CANON (Willison/Ronacher/Osmani) | densest canon territory; superpowers verified ✗ (diagnostic applied TO it); Bitter-Lesson delta stays |
| intent-alignment-audit | KEEP-SOLE (crown jewel) | instrument nobody ships; next investment = run on ≥2 external projects, not absorption-watching |
| mcp-patterns | KEEP-SOLE | OWASP mapping has no home elsewhere (security hub attempt died in a day); receives CLI+Skill relocation |
| mcp-vs-skills-economics | RETIRE (partial, gated → RETIRING in place) | `/usage` Sub=partial: supersedes stale absolute figures, cannot produce the controlled A/B; CLI+Skill relocates |
| memory-system-patterns | KEEP-SOLE | mem0/Letta ship engines, not sizing evidence |
| memory-systems-archetype-a-curated-kb | FOLLOW-CANON (Karpathy LLM-wiki) | paradigm is his; implementation evidence is ours |
| memory-systems-archetype-recommendations | KEEP-SOLE (medium runway) | fastest-absorbing space; flips to candidate-verify when mem0/Letta grow archetype guidance |
| memory-systems-graphify-vs-understand-anything | KEEP-SOLE | original A/B measurement no one replicates |
| memory-systems-recommendation-methodology | KEEP-SOLE | internal scaffolding; fold-in candidate at next reduction |
| model-migration-anti-patterns | KEEP-SOLE + staged upgrade | instrument, not commentary; single-source→emerging staged for owner ruling (Vertrees is provenance-only) |
| orchestration-comparison | KEEP-SOLE + receives merge | superpowers verified ✗ (compared object); when-NOT + measured overhead have no absorber |
| plugins-and-extensions | CANDIDATE-STAGED | Sub=partial: decision framework fully native + already cut; migrate residual → retire at next review (2026-09-30) |
| safety-and-sandboxing | KEEP-SOLE | distributed coverage, no community hub; Vercel/Shopify = directional canons only |
| scheduled-and-looping-primitives | FOLLOW-CANON (Osmani/Ronacher/Ng) | primitive inventory already first-party; commentary lineage is canon territory; promotion check run this wave |
| secure-code-generation | COLLAPSE-ROUND-2 | CodeGuard upstream Sub=partial: Options B/C → upstream pointer; Option A + remediation stay (no upstream home) |

## §2 Substance-check protocol + findings (criterion 3 discharge)

Protocol: read the absorber's actual named content against the doc's specific claims; record a short finding with quote or path; star counts never discharge criterion 3. Four checks run 2026-07-16 by parallel read-only agents; full evidence in SOURCES.md dossiers.

1. **`/usage` vs mcp-vs-skills-economics — PARTIAL.** Official costs page confirms `/usage` "attributes recent usage to skills, subagents, plugins, and individual MCP servers, with each shown as a percentage of the total" (code.claude.com/docs/en/costs; GA, plan-gated, citeable). It is an observational monitor of your live usage mix; it structurally cannot produce the doc's controlled same-workflow A/B delta (identical task built both ways), reports no per-implementation duration/cached-token comparison, and is explicitly local-machine approximate. Clears S/GA/Cite; Sub partial — enough to defer the stale absolute Tenzir figures, not the comparative instrument. **Consequence: RETIRING in place (session-quality cadence), not straight-to-archive — a deviation from the approved plan's 27→24 count, forced by the plan's own gate.** Corpus lands at 25 files / 24 routable.
2. **features-overview vs plugins-and-extensions — PARTIAL, retire-ready with migrations.** The Skills-vs-MCP-vs-Hooks decision framework is fully native (features-overview "Match features to your goal" + "Compare similar features" + context-cost tables) and the doc had already cut it; "custom commands have been merged into skills" moots part of the old 4-way matrix. Both stale measurement claims are decorative (Playwright 4x is homed in mcp-patterns; Tenzir in the economics doc). Residual with no home: the community-marketplace curation table (link-rot-prone), the 6-point checklist *packaging*, the 300–800ms latency figure (→ mcp-patterns if kept). Doc's MCP-schema-overhead prose is stale-to-wrong under default tool search. Staged: migrate residual → retire at the 2026-09-30 revalidate.
3. **CodeGuard upstream vs secure-code-generation — PARTIAL.** Upstream (OASIS CoSAI; Cisco-donated 2026-02) now ships a first-party Claude Code marketplace plugin (`/plugin install codeguard-security@project-codeguard`, team settings.json deploy, from-source build) — absorbing Option C fully and Option B's substance. No upstream CLAUDE.md-paste path (Option A stays ours) and no commit-security-paths framing (remediation stays ours). Factual drift caught: upstream's critical triad is credentials/crypto-algorithms/**digital-certificates**, not our credentials/crypto/input-validation — reconciled in the collapse edit.
4. **superpowers v6.1.1 vs orchestration/framework-selection/harness-engineering — ✗ on all three.** Full skill tree enumerated: no security skill (OWASP=0, CVE=0), no "bitter lesson" (0 hits), no framework comparison ("when not to"=0). Superpowers is a compared *object* in our overhead table and Bitter-Lesson spectrum, not a comparator. SOURCES "independently implements equivalent patterns" claim re-verified accurate at v6.x. Its two-stage review varies *what* is reviewed on the same weights; Wiggins cross-model-family review varies *whose weights* review — distinct practices, so the Wiggins delta stands. The secure-code-generation advance trigger (superpowers shipping an OWASP-mapped security-review module) has NOT fired.

## §3 Dossier work queued for Phase 5 (SOURCES.md)

Update: superpowers (v6.1.1 re-verification), ECC (rename history + worldflowai disambiguation), Osmani/Willison/Ronacher/Ng/Miessler canon entries (follow-lane pointers). Add: AGENTS.md/Agentic-AI-Foundation, ClaudeLog, awesome-claude-code (index lane), anthropics/skills + claude-plugins-official, cosai-oasis/project-codeguard (plugin + integration docs). Negative dossiers (prevent re-litigating): HumanLayer 12-factor FROZEN 2025-09-21; ACE stale 2025-12; disler/hooks-mastery stale 2026-03; efij/awesome-claude-code-security abandoned. Quarantine (unverified, directional only): ECC component counts, /insights ~Feb-2026 GA date, marketplace aggregate totals, Shopify 60–70% auto-merge figure.

## §4 Wave sequence + deviations

- **Phase 0** (done): instrument — map, `follows:` field, CONTRIBUTING lane, weekly-review 5b, monitor v2.2.0.
- **Phase 1** (this artifact).
- **Phase 2**: five `follows:` adds + keep-sole annotations + secure-code-generation collapse-round-2; scheduled-and-looping EMERGING→PRODUCTION promotion check. No routing impact.
- **Phase 3**: three atomic commits — economics RETIRING + CLI+Skill relocation; framework-selection → orchestration-comparison merge; confidence-scoring → evidence-tiers merge + prune. AUDIT-CONTEXT routing in-commit; fleet-audit regression per push.
- **Phase 4**: seven-lane README repositioning + CLAUDE.md self-model fix (+ restore intent-alignment-audit to the Core Analysis table — found missing during this wave).
- **Phase 5**: SOURCES dossiers + PLAN.md refresh + Decision 12.

**Deviations from the approved plan, with reasons:**
1. mcp-vs-skills-economics: RETIRING in place (not RETIRED+archive) — the plan gated retirement on the substance check, which returned PARTIAL (§2.1). Corpus 27→**25** files (24 routable), not 24.
2. `follows:` guard: valid on PRODUCTION **or EMERGING** (design said PRODUCTION-only) — two of the five follow-lane docs are EMERGING; the anti-shadow-status intent is preserved by the RETIRING/RETIRED exclusion and the mutual-exclusion rule.
3. Decision 12 lands in the wave-completion commit (design put it in Phase 0) — so its Impact section records actual, not predicted, counts.

**Staged for owner ruling — all ruled 2026-07-16 (same-day):** model-migration-anti-patterns single-source→emerging **approved** (both exemplars now recorded in-doc with the Vertrees provenance-only caveat explicit); automated-config-assessment's candidate-emerging note **declined** (stays single-source — doctor/checkup are install-health tooling, not config-assessment substance; advance trigger unchanged); plugins-and-extensions final retirement **approved as staged** for the 2026-09-30 revalidate, residual migration first; wire-or-retire `best_practices_reviewer.py` **ruled retire** (removal executes project1-side). A fifth item staged in PLAN.md only — the memory-systems-recommendation-methodology fold-in — was **approved and batched** to the same 2026-09-30 session.

---

*Produced 2026-07-16 on claude-fable-5; substance checks by four parallel read-only agents (web + repo).*
