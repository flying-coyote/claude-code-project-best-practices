---
name: pattern-version-updater
version: 1.0.0
description: Updates pattern files with new version requirements and dependencies
triggers:
  - "update pattern versions"
  - "add version requirements"
  - "new claude code version"
  - "version dependency"
auto_load: false
---

# Pattern Version Updater Skill

**Purpose**: Update pattern files with new version requirements when Claude Code releases new features or breaking changes.

**When to Use**:
- New Claude Code version released (e.g., v2.2.0)
- Feature added that supersedes existing pattern
- Breaking change requires version pinning
- Model capability update (e.g., Opus 5.0)
- User says "update pattern versions" or similar

**What This Skill Does**:
1. Analyzes Claude Code release notes or CHANGELOG.md
2. Identifies features mentioned in patterns
3. Updates pattern frontmatter with version requirements
4. Cross-references related patterns for consistency
5. Updates TOOLS-TRACKER.md matrix
6. Creates summary of changes

---

## Workflow

### Phase 1: Analyze Release Information

**Input Required**:
- Claude Code version (e.g., "v2.2.0")
- Release notes URL or CHANGELOG excerpt
- List of new features (if known)

**Steps**:
1. Read CHANGELOG.md or release notes
2. Extract new features and breaking changes
3. Identify deprecated features
4. Note version-specific capabilities

**Example Analysis**:
```
Version: v2.2.0
New features:
- Context editing API (new capability)
- Enhanced memory tool (improvement)
- Breaking: Deprecated --old-flag

Features mentioned in patterns:
- context-engineering.md: Memory tool
- advanced-tool-use.md: Context editing
```

### Phase 2: Identify Affected Patterns

**Process**:
1. Search patterns/ for feature mentions
2. Use Grep to find relevant keywords
3. Prioritize patterns with explicit version mentions
4. Check for related patterns (cross-references)

**Pattern Classification**:
- **Direct mention**: Pattern explicitly describes the feature
- **Indirect impact**: Pattern uses capability that changed
- **Deprecation**: Pattern recommends deprecated approach

**Output**: List of pattern files to update

### Phase 3: Update Pattern Frontmatter

**For each affected pattern**:

1. **Add or update YAML frontmatter**:
```yaml
---
version-requirements:
  claude-code: "v2.2.0+"  # New minimum version
  model: "Opus 4.6+"      # If model-specific
measurement-claims:
  - claim: "Context editing: 29% improvement"
    source: "Anthropic release notes"
    date: "2026-03-15"
    revalidate: "2027-03-15"
status: "PRODUCTION"
last-verified: "2026-03-15"
---
```

2. **Preserve existing frontmatter** - merge, don't overwrite

3. **Add inline version context** where feature is mentioned:
```markdown
**Session Memory** (v2.1.30+) enables persistent learning across sessions.
```

### Phase 4: Update Cross-References

**Check "Related Patterns" sections**:
- Ensure version requirements are consistent
- Update links if patterns were renamed/deprecated
- Add notes for version-dependent interactions

**Example**:
```markdown
## Related Patterns
- [Context Engineering](./context-engineering.md) - Requires v2.1.30+ for session memory
- [Memory Architecture](./memory-architecture.md) - Enhanced in v2.2.0
```

### Phase 5: Update TOOLS-TRACKER.md

**Run automation**:
```bash
python scripts/generate-tools-tracker.py
```

**Manual verification**:
- Check Version Dependency Matrix reflects new version
- Verify measurement claims have expiry dates
- Ensure new features listed with correct status

### Phase 6: Document Changes

**Create summary**:
```markdown
## Pattern Version Update: v2.2.0

**Patterns Updated**: 5
**New Version Requirements**: 3
**Measurement Claims Added**: 2

### Changes:
- context-engineering.md: Added v2.2.0+ requirement for context editing
- memory-architecture.md: Updated measurement claim (29% improvement)
- advanced-tool-use.md: Added context editing API section
- DEPRECATIONS.md: Documented --old-flag deprecation
- TOOLS-TRACKER.md: Auto-regenerated with new matrix

### Breaking Changes:
- --old-flag deprecated in v2.2.0 (grace period: 90 days)

### Action Required:
- [ ] Review all 5 updated patterns
- [ ] Test examples with v2.2.0
- [ ] Update SOURCES.md if new blog post released
- [ ] Run dogfooding audit
```

---

## Best Practices

### Version Requirement Format

**Use semantic versioning with + suffix**:
- ✅ `v2.1.30+` - Feature requires this version or later
- ✅ `v2.0.0+` - Works with v2.0.0 and above
- ❌ `v2.1.30` - Implies exact version only (rarely needed)

**Model-specific versions**:
- ✅ `Opus 4.6+` - Capability requires this model
- ✅ `Opus 4.6 - Opus 4.9` - Version range (if breaking change in 5.0)
- ⚠️ Use model requirements sparingly (most patterns are model-agnostic)

### Measurement Claim Attribution

**Always include**:
- Exact claim text from source
- Source (Anthropic blog, release notes, etc.)
- Original date
- Revalidate date (1 year for benchmarks)

**Example**:
```yaml
measurement-claims:
  - claim: "Context editing reduces tokens by 84% in 100-round search"
    source: "Anthropic Engineering Blog"
    date: "2025-11-24"
    revalidate: "2026-11-24"
    context: "Tested with Opus 4.6, may change with Opus 5.0"
```

### Handling Breaking Changes

**When feature is deprecated**:
1. Update pattern with deprecation notice
2. Add migration guidance
3. Document in DEPRECATIONS.md
4. Keep pattern in place during grace period
5. Archive after grace period expires

