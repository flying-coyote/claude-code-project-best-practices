# Issue Draft: Claude in Chrome MCP Deprecated - Recommend Playwright

**Target**: https://github.com/shanraisshan/claude-code-best-practice/issues

**Type**: Deprecation Report

**Labels**: deprecation, mcp, tools

---

## Issue Title

Claude in Chrome MCP deprecated (2026-01-10) - recommend Playwright migration

## Issue Body

### Summary

The "Claude in Chrome" MCP server has been deprecated as of January 10, 2026, with a 90-day grace period ending April 10, 2026. We recommend updating the MCP recommendations to suggest **Playwright** as the migration path.

### Evidence

**Deprecation announcement**: [Citation needed - check Anthropic announcements]

**Token efficiency comparison**:
- Claude in Chrome MCP: ~114K tokens at startup
- Playwright CLI: ~27K tokens
- **Improvement**: 76% token reduction (4x more efficient)

Source: [MCP Context Budget Analysis](https://dev.to/valgard/claude-code-must-haves-january-2026-kem)

### Recommended Migration Path

#### Option 1: Playwright MCP (If MCP protocol required)
```bash
claude-code mcp install playwright
```
- Token cost: ~20K tokens
- Provides: Browser automation, testing, screenshots
- Best for: Frontend/fullstack testing needs

#### Option 2: Playwright CLI (Most token-efficient)
```bash
npm install -D @playwright/test
```
- Token cost: ~27K tokens (via Bash tool invocation)
- Same capabilities as MCP
- Best for: Token budget optimization

### Suggested Changes to Repository

**In MCP recommendations section**:

```diff
- ❌ Claude in Chrome (browser automation, console debugging)
+ ✅ Playwright (browser automation, E2E testing, UI interactions)
+    - Replaces Claude in Chrome (deprecated 2026-01-10)
+    - 4x more token-efficient
+    - Production-ready vs experimental
```

**Add deprecation notice**:
```markdown
### ⚠️ Recently Deprecated

- **Claude in Chrome** (deprecated 2026-01-10, grace period ends 2026-04-10)
  - **Migration**: Use Playwright MCP or Playwright CLI
  - **Reason**: Token efficiency (4x improvement) + production readiness
```

### Our Offer

We maintain a [deprecation tracking process](https://github.com/flying-coyote/claude-code-project-best-practices/blob/master/DEPRECATIONS.md) as part of our quarterly reviews. We're happy to:

1. Submit this as a PR if you prefer
2. Continue monitoring for future deprecations (quarterly reports)
3. Provide migration guides as tools evolve

### Additional Context

We track deprecations systematically to help the community avoid outdated tools. Our full deprecation log: [DEPRECATIONS.md](https://github.com/flying-coyote/claude-code-project-best-practices/blob/master/DEPRECATIONS.md)

**Related**: We also found that the sweet spot for daily use is **Context7 + Sequential Thinking** (25K tokens = 12.5% of context budget), with specialized MCPs like Playwright enabled per-project via `.claude/settings.json`.

---

### Checklist

Before submitting this issue:
- [ ] Verify Claude in Chrome deprecation date and source
- [ ] Confirm Playwright is recommended alternative (check official Anthropic guidance)
- [ ] Test Playwright MCP installation to verify instructions
- [ ] Check shanraisshan's repository for existing issues about this
- [ ] Review shanraisshan's contribution guidelines
- [ ] Prepare PR if they prefer PRs over issues

### Tone Notes

- Helpful, not prescriptive ("recommend" not "you should")
- Provide evidence, not opinion
- Offer ongoing help, not one-time correction
- Credit their work (5.6k+ stars, valuable community resource)
