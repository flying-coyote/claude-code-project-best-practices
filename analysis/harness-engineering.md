---
version-requirements:
  claude-code: "v2.1.0+"
version-last-verified: "2026-03-30"
measurement-claims:
  - claim: "Frontier models score 90%+ on benchmarks but only 24% on real professional tasks"
    source: "Prompt Engineering YouTube - The AI Model Doesn't Matter Anymore"
    date: "2026-02-01"
    revalidate: "2026-08-01"
  - claim: "Vercel text-to-SQL: removing 80% of tools improved accuracy from 80% to 100%"
    source: "Prompt Engineering YouTube (citing Vercel experiment)"
    date: "2026-02-01"
    revalidate: "2026-08-01"
  - claim: "everything-claude-code: 136+ skills, 30 subagents, 119K+ stars"
    source: "GitHub repository analysis"
    date: "2026-03-30"
    revalidate: "2026-09-30"
  - claim: "superpowers: 294K+ installs, 7-stage mandatory workflow"
    source: "Claude plugin directory + GitHub repository"
    date: "2026-03-30"
    revalidate: "2026-09-30"
  - claim: "NLH representation: 30.4% to 47.2% performance, 1200 to 34 LLM calls"
    source: "Pan et al. (Tsinghua + Harbin IT), arXiv:2603.25723"
    date: "2026-03-26"
    revalidate: "2026-09-26"
  - claim: "Verifiers hurt performance: -0.8 SWE-bench, -8.4 OS World"
    source: "Pan et al. (Tsinghua + Harbin IT), arXiv:2603.25723"
    date: "2026-03-26"
    revalidate: "2026-09-26"
  - claim: "Meta-Harness: Rank 1 TerminalBench 2 with Haiku 4.5 via harness optimization"
    source: "Lee, Nair, Zhang, Lee, Khattab, Finn (Stanford + MIT), arXiv:2603.28052"
    date: "2026-03-30"
    revalidate: "2026-09-30"
  - claim: "6x performance gap from harness changes alone on the same benchmark"
    source: "Lee et al., Meta-Harness, arXiv:2603.28052 (paper's headline quote)"
    date: "2026-03-30"
    revalidate: "2026-09-30"
  - claim: "Independent 6x corroboration: Opus 4.5 scores 12% on Cursor vs 2% on OpenCode"
    source: "Tian et al., SWE-Bench Mobile, arXiv:2602.09540"
    date: "2026-02-10"
    revalidate: "2026-08-10"
  - claim: "v2 DAW built in 4 hours for $125 after harness simplification"
    source: "Anthropic engineering blog"
    date: "2026-04-01"
    revalidate: "2026-10-01"
status: PRODUCTION
follows: "Willison 'designing agentic loops' canon (simonwillison.net/tags/coding-agents/) + Ronacher inner-vs-outer-loop essays (lucumr.pocoo.org — 'The Coming Loop', 2026-06-23) + Osmani own-the-outer-loop (addyosmani.com/blog/agentic-engineering/) (Tier B practitioner canons, verified 2026-07-16) — the harness-design commentary layer. Bar status: fails Supported (blog-form canons). Delta kept here: the Bitter-Lesson diagnostic, accretion heuristics, and portfolio measurements — verified 2026-07-16 that no canon or framework carries these (superpowers v6.1.1: zero 'bitter lesson' hits; the diagnostic is applied TO it in this doc). Advance trigger: a Supported harness-design guide (first-party or maintained community) absorbing the diagnostic function."
last-verified: "2026-07-16"
evidence-tier: Mixed
convergence: converged  # vendor-official (Anthropic best-practices page + engineering blog) + independent academic (arXiv:2603.28052, arXiv:2603.25723) + LangChain + mass-adopted community frameworks — all cited in-doc
applies-to-signals: [harness-hooks, harness-minimal, harness-comprehensive, commit-bursts, session-error-loop, model-version-4-8, harness-goal-completion-loop, harness-dynamic-workflows]
revalidate-by: 2026-11-30
---

# Harness Engineering: Diagnostic Framework for Agent Infrastructure

> **Collapsed 2026-07-10 (Reduction Phase 4).** The harness-design mechanism half is now first-party — Anthropic's official best-practices page (2026 rewrite) and "How Claude Code works in large codebases" (2026-05-14). This doc keeps the delta the official docs don't carry: the Bitter-Lesson diagnostic, the accretion heuristics, and the portfolio's measured evidence.

**Evidence Tier**: Mixed (A-B) — Anthropic engineering blog, expert practitioners, production-validated community frameworks

> **Following the Willison/Ronacher/Osmani harness canons since 2026-07-16.** New coverage effort on harness-design commentary goes to tracking those canons, not growing this doc. Delta kept: the Bitter-Lesson diagnostic, accretion heuristics, portfolio measurements.

## Purpose

