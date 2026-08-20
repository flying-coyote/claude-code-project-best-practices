# Source refresh 2026-08-19 — DeepSeek Harness (dsh) v0.1

**APPLIED 2026-08-19** (owner-directed, same day): the §3 apply-set landed across SOURCES.md + 11 docs — every table row except the two owner calls, which resolved as the brief leaned: cross-harness portability became a bounded section in analysis/harness-engineering.md (no new doc, per the shrinking-corpus charter) and README.md took the minimal scope note (no new lane). The new audit signal is `second-runtime-present`, routing to harness-engineering + safety-and-sandboxing. A sixth stale tool-ecosystem.md pointer (SOURCES.md ~L813) was found and repaired during application. Also applied: the verified SANS Find Evil! finalist-stage facts as harness-engineering delta (winners pending 2026-08-26). This file remains the evidence dossier; §§1–7 below are unchanged.

**Staged report only.** Following the SOURCE-REFRESH-2026-07-09-cowork.md discipline: this file is the single artifact of the refresh, nothing else in the repo was edited, and a later local pass applies the corrections. Every claim carries an A–D tier and a primary URL; access dates 2026-08-18/19. All fetched content was treated as data, not instructions.

**Provenance.** Overnight local session (not a cloud/Cowork run — the research needed only public web plus this repo, so nothing justified leaving the machine). Two orchestrated passes: a six-slice research fan-out (primary repo/docs, official announcement + business context, HN/community, concept-by-concept Claude Code comparison, interop + security, local repo map — 120 tier-tagged findings), then an 11-agent adversarial verification pass over the claims that carry the recommendations (25 verdicts: 20 CONFIRMED, 5 PARTIAL, 0 REFUTED). Corrections from the adversarial pass are folded in below; nothing here rests on an unverified press claim without saying so.

---

## Headline

DeepSeek released **DeepSeek Harness (dsh) v0.1** in developer preview on 2026-08-13: an MIT-licensed, TypeScript, web-UI-first agent runtime built on the pre-existing community plugin kernel **Cordis** (Shigma, npm first publish 2022-04-21, vendored with upstream MIT preserved — Tier A, registry.npmjs.org/cordis + vendor/README.md), organized so that models, tools, skills, sessions, sandboxes, filesystems, the approval system, and the agent loop itself are swappable providers behind what its docs call capability "seams" (their term). Repo `deepseek-ai/deepseek-harness`: 160,435 stars at 2026-08-18T20:47 ET, 162,021 at 2026-08-19T00:15 ET, still accruing roughly 450/hour five days in (Tier A, GitHub API, both readings mine).

For this project the release matters less as a competitor and more as **the first at-scale test of cross-harness portability of the practices this repo audits**, because dsh natively consumes the Claude Code artifact set rather than replacing it:

- it discovers and injects **AGENTS.md and CLAUDE.md** (plus `.local.md` overlays) from home and root-to-cwd, in system-reminder-style tags with a maxBytes budget (Tier A, packages/context/agent-instructions/README.md);
- it implements the **SKILL.md format** — `<name>/SKILL.md` bundles, kebab-case `disable-model-invocation` / `user-invocable`, two-stage progressive disclosure — and honors a vendor-neutral `.agents/skills` tree, without ever naming Anthropic or agentskills.io (Tier A, docs/subsystems/skills.md; the ~/.agents default is in docs/config-catalog.md);
- it ships a first-party **Claude Code hooks.json bridge** — real but a subset, see corrections below (Tier A, packages/hooks/hooks-claude-code/README.md);
- it speaks **MCP client-side** with the same stdio/streamable-http transports (Tier A, docs/config-catalog.md);
- and it drives **Claude Code itself as an opt-in subagent** through Anthropic's official Agent SDK (Tier A, packages/subagent/subagent-claude-code/README.md).

So a meaningful slice of this repo's guidance is now *testably* harness-portable rather than speculatively so, the audit gains a set of blind spots it could not have had a week ago, and the third-party migration ecosystem (dsh-claude-move, dsh-claude-compat, dsh-inherit — Tier C, awesome-lists) is already treating `.claude/` as a de facto portable standard.

---

## 1. Corrections to circulating claims (adversarial-pass results)

