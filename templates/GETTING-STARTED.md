# Getting Started with Claude Code Harness Engineering

A practical guide for setting up Claude Code in an existing repository. Based on patterns validated across 7 production repos (86% co-authoring rate in the most instrumented).

## What You Need

Three things make the biggest difference:

1. **CLAUDE.md** — A resource map telling Claude what's in your repo and how to work with it
2. **Rules files** — Domain-specific instructions that load only when relevant (`.claude/rules/*.md`)
3. **Settings** — Permission and behavioral defaults (`.claude/settings.json`)

Everything else (hooks, commands, skills, memory) is optional and can be added as you find the need.

## Quick Setup (5 Minutes)

```bash
# 1. Create the .claude directory
mkdir -p .claude/rules

# 2. Copy the CLAUDE.md template (pick your tier)
cp templates/claude-md-tier1-minimal.md CLAUDE.md    # Simple projects
cp templates/claude-md-tier2-standard.md CLAUDE.md   # Most projects
cp templates/claude-md-tier3-advanced.md CLAUDE.md   # Complex domains

# 3. Add basic settings
cp templates/settings.json .claude/settings.json

# 4. Add a domain rule (optional but recommended)
cp templates/rules/code-style.md .claude/rules/code-style.md
```

Then edit each file to match your project. The templates have comments explaining what to customize.

## The ~150 Instruction Cap

CLAUDE.md adherence drops below 80% when instructions exceed ~150 lines. Keep CLAUDE.md lean:

- **CLAUDE.md**: Resource map + key commands + critical rules only
- **Rules files**: Domain-specific detail (testing patterns, API conventions, security boundaries)
- **Commands/skills**: Reusable workflows (deploy, review, release)

This is progressive disclosure — Claude loads CLAUDE.md on every turn but only reads rules files when working in the relevant directory.

## Maturity Progression

Don't over-engineer the harness upfront. Start minimal and add as you hit friction:

| Stage | What to Add | Why |
|-------|-------------|-----|
| Week 1 | CLAUDE.md + settings.json | Baseline context + permissions |
| Week 2 | 1-2 rules files | Address first domain mistakes |
| Month 1 | Hooks (lint, test) | Catch regressions automatically |
| Month 2+ | Commands, skills, memory | Encode repeatable workflows |

## File Reference

| File | Purpose | When |
|------|---------|------|
| `CLAUDE.md` | Project context loaded every turn | Always |
| `.claude/settings.json` | Permissions and model defaults | Always |
| `.claude/rules/*.md` | Domain rules loaded by path match | When editing matching files |
| `.claude/commands/*.md` | Slash commands (`/deploy`, `/review`) | When you have repeatable workflows |
| `.claude/skills/*.md` | Multi-step capabilities | Complex automation |

## Anti-Patterns

- **Don't put everything in CLAUDE.md.** Move domain detail to rules files.
- **Don't duplicate what the code says.** CLAUDE.md is a map, not documentation.
- **Don't add rules speculatively.** Add rules when Claude makes a mistake, not before.
- **Don't restrict tool permissions too early.** Start permissive, tighten after you see what Claude does.