This document evaluates **harness engineering** against two standing questions that recur every model release: whether a piece of harness machinery still earns its keep once the model gets smarter (the Bitter-Lesson diagnostic), and whether the harness has accreted complexity nobody has pruned back out (the accretion heuristics). Mechanism selection — which extension point to reach for, CLAUDE.md vs. hooks vs. skills vs. plugins vs. LSP — is now covered by Anthropic's official best-practices page and the "How Claude Code works in large codebases" guide (2026-05-14); this document doesn't re-derive that ground. What it keeps is the portfolio's measured evidence and the failure modes those two sources don't cover.

For domain-heavy projects (complex rule ecosystems, specialized tooling), see the companion document: [Domain Knowledge Architecture](./domain-knowledge-architecture.md).

---

## The Harness Thesis

> "The model is not the bottleneck; the harness is."
> — Prompt Engineering, "The AI Model Doesn't Matter Anymore" (February 2026)

The central claim: in 2026, raw model capability is becoming commoditized, so the infrastructure wrapped around the model — what it can see, what tools it can use, how it recovers from mistakes, how it tracks progress — determines whether an agent actually works. A study cited in that video found frontier models scoring 90%+ on standard benchmarks but only **24%** on real professional tasks (1-2 hours), rising to **~40%** after 8 attempts. Researchers traced the gap to execution and orchestration rather than model intelligence: agents got lost after too many steps, looped back to approaches already tried and failed, and lost track of their original objective. Those are harness problems, not model problems — the same three failure patterns recur later in this document as the RETHINK-limb diagnostic.

---

## Harness Representation and Optimization

Research from March 2026 shows that **how** a harness is expressed and optimized matters independently of what it does.

### Natural Language Harness (NLH) Representation Gains

Migrating OS Symfony's native code harness into a Natural Language Harness representation produced dramatic improvements:

| Metric | Native Code Harness | NLH Representation | Change |
|--------|--------------------|--------------------|--------|
| Performance | 30.4% | **47.2%** | +55% relative |
| Runtime | 361 min | **141 min** | -61% |
| LLM calls | 1,200 | **34** | -97% |