These are the deltas between what press/community coverage says and what the primary sources support. Anything staged into SOURCES.md should use the corrected wording.

1. **"Runs Claude Code hooks faithfully" — overstated (PARTIAL).** The bridge maps **7 of Claude Code's 30 hook events** (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SubagentStart, SubagentStop; the other 23 explicitly unsupported), runs only shell-form `type:'command'` hooks (http/mcp_tool/prompt/agent hooks are parsed-and-skipped with a warning), and degrades even the mapped ones: PreToolUse cannot pre-approve, UserPromptSubmit/Stop ignore matchers, SubagentStart/Stop report a constant `agent_type` of `general-purpose` so specific-kind matchers never fire. The README's own framing is "a compatibility path for the mapped CC command-hook subset" (Tier A, verbatim-quoted). Hooks-for-automation practice transfers *partially*, not as-is.
2. **"Calls Claude Code as a sub-agent" — true but narrower than the press version (CONFIRMED with envelope).** The provider is **off by default** ("Production dsh does not install or mount this optional provider"), and a run is strictly one-shot: `persistSession: false`, no resume, no streaming, no wall-clock timeout, no side-effect rollback, AskUserQuestion disabled, no parent-conversation transfer (only cwd). Transport is the official `@anthropic-ai/claude-agent-sdk@0.3.220` `query()` against the host's native `claude` install and login; credential-shaped ambient env vars are scrubbed before the explicit env overlay (all Tier A).
3. **The loss-leader reading is press speculation, not a DeepSeek claim.** V4-Pro API pricing did rise sharply alongside the release (to peak/off-peak tiers, up to ~4.5× on output at peak — Tier C, techtimes + the-decoder with matching figures), but the-decoder explicitly notes no stated link between the Harness open-sourcing and the pricing move, and dsh's own model-agnosticism (Anthropic/OpenAI/Bedrock/Vertex/Azure/custom endpoints first-party; ~40 providers per Tier B Tencent-cloud coverage; Ollama shipped `ollama launch dsh` support, Tier B) cuts against a narrow drive-V4-traffic thesis. Report as unconfirmed interpretation.
4. **Instruction-file mechanic, precise version:** over budget, broader files are **dropped whole** before the single most-specific file is truncated, with a visible notice naming omitted paths — not "broader files truncated first" as I first had it (Tier A, corrected verbatim).
5. **HN thread numbers:** 739 points exact; comments were 309 at verification time (a ~298 reading was a stale snapshot). Thread id 49285244, verified via Algolia API.
6. **Goldie head-to-head temporal nit:** Claude Code's 48,000-token figure is at the 20-minute mark, not the 30-minute mark where it was still running (Tier B, juliangoldie.com — otherwise verified verbatim: 11 min / ~483k tokens / ~5 cents for dsh, ~57× more per token for CC, CC output judged better 9/10 vs 7/10, and his recommendation is dual-running by task type through an orchestrator, not switching).

---

## 2. The settingSources resolution (decides whether CC config binds under dsh)

The open question that mattered most: dsh's design note claims that omitting `settingSources` makes the Agent SDK load the host's normal Claude settings. **Resolved in dsh's favor for current SDK versions** (Tier A, code.claude.com/docs/en/agent-sdk/claude-code-features + migration-guide): omitting `settingSources` on `query()` loads user + project + local filesystem settings — `settings.json` allowlists, CLAUDE.md, skills, commands — relative to cwd, matching the CLI. The no-filesystem-settings default existed only briefly at SDK v0.1.0 and was reverted.

Two consequences worth wiring into the audit:

- **A CLAUDE.md and a permission allowlist DO govern a dsh-spawned Claude Code run** (project `.claude/` loads only from cwd with no parent-directory fallback; CLAUDE.md also loads from parents). Config discipline written for interactive CC therefore silently extends to foreign-orchestrator runs.
- The inverse is the risk: **an over-broad `.claude/settings.json` allowlist becomes remotely drivable capacity for any outer harness** that shells into the project, headless, with no human at the prompt. The allowlist is the *only* permission surface in that spawn path (the provider supplies no canUseTool callback and disables AskUserQuestion).

---

## 3. Repo impact — per-doc actions (all file/line claims re-derived on disk)

