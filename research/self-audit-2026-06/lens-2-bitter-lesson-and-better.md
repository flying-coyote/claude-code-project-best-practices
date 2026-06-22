---
lens: bitter-lesson-and-better
prompts:
  - "Fable #2 — bitter-lesson optimization (where hand-built scaffolding loses to a more general/scalable approach)"
  - "Fable #5 — what does 'better' mean (evals / regression on the repo's own output)"
date: 2026-06-21
target-repo: /home/jerem/claude-code-project-best-practices
status: DRAFT
---

# Self-audit lens 2: bitter lesson, and "is this repo getting better?"

Two questions drive this lens. First, the bitter-lesson one: where does the repo lean on hand-built scaffolding — routing tables, compliance matrices, parsing scripts — that a more general or more scalable approach (or a first-party feature) would beat as models and the platform improve? Second, the harder one: does the repo have any way to tell whether *it* is getting better over time? Regression tests on its own recommendations, eval fixtures, a measurement-expiry gate that actually fires? The repo teaches both of these to other projects, in `analysis/harness-engineering.md` (Bitter Lesson section) and `analysis/agent-evaluation.md` (eight eval patterns including regression testing). The interesting gap is that it largely does not apply either discipline to itself.

The honest headline is mixed. On bitter-lesson awareness the repo is genuinely strong — it tracks first-party feature convergence, retired `session-quality-tools.md` when `/insights` shipped, and keeps the routing map deliberately thin. On "is it getting better," the repo has the *vocabulary* (revalidate-by dates, measurement-claims frontmatter, an eval doc) but its one automated regression mechanism is pointed at a directory that no longer exists, so it silently passes while real claims go stale.

---

## Findings

### Finding 1 — The measurement-expiry gate is dead-pointed at a deleted directory; it reports all-clear while real claims are 93 days overdue (HIGH)

This is the central "is the repo getting better" failure. The repo's one automated self-regression mechanism does not run against the content it is supposed to guard.

`scripts/check-measurement-expiry.py:196` defaults `--patterns-dir` to `patterns`. The v1→v2 migration moved all content from `patterns/` to `analysis/` (the `patterns/` directory no longer exists at the repo root). The daily workflow `.github/workflows/tools-evolution-tracker.yml:57-60` invokes the script with `--create-issue` but **no** `--patterns-dir`, so it scans the nonexistent `patterns/`, finds 0 files, and exits 0 ("All measurement claims current"). I ran both paths to confirm:

- Default (what CI runs): `Found 0 pattern files ... ✅ All measurement claims are current.`
- Pointed at the real content (`--patterns-dir analysis`): `Found 43 pattern files ... ⚠️ Expired: 2 claims` — both in `analysis/mcp-patterns.md` ("~43% of MCP servers have command injection vulnerabilities" and "Only ~10 of 5,960+ MCP servers are genuinely trustworthy"), each **93 days overdue** (revalidate date 2026-03-20).

The failure compounds three ways. The CI step also carries `continue-on-error: true` (line 61) and the issue-creation step only fires `if: steps.check_expiry.outcome == 'failure'` (line 64) — but the script exits 0, so even if it found the claims, the gate is non-blocking. And `scripts/generate-tools-tracker.py:30` has the identical bug (`PATTERNS_DIR = Path("patterns")`), so the *other* half of the same daily workflow is also scanning an empty target. The repo's own `analysis/evidence-based-revalidation.md:188` names this exact failure — "Revalidation as honor-system → `revalidate-by` dates pass silently; stale generated values ship" — and claims a fix exists; line 176 asserts "This is revalidation built into the document format." The mechanism is built but disconnected, which is worse than absent because the green CI run reads as evidence the claims are fresh.

**Evidence**: `scripts/check-measurement-expiry.py:3,196`; `scripts/generate-tools-tracker.py:30`; `.github/workflows/tools-evolution-tracker.yml:57-64`; live run showing 2 expired claims in `analysis/mcp-patterns.md`; `analysis/evidence-based-revalidation.md:176,188`.