The harness did the same thing in both cases — the representation changed. This suggests that expressing harness logic in natural language (closer to the model's native reasoning) is a distinct optimization axis from harness design itself.

Source: Pan, Zou, Guo, Ni, Zheng (Tsinghua University + Harbin Institute of Technology), ["Natural-Language Agent Harnesses"](https://arxiv.org/abs/2603.25723), 2026-03-26.

### Ablation Evidence: Verifiers Hurt, Self-Evolution Helps

The same Tsinghua/Harbin paper (Pan et al., arXiv:2603.25723) ran ablation studies on harness modules:

| Module | SWE-bench Impact | OS World Impact | Net Effect |
|--------|-----------------|-----------------|------------|
| Verifiers | **-0.8** | **-8.4** | Hurt performance |
| Multi-candidate search | **-2.4** | **-5.6** | Hurt performance |
| Self-evolution (narrowing the agent's own attempt loop) | **+4.8** | **+2.7** | **Only consistently helpful module** |

**Key nuance for harness design**: explicit verifier modules — separate components that check the agent's work — actively degraded performance. The agent's own iterative refinement (self-evolution) was the only module that consistently helped.

**Caveat**: this is benchmark evaluation, not production deployment. Production environments with real consequences may benefit from verification that benchmarks don't reward. But the default assumption should be: let the agent self-correct rather than bolting on external verifiers.

Source: Pan et al. (Tsinghua + Harbin IT), arXiv:2603.25723, 2026-03-26.

### Meta-Harness: Automated Harness Optimization

Lee, Nair, Zhang, Lee, Khattab, Finn (Stanford + MIT) treat the harness itself as an optimization target:

- An agentic proposer reads failed execution traces
- It diagnoses breakages and writes a complete new harness
- Cost: ~10M tokens per iteration, 82 files read per round
- Result: **76.4% on TerminalBench-2 with Opus 4.6** (rank 2 among Opus agents) and **37.6% with Haiku 4.5** (rank 1 among Haiku agents, outperforming Goose at 35.5%) — a smaller, cheaper model outranking larger ones through harness optimization alone

**Cross-model transfer**: a harness optimized on one model transferred to five others, improving all of them (+7.7 points on text classification using 4× fewer context tokens; +4.7 points on IMO-level math across five held-out models). This is strong evidence that harness quality is model-independent — good infrastructure helps any model.

**Convergence note**: Andrej Karpathy (Authority 4/5) independently described the same concept — meta-optimization of program.md — without referencing the Stanford+MIT work.

Source: Lee, Nair, Zhang, Lee, Khattab, Finn (Stanford + MIT), ["Meta-Harness: End-to-End Optimization of Model Harnesses"](https://arxiv.org/abs/2603.28052), 2026-03-30.

### 6× Performance Gap from Harness Changes Alone

The Meta-Harness paper states it as the headline finding: *"Changing the harness around a fixed large language model (LLM) can produce a 6× performance gap on the same benchmark."* No model changes, no prompt changes — purely orchestration code.

**Specific replication with full citation**: LangChain's terminal-bench-2 submission moved from outside the top 30 to rank 5 by changing only the harness code. LangChain published the work as ["Improving Deep Agents with Harness Engineering"](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering) (2026-02-17): deepagents-cli went **52.8% → 66.5% on TerminalBench-2** (13.7 points) holding gpt-5.2-codex constant, via five documented middleware changes: (1) a self-verification loop (`PreCompletionChecklistMiddleware`), (2) startup directory/tooling mapping (`LocalContextMiddleware`), (3) per-file edit-count loop detection for "doom loops," (4) a "reasoning sandwich" effort allocation (xhigh-high-xhigh) across plan/build/verify, and (5) time-budget warnings.

**Independent benchmark corroboration**: Tian et al. *SWE-Bench Mobile* ([arXiv:2602.09540](https://arxiv.org/abs/2602.09540), 2026-02-10) reports the same model (Opus 4.5) scoring **12% on Cursor vs 2% on OpenCode** across 22 agent-model configurations — exactly 6×, in a separate venue, on a separate benchmark, from scaffold differences alone.

Source: Lee et al., Meta-Harness, arXiv:2603.28052 (primary); Tian et al., SWE-Bench Mobile, arXiv:2602.09540 (independent corroboration).

---

## The "Less Is More" Evidence

The strongest and most counterintuitive finding across all sources.

### The Vercel Experiment

Vercel built a text-to-SQL agent with specialized tools: one for understanding database schemas, one for writing queries, one for validation. Complex error handling. It worked about 80% of the time.

Then they removed 80% of the agent's tools. They gave it basic capabilities — bash, grep, cat.

| Metric | Specialized Tools | General-Purpose Tools | Change |
|--------|------------------|----------------------|--------|
| Accuracy | 80% | **100%** | +25% |
| Token usage | Baseline | **40% of original** | -60% |
| Speed | Baseline | **3.5x faster** | +250% |

### The Manus Experience

Manus (acquired by Meta) rebuilt their agent framework five times in six months. Their biggest performance gains came from **removing features** — ripping out complex document retrieval and fancy routing logic, replacing them with general-purpose shell executions and structured handoffs.

They also solved a critical memory problem: tasks requiring ~50 tool calls caused performance degradation even with large context windows (signal drowned by noise). Solution: treat the file system as external memory. Write important information to markdown files; read when needed.

### The Bitter Lesson (Richard Sutton, Applied to Agents)

Sutton's core argument: approaches that scale with computational power always beat approaches relying on human-engineered domain knowledge.

Applied to agent harnesses: **as models get smarter, your harness should get simpler**. If you are adding hand-coded logic and specialized routing with every model upgrade, you are swimming against the current.

> "Every piece of your harness should be built for deletion — ready to be removed when the model no longer needs it."

### v2 Harness Simplification (Anthropic, April 2026)

Anthropic's Claude Code v2 with Opus 4.6 provides concrete evidence for "harness should simplify as models improve":

- **Removed**: Sprints, contract negotiation, context resets
- **Replaced with**: Single build session with evaluator at the end only
- **Result**: DAW built in 4 hours for $125

This is a vendor demonstrating the Bitter Lesson on their own product — stripping orchestration complexity because the model no longer needs it. The evaluator-at-the-end pattern also matches the ablation evidence above: self-evolution during work, verification only at completion.

The generator/evaluator pattern this simplifies traces to Anthropic's primary write-up: Prithvi Rajasekaran, ["Designing a harness for long-running application development"](https://www.anthropic.com/engineering/harness-design-long-running-apps) (2026-03-24, Tier A) — three agents (planner/generator/evaluator), a Playwright-driven evaluator scoring quality/originality/craft/functionality across 5–15 iterations, ~4 hours at ~$200/6hr versus ~$9/20min for a single-agent pass. It's also the source of the self-evaluation caution this document leans on: agents asked to grade their own work "tend to respond by confidently praising the work — even when... the quality is obviously mediocre," which is why verification belongs in a separate evaluator rather than the generator's own self-report.

**Caveat — vendor-side regression in the same window**: the same vendor shipped a quality regression spanning March 4 – April 20, 2026 ([April 23 postmortem](https://www.anthropic.com/engineering/april-23-postmortem)) — reasoning-effort default flipped to `medium`, an extended-thinking-block caching bug, and a system-prompt verbosity cap that hurt coding quality. None of these invalidate the v2 simplification thesis (the orchestration changes were a separate workstream), but they demonstrate that "trust the vendor's defaults" is the wrong reading. Harness designers should pin effort levels explicitly and treat vendor-side defaults as version-anchored. See [Behavioral Insights — April 2026 Postmortem](behavioral-insights.md#vendor-side-quality-regression-case-study-the-april-2026-postmortem) for the full analysis.

Source: Anthropic engineering blog, April 2026. Authority 5/5.

### Loop Engineering and the RETHINK Limb

"Loop engineering" (Boris Cherny, June 2026; term coined by Addy Osmani) labels the orchestration and iteration-cadence layer this document already covers: GENERATE → SELECT → EVALUATE → ACCUMULATE → PUBLISH → RETHINK. It doesn't replace the harness-engineering framing — it stresses cadence, where harness engineering is the whole infrastructure stack — but splitting the loop into stages shows one recurring pattern: the Act stages (generate, evaluate, publish) get built first and hardest, while RETHINK — re-deriving the question the loop is answering before the next iteration — is usually weak or missing. Karpathy's complementary framing is that coding is the ideal self-improvement loop because it has built-in verification — "tests pass or fail, programs run or crash, diffs can be inspected" (Tier B, [Sequoia Ascent 2026](https://karpathy.bearblog.dev/sequoia-ascent-2026/), 2026-04-30) — but that verification keeps the Act limb honest without ever asking whether the loop is still solving the right problem. In harness terms, RETHINK isn't a new layer; it's the part of state-tracking and verification that checks the objective itself, not just the work toward it. A fast Act limb paired with a stale Orient limb produces confident motion toward the wrong target — the same failure the 24%-on-real-tasks study attributed to agents that "lost track of their original objective" and "looped back to approaches already tried."

A single-practitioner instance makes the fix concrete (Tier B, not independently reproduced): a security-data research project scored its own loop in [`LOOP-ENGINEERING-DESIGN-2026-06-15.md`](../../project1/02-projects/securitydataworks/LOOP-ENGINEERING-DESIGN-2026-06-15.md), found GENERATE/EVALUATE strong but RETHINK absent — gap G4, "no standing question-quality / drift instrument — the human is the instrument" — and wired the fix in as a step-0 ORIENT opening every iteration of two standing loop-state machines ([`BENCH-LOOP-STATE.md`](../../project1/02-projects/securitydataworks/BENCH-LOOP-STATE.md), [`CONSOLE-LOOP-STATE.md`](../../project1/02-projects/securitydataworks/CONSOLE-LOOP-STATE.md)). The productized scheduling primitives (`/loop`, `/goal`, Routines) get their own treatment in [Scheduled & Looping Primitives](scheduled-and-looping-primitives.md); the generalized "does each mechanism still match its intent?" pass is [Intent-Alignment Audit](intent-alignment-audit.md).

### Counter-signal: Opus 4.7 Pushes *Prompt* Complexity Up (April 2026)

The Bitter Lesson predicts monotonic simplification as models improve. Opus 4.7 complicates the picture: the *harness* continues to simplify (Anthropic's migration guide confirms "fewer subagents spawned by default," "fewer tool calls by default"), but the *prompt* may need to be **more explicit**, not less.

4.7's literal interpretation (see [Model Migration Anti-Patterns](model-migration-anti-patterns.md)) means instructions that 4.6 successfully generalized now fail silently. Remediation per the Anthropic migration guide: enumerate cases, anchor triggers, declare dispatch mechanism, add verbosity directives. These are prompt-side additions, not harness-side.

**Diagnostic split for 4.7**:

| Layer | Direction | Evidence |
|---|---|---|
| Harness (orchestration, tooling, subagent wiring) | ↓ Simpler | Anthropic migration guide: fewer default subagents, fewer tool calls |
| Prompt (instructions, CLAUDE.md, skill bodies) | ↑ More explicit | Anthropic migration guide: literal interpretation, no silent generalization |

This does not invalidate the Bitter Lesson — the *orchestration* around the model is still simplifying. But the prompt itself is a joint product of human intent and model inference, and 4.7 shifts the inference burden back to the human. Treat this as version-scoped: a future model that re-adds intent inference would reverse the prompt-complexity pressure.

Source: Anthropic migration guide (April 2026), [Model Migration Anti-Patterns](model-migration-anti-patterns.md). Authority 5/5 (Tier A).

**Opus 4.8 update (2026-05-28)**: the prompt-side pressure *persists* — 4.8 keeps the literal-interpretation posture, so the prompt-complexity guidance above is unchanged. Three 4.8 deltas do touch the harness layer and are worth re-tuning for ([4.8 docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8), Tier A):

| 4.8 delta | Harness-layer implication |
|---|---|
| **Fewer compactions + better compaction recovery** ("long agentic traces stay on task with fewer derailments after compaction") | Compaction-timing heuristics tuned on 4.7 are likely *too aggressive* on 4.8. The document-and-clear / fresh-session discipline (and the 60% context trigger in [Behavioral Insights](behavioral-insights.md)) remains the safe default, but re-measure before assuming the same intervention cadence — 4.8 may sustain longer traces between resets. Do not assume a fixed token threshold carried over from 4.7. |
| **Better tool triggering** ("less likely to skip a tool call the task required") | The harness still needs mechanical enforcement (PreToolUse hooks, explicit Read steps) for 100%-adherence requirements — the improvement is a frequency reduction, not a guarantee. But the "references not read" symptom that pushed users toward heavy enforcement scaffolding is *softer* on 4.8; audit whether some belt-and-suspenders enforcement can be relaxed. |
| **Adaptive thinking is the only thinking mode; extended-thinking budgets return 400; default effort `high`** | Any harness or skill still passing `thinking: {type: "enabled", budget_tokens: N}` will hard-fail with a 400 on 4.8. Migrate to `thinking: {type: "adaptive"}` + the `effort` parameter (`low`/`medium`/`high`/`xhigh`). The reasoning-budget allocation pattern (e.g., LangChain's "reasoning sandwich" xhigh-high-xhigh across plan/build/verify, cited above) is expressed via *effort levels* in Claude Code and is unaffected — but any raw-API harness using numeric token budgets must be ported. |

This is a recovery release for harness purposes: 4.8 reduces the 4.7 failure modes that most stressed the harness (compaction derailment, skipped tool calls), while the one hard-breaking change is the extended-thinking-budget 400.

---

## Three Harness Philosophies: The Bitter-Lesson Read

Three community approaches sit at different points on the Bitter-Lesson spectrum. Everything-Claude-Code (ECC) is batteries-included — 136+ skills, 30 subagents, 60+ commands, 119K+ GitHub stars, an Anthropic hackathon winner — and ranks lowest on Bitter-Lesson alignment: its runtime profiles (`ECC_HOOK_PROFILE=minimal`) let you dial complexity down, but the default trajectory adds tooling with each release, working against the Vercel/Manus evidence above. Superpowers is methodology-enforced — a mandatory 7-stage workflow, ~14 skills, 294K+ installs — and ranks in the middle: it enforces process without adding tools, so it doesn't accrete the way ECC does, though the ceremony has a real cost on small tasks. Anthropic's own minimal approach (CLAUDE.md + progress file, a 2-agent architecture, external artifacts as memory) ranks highest: it's the one most clearly built for deletion. GitHub stars and plugin installs are different metrics measuring different things — useful within their own claim, not comparable to each other.

---

## Anti-Patterns

| Anti-Pattern | Source | Symptom | Fix |
|-------------|--------|---------|-----|
| Tool proliferation | Vercel experiment | Low accuracy despite many specialized tools | Strip to general-purpose tools |
| Context stuffing | Manus experience | Performance degrades at 50+ tool calls | File system as external memory |
| Hook storms | ECC patterns | Excessive token consumption from cascading hooks | Runtime profiles (`ECC_HOOK_PROFILE=minimal`) |
| Ceremony overhead | Superpowers pattern | Small tasks take disproportionate time | Scale harness to task complexity |
| Configuration drift | Anthropic minimal | Team members get inconsistent results | Hooks for enforcement + shared settings.json |
| Swimming against the current | Bitter Lesson | Harness complexity grows with each model upgrade | Build every component for deletion |
| Harness-as-specification neglect | Video thesis | Building agent first, retrofitting tests later | Define harness (behavioral tests) before agent logic |
| Accretion without pruning | Practitioner heuristic | Repo accumulates custom code and raw captures the model must re-read each session | Necessity ladder before writing code (see [Secure Code Generation](./secure-code-generation.md)); archive or delete superseded material |

---

## The "Model Doesn't Matter" Thesis: Evaluation

### Evidence Supporting the Thesis

| Evidence | Source | Tier |
|----------|--------|------|
| Harness design was the breakthrough for long-running agents | Anthropic engineering blog (Nov 2025) | A |
| 90%+ on benchmarks / 24% on real tasks — the gap is harness | Research study cited in video | B |
| Removing tools improved accuracy, speed, and cost (Vercel) | Vercel experiment cited in video | B |
| Removing features was the primary optimization (Manus) | Manus context engineering (5 rebuilds) | B |
| Same harness works across Claude Code, Cursor, OpenCode, Codex | everything-claude-code cross-platform support | B |
| Boris Cherny's success depends on parallel sessions, hooks, permissions — all harness | Boris Cherny interviews (March 2026) | A |
| NLH representation: same harness logic, 30.4% → 47.2% perf + 1200 → 34 LLM calls | Pan et al. (Tsinghua + Harbin IT), [arXiv:2603.25723](https://arxiv.org/abs/2603.25723) (March 2026) | B |
| Meta-Harness: Haiku 4.5 ranks #1 among Haiku agents on TerminalBench-2 via harness optimization alone | Lee, Nair, Zhang, Lee, Khattab, Finn (Stanford + MIT), [arXiv:2603.28052](https://arxiv.org/abs/2603.28052) (March 2026) | B |
| **"Changing the harness around a fixed LLM can produce a 6× performance gap on the same benchmark"** (paper's headline quote) | Lee et al., Meta-Harness, [arXiv:2603.28052](https://arxiv.org/abs/2603.28052) (March 2026) | B |
| Independent corroboration: Opus 4.5 scores 12% on Cursor vs 2% on OpenCode — exactly 6×, scaffold-only | Tian et al., SWE-Bench Mobile, [arXiv:2602.09540](https://arxiv.org/abs/2602.09540) (Feb 2026) | B |
| v2 harness simplification: removed sprints/negotiation, DAW in 4h/$125 | Anthropic engineering blog (April 2026) | A |
| **1000+ PRs in 3 weeks** with ~5 manual IDE edits — review-loop development | Nick Schrock, Dagster founder (Dec 2025) | B |
| **3x velocity** with agents handling commits, changelogs, docs, releases — org transformation | Matthias Vallentin, Tenzir CEO (Dec 2025) | B |
| Grep with a good harness ≥ vector retrieval on LongMemEval across 4 harnesses; scores depend strongly on harness regardless of retrieval choice | Sen, Kasturi, Lumer, Gulati, Subbiah (PwC US), [arXiv:2605.15184](https://arxiv.org/abs/2605.15184) (May 2026) | B |

### Production-Scale Agent-Driven Development (New Evidence, April 2026)

Two practitioners give the production-scale version of the table rows above, and both attribute the gains to the harness rather than the model. **Nick Schrock (Dagster)** merged 1,000+ PRs in 3 weeks with about 5 manual IDE edits, via a local-dev -> cloud-review -> agent-applies-feedback loop where CI errors are downloaded and fixed automatically ("This isn't vibe coding. The process is still software engineering forward."). **Matthias Vallentin (Tenzir)** got a 3x velocity improvement with agents handling commits, changelogs, docs, and releases, framed as org transformation rather than individual productivity — the same team whose MCP vs Skills production data ([MCP vs Skills Economics](./mcp-vs-skills-economics.md)) showed a 50% cost reduction through architecture choices.

### Evidence Nuancing the Thesis

| Evidence | Source | Tier |
|----------|--------|------|
| Lower-tier models (Haiku, Flash) still need more structured tooling | Video acknowledgment | B |
| Model version changes (Opus 4.5→4.6) require harness retuning | Behavioral Insights — prompt sensitivity | A |
| Opus 4.7 literalism pushes *prompt* complexity up while harness simplifies; persists on 4.8 | Anthropic migration guide (April 2026); [4.8 docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8) (May 2026) | A |
| Opus 4.8 recovers harness-stressing 4.7 failure modes (fewer compactions, better tool triggering); one hard-break: extended-thinking budgets now 400 | [4.8 docs](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8) (May 2026) | A |
| 1M context window fundamentally changes context management strategies (4.8 default on API/Bedrock/Vertex; 200k Microsoft Foundry) | Anthropic model release; 4.8 docs | A |
| Specification gap: model architecture determines task feasibility | Nate B. Jones (2026) | B |
| Explicit verifier modules hurt benchmark performance (-0.8 SWE, -8.4 OS World) | Pan et al. (Tsinghua + Harbin IT), [arXiv:2603.25723](https://arxiv.org/abs/2603.25723) (March 2026) | B |

**Practical implication of the nuancing evidence**: The "harness simplifies as models improve" thesis holds, but three specific decisions should be hedged:

1. **Don't strip harness for lower-tier models.** If your project routes some tasks to Haiku for cost reasons, the harness those tasks need is *not* the same as the harness Opus needs. Keep fallback scaffolding for cheaper models rather than optimizing for the top tier only.
2. **Retune prompts on every model release, even if the harness is unchanged.** Opus 4.6 → 4.7 is the canonical case: the harness did not need to change, but prompt idioms that assumed inferred intent silently regressed. See [model-migration-anti-patterns.md](model-migration-anti-patterns.md).
3. **Don't add verifier modules prophylactically.** The Pan et al. ablation (arXiv:2603.25723) is narrow but pointed: explicit verifiers hurt benchmark performance. Reserve verification for where you have evidence the agent is getting it wrong, not as a default safety layer.

### Verdict

**The model is necessary but not sufficient. The harness is the multiplier.**

As models improve, the optimal harness gets simpler — but the *need* for harness engineering increases, not decreases. The smartphone analogy holds: when processors commoditized, the OS and ecosystem became the differentiator, not irrelevant.

**Confidence**: Medium-High. The "Less Is More" evidence is strong and convergent across independent sources. The nuancing evidence is real but addresses edge cases rather than undermining the core thesis.

---

## Hypothesis Status and Falsifiability

This document's thesis is tracked across repositories as **H-HARNESS-01: Harness Engineering Yields Larger Gains Than Model Upgrades**. Consolidating the evidence in one place lets future revalidations check the claim systematically rather than re-deriving it from scattered sources.

### Consolidated Claim

> Investing in agent harness architecture (orchestration, memory, verification, state management) yields larger, faster, and more reliable performance gains than waiting for the next model upgrade.

**Current evidence-tier**: B+ leaning A. The Meta-Harness primary source ([arXiv:2603.28052](https://arxiv.org/abs/2603.28052), Lee/Nair/Zhang/Lee/Khattab/Finn, Stanford+MIT, 2026-03-30) and the Tsinghua NLH paper ([arXiv:2603.25723](https://arxiv.org/abs/2603.25723), Pan et al., 2026-03-26) are now both located and registered (resolution: 2026-05-24). The 6× orchestration-only figure is the Meta-Harness paper's headline quote and is independently corroborated by SWE-Bench Mobile ([arXiv:2602.09540](https://arxiv.org/abs/2602.09540), Opus 4.5: 12% Cursor / 2% OpenCode). Karpathy's independent convergence on meta-optimization (Authority 4/5) and Anthropic's v2 simplification with Opus 4.6 (Authority 5/5, Tier A) remain the strongest practitioner corroboration.

### Falsifiability

The claim is falsifiable in a single test:

> **Find a benchmark where a model upgrade (e.g., Sonnet → Opus) holding harness constant provides >6× improvement.**

Such a result would invalidate the "harness is the multiplier" framing — if a pure model swap can match the Stanford-reported 6× orchestration-only delta, then the harness-vs-model trade-off collapses to a routine optimization rather than a structural shift. As of 2026-05-24, no such benchmark has surfaced; the dominant cross-model deltas reported in 2026 (TerminalBench 2, SWE-bench, OSWorld) sit well below 6× even across major version jumps.

### Provenance

An academic-source sweep on 2026-05-24 closed all three previously-tracked provenance gaps: the 6× figure is the Meta-Harness paper's own headline quote, not a transcript paraphrase (Lee et al., [arXiv:2603.28052](https://arxiv.org/abs/2603.28052), 2026-03-30, corrected result quantification: 76.4% Opus 4.6 / 37.6% Haiku 4.5 on TerminalBench-2); and "Tingua NLH" was a misspelling of Tsinghua — the paper is Pan, Zou, Guo, Ni, Zheng (Tsinghua + Harbin Institute of Technology), [arXiv:2603.25723](https://arxiv.org/abs/2603.25723), 2026-03-26, whose ablation numbers in this doc (verifiers -0.8 SWE / -8.4 OSWorld; multi-candidate search -2.4 / -5.6; self-evolution +4.8 / +2.7) match the published paper exactly. Net effect: H-HARNESS-01 moves from "B+ with three outstanding gaps" to "B+ with primary sources verified."

### Cross-Repository Tracking

The hypothesis is mirrored in a personal hypothesis tracker (`project1/01-knowledge-base/hypotheses/relocated-out-of-scope.md`) that aggregates evidence across the author's portfolio (security data, MCP prototypes, second-brain). Findings flow into this document; tracker-side updates do not propagate automatically, so revalidation should consult both.

---

## Where Failure Actually Lives

The most counterintuitive finding: developers expect failures in agent logic (bad prompts, hallucinations). In practice, **most reliability failures happen in the harness itself**.

| Failure Location | Expected | Actual |
|-----------------|----------|--------|
| Agent logic (prompts, reasoning) | Primary source | Secondary |
| **Harness infrastructure** | Secondary | **Primary** |

### Common Harness Failures

- **Flaky tool mocks** that differ from production environments
- **Test inputs** that don't cover real-world data distribution
- **Hermetic/production gap** — isolated tests are fast and reproducible, but the gap between them and production is where the worst bugs hide

### Recommended Testing Strategy

1. **Hermetic testing** for unit-level agent behaviors (fast, reproducible)
2. **Production-like testing** for integration behaviors (catches the real bugs)
3. **Harness-first development** — define behavioral test suite before implementing agent logic

---

## Sources

### Tier A (Primary Vendor)

- Anthropic: ["Effective harnesses for long-running agents"](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (November 2025)
- Anthropic: Prithvi Rajasekaran, ["Designing a harness for long-running application development"](https://www.anthropic.com/engineering/harness-design-long-running-apps) (2026-03-24) — the generator/evaluator source the v2 simplification derives from
- Anthropic: v2 harness simplification with Opus 4.6 (April 2026)
- Anthropic: [Migration Guide](https://platform.claude.com/docs/en/about-claude/models/migration-guide) (April 2026) — Opus 4.7 literal interpretation
- Anthropic: ["What's New Claude 4.8"](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8) (Tier A, fetched 2026-05-30)
- Boris Cherny: Interviews and posts (March 2026) — parallel sessions, hooks, permissions pre-configuration, Document-and-Clear pattern

### Tier B (Validated / Expert Practitioner)

- Prompt Engineering: ["The AI Model Doesn't Matter Anymore"](https://www.youtube.com/watch?v=1Ohf2aeSPFA) (February 2026) — source for the Harness Thesis, Vercel, Manus, and Bitter Lesson material above
- Pan, Zou, Guo, Ni, Zheng (Tsinghua University + Harbin Institute of Technology): ["Natural-Language Agent Harnesses"](https://arxiv.org/abs/2603.25723) — arXiv:2603.25723, 2026-03-26. *(Previously cited as "Tingua NLH" — attribution corrected 2026-05-24.)*
- Lee, Nair, Zhang, Lee, Khattab, Finn (Stanford + MIT): ["Meta-Harness: End-to-End Optimization of Model Harnesses"](https://arxiv.org/abs/2603.28052) — arXiv:2603.28052, 2026-03-30. **Source for the "6× performance gap from harness changes alone" headline figure.**
- Tian, Wang, Yang et al.: ["SWE-Bench Mobile: Can LLM Agents Develop Industry-Level Mobile Apps?"](https://arxiv.org/abs/2602.09540) — arXiv:2602.09540, 2026-02-10
- Sen, Kasturi, Lumer, Gulati, Subbiah (PwC US): ["Is Grep All You Need? How Agent Harnesses Reshape Agentic Search"](https://arxiv.org/abs/2605.15184) — arXiv:2605.15184, May 2026. Tier B preprint, not yet peer-reviewed.
- Andrej Karpathy: Meta-optimization of program.md (March 2026, No Priors podcast). Authority 4/5.
- Andrej Karpathy: ["Sequoia Ascent 2026"](https://karpathy.bearblog.dev/sequoia-ascent-2026/) (2026-04-30). Authority 4/5.
- Armin Ronacher: ["The Coming Loop"](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/) (lucumr.pocoo.org, 2026-06-23) — inner agent loop vs. outer harness loop distinction. Tier B.
- `project1` (security-data research portfolio), ["SDW Loop Engineering"](../../project1/02-projects/securitydataworks/LOOP-ENGINEERING-DESIGN-2026-06-15.md) (2026-06-15) + [`BENCH-LOOP-STATE.md`](../../project1/02-projects/securitydataworks/BENCH-LOOP-STATE.md) / [`CONSOLE-LOOP-STATE.md`](../../project1/02-projects/securitydataworks/CONSOLE-LOOP-STATE.md) — single-source, bias-flagged; cites Arike et al., AIES 2025, on emergent goal-drift
- LangChain DeepAgents team: ["Improving Deep Agents with Harness Engineering"](https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering) (2026-02-17). Authority 4/5.
- [everything-claude-code](https://github.com/affaan-m/everything-claude-code) — 119K+ stars, Anthropic hackathon winner
- [superpowers](https://github.com/obra/superpowers) — 294K+ installs
- Richard Sutton: "The Bitter Lesson"

### Related Analysis

- [Behavioral Insights](./behavioral-insights.md) — Context thresholds, CLAUDE.md adherence, prompt sensitivity
- [Domain Knowledge Architecture](./domain-knowledge-architecture.md) — Companion document for domain-heavy projects
- [MCP vs Skills Economics](./mcp-vs-skills-economics.md) — Cost trade-offs the Schrock/Vallentin evidence draws on
- [Model Migration Anti-Patterns](./model-migration-anti-patterns.md) — Prompt anti-patterns that break on Opus 4.7 (carry forward to 4.8); split between harness (simpler) and prompt (more explicit); 4.8 net-deltas table
- [Scheduled & Looping Primitives](./scheduled-and-looping-primitives.md) — the scheduling-facing companion: `/loop`, `/goal`, Routines, Desktop scheduled tasks, the Ralph lineage, and the "loop engineering" framing turned into audit signals; carries the matching "weak RETHINK limb" treatment from the scheduling side plus the `project1` case study
- [Intent-Alignment Audit](./intent-alignment-audit.md) — the RETHINK companion: the standing "does each mechanism still match its intent?" pass, of which an absent loop RETHINK limb is one instance
- [Safety & Sandboxing](./safety-and-sandboxing.md) + [Secure Code Generation](./secure-code-generation.md) — the security layer of the harness stack
- [Agent-Driven Development](./agent-driven-development.md) — harness concepts tested against 7-repo evidence

---

*Last updated: 2026-07-16 (follows: Willison/Ronacher/Osmani harness canons added — doc now tracks those canons for harness-design commentary, keeps the Bitter-Lesson diagnostic, accretion heuristics, and portfolio measurements as delta; added Ronacher's "The Coming Loop" to Sources). Prior: 2026-07-10 (Reduction Phase 4 — collapsed the harness-design mechanism half now carried by Anthropic's official best-practices page and "How Claude Code works in large codebases"; kept the Bitter-Lesson diagnostic, the accretion heuristics, and all measured/portfolio evidence; cut the 6-layer harness stack, the harness-toolkit changelog table, the philosophy feature-comparison detail, the symptom-to-mechanism diagnostic router, the task-complexity decision tree, and the standalone Resource Map — all now owned by the two first-party sources; confirmed no surviving links to the docs retired elsewhere in this pass). Prior: 2026-06-21 (RETHINK limb elevated). Prior: 2026-06-15 (loop-engineering framing + `/goal` version/claim fix + Rajasekaran and Scaling Managed Agents primary citations + Karpathy Sequoia Ascent). Prior: May 2026 (Opus 4.8 harness-layer deltas).*

<!-- graphify-footer:start -->

## Related (from graph)

- [`analysis/model-migration-anti-patterns.md`](analysis/model-migration-anti-patterns.md) [EXTRACTED (1.00)] — references
- [`analysis/claude-md-progressive-disclosure.md`](analysis/claude-md-progressive-disclosure.md) [EXTRACTED (1.00)] — references

<!-- graphify-footer:end -->