| Path | Action | Why (verified) |
|---|---|---|
| SOURCES.md | add-source | New entry in the Alternative AI Coding Agents table (heading L1272, rows from L1276) plus a full harness-cluster entry near the Fudan/Harness-Bench block (L2162–2164). Paste blocks in §6. |
| SOURCES.md | fix stale pointers | Five references to `analysis/tool-ecosystem.md` (deleted 2026-07-10, confirmed absent on disk): L1282, L1300, L1326, plus L485 and L563 found during verification. |
| analysis/harness-engineering.md | update | Live major-lab evidence for the harness thesis it already carries (6× scaffold gap at L129–135; cross-model transfer L123). dsh is a new comparator; add measured delta only, per its follow-lane freeze. |
| analysis/orchestration-comparison.md | update | New topology with no current row: CC as worker under a non-Anthropic orchestrator. The Wiggins cross-model-family recommendation gains a concrete shipped stack. |
| analysis/safety-and-sandboxing.md | update | The §2 trust boundary; plus dsh's sandbox is filesystem-only *by design* ("Network and process visibility are outside this vocabulary", Tier A) where CC's enforces filesystem AND network with domain allowlists — network egress control and credential masking are CC-specific practices, non-portable, and a risk delta when workflows move. |
| analysis/plugins-and-extensions.md | update + re-examine retirement | Staged retirement 2026-09-30 (PLAN.md L37) assumed the slice went first-party; a competing plugin-native runtime with an uncurated install path is evidence the cross-runtime residual may grow. Re-examine at the revalidate, do not silently execute. |
| AUDIT-CONTEXT.md | update | New signal candidate: multi-runtime coexistence (a `.dsh/` or `~/.dsh` config tree, `.agents/skills`, or dsh profiles alongside `.claude/`), on the precedent of the repo-has-agents-md row; meanwhile note the foreign-outer-loop blind spot beside the cloud-Routines one (L91–93). |
| README.md | update (scope note) | The seven-lane map has no lane for a competing runtime that also hosts CC; one paragraph marking competing runtimes out-of-scope-but-tracked is the minimal fix. A new lane is an owner call. |
| ABSORPTION-MAP.md | update (watch item) | Add dsh under Non-doc watch items (L40) for the harness-engineering and plugins rows; sanctioned evaluation point is the ~2026-10 Phase F sweep. |
| PLAN.md | update | Add dsh to the review-cadence watched set; annotate the 2026-09-30 plugins-and-extensions row. |
| analysis/claude-md-progressive-disclosure.md | update | The AGENTS.md/CLAUDE.md split-brain audit now covers files consumed by two runtimes *in fact* (dsh reads both, verified). Its maxBytes drop-whole-then-truncate behavior is a second data point beside CC's 200-line/25KB memory boundary. |
| analysis/scheduled-and-looping-primitives.md | update (one line) | Its failure framing applies to a foreign outer loop driving CC; its signals cannot see that topology. Scope note only — the doc is follow-lane-frozen. |
| analysis/mcp-patterns.md | minor update | MCP is confirmed first-party client-side in dsh, so the OWASP mapping gains a second client population; note that dsh mounts MCP through the same tool registry as native tools (demoted from privileged protocol to one plugin among many). |
| SOURCES-QUICK-REFERENCE.md, model-migration-anti-patterns.md, behavioral-insights.md | none | Below the authority bar / out of scope, unchanged. |
| analysis/cross-harness-portability.md | **new-doc — owner call** | See gap G2. Creating a doc cuts against the shrinking-corpus charter; the alternative is a bounded section in harness-engineering.md. Not staged here; decision needed first. |

---

## 4. Audit gaps the release exposes