**Example deprecation notice**:
```markdown
## Session Storage (Deprecated in v2.2.0)

**Status**: ❌ DEPRECATED
**Replaced by**: Enhanced memory tool (v2.2.0+)
**Grace period**: Until v2.3.0 (estimated 2026-06-01)

**Migration**:
- Old: `--session-storage` flag
- New: Automatic via memory tool (no flag needed)

See: [DEPRECATIONS.md](../../DEPRECATIONS.md#session-storage)
```

### Consistency Checks

**Before finalizing updates**:
- [ ] All affected patterns have frontmatter
- [ ] Version requirements are consistent across related patterns
- [ ] Measurement claims all have revalidate dates
- [ ] TOOLS-TRACKER.md reflects changes
- [ ] Cross-references updated
- [ ] No broken links
- [ ] DEPRECATIONS.md updated if needed

---

## Example Usage

### Scenario 1: New Feature Release

**User input**: "Claude Code v2.3.0 just released with Playwright integration. Update relevant patterns."

**Skill process**:
1. Analyze: v2.3.0 adds native Playwright support
2. Identify: tool-ecosystem.md, mcp-patterns.md mention Playwright
3. Update frontmatter:
   ```yaml
   version-requirements:
     claude-code: "v2.3.0+"
   ```
4. Add inline mention: "Native Playwright integration (v2.3.0+) replaces MCP-based approach"
5. Update TOOLS-TRACKER.md
6. Document in summary

### Scenario 2: Model Capability Update

**User input**: "Opus 5.0 released with extended reasoning improvements. Update patterns."

**Skill process**:
1. Analyze: Opus 5.0 improves think tool performance
2. Identify: context-engineering.md, advanced-tool-use.md
3. Update frontmatter:
   ```yaml
   version-requirements:
     model: "Opus 4.6+"  # Works with 4.6, better with 5.0
   ```
4. Add note: "Performance improved in Opus 5.0 (2x faster extended reasoning)"
5. Check if measurement claims need revalidation
6. Update TOOLS-TRACKER.md

### Scenario 3: Breaking Change

**User input**: "v2.4.0 removes legacy skill format. Update patterns and deprecate old approach."

**Skill process**:
1. Analyze: Legacy skill format removed
2. Identify: skills-domain-knowledge.md
3. Add deprecation notice to pattern
4. Update DEPRECATIONS.md:
   ```markdown
   ### Legacy Skill Format
   **Deprecated**: v2.4.0 (2026-04-01)
   **Removed**: v2.4.0 (no grace period - breaking change)
   **Migration**: Use YAML frontmatter format (see skills-domain-knowledge.md)
   ```
5. Update frontmatter to require v2.4.0+ for new format
6. Create migration guide

---

## Error Handling

### Invalid Version Format

**If version format is unclear**:
- Ask user for clarification: "Is this v2.2.0 or v2.2.0-beta?"
- Default to standard format: v{major}.{minor}.{patch}+

### Conflicting Requirements

**If patterns have contradictory version requirements**:
- Flag for manual review
- List conflicts in summary
- Suggest resolution (typically use higher version requirement)

**Example conflict**:
```
⚠️ Version Conflict Detected:
- context-engineering.md: v2.1.30+
- memory-architecture.md: v2.0.0+

Both reference session memory feature.
Suggestion: Update memory-architecture.md to v2.1.30+ (feature introduced in 2.1.30)
```

### Missing Release Information

**If CHANGELOG.md or release notes unavailable**:
- Ask user to provide release notes URL
- Check Anthropic blog for announcement
- Use GitHub releases: https://github.com/anthropics/claude-code/releases
- If unavailable: Flag for manual research

---

## Integration with Other Systems

### With emerging-pattern-monitor

**Coordinate on EMERGING patterns**:
- If new version validates EMERGING pattern → promote to PRODUCTION
- Update promotion criteria in pattern frontmatter
- Cross-reference in TOOLS-TRACKER.md

### With TOOLS-TRACKER.md

**Always regenerate after updates**:
```bash
python scripts/generate-tools-tracker.py
```

**Verify**:
- Version Dependency Matrix includes new version
- Measurement Claims Registry has expiry dates
- Component Coverage unchanged (unless new patterns added)

### With DEPRECATIONS.md

**When deprecating features**:
- Add to Active Deprecations section
- Document migration path
- Set grace period (default: 90 days)
- Update affected pattern files with notices

---

## Testing Checklist

**Before committing version updates**:
- [ ] All frontmatter is valid YAML (no syntax errors)
- [ ] Version formats are consistent (vX.Y.Z+ format)
- [ ] Measurement claims have all required fields
- [ ] Cross-references are accurate (no broken links)
- [ ] TOOLS-TRACKER.md regenerates without errors
- [ ] Related patterns are consistent
- [ ] Inline version mentions match frontmatter
- [ ] DEPRECATIONS.md updated if applicable
- [ ] Summary document created

**Test commands**:
```bash
# Validate YAML frontmatter
python scripts/validate-frontmatter.py patterns/

# Regenerate TOOLS-TRACKER.md
python scripts/generate-tools-tracker.py

# Check for broken links
npm run lint

# Test pattern reads
cat patterns/context-engineering.md | head -30
```

---

## Related Patterns

- [Evidence Tiers](../../patterns/evidence-tiers.md) - Version-aware citations
- [Documentation Maintenance](../../patterns/documentation-maintenance.md) - Update cadence
- [Skills Domain Knowledge](../../patterns/skills-domain-knowledge.md) - Skill structure

---

## Skill Maintenance

**This skill should be updated when**:
- Claude Code versioning scheme changes
- New pattern file formats introduced
- YAML frontmatter schema changes
- TOOLS-TRACKER.md structure changes

**Last Updated**: 2026-02-16
**Skill Version**: 1.0.0
