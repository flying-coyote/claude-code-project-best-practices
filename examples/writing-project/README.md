# Writing Project Example

**Type**: Technical blog / content creation project

**Demonstrates**: Claude Code setup for writing, research, and documentation work

---

## What This Example Shows

### Tier 1 Infrastructure (5 minutes)
✅ **Stop hook** - Warns about uncommitted/unpushed changes
- Critical for writing: prevents losing draft changes
- Custom message: "save your draft" instead of generic warning
- See `.claude/settings.json` lines 13-22

### Tier 2 Infrastructure (15 minutes)
✅ **Pre-approved permissions** - Markdown linting, git operations
- `npm run lint`, `npx markdownlint`
- `git status`, `git diff`, `git log`
- See `.claude/settings.json` lines 2-9

✅ **Minimal CLAUDE.md** - 29 lines (target ~60)
- Voice rules that get repeatedly violated (learn from mistakes)
- Evidence tiers for research claims
- Known gotchas specific to this blog (image paths, link formatting)
- See `.claude/CLAUDE.md`

### Tier 3 Infrastructure (30 minutes)
✅ **PostToolUse hook** - Auto-lints markdown files on write
- Runs `markdownlint --fix` after every .md file write
- Enforces consistent formatting automatically
- Fails gracefully if markdownlint not installed
- See `.claude/settings.json` lines 23-32

---

## File Structure

```
writing-project/
  .claude/
    CLAUDE.md              # Minimal context (29 lines)
    settings.json          # Hooks + permissions
  README.md               # This file (explains the example)
  docs/                   # Separate documentation
    PUBLISHING.md         # Publication checklist (not in CLAUDE.md)
    STYLE-GUIDE.md        # Voice and tone (not in CLAUDE.md)
```

---

## Key Differences from Coding Projects

### 1. Evidence Tiers in CLAUDE.md
**Why included**: Writing projects need research standards
- Technical blog requires source attribution
- "Strong claims require Tier A/B evidence" prevents unsupported assertions
- This has prevented 6+ instances of unverified claims

**Not included**: Full evidence tier documentation (that's in docs/STYLE-GUIDE.md)

---

### 2. Voice Rules (Violations Only)
**What's included**:
```markdown
## Voice Rules (Repeatedly Violated)
- Use first person "I" for personal experience
- Specific tools with versions ("PostgreSQL 15") not generic ("database")
- Acknowledge tradeoffs - no silver bullets
```

**What's NOT included**: Full style guide (100+ lines in separate doc)

**Principle**: CLAUDE.md documents what Claude gets wrong, not comprehensive guidelines.

---

### 3. Markdown-Specific Gotchas
**Included because they caused actual errors**:
- Images must be in images/ subdirectory (broke 4 posts)
- Markdown links are case-sensitive (2 broken links)
- Draft files not linted (caused 2 publishing errors)
- Internal links use relative paths (3 broken references)

These are **project-specific** - not general markdown rules.

---

## Usage

### Quick Start (Copy this setup)
```bash
# In your writing/documentation project
mkdir -p .claude
cp examples/writing-project/.claude/CLAUDE.md .claude/
cp examples/writing-project/.claude/settings.json .claude/

# Install markdown linter (if not already present)
npm install -g markdownlint-cli

# Customize CLAUDE.md with your project's voice rules and gotchas
```

### Customize for Your Project

1. **CLAUDE.md Voice Rules**:
   - Replace with YOUR repeatedly violated rules
   - Don't copy generic style guidelines
   - Only include what Claude actually gets wrong

2. **Evidence Tiers**:
   - Keep if you do research/technical writing
   - Remove for creative writing or documentation
   - Adjust tiers to match your standards

3. **Gotchas**:
   - Replace with YOUR actual broken posts/documents
   - Remove if you haven't hit those issues
   - Add new ones as you discover them

4. **PostToolUse Hook**:
   - Change to your linter (Vale, textlint, etc.)
   - Remove if manual linting preferred
   - Add multiple hooks for different checks

---

## Common Adaptations

### For Documentation Sites (Docusaurus, VitePress, etc.)
**settings.json**:
```json
"permissions": {
  "allow": [
    "Bash(npm run docs:dev*)",
    "Bash(npm run docs:build*)",
    "Bash(npm run docs:serve*)",
    "Bash(git status*)",
    "Bash(git diff*)"
  ]
}
```

**PostToolUse for multiple file types**:
```json
{
  "matcher": "Write(**/*.{md,mdx})",
  "hooks": [{
    "type": "command",
    "command": "npx prettier --write \"$FILE\" 2>/dev/null || true"
  }]
}
```

### For Books / Long-Form Content
**CLAUDE.md gotchas** (different from blog posts):
```markdown
## Known Gotchas
- Chapter files must be numbered (01-intro.md, 02-setup.md)
- Cross-references use anchor links (#heading-name)
- Build process concatenates in directory order
- Images referenced from book root, not chapter directory
```

### For Academic Writing
**Evidence tiers** (stricter):
```markdown
## Citation Requirements
- **Primary sources only** for core claims
- Industry sources require 2+ independent confirmations
- Preprints marked as "under review"
- All statistics include source and date
```

---

## Hook Examples for Writing

### Pre-Commit Link Checker
Prevent broken links before committing:
```json
{
  "matcher": "Bash(git commit*)",
  "hooks": [{
    "type": "command",
    "command": "npx markdown-link-check **/*.md || (echo '⚠️ Broken links detected'; exit 1)"
  }]
}
```

### Word Count on Stop
Show progress on session end:
```json
{
  "matcher": "",
  "hooks": [{
    "type": "command",
    "command": "bash -c 'wc -w drafts/*.md | tail -1 | awk \"{print \\\"📝 Total words: \\\" \\$1}\"'"
  }]
}
```

### Spell Check on Write
```json
{
  "matcher": "Write(**/*.md)",
  "hooks": [{
    "type": "command",
    "command": "aspell check \"$FILE\" 2>/dev/null || true"
  }]
}
```

---

## Validation Checklist

After setting up:
- [ ] CLAUDE.md is under 60 lines (this example: 29 lines)
- [ ] Voice rules reflect YOUR actual violations, not generic advice
- [ ] Evidence tiers match your research standards (if applicable)
- [ ] Gotchas are project-specific (caused actual errors)
- [ ] Stop hook warns about uncommitted drafts
- [ ] PostToolUse hook lints markdown files
- [ ] Pre-approved linting commands work

---

## Related Patterns

- [context-engineering.md](../../patterns/context-engineering.md) - Minimal CLAUDE.md principles
- [evidence-tiers.md](../../patterns/evidence-tiers.md) - Research and claim validation
- [documentation-maintenance.md](../../patterns/documentation-maintenance.md) - Long-term doc management
- [FOUNDATIONAL-PRINCIPLES.md](../../FOUNDATIONAL-PRINCIPLES.md) - The Big 3

---

## Notes

- This is a **reference example**, not a real blog
- No actual posts included (focus on .claude/ structure)
- Customize for your writing style and standards
- Evidence tiers are optional (remove if not doing research)

**Last Updated**: February 2026