- **G1 — Multi-runtime coexistence detection.** No Signal Collection command detects a second agent runtime configured in an audited repo, and no routing row covers split-brain drift between two runtimes' instruction/permission configs beyond the single CLAUDE.md-vs-AGENTS.md note.
- **G2 — Cross-harness portability of practices.** The evidence anchors are already registered (SOURCES.md L2162 Fudan: "factual harness structure transfers while prose-level strategy does not"; L2164 Harness-Bench: report capability at the model-harness configuration level; harness-engineering.md 6× gap) but nothing routes to them and the audit assumes a Claude Code target. dsh makes portability *testable*: the same hooks.json/SKILL.md/CLAUDE.md can be executed under both harnesses and the transfer measured per practice.
- **G3 — Foreign-orchestrator trust boundary.** §2's finding: whose permission system governs a headless CC spawn, now answered (the project's own settings), which converts allowlist hygiene from an interactive concern into an exposure question no current doc models.
- **G4 — Competing-runtime plugin supply chain.** The evaluation checklist and OWASP-MCP mapping are Claude-marketplace/MCP-scoped; nothing covers an everything-is-a-plugin ecosystem where install is pnpm passthrough and a plugin can replace the logger and the loop.
- **G5 — Convergence semantics under-credit competitors.** Independent implementation of a practice by a rival runtime (SKILL.md, AGENTS.md, MCP, the .agents tree) is arguably the strongest convergence evidence available, and the single-source/emerging/converged field has no way to record it.
- **G6 — Same-model/two-harness A/B.** All behavioral measurements are conditioned on CC's harness; the same Claude model is now drivable by two harnesses, and the archived probe instruments are the natural basis for the repo's most original possible contribution.

---

## 5. Security posture notes (feeds the attack-surface register and the SDW lane)

- **Sandbox:** filesystem confinement only, fail-closed (`SANDBOX_UNAVAILABLE`, "Silent unconfined passthrough is never legal") — genuinely credit-worthy — but network and process visibility are excluded from the vocabulary, so read-and-exfiltrate is open by design (Tier A). CC's two-layer sandbox with `network.allowedDomains` is the contrast case (Tier A).
- **Plugins run in-process with host authority** — no runtime isolation, MCP stdio processes launch outside the managed command sandbox, Code Mode workers share process identity (Tier B, Hedemark code-level review, corroborated by the official "no privileged core" architecture doc and the install-docs warning). Plugin trust is total trust.
- **Install path:** pnpm passthrough (npm names, `github:` specs, tarballs), no registry, no signing, no review; official advice is commit-SHA pinning and reading source (Tier A, publish.md, adversarially probed for any registry/signing mention — none exists).
- **The Safe Use Policy concedes prompt injection in plain terms** ("the Agent may execute commands embedded in content, even if those commands conflict with the assigned task") and assigns mitigation to the operator: dedicated VM/container, human approval, trusted-source plugins only (Tier A, verbatim, deepseek.com/harness/en/privacy/).
- **Telemetry:** disabled by default, but when enabled sends prompts, output, tool calls, approvals, plus a stable pseudonymous UUID header — a policy default, not a structural boundary (Tier B, Hedemark).
- **Provenance gap at launch:** npm published rc.6 while source declared rc.5, no matching tag, no gitHead/attestation (Tier B, Hedemark; not independently re-checked).
- **Ecosystem pattern:** defensive plugins (dsh-poison-guard, dsh-guardian, dsh-defend, dsh-permission-rules) arriving through the same uncurated channel they police, and at least six independent lookalike "plugin store" domains within five days (Tier C, awesome-lists; typosquat/poisoning potential is Tier D speculation, labeled).
- **No CVEs or advisories as of 2026-08-18** (Tier A, empty security-advisories API): five days post-release this reflects elapsed time, not assurance. Date-stamping this baseline is the point.

Related, same week: SANS' "Find Evil!" hackathon names its five open-source autonomous-IR **harnesses** as finalists (Rob T. Lee, 2026-08-18) — the harness-era framing is arriving in the security lane too; that review is scheduled separately.

---

## 6. Staged SOURCES.md paste blocks

**(a) Alternative AI Coding Agents table row** (after the Crush row, ~L1280):

```markdown
| **DeepSeek Harness (dsh)** | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | Everything-is-a-plugin runtime on the vendored Cordis kernel; model-agnostic (Anthropic/OpenAI/Bedrock/Vertex/custom); reads AGENTS.md/CLAUDE.md; SKILL.md-format skills; MCP client; opt-in Claude Code/Codex subagent providers via official SDKs | Framework-builders; cross-harness portability testing; NOT production (v0.1 preview, "THERE WILL BE COMPATIBILITY-BREAKING CHANGES") |
```

**(b) Full entry for the harness cluster** (near L2162–2164):

