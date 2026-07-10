---
status: PARTIALLY EXECUTED 2026-07-10 — Phases 0-2 done + pushed (husk removal, currency fixes, 5 routing-safe deletes; corpus 44→39; fleet-audit regression green 32/32). Phase 3 (memory fold) is the next mechanical unit, no sign-off needed. Phases 4-6 await Jeremy's rulings — consolidated agenda: project1/02-projects/system-audit-2026-06/C2-SIMPLIFICATION-PLAN-2026-07.md
date: 2026-07-09
scope: Fable-era gap scan + staged reduction plan for this repo
method: own-harness surface (running claude-fable-5) + claude-code-guide changelog sweep + official docs fetch + fleet-audit dependency trace + web source refresh
goal: REDUCE repo complexity; hand slices off to Claude Code built-ins and external sources per CONTRIBUTING.md § Retiring a Doc ("shrinking coverage is success, not decay")
---

# Reduction Proposal 2026-07 — Fable-Era Gap Scan

Last substantive work in this repo landed 2026-06-16/21, before the Fable 5 release cycle finished shipping. Since then Anthropic shipped, natively, a large slice of what this repo maintains by hand: a rewritten first-party best-practices guide, bundled `/code-review` / `security-review` / `verify` / `claude-api` / `update-config` / `fewer-permission-prompts` skills, dynamic workflows (`ultracode`, v2.1.154), agent teams v2 (v2.1.178), nested subagents (v2.1.172), MCP tool search with deferred definitions (v2.1.121+, default-on), documented managed-memory limits (200 lines / 25KB), worktree isolation, cloud Routines (`/schedule`, v2.1.198), and — as of v2.1.205 (2026-07-08) — a native `claude doctor` that replaces the community `claude-doctor` this repo's audit still shells out to. The repo's own CONTRIBUTING.md anticipated exactly this: it calls itself a *temporary analytical layer* and defines the RETIRING lane. This proposal runs that lane at scale.

**Primary evidence note**: this scan was produced by a session running `claude-fable-5` on 2026-07-09. The AUDIT-CONTEXT.md claim that Fable 5 "was suspended worldwide 2026-06-12... broken until access is restored" is stale — access is restored and Fable is in production use. That row needs a currency fix regardless of everything else here.

**Verdict summary (analysis/, 44 docs)**: **KEEP 12 · COLLAPSE 18 · DELETE 14** (3 of the COLLAPSEs merge away into a sibling doc, so the post-reduction analysis/ count is **27 files**).

Verdict key:
- **DELETE** — a built-in or external source fully covers it; remove (tombstone or archive/), update routing.
- **COLLAPSE** — shrink to a pointer at the replacement plus the delta the replacement doesn't cover (the RETIRING pattern session-quality-tools.md already models).
- **KEEP** — no built-in equivalent; still earns its bytes.
- **(R)** — routed by AUDIT-CONTEXT.md: the change MUST land in the same commit as the routing-map update and be pushed to GitHub master (see § Fleet-audit compatibility).

---

## 1a. Verdict table — analysis/ (all 44 docs, no omissions)

