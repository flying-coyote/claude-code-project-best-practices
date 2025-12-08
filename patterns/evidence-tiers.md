# Evidence Tier System

A classification framework for source quality and claim confidence.

## Tier Definitions

### Tier A: Primary Sources
- **What**: Direct observation, production data, official documentation
- **Examples**:
  - Anthropic's own engineering blog posts
  - Your own production implementation results
  - Official vendor documentation
  - Published specifications (RFC, IEEE, NIST)
- **Weight**: Strongest evidence - suitable for definitive claims

### Tier B: Peer-Reviewed & Expert
- **What**: Academic publications, expert interviews, validated analyses
- **Examples**:
  - Peer-reviewed academic papers
  - Expert interviews with named sources
  - Conference proceedings (USENIX, IEEE S&P)
  - Industry certifications and audits
- **Weight**: Strong evidence - suitable for confident claims

### Tier C: Industry & Analysis
- **What**: Industry reports, vendor documentation, analysis pieces
- **Examples**:
  - Gartner/Forrester reports
  - Vendor whitepapers (treated with skepticism)
  - Industry blog posts from practitioners
  - Community best practices
- **Weight**: Supporting evidence - should be corroborated

### Tier D: Opinions & Speculation
- **What**: Personal opinions, speculative analysis, unverified claims
- **Examples**:
  - Social media discussions
  - Unattributed claims
  - Theoretical projections
  - Your own speculation
- **Weight**: Context only - not suitable for definitive claims

## Usage Guidelines

### For Publication
- **Strong claims**: Require Tier A or B evidence
- **Opinions**: Can use Tier C with attribution
- **Speculation**: Must be clearly labeled as such
- **Never**: Present Tier D as fact

### For Research
- **Hypothesis formation**: Any tier can inspire hypotheses
- **Hypothesis validation**: Requires Tier A or B
- **Confidence levels**:
  - High (5): Multiple Tier A sources
  - Medium (3-4): Tier B sources
  - Low (1-2): Tier C or single source

### For Decision Making
- **Architectural decisions**: Tier A or B required
- **Tool selection**: Tier B acceptable, verify with POC
- **Best practices**: Tier C acceptable if consensus exists

## Citation Format

```markdown
**Claim** (Tier X - Source Type)
Source: [Name/Title]
URL: [if applicable]
Date: [when published/accessed]
```

Example:
```markdown
**Tool Search Tool reduces context by 85%** (Tier A - Primary Source)
Source: Anthropic Developer Blog
URL: https://www.anthropic.com/engineering/...
Date: November 24, 2025
```

## Contradiction Handling

When sources conflict:
1. **Note the contradiction** - Document both positions
2. **Evaluate tier quality** - Higher tier takes precedence
3. **Seek resolution** - Look for additional sources
4. **Be transparent** - Acknowledge uncertainty in your claims

Example:
> "Vendor X claims 10x performance improvement (Tier C), while independent benchmark shows 3x (Tier B). The conservative estimate is more reliable."

## Integration with Skills

### academic-citation-manager
- Validates evidence tiers in claims
- Flags unsupported assertions
- Suggests appropriate tier for sources

### publication-quality-checker
- Requires Tier A-B for strong claims
- Warns on Tier C without corroboration
- Blocks Tier D presented as fact

### hypothesis-validator
- Tracks evidence tier per hypothesis
- Requires higher tier for validation
- Distinguishes speculation from evidence
