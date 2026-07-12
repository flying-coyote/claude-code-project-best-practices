# Content-portfolio review protocol — seeded 2026-07-12 from project1 Phase 0B
Plan of record lives in the hub.
This file is the spoke session's context — hub memory is NOT visible here.

## Standing rules (every program session)

- **Anatomy**: findings land as staged-decision batches in `02-projects/staged-decisions-2026-07/` (frontmatter `type: review`; header lists apply_now items already committed WITH hashes; then numbered owner forks, each with two defensible choices + cascades + "I did NOT edit"). Phase closes with a RUN-REPORT.
- **apply_now requires ALL of**: mechanically derivable from a named source; reversible in one commit; no narrative/voice/framing change; no price/tier/taxonomy choice; not touching DO-NOT-REFLAG.
- **Numbers**: every quantitative claim in agent-drafted publication-bound prose is re-derived by a DIFFERENT agent from the named source before commit; unverifiable → stage, never ship.
- **Subagents never run git** (file-mutating fan-out prompts carry the prohibition explicitly); the orchestrator commits after reconciling `git status --porcelain` against surviving agents' vouched edit lists; unvouched changes quarantine. One file-mutating fan-out per repo at a time.
- **Path moves**: §11.1 sweep (hooks, cron prompts + routines, automation, cross-repo-progress.json, memory pointers, taskmaster, crontab) — baseline grep BEFORE recorded in the staged file, old+new grep AFTER; residual old-path hits are defects. project1's ROOT path is frozen (memory store keyed to it).
- **After committed changes**: the §11.2 battery (daily_health_check, check_memory_index, check_hypothesis_counts, INDEX regen + diff, hooks dry-run). Failure halts the phase.
- **Public-safe**: several spokes are public repos — protocols and staged text carry no pricing, client names, or unpublished business detail; DeWitt + paid/public Matrix firewalls bind as written in each spoke's CLAUDE.md.
- **Prose depth (D0.1)**: book/litreview prose rework follows the global writing spec, gated by voice-consistency-enforcer + publication-quality-checker; book story beats are REAL stories grilled from the owner, never invented; after every scrub, name the additive counterpart.

## Per-repo section

### claude-code-project-best-practices (~/claude-code-project-best-practices)
Rulings ratified — see the loop-eng staged file §6: current-awareness-feed primary; binding convergence field; fidelity gate (source-quote beside local translation); real weekly cadence restored via scheduled routine; fidelity audit covers all three import layers equally. 1L-bp also: fix README 42-vs-27 drift; rule the shallow `best_practices_reviewer.py` coupling (wire or retire); the concept→implementation pair map is in the plan's F7 recon.

## DO-NOT-REFLAG (sanitized for a public spoke — redact-to-pointer ruling, 2026-07-12)

The full, itemized ledger lives in the PRIVATE hub (`project1/02-projects/content-portfolio-review-2026-07/protocols/DO-NOT-REFLAG.md`); additions require an owner-ratified edit THERE. A finding that contradicts a settled decision is reported as "conflicts with settled decision X" for the owner — never re-litigated by an agent. The generic rules that bind in this repo:

1. Settled fleet dispositions are settled — topology questions are fresh ground; maintain-vs-dormant is not.
2. WITHDRAWN markers and folded-correction banners are RECORDS, not violations.
3. The keep-and-grow boundary from the June audits is not relitigable.
4. Anything adjudicated in a repo CHANGELOG 2026-07 subsection or a monthly packet is final.
5. Owner-held forks marked inline are undecided by design — do not "resolve" them.
6. The owner's ratified 2026-07 program rulings (recorded in the private hub's staged-decision files) are decided — do not re-ask them.
7. Repo-specific publish firewalls and confidentiality boundaries bind as written in each spoke's own CLAUDE.md.
