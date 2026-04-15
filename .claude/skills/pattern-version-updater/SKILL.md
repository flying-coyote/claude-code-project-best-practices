---
name: analysis-version-updater
version: 2.0.0
description: Updates analysis documents with new version requirements and dependencies when Claude Code releases new features
triggers:
  - "update analysis versions"
  - "add version requirements"
  - "new claude code version"
  - "version dependency"
auto_load: false
---

# Analysis Version Updater Skill

**Purpose**: Update analysis documents with new version requirements when Claude Code releases new features or breaking changes.

**When to Use**:
- New Claude Code version released (e.g., v2.2.0)
- Feature added that supersedes existing analysis
- Breaking change requires version pinning
- Model capability update (e.g., Opus 5.0)
- User says "update analysis versions" or similar

**What This Skill Does**:
1. Analyzes Claude Code release notes or CHANGELOG.md
2. Identifies features mentioned in analysis documents
3. Updates analysis docs with version context
4. Cross-references related analysis docs for consistency
5. Updates SOURCES.md with new release entries
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

### Phase 2: Identify Affected Analysis Documents

**Process**:
1. Search analysis/ for feature mentions
2. Use Grep to find relevant keywords
3. Prioritize documents with explicit version mentions
4. Check for related analysis docs (cross-references)

**Classification**:
- **Direct mention**: Analysis doc explicitly describes the feature
- **Indirect impact**: Analysis doc references capability that changed
- **Deprecation**: Analysis doc recommends deprecated approach

### Phase 3: Update Analysis Documents

**For each affected document**:

1. Add version context inline where feature is mentioned:
```markdown
**Session Memory** (v2.1.30+) enables persistent learning across sessions.
```

2. Update measurement claims if new data available:
```markdown
**Claim**: Context editing reduces tokens by 84% in 100-round search
**Source**: Anthropic Engineering Blog (November 2025)
**Revalidate**: November 2026
```

3. Add deprecation notices for superseded approaches:
```markdown
> **Deprecated in v2.2.0**: [Old approach] replaced by [new approach].
```

### Phase 4: Update Cross-References

- Ensure version context is consistent across related analysis docs
- Update links if analysis docs were renamed
- Add notes for version-dependent interactions

### Phase 5: Update SOURCES.md

- Add new release to Claude Code Changelog section
- Update any source entries affected by the release
- Ensure evidence tier is maintained

### Phase 6: Document Changes

**Create summary**:
```markdown
## Analysis Version Update: v2.2.0

**Documents Updated**: [count]
**New Version Context**: [count]
**Measurement Claims Updated**: [count]

### Changes:
- [list of files and what changed]

### Breaking Changes:
- [list any deprecations]
```

---

## Best Practices

### Version Requirement Format

- `v2.1.30+` - Feature requires this version or later
- `Opus 4.6+` - Capability requires this model
- Use model requirements sparingly (most analysis is model-agnostic)

### Measurement Claim Attribution

Always include: exact claim text, source, date, revalidate date.

### Handling Breaking Changes

1. Update analysis doc with deprecation notice
2. Add migration guidance
3. Document in SOURCES.md changelog section
4. Keep analysis in place during grace period

---

## Related Analysis

- [Evidence Tiers](../../analysis/evidence-tiers.md) - Version-aware citations
- [Harness Engineering](../../analysis/harness-engineering.md) - Update cadence
- [Domain Knowledge Architecture](../../analysis/domain-knowledge-architecture.md) - Skill structure

---

## Skill Maintenance

**This skill should be updated when**:
- Claude Code versioning scheme changes
- Analysis document formats change
- SOURCES.md structure changes

**Last Updated**: April 2026
**Skill Version**: 2.0.0