**Recommendation**: Change both scripts' default target from `patterns` to `analysis` (or pass `--patterns-dir analysis` in the workflow), then remove `continue-on-error: true` for the expiry step so the daily run actually fails on overdue claims. Re-validate the two `mcp-patterns.md` claims against current OWASP MCP data and push their `revalidate` dates forward, or mark them historical. This is the single highest-leverage fix in this lens: it is the only place the repo could mechanically tell itself it is decaying, and right now it cannot.

---

### Finding 2 — No regression fixture exists for the audit's own output; the repo teaches regression testing but does not run it on itself (HIGH)

This is the bitter-lesson-adjacent "what does better mean" gap. The repo's product is the adaptive routing audit (`AUDIT-CONTEXT.md` + `ONE-LINE-PROMPT.md`): given a project's signals, it should fetch the right 4-8 of 42 docs and emit cited recommendations. There is no fixture anywhere that pins "fixture project X with these signals should trigger these signal keys and fetch these docs," so there is no way to know whether an edit to the routing table improved or silently broke the routing — the exact regression-testing pattern the repo documents at `analysis/agent-evaluation.md:100-106` (pattern #6) and `:59-64` (Golden Answer Comparison). `analysis/agent-evaluation.md:22` even states the principle: "You can't improve what you can't measure." `PLAN.md:38` shows the team considered this and **deferred** it: "CI regression tests for prompt anti-patterns (Vertrees proposal) — Deferred — out of scope until Anthropic publishes guidance."

The deferral reasoning is too conservative for the cheap version. You do not need Anthropic guidance to assert deterministic routing invariants: a fixture directory with, say, three synthetic mini-projects (a minimal CLAUDE.md-only repo, an MCP-heavy repo, a 300-md-file knowledge corpus), each with an expected signal-key set and expected fetch list, checked by a script that runs the Signal Collection commands and diffs observed-vs-expected. That is golden-answer comparison on the routing layer — pure determinism, no model in the loop, no benchmark saturation concern. The LLM-judged "are the recommendations good" layer is genuinely hard and reasonably deferred; the routing-determinism layer is not, and it is where edits actually break things.

**Evidence**: absence of any fixture/golden directory (no `regression`, `fixtures`, `golden`, `self-test` anywhere outside `node_modules` per grep); `analysis/agent-evaluation.md:22,59-64,100-106`; `PLAN.md:38`.

**Recommendation**: Add a small `tests/routing-fixtures/` with 3-5 synthetic repos and a deterministic checker that asserts each fixture's observed signal keys and fetched-doc list match an expected manifest. Run it in CI on every PR that touches `AUDIT-CONTEXT.md` or doc frontmatter. Keep it model-free — this is the cheap, high-value half of "what does better mean" that needs no vendor guidance.

---

### Finding 3 — `AUDIT-CONTEXT.md` asserts a sync linter "must" exist to keep routing rows and doc frontmatter in agreement, but no such linter exists (HIGH)

The routing map is hand-maintained scaffolding with a documented invariant the repo cannot currently enforce. `AUDIT-CONTEXT.md:10` states routing rows and doc `applies-to-signals` frontmatter "must stay in sync," and `:242` goes further: "A sync linter must whitelist these classes rather than flag them" — language that presumes a linter. There is none. Grep for `applies-to-signals` across `scripts/`, `automation/`, and `.github/` returns nothing; `automation/` contains only `generate_index.py`. So the two-sided contract (every top-level signal key in the table has a doc that declares it; every routable doc is reachable from a row) is maintained by hand across a 42-doc corpus with 78 distinct `applies-to-signals` tokens. This is the textbook hand-built-scaffolding-that-drifts problem, and the repo's own `generated-docs-no-drift-gate` routing row (`AUDIT-CONTEXT.md:199`) flags exactly this pattern *for other projects*.

This is moderate-probability-but-high-blast-radius: routing drift does not crash anything, it silently degrades the audit (a doc becomes unreachable, or a signal key routes to nothing), and there is no test that would catch it. It compounds Finding 2 — the same fixture harness could host this linter.

**Evidence**: `AUDIT-CONTEXT.md:10,242`; `automation/` contains only `generate_index.py`; no `applies-to-signals` reference in any script/workflow; 78 distinct tokens across `analysis/*.md`.

**Recommendation**: Write the sync linter the doc already presumes — parse every `applies-to-signals` token from `analysis/*.md` frontmatter, parse every signal key from the `AUDIT-CONTEXT.md` routing tables, diff the two sets with the documented whitelist (`commit-low-activity`, `cron-disabled`, `audit-always-fetch`, `contributing-new-analysis`, and the index-internal sub-routing tokens), and fail CI on any unreachable doc or dangling signal key. This is deterministic, ~50 lines, and closes a gap the repo has already written prose committing to.

---

### Finding 4 — `V2-COMPLIANCE-MATRIX.md` is a hand-built, point-in-time scaffold gone stale; it is the orphaned-snapshot anti-pattern the repo warns about (MEDIUM)

`V2-COMPLIANCE-MATRIX.md:3` is dated "Generated: 2026-03-31" but is not in fact regenerated by anything — grep shows it is referenced only from `INDEX.md`, never re-emitted. It scores 15 named sibling repos (best-practices, genealogy, security-architect-mcp, blog, ...) on a 10-dimension hand-built rubric. Several of those repos are now stale per the workspace's own records — `security-architect-mcp` is "abandoned-as-brand May 2026" and `blog` was "RETIRED 2026-05-24 / archived read-only 2026-06-05" per the project1 CLAUDE.md cross-repo map — yet the matrix still lists them as GOOD. This is a frozen snapshot masquerading as current state: a hand-curated compliance table that decays the moment the underlying repos change and has no regeneration path. The bitter-lesson reading is that a per-repo audit *generated on demand* (which is exactly what this repo's own one-prompt audit produces) makes a static cross-repo matrix redundant — the matrix is the hand-built artifact the adaptive audit was designed to replace.