| # | Doc | Verdict | Replacement / where it goes | Why |
|---|-----|---------|------------------------------|-----|
| 1 | CANONICAL-DOC-TEMPLATE.md | KEEP | — | Contributor template; needed while any analysis doc remains; 9KB. |
| 2 | agent-driven-development.md | COLLAPSE (R) | Official best-practices § Automate and scale + headless docs | The how-to half is now first-party; keep the 7-repo portfolio evidence (the measured maturity model) as the delta. |
| 3 | agent-evaluation.md | KEEP (R) | — | Per-version eval baselines for custom agents have no native equivalent; feeds `revalidation-trigger`. |
| 4 | agent-principles.md | DELETE (R) | Official best-practices (verification, planning, explicit subagent dispatch) | Generic pre-Fable principles, Tier B/C sourced (Nate B. Jones); the official guide now states all of it with examples. Repoint `harness-custom-agents` row at orchestration-comparison + agent-evaluation only. |
| 5 | automated-config-assessment.md | COLLAPSE | Native `claude doctor` / `/checkup` (v2.1.205) + `fewer-permission-prompts` + `update-config` skills | The CC-config-assessment slice went native; keep the Hoosier 12/12 ground-truth evidence as a short measurement note. |
| 6 | behavioral-insights.md | KEEP (R) | — | Always-Fetch doc; quantified thresholds (80% CLAUDE.md adherence, context-quality boundary) have no native home. Flag: numbers are Opus-4.x-era, re-measure on Fable before next revalidate-by. |
| 7 | claude-md-progressive-disclosure.md | COLLAPSE (R) | Official CLAUDE.md guidance (include/exclude table, imports, child files, "prune ruthlessly") + `/init` | First-party docs now carry the whole prescription; keep the measured 42–209-line portfolio data and the ~150-line boundary evidence. |
| 8 | confidence-scoring.md | KEEP (R) | — | 1–5 claim-strength methodology; nothing native; small. |
| 9 | cross-project-synchronization.md | COLLAPSE (R) | Agent teams v2 + worktrees docs for the mechanism half | Keep the hub-spoke portfolio evidence; the multi-session mechanics are now first-party. |
| 10 | dapr-durable-agents.md | DELETE (R) | Dapr's own docs; SOURCES.md entry stays as pointer | `project-type-agent-infra` has never fired in the fleet; niche single-source doc; maintaining a Dapr explainer here is exactly the parallel-infrastructure habit to drop. Drop the routing row. |
| 11 | domain-knowledge-architecture.md | COLLAPSE (R) | Official skills docs ("use skills for domain knowledge, CLAUDE.md for what applies broadly") | The core recommendation is now the documented default; keep the domain-heavy findability patterns that go beyond it. |
| 12 | evidence-based-revalidation.md | KEEP (R) | — | Always-Fetch; the freshness discipline (revalidate-by, claim half-life) is the repo's spine and nothing ships it natively. |
| 13 | evidence-tiers.md | KEEP (R) | — | Core methodology; fleet-audit's output contract reads `evidence-tier` frontmatter from every fetched doc. |
| 14 | federated-query-architecture.md | DELETE (R) | ~/sdw-lab-benchmarks + project1 canon | Security-data spoke content living in the wrong repo (cross-repo boundary rule); the CC-relevant residue is one paragraph. Repoint `project-type-data-pipeline` row or drop it. **Sign-off**. |
| 15 | framework-selection-guide.md | COLLAPSE (R) | Official "Extend Claude Code" features-overview (Match features to your goal) | Native-mechanism selection is now a first-party decision table; keep only the external-framework (LangChain/CrewAI-class) comparison. |
| 16 | harness-engineering.md | COLLAPSE (R) | Official best-practices + Anthropic "Claude Code in large codebases" (2026-05-14) | Biggest doc (62KB); the harness-design half is now first-party (the at-scale guide even names the harness concept). Keep the Bitter-Lesson diagnostic + accretion heuristics — the audit's `harness-comprehensive` row depends on them. |
| 17 | intent-alignment-audit.md | KEEP (R) | — | The RETHINK layer is this repo's unique value; no built-in asks *why* a mechanism exists. |
| 18 | local-cloud-llm-orchestration.md | DELETE (R) | Spoke repos (mndr work); SOURCES pointer | Portfolio case study of a non-fleet project; hybrid-LLM routing signal is off-mission for a CC best-practices layer. **Sign-off**. |
| 19 | mcp-client-integration.md | DELETE (R) | Merge residue into mcp-patterns.md; official MCP docs | Two-architecture comparison is thin next to first-party MCP docs; `harness-mcp` row drops to two docs. |
| 20 | mcp-daily-essentials.md | COLLAPSE→merge (R) | mcp-patterns.md + native MCP tool search | Its headline problem (40%+ context at startup) is largely solved by deferred tool definitions (v2.1.121+, default-on); fold the still-true residue into mcp-patterns. File goes away. |
| 21 | mcp-patterns.md | COLLAPSE (R) | Official MCP docs + OWASP MCP Top 10 (external) | Becomes the single MCP doc (absorbing #20's residue): keep the OWASP mapping + the plugin/MCP sweet-spot evidence; cut the 948-line mechanism walkthrough the docs now own. |
| 22 | mcp-vs-skills-economics.md | COLLAPSE (R) | Features-overview decision table | The choice guidance went native; keep the Tenzir cost measurements ($10.27 vs $20.78/task) as evidence — but note tool-search changed MCP's token economics, so mark the numbers stale-pending-remeasure. |
| 23 | memory-system-patterns.md | COLLAPSE (R) | Official memory docs (MEMORY.md conventions, 200-line/25KB limits now documented) | The conventions half went native; keep the portfolio sizing evidence. |
| 24 | memory-systems-archetype-a-curated-kb.md | KEEP (R) | — | Primary archetype, heavily routed (6+ signals incl. `typed-memory-no-registry` §A1b); no native equivalent for corpus-scale guidance. |
| 25 | memory-systems-archetype-b-code-monorepo.md | DELETE→fold | memory-systems-archetype-recommendations.md | 82-line index-internal doc; folds into the index as a section. |
| 26 | memory-systems-archetype-c-egress-constrained.md | COLLAPSE→fold | recommendation-methodology.md (owner-authorized-egress rule) | Index-internal; the deciding rule is one paragraph plus sensitivity tags — fold and delete the file. |
| 27 | memory-systems-archetype-c-personal-second-brain.md | COLLAPSE→fold (R) | archetype-recommendations index | Routed by `vault-obsidian` — repoint that row at the index in the same commit; content folds to a section. |
| 28 | memory-systems-archetype-d-cross-project-portfolio.md | DELETE→fold | archetype-recommendations index | 78-line index-internal doc. |
| 29 | memory-systems-archetype-e-work-state-tracker.md | DELETE→fold | archetype-recommendations index | 79-line index-internal doc. |
| 30 | memory-systems-archetype-f-session-archive.md | DELETE→fold | archetype-recommendations index; native session resume/`/rewind` covers part of the slice | 75-line index-internal doc. |
| 31 | memory-systems-archetype-g-team-shared-memory.md | DELETE→fold (R) | archetype-recommendations index | Routed by `md-corpus-very-large` — repoint that row at the index in the same commit. |
| 32 | memory-systems-archetype-recommendations.md | KEEP (R) | — | The two-level routing index; absorbs B/D/E/F/G (+C-personal) as sections. Net: 8 archetype files → 2 (this index + archetype-A). |
| 33 | memory-systems-genealogy-baseline.md | DELETE→archive/ | Dated measurement (revalidate-by 2026-07-29, about to lapse) | Personal-domain baseline snapshot; archive with the raw outputs, keep the one-line finding in the index. |
| 34 | memory-systems-graphify-vs-understand-anything.md | KEEP (R) | — | Measured tool comparison (~25% hallucinated EXTRACTED edges, n=8) that no vendor doc will publish; routed by 3 corpus signals. |
| 35 | memory-systems-recommendation-methodology.md | KEEP (R) | — | The scale-band + assumptions methodology; routed by 4 signals; absorbs C-egress's deciding rule. |
| 36 | model-migration-anti-patterns.md | KEEP + refresh (R) | Partial: `/claude-api` bundled skill now carries migration guidance | Most-routed doc (9 signals). No built-in audits *your repo's prompts* for migration breaks. Needs the Fable delta: suspension claim stale (restored — this scan ran on claude-fable-5), adaptive thinking replaced budgets (v2.1.170), Sonnet 5 default (v2.1.197), `[1m]` suffix auto-stripped (v2.1.205), permission mode renamed Manual (v2.1.200). |
| 37 | orchestration-comparison.md | COLLAPSE (R) | Official workflows (`ultracode`), agent-teams, sub-agents docs | Everything native it compares shipped/changed post-doc (teams v2 breaking change v2.1.178, nested subagents v2.1.172, background-by-default v2.1.198); keep the external-framework comparison + when-NOT-to-orchestrate guidance. |
| 38 | plugins-and-extensions.md | COLLAPSE (R) | Official plugins/skills docs + `/plugin` marketplace + nested skills (v2.1.157) | Mechanism documentation went native; keep the marketplace-evaluation and token-economics deltas. |
| 39 | safety-and-sandboxing.md | COLLAPSE (R) | Official sandboxing + permission-modes + auto-mode docs (`autoMode.classifyAllShell` v2.1.193) | First-party docs now carry the mechanism half; keep the OWASP mapping, cred-scan hook pattern (absorb templates/hooks snippet), and unattended-execution controls. Routed by 6 signals — collapse carefully. |
| 40 | scheduled-and-looping-primitives.md | COLLAPSE (R) | Official scheduled-tasks / `/goal` / workflows docs; Routines GA'd v2.1.198 | The mechanism inventory went native; keep the risk-surface→control table (the audit's Unattended Execution section renders from it) — that framing is the delta. |
| 41 | secure-code-generation.md | COLLAPSE (R) | Native `security-review` skill + official security-guidance plugin (v2.1.144+) | The review workflow went native; keep the CodeGuard rule-import guidance + the `commit-security-paths` remediation specifics. |
| 42 | security-data-pipeline.md | DELETE (R) | ~/sdw-lab-benchmarks (canonical Zeek→OCSF numbers live there) | Spoke content in the wrong repo; same call as #14. **Sign-off**. |
| 43 | session-quality-tools.md | DELETE (R) | Native `claude doctor` / `/checkup` (v2.1.205) | Already RETIRING — the robustness bar is now fully cleared by a first-party GA tool. Complete the lane: tombstone the doc, move the one surviving check ("is the repeated instruction actually committed to CLAUDE.md") into the AUDIT-CONTEXT session rows, update the signal command from `npx -y claude-doctor` to `claude doctor`. Note: this doc claims `/insights` GA Feb 2026; the July-2026 docs sweep could not confirm `/insights` exists under that name — verify once, then cite whichever first-party tool is real. Either way the replacement is first-party. |
| 44 | tool-ecosystem.md | DELETE (R) | `/plugin` marketplace + community directories (SOURCES pointers) | Tier B/C tool survey with dated token-efficiency claims; the highest-staleness-per-byte doc in the repo. Repoint `project-type-framework-selection` at framework-selection-guide alone. |