```markdown
- **DeepSeek Harness v0.1 (dsh)** (`github.com/deepseek-ai/deepseek-harness`, released 2026-08-13, MIT, developer preview, Tier A for its own docs/code). Agent runtime where model adapters, tools, skills, sessions, sandboxes, approval, and the loop are swappable providers on the vendored Cordis plugin kernel (Shigma, npm 2022-04-21 — pre-existing community framework, upstream MIT preserved in vendor/). Consumes the Claude Code artifact set natively: AGENTS.md/CLAUDE.md discovery with .local overlays (packages/context/agent-instructions), SKILL.md skills with `disable-model-invocation`/`user-invocable` and a vendor-neutral `.agents/skills` tree (docs/subsystems/skills.md), MCP client with stdio/streamable-http (docs/config-catalog.md), and a partial CC hooks.json bridge — 7 of 30 events, command-type only (packages/hooks/hooks-claude-code). Drives Claude Code as an OPT-IN one-shot subagent via `@anthropic-ai/claude-agent-sdk@0.3.220` `query()`; omitted settingSources means the host project's settings.json + CLAUDE.md bind the run (SDK docs, verified 2026-08-19). Sandbox is filesystem-only fail-closed (network/process visibility explicitly out of scope) vs CC's filesystem+network layers. Plugin install is pnpm passthrough, no registry/signing; plugins run in-process with host authority; Safe Use Policy assigns injection mitigation to the operator. Community reception split: append-only replayable session log praised (HN 49285244, 739 pts); plugin-fatigue/over-engineering and npm-supply-chain criticism recurring; Justin3go reports ~3–10× token overhead vs leaner harnesses and a 96.4-vs-80.6 self-vs-independent benchmark discrepancy (Tier C). Practitioner head-to-head (Goldie, Tier B): dsh far cheaper per attempt, CC better output; recommends dual-running by task type, not switching. Revalidate-by: 2026-10 Phase F sweep (v0.1 preview iterates fast; expect breaking changes).
```

**(c) Unverified section additions** (L2369 section):

```markdown
- DeepSeek Harness (added 2026-08-19): the ~40-model-provider count (Tier B, Tencent-cloud coverage, no primary enumeration read); the "Model + Harness = Agent" recruiting-copy quote (Chinese-press paraphrase of a listing not reached); any V4-Pro loss-leader link (explicitly absent from DeepSeek statements — press interpretation only); dsh-external/hub official plugin hub (API 404s, org empty); the npm rc.6-vs-rc.5 provenance gap and telemetry payload details (Hedemark Tier B, not independently re-derived); whether subagent-acp implements Zed's ACP (name-plausible, undocumented); VentureBeat article body (403 on fetch; snippets only).
```

---

## 7. Not found / still unverified

- Whether the spawned `claude` child runs inside dsh's sandbox confinement at all (the design note assigns sandboxing to "native product responsibility", implying outside, but no doc states the exemption explicitly).
- Network egress behavior of dsh's bwrap/Landlock profiles beyond the vocabulary statement (filesystem is detailed; egress simply isn't governed).
- Reddit sentiment: WebFetch cannot reach reddit.com and no indexed threads surfaced with citable text — secondhand characterizations exist but were excluded.
- The Cordis paper's "spatiotemporal composability" claims (cordiverse/paper): cited everywhere, read nowhere in this pass; treat framework-superiority claims derived from it as unverified.
- Real-world identity of HN commenter "tianyicui" (self-identified dsh author in-thread; consistent with The Register naming Tianyi Cui as a paper author, but not independently verified).
- Default permission preset on a fresh install (workspace-write+ask presumed of the two documented presets; unstated).

---

## Bottom line

dsh is a v0.1 preview that will break, its plugin plane is a supply-chain surface its own policy hands to the operator, and nothing here says migrate — but it is also the strongest convergence evidence this project has ever received, because a competing major-lab runtime independently adopted CLAUDE.md, SKILL.md, MCP, and the hooks protocol rather than inventing alternatives. The repo's practices split cleanly into a harness-portable layer that just became testable and a CC-specific layer (network sandboxing, credential masking, allowlist granularity, marketplace trust) that just became legible as *differentiators* rather than defaults. The pruning charter holds; what changes is that "portability" moves from assumption to measurement, and the audit needs eyes for a second runtime standing next to `.claude/`.