**Evidence**: `V2-COMPLIANCE-MATRIX.md:3,26,28` (stale `security-architect-mcp` / `blog` rows scored GOOD); referenced only from `INDEX.md`; project1 `.claude/CLAUDE.md` cross-repo map marks both repos retired/abandoned.

**Recommendation**: Either move `V2-COMPLIANCE-MATRIX.md` to `archive/` with a dated "snapshot, not maintained" banner, or replace it with a generated artifact that runs the repo's own audit across the live repo list. Do not leave it linked from `INDEX.md` as if it were current state — a reader can't tell a snapshot from a live dashboard, which is the same legibility failure the repo flags for generated docs elsewhere.

---

### Finding 5 — Bitter-lesson self-awareness is genuinely strong; the repo applies the diagnostic to others but never runs it on its own 42-doc footprint (MEDIUM)

Credit where due, then the gap. The repo's bitter-lesson posture is one of its best features: `analysis/harness-engineering.md:218-234` lays out Sutton's argument and the "built for deletion" discipline; `PLAN.md:39` runs an active "monitor first-party feature convergence for retirement" lane that actually retired `session-quality-tools.md` when `/insights` shipped; `analysis/harness-engineering.md:242-257` tracks which custom patterns the platform absorbed into native primitives (`/goal`, `worktree.bgIsolation`, per-category `/usage`). The repo also keeps the audit prompt deliberately thin (`ONE-LINE-PROMPT.md:19`) precisely so the prompt and the routing map don't drift — a bitter-lesson-aligned choice.