## 1b. Verdict table — non-analysis components

| Component | Verdict | Replacement / where it goes | Why |
|-----------|---------|------------------------------|-----|
| mcp-server/ | DELETE | Already archived: archive/mcp-server-v1/ | Git tracks only its .gitignore — the 73MB on disk is untracked .venv/pycache residue of a server whose source was already removed. Delete the directory; zero audit impact. |
| examples/ | DELETE | archive/examples-v1/ | Untracked husk (git tracks nothing under it); v1 examples already archived. |
| templates/ (CLAUDE.md tiers, settings.json, hooks, rules) | DELETE | Native `/init` (incl. interactive flow v2.1.152+), `update-config` + `fewer-permission-prompts` skills, official hooks docs ("Claude can write hooks for you") | The tier templates predate `/init` doing this job per-project from the actual codebase; fold the cred-scan PreToolUse hook example into safety-and-sandboxing.md before deleting. **Sign-off** (project-bootstrapper skill uses `~/.claude/excellence-kit/`, not this dir — verified no dependency). |
| automation/generate_index.py | KEEP | — | Tiny; regenerates INDEX.md; needed by the reduction itself. |
| scripts/check-measurement-expiry.py | KEEP | — | Enforces the revalidate-by discipline the KEEP docs rely on. |
| scripts/generate-tools-tracker.py | DELETE | Serves archived docs-v1 TOOLS-TRACKER only | Orphaned generator. |
| scripts/check-anthropic-rss.py + analyze-blog-post.py | DELETE | project1's existing 00-inbox/rss pipeline already ingests these feeds; `/schedule` Routine if a dedicated watcher is still wanted | Duplicate ingestion path maintained in the wrong repo. **Sign-off**. |
| scripts/graphify_*.py (2) | KEEP (move note) | — | Part of the graphify measurement tooling cited by analysis #34; cheap to keep. |
| .github/workflows/tools-evolution-tracker.yml | DELETE | — | Runs the orphaned tracker generator. |
| .github/workflows/anthropic-blog-rss.yml | DELETE | Same as scripts row above | **Sign-off** with the RSS scripts. |
| .graphify-venv/, graphify-out/, .understand-anything/ | DELETE | Measurements already recorded in analysis #34 | Untracked experiment residue. |
| V2-COMPLIANCE-MATRIX.md | DELETE→archive/ | project1/02-projects/fleet-audit/ per-repo outputs are the live successor | 2026-03-31 snapshot; several listed projects (security-architect-mcp, blog, splunk-benchmark) have since been archived — the matrix now asserts stale facts as current. |
| SOURCES.md | KEEP + prune | — | The evidence backbone (217KB). Prune superseded entries (§3), add new ones; target ~25% smaller. |
| SOURCES-QUICK-REFERENCE.md | KEEP + refresh | — | Linked from ONE-LINE-PROMPT.md; refresh top-36 for §3 changes. |
| ONE-LINE-PROMPT.md | KEEP + refresh | — | Fleet-audit's local entry point (read by path). Refresh: session-quality section (`claude doctor` not `npx claude-doctor`/`/insights`), doc-count strings ("4–8 of 42" → post-reduction count), Fable-status language. |
| AUDIT-CONTEXT.md | KEEP + refresh | — | THE essential file — every fleet audit WebFetches it from GitHub master. Every (R) verdict above lands here as a routing-row edit in the same commit. Plus: Fable-suspension row fix, `claude doctor` signal command, Sonnet 5 in the model grep sanity-check. |
| README.md, ARCHITECTURE.md, PLAN.md, DECISIONS.md, CONTRIBUTING.md, ARCHIVE.md, INDEX.md | KEEP + count fixes | — | README says "42 docs" (it's 44 today, ~27 after); ARCHITECTURE.md still says 26; INDEX regenerates. Log this pass in DECISIONS.md. |
| research/ (6 root notes) | DELETE→archive/ | Their conclusions shipped into the analysis docs they fed | Point-in-time inputs (memory-systems axes/inventory/archetypes, ai-creators, rethink prompt, codeguard review); codeguard-review stays if secure-code-generation keeps citing it — verify at execution. |
| research/self-audit-2026-06/ | KEEP | — | Cited by intent-alignment-audit.md (a KEEP) as its origin evidence. |
| archive/ | KEEP as-is | — | Already the archive; gains V2 matrix, genealogy baseline, research notes. |
| drafts/, .claude/, node_modules+package.json (markdownlint), .github/link-check | KEEP | — | Working infrastructure. |

---

## 2. Fleet-audit compatibility plan (the constraint)

`/fleet-audit` lives at `/home/jerem/project1/.claude/commands/fleet-audit.md` (a command, not a skill dir — the skills list surfaces it as `fleet-audit`). Traced dependencies, exactly:

1. **Local path** `~/claude-code-project-best-practices/ONE-LINE-PROMPT.md` — read at run time as the canonical prompt; the command also cites its "Wire It as a Recurring RETHINK Tick" section and the structured-output frontmatter fields (`audit-date`...`signals-triggered`) by name. File must keep its path, those section anchors, and the output format.
2. **Remote URL** `https://raw.githubusercontent.com/flying-coyote/claude-code-project-best-practices/master/AUDIT-CONTEXT.md` — WebFetched every run. The audit fetches **GitHub master**, not the local checkout: local-only edits don't reach the fleet, and pushed doc deletions without routing updates 404 mid-audit.
3. **Remote URLs** `master/analysis/{doc}.md` for every doc a routing row names — currently 37 of 44. Every (R)-flagged verdict is therefore CAREFUL: doc change + routing-row change in ONE commit, pushed, then a smoke-test audit run.
4. **Frontmatter contract** — each fetched doc must carry machine-readable `evidence-tier:` (the output requirement reads it, not prose). Collapsed docs keep their frontmatter.
5. **Soft links** — SOURCES-QUICK-REFERENCE.md and analysis/evidence-tiers.md are linked from the prompt's tier section; keep both paths.
6. **project1 side** — `automation/orchestrator/best_practices_reviewer.py` (separate shallow cron) needs only the repo directory to exist; `BEST-PRACTICES-REVIEW-WORKFLOW.md` and `daily-brief-routine.md` reference the command and ONE-LINE-PROMPT by name only; the `Next fleet-audit due` cadence line is repo-independent.

**Not depended on at all** (safe to remove without any compatibility work): mcp-server/, examples/, templates/, scripts/, research/, drafts/, V2-COMPLIANCE-MATRIX.md, SOURCES.md (the big file — only the QUICK-REFERENCE is linked), the graphify dirs, both CI workflows.

**Regression test** (run after every pushed phase): `/fleet-audit claude-code-project-best-practices` — audit the auditor — and diff `docs-fetched` / `signals-triggered` frontmatter against the prior run. A 404 in docs-fetched or a signal routing to a deleted path fails the phase.

---

## 3. Source refresh — new sources worth adding, stale entries

### Add

| Source | Tier | What it is |
|--------|------|------------|
| Anthropic — "How Claude Code works in large codebases" / Claude Code at scale (claude.com blog, 2026-05-14, Applied AI team) | **A** | First-party harness-design guidance at enterprise scale: five extension points (CLAUDE.md, hooks, skills, plugins, LSP), no-index filesystem navigation, and the directly reduction-relevant line that instructions written for an older model may constrain a 2026 model. Replaces chunks of harness-engineering.md. |
| Daniel Miessler — PAI 5.0 "Life Operating System" (2026-04-30) + LifeOS 6.0.2 rename (2026-07-02) | **B** | His current harness: Algorithm v6.x (OBSERVE→...→LEARN loop with verifiable Ideal State Criteria), Memory v7.x (three typed surfaces), deterministic lifecycle hooks, 45 composable skills — and the explicit stance that you extend Claude Code as the runtime rather than building parallel infrastructure, which is this proposal's thesis from a voice SOURCES already tracks (the TELOS/SPQA entry it supersedes). |
| Simon Willison — "Agentic Engineering Patterns" guide (2026, first chapters published) | **B** | His consolidated coding-agent patterns; his deterministic-constraints-over-behavioral-instructions position matches this repo's hooks-over-CLAUDE.md-prose findings. Extends the existing Willison entries. |
| Anthropic — Claude Code official best-practices page (code.claude.com/docs/en/best-practices, 2026 rewrite) + changelog | **A** | Refresh of existing entry #2; now carries verification-loop, plan-mode, CLAUDE.md include/exclude, subagent, permission/sandboxing, and fan-out guidance that a dozen analysis docs previously covered alone. The changelog is the revalidation feed (native `claude doctor` v2.1.205, Routines v2.1.198, Sonnet 5 v2.1.197, agent teams v2 v2.1.178). |

### Stale / superseded existing entries

- **claude-doctor (community)** — superseded by native `claude doctor` (v2.1.205); the audit's signal command must change too.
- **`/insights` First-Party Introspection entry (SOURCES §572)** — could not be confirmed in the July-2026 docs; verify once and either re-cite or fold into the native-doctor entry.
- **Fable 5 / Mythos 5 entry (#34)** — suspension framing stale; running-in-production as of this scan; add Sonnet 5 (2026-06-30, native 1M context, new default).
- **Anthropic Opus 4.7 Migration Guide (#27)** — historical; Fable-era guidance now ships in the bundled `/claude-api` skill.
- **Jason Vertrees "4.7 Quietly Broke..." (#29)** — historical, keep only as provenance for the anti-patterns doc.
- **Builder.io 50 Tips / Morph 2026 Guide / shanraisshan** — community restatements; the official rewrite covers their durable content.
- **Playwright-CLI 4× token claim, MCP context-budget (valgard) numbers** — pre-tool-search measurements; economics changed at v2.1.121; mark stale-pending-remeasure.
- **everything-claude-code star counts and similar point-in-time stats** in README/SOURCES — drop the numbers, keep the links.

---

## 4. Net-size projection

| Slice | Before | After | Δ |
|-------|--------|-------|---|
| analysis/ docs | 44 files / ~860KB | 27 files / ~420KB | −17 files, −~50% bytes (deletes −160KB; collapses ~433KB→~200KB; keeps 223KB incl. refreshes) |
| Live non-archive docs (root+analysis+research+templates+drafts) | 78 | ~49 | −~37% |
| SOURCES.md | 217KB | ~160KB | pruned per §3 |
| Root snapshot docs | V2 matrix live | archived | −1 stale-asserting doc |
| Untracked disk | mcp-server 73MB + graphify residue | 0 | −~75MB |
| scripts/ + CI workflows | 6 scripts, 3 workflows | 3 scripts, 1 workflow | orphan removal |

Direction confirmed DOWN on every axis; the routed surface the fleet depends on shrinks from 37 routed docs to ~24 while keeping every signal key answerable.

---

## 5. Sequenced execution plan

Each phase = one commit (+ push where flagged) + INDEX regen + the §2 regression test after push. Ordered so the cheapest, least-reversible-risk cuts go first.

1. **Phase 0 — husk removal (no sign-off, no push needed, zero audit surface)**: delete mcp-server/ (untracked residue), examples/, .graphify-venv/, graphify-out/, .understand-anything/; archive V2-COMPLIANCE-MATRIX.md; delete tools-evolution-tracker.yml + generate-tools-tracker.py.
2. **Phase 1 — currency fixes to the two essential files (push)**: AUDIT-CONTEXT.md Fable row + `claude doctor` signal command; ONE-LINE-PROMPT.md session-quality block + count strings; resolve the `/insights` question while in there. This unblocks correct audits immediately and touches no doc verdicts.
3. **Phase 2 — routing-safe deletes (push)**: session-quality-tools (complete the retirement), tool-ecosystem, agent-principles, dapr-durable-agents, mcp-client-integration + their routing-row updates in the same commit.
4. **Phase 3 — memory-cluster fold (push)**: B/D/E/F/G (+C-personal, C-egress) into the recommendations index/methodology; genealogy-baseline to archive/; repoint `vault-obsidian` + `md-corpus-very-large` rows. 12 memory docs → 5.
5. **Phase 4 — the big collapses (Jeremy sign-off first; push per doc or per pair)**: harness-engineering, mcp-patterns (+absorb daily-essentials), orchestration-comparison, safety-and-sandboxing (+absorb templates' cred-scan hook), scheduled-and-looping-primitives, plus the smaller collapses (#2, 5, 7, 9, 11, 15, 22, 23, 38, 41). These are the audit's core routed docs — collapse one, regression-test, proceed.
6. **Phase 5 — spoke-content eviction (sign-off)**: federated-query-architecture, security-data-pipeline, local-cloud-llm-orchestration out (tombstones → spoke repos); routing rows repointed or dropped.
7. **Phase 6 — periphery + sources (sign-off on the RSS pair)**: templates/ deletion, RSS scripts+workflow decision, SOURCES.md prune + §3 additions, SOURCES-QUICK-REFERENCE refresh, README/ARCHITECTURE/DECISIONS count-and-log updates, model-migration-anti-patterns Fable delta, behavioral-insights re-measure flag.

**Needs Jeremy's explicit sign-off before execution**: Phase 4 collapse depth on the five core routed docs; Phase 5 spoke eviction (cross-repo boundary call); templates/ deletion; the RSS watcher pair (duplicate of project1's inbox pipeline, but it opens GitHub issues — confirm nothing reads those); archiving the research/ root notes.

**Open questions**: (1) `/insights` — real under another name, or a claim to retract? one docs check settles it; (2) whether the `project-type-data-pipeline` and `project-type-hybrid-llm` routing rows survive Phase 5 pointing at external repos, or drop — dropping is cleaner, the fleet's data repos get their depth from the spoke canon anyway.
