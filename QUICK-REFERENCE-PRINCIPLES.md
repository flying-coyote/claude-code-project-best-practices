# The Big 3 Principles - Quick Reference

**Purpose**: One-page reference for Claude Code project setup and maintenance. Print and keep visible.

---

## The Big 3: Non-Negotiable Principles

| # | Principle | Target | Rule |
|---|-----------|--------|------|
| **1** | **Keep CLAUDE.md Ruthlessly Minimal** | ~60 lines | "Would removing this cause mistakes? If not, cut it." |
| **2** | **Plan First, Always** | Non-trivial work | Use `/plan` before implementing features, architectural changes, or multi-file work |
| **3** | **Context Engineering > Prompt Engineering** | External artifacts | Specs, ARCHITECTURE.md, git history = agent memory. One feature at a time. |

---

## Red Flags (You're Violating These Principles)

- 🚩 **CLAUDE.md is >100 lines** → Ruthlessly cut
- 🚩 **Implementing without planning** → Stop, use /plan
- 🚩 **Skills >500 lines** → Split or use multi-workflow
- 🚩 **Custom slash commands list is long** → Delete most, use natural language
- 🚩 **Context feels exhausted** → One feature at a time
- 🚩 **No verification step** → Add tests/linters
- 🚩 **Permission prompts interrupt constantly** → Pre-approve patterns
- 🚩 **Exotic hooks/customization** → Simplify to standard patterns

---

## When to Apply

| Situation | Apply Principle |
|-----------|-----------------|
| Starting new project | All 3 (setup CLAUDE.md, plan architecture, create specs) |
| Adding feature >2-3 files | Principle 2 (use /plan first) |
| CLAUDE.md exceeds 80 lines | Principle 1 (ruthless minimalism audit) |
| Context feels exhausted | Principle 3 (one feature at a time, external artifacts) |
| New team member joining | Share this reference, audit compliance |

---

## Quick Audit Checklist

**CLAUDE.md Audit**:
- [ ] Under 60 lines (80 max tolerable)?
- [ ] Only includes project purpose, key commands, gotchas, current focus?
- [ ] No examples, essays, or comprehensive command lists?

**Planning Audit**:
- [ ] Used `/plan` for last 3 non-trivial features?
- [ ] Plans approved before implementation started?

**Context Engineering Audit**:
- [ ] ARCHITECTURE.md exists for system design?
- [ ] Specs written before code (when applicable)?
- [ ] Working on one feature at a time?

---

## Key Quotes

> "CLAUDE.md should be concise (~60 lines recommended)" - Anthropic Official Docs

> "Great Planning is Great Prompting" - IndyDevDan

> "Context engineering supersedes prompt engineering for agents" - Anthropic Engineering

> "Verification = 2-3x Quality" - Boris Cherny

> "Principles over tools... learn to endure change with principle" - IndyDevDan

---

**Full Details**: See FOUNDATIONAL-PRINCIPLES.md | **Sources**: SOURCES.md | **Version**: 1.3