The gap is that `AUDIT-CONTEXT.md:126` offers a "Bitter Lesson diagnostic" row (`harness-comprehensive`: "is the harness buying you anything, or accreting complexity?") that the repo points at *other* projects and never at itself. The repo now carries 42 analysis docs, 8 memory-system archetype files, multiple near-overlapping memory docs, and a routing table that has grown a "Unattended / Long-Running Execution" section, a two-level memory sub-route, and a volatile Fable-5 row. Some of that growth is necessary coverage; some is accretion that a more general framing (or a first-party feature) may shortly obsolete. There is no scheduled self-application of the `harness-comprehensive` question to this repo's own surface area — no "which of these 42 docs earned its place this quarter, which got absorbed by a native feature, which should merge."

**Evidence**: `analysis/harness-engineering.md:218-257`; `PLAN.md:39` (retirement lane); `AUDIT-CONTEXT.md:126` (diagnostic offered outward only); 42 docs + 8 archetype files + grown routing sections.

**Recommendation**: Add a recurring (e.g., quarterly, alongside the existing obsolescence sweep) self-application of the `harness-comprehensive` / Bitter-Lesson diagnostic to this repo — a short checklist: which docs were absorbed by a first-party feature since last sweep, which two docs now overlap enough to merge, which routing rows fire so rarely they are noise. The machinery (the retirement lane) already exists; it just is not turned on the repo's own doc footprint. This is the "minimal eval" answer for the bitter-lesson half: not a benchmark, a scheduled pruning question.

---

### Finding 6 — `revalidate-by` dates are honor-system across the corpus, and the date the gate would have caught has already passed (MEDIUM)

Distinct from Finding 1 (the gate is misconfigured), this is about coverage: even a fixed gate only checks docs that carry `measurement-claims` frontmatter with `revalidate` sub-dates. Many analysis docs carry a top-level `revalidate-by` (e.g., `analysis/evidence-tiers.md:4` → 2026-10-22) that the expiry script does **not** read — it only parses the nested `measurement-claims[].revalidate` field (`scripts/check-measurement-expiry.py:102`). So the top-level `revalidate-by` dates are pure honor-system with no automated check at all, which is the failure mode `analysis/evidence-based-revalidation.md:188` names. Today is 2026-06-21; several docs carry `revalidate-by: 2026-10-22` (not yet due, fine), but the *nested* claims in `mcp-patterns.md` were due 2026-03-20 and nothing surfaced them. The pattern: the repo has two parallel expiry fields (`revalidate-by` top-level, `measurement-claims[].revalidate` nested), and the automated checker reads only one of them, on a directory it can't see.

**Evidence**: `scripts/check-measurement-expiry.py:102` (reads only nested `revalidate`); `analysis/evidence-tiers.md:4` and many docs carry an unchecked top-level `revalidate-by`; `analysis/evidence-based-revalidation.md:188`.

**Recommendation**: After fixing the directory target (Finding 1), extend the checker to also read the top-level `revalidate-by` field, so the dominant expiry annotation in the corpus is actually gated. Then the two fields are either both checked or consolidated to one.

---

## What the minimal eval would be

Pulling the "what does better mean" thread to a concrete answer, the cheapest eval that would tell this repo whether it is improving is three deterministic, model-free checks, all runnable in CI on PR:

1. **Expiry gate, fixed** (Finding 1 + 6): point the existing script at `analysis/`, read both expiry fields, fail on overdue. The repo already has the script; it needs two one-line fixes.
2. **Routing-determinism fixtures** (Finding 2): 3-5 synthetic repos with expected signal-key + fetched-doc manifests, diffed. Golden-answer comparison on the routing layer, no LLM.
3. **Sync linter** (Finding 3): parse `applies-to-signals` vs routing-table keys, fail on drift. The doc already says this "must" exist.

None of the three need a model in the loop, none need Anthropic to publish guidance (the `PLAN.md:38` deferral reason), and together they would catch the three ways the repo can silently rot: stale claims, broken routing, and orphaned docs. The LLM-judged "are the recommendations actually good" eval is the genuinely hard part and is reasonably deferred — but deferring the deterministic half too is what left a 93-day-overdue claim shipping under a green CI badge.
