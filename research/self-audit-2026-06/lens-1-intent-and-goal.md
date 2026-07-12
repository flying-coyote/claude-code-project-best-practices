---
lens: intent-and-goal
prompts:
  - "Fable #1 goal-orientation"
  - "Fable #3 self-model"
  - "Fable #9 ikigai/big-picture"
  - "Fable #13 the-one-real-constraint"
date: 2026-06-21
repo: /home/jerem/claude-code-project-best-practices
convergence: single-source
---

# Lens 1 — Intent and Goal

Applying four Miessler "Fable" prompts to the best-practices repo itself: what is it *for* (#1), does it hold an accurate model of itself (#3), where does it sit in the bigger picture (#9), and what single thing most limits its usefulness (#13).

## What the repo is for (Fable #1, goal-orientation)

The README states the goal cleanly: "A portable, evidence-based audit you can run against any Claude Code project to get recommendations specific to *that project* — not generic best-practice advice." The mechanism is the adaptive routing audit (`AUDIT-CONTEXT.md` + `ONE-LINE-PROMPT.md`): collect signals from a target repo, route to 4-8 of 42 analysis docs, emit recommendations that each cite signal + source doc + evidence tier. That goal is coherent and the structure mostly serves it — the routing map, the anti-bloat rule, the output format, and the per-doc `applies-to-signals` frontmatter all exist to make the one-prompt audit work. On the goal-orientation prompt the repo scores well: it knows what job it does and the load-bearing files are built for that job.

The weakness is that the goal is stated in three incompatible ways across the identity docs (see Finding 1). A reader who opens `package.json` first ("a curated collection of patterns and prompts") or `ARCHITECTURE.md` first ("the Consumer Reports for Claude Code tooling") gets a materially different answer than the README gives, and `DECISIONS.md` opens with eight decisions about a bootstrap/preset/wizard product the repo no longer is.

## Whether the repo models itself accurately (Fable #3, self-model)

This is where the audit is weakest. The repo's authoritative-looking self-description in `ARCHITECTURE.md` is a stale snapshot from April 13: it claims 26 analysis documents (the README, PLAN, INDEX, and the actual `analysis/` directory all say 42-43), it cites the wrong GitHub URLs and star counts for its two sibling projects, and it describes a directory tree that no longer matches the repo. A best-practices project whose own ARCHITECTURE.md fails the staleness check it teaches others to run has an inaccurate model of itself. The framework for catching exactly this — `evidence-based-revalidation.md`, the `revalidate-by` cadence, the generated-docs-drift signal — is the repo's own content, applied to everyone except itself.

## The bigger picture (Fable #9, ikigai/big-picture)

The three-project framing (this repo = evidence/analysis; everything-claude-code = tooling; superpowers = methodology) is a genuine niche and the README's "What It Is *Not*" section defends it honestly. The unique-value claims (evidence tiers, ~80% CLAUDE.md adherence, MCP-vs-Skills economics, model-migration anti-patterns, memory archetypes) do appear to be absent from the two siblings, so the differentiation is real rather than asserted. The big-picture story holds. What is missing from it is any signal that the artifact is *used* — no adoption evidence, no captured audit run, no dogfood output (see Finding 4).

## The one real constraint (Fable #13)

The single biggest limit on this repo's usefulness is that **the audit has never been demonstrated end-to-end** — there is no captured audit output anywhere in the repo, not even a self-audit of this repo, which is the obvious dogfood. The entire value proposition ("run this one prompt, get cited recommendations") rests on a 65-line protocol spread across `AUDIT-CONTEXT.md` and `ONE-LINE-PROMPT.md` that no committed artifact shows actually executing and producing the promised output. Everything else — doc count, license, prose polish — is downstream of this. If the audit produces a good result, the staleness and license bugs are footnotes; if it does not, the 42 polished docs are a library nobody can route into. That is the constraint worth fixing first.

---

## Findings

### Finding 1 — The repo gives three incompatible answers to "what is this" (self-model fragmentation)

**Severity**: medium

**Evidence**: `README.md:3` ("a portable, evidence-based audit you can run against any Claude Code project"); `ARCHITECTURE.md:10` ("an evidence-based analytical layer ... the 'Consumer Reports' for Claude Code tooling"); `package.json:4` ("A curated collection of patterns and prompts for AI-driven software development"); `DECISIONS.md:5-173` (Decisions 1-8 describe a bootstrap/preset/wizard tool with `MAKE-PROJECT-RECOMMENDATIONS.md`, four presets, infrastructure tiers). These are three different products: an audit tool, an analytical reference library, and a project-bootstrapper. The bootstrapper identity was archived in the v2.0 repositioning (`DECISIONS.md:445`) but its decision records still open the file unlabeled.

**Recommendation**: Pick one canonical one-sentence answer (the README's audit framing is the right one) and make the other three surfaces defer to it. Update `package.json` description to match; add a one-line "what this is" banner to the top of `ARCHITECTURE.md` that matches the README; prepend a "Decisions 1-8 describe the pre-v2.0 bootstrap product, superseded — see Decision 'Reposition as Analytical Layer'" note to `DECISIONS.md` so the historical records do not read as the current self-model.

### Finding 2 — ARCHITECTURE.md is a stale, self-contradicting self-model

**Severity**: high

**Evidence**: `ARCHITECTURE.md` "Last Updated: April 13, 2026" and claims **26** analysis documents at lines 33, 46, 108, 133, with a directory tree listing exactly those 26. The README (`README.md:82`), `PLAN.md:20`, `INDEX.md:7` (analysis: 43), and the live `analysis/` directory all say **42 routable docs / 43 files**. ARCHITECTURE also gives wrong sibling-repo URLs (`anthropics-solutions/everything-claude-code` at line 18, `obraun-cl/superpowers` at line 20) which contradict the README's real URLs (`affaan-m/everything-claude-code`, `obra/superpowers`) and a stale star count (110K at line 107 vs the README's 119K). The repo's own `generated-docs-no-drift-gate` and `revalidation-trigger` signals exist precisely to catch this.

**Recommendation**: Rewrite ARCHITECTURE.md to the current 42-doc reality, or replace its hand-maintained doc tree with a pointer to the auto-generated `INDEX.md` so it cannot drift again. Fix the two sibling URLs to match the README's verified ones. Add a `revalidate-by` date. This is the highest-severity finding because the repo teaches staleness-detection and fails it on its own primary design doc.

### Finding 3 — License declared three ways, with no LICENSE file

**Severity**: medium

**Evidence**: `README.md:203` says "MIT License." `package.json:19` says `"license": "ISC"`. There is no `LICENSE` file in the repo root (confirmed: `ls LICENSE*` returns nothing). `package.json:3` also pins `"version": "1.0.0"` while every narrative doc calls the project v2.1. For a public repo whose stated purpose is to be referenced and reused ("MIT License — use freely"), an ambiguous and unfiled license is a real adoption blocker, not a cosmetic one.

**Recommendation**: Decide MIT (the README's intent), add a root `LICENSE` file with the MIT text, and change `package.json` `"license"` to `"MIT"`. Bump `package.json` `"version"` to `2.1.0` to match the documented project version, or drop the field if npm versioning is not meaningful for a docs repo.

### Finding 4 — The audit has no demonstrated end-to-end run (the one real constraint)

**Severity**: high

**Evidence**: The whole value proposition is the one-prompt adaptive audit (`README.md:53-67`, `ONE-LINE-PROMPT.md`). No committed file anywhere contains the promised output: a search for the audit's own output markers (`audit-date:` / `repo-name:` from the `ONE-LINE-PROMPT.md` Structured Output Format) finds only the template in `ONE-LINE-PROMPT.md` itself — no actual run. `examples/` contains only an archived v1 `research-project` README, not an audit output. `PLAN.md` and `README.md` carry no adoption, usage, or feedback evidence. The repo cannot point to a single instance of its core mechanism working, including on itself.

**Recommendation**: Run the audit against this repo and commit the output as `examples/self-audit-output.md` (a true dogfood — it would also have caught Findings 2 and 3 mechanically). Then run it against one external repo and commit that output too. Two committed sample runs convert the audit from an untested protocol into a demonstrated capability, and give contributors a regression fixture to diff against when the routing map changes.

### Finding 5 — Structure genuinely serves the goal (what is fine — do not change)

**Severity**: low

**Evidence**: The routing machinery is coherent and self-consistent where it matters most: `AUDIT-CONTEXT.md` phrases every signal as an agent-verifiable command (lines 20-68), documents edge cases so the audit degrades rather than fails (lines 70-84), enforces the anti-bloat budget deterministically (lines 203-215), and maintains a signal-vocabulary invariant tying routing rows to per-doc frontmatter (lines 242). The README's "What It Is *Not*" (`README.md:45-49`) honestly cedes the tooling and methodology lanes to named siblings rather than overclaiming. The evidence-tier discipline (signal + source + tier on every recommendation) is applied consistently across `AUDIT-CONTEXT.md`, `ONE-LINE-PROMPT.md`, and the worked examples. This is real structural fitness-for-purpose and should be preserved as-is; the findings above are drift and demonstration gaps around a sound core, not a flawed design.

**Recommendation**: No change to the routing design. When fixing Findings 1-4, keep the README + `AUDIT-CONTEXT.md` + `ONE-LINE-PROMPT.md` trio as the canonical identity surface and let the weaker docs (ARCHITECTURE, package.json, DECISIONS) defer to it rather than restate it.

---

## Top recommendation

Fix the one real constraint first: run the audit against this repo and one external repo and commit both outputs under `examples/` (Finding 4). A self-audit run is also the cheapest mechanical fix for the staleness and license drift (Findings 2-3), because the audit's own staleness and generated-doc signals would surface them — closing the gap between what the repo teaches and what the repo demonstrates about itself.
