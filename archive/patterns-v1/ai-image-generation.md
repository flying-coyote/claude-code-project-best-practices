# AI Image Generation for Development

**Source**: [google-image-gen-api-starter](https://github.com/AI-Engineer-Skool/google-image-gen-api-starter), production experience
**Evidence Tier**: C (Community tool, production-validated)

## Overview

AI image generation tools can accelerate development workflows by automating visual asset creation. This pattern covers when to use AI image generation, how to integrate it effectively, and best practices for maintaining quality and consistency.

**Key Insight**: AI image generation is most valuable when integrated into automated pipelines, not as a replacement for professional design work.

---

## When to Use AI Image Generation

### Good Fits

| Use Case | Why AI Works | Example |
|----------|--------------|---------|
| **Documentation diagrams** | Consistent style, quick iteration | Architecture diagrams, flow charts |
| **Placeholder assets** | Speed over polish during development | Prototype UI mockups |
| **Icon generation** | Batch creation with style templates | App icons, UI elements |
| **Visual explanations** | Conceptual illustrations | README banners, blog illustrations |
| **Automated pipelines** | Scriptable, reproducible | CI/CD asset generation |

### Poor Fits

| Use Case | Why Not | Alternative |
|----------|---------|-------------|
| **Brand-critical assets** | Inconsistent with brand guidelines | Professional design |
| **Photography replacement** | AI artifacts, uncanny valley | Stock photos, professional shoots |
| **Legal/compliance visuals** | Accuracy requirements | Manual verification required |
| **High-resolution print** | Resolution limitations | Vector graphics, professional tools |

---

## Tool Recommendation: google-image-gen-api-starter

### Overview

A CLI tool for generating images using Google's Gemini API, designed for developer workflows.

**Repository**: https://github.com/AI-Engineer-Skool/google-image-gen-api-starter

### Key Features

| Feature | Description |
|---------|-------------|
| **CLI-native** | Integrates with scripts and automation |
| **Style templates** | Reusable prompts in markdown files |
| **Reference images** | Use existing images for style consistency |
| **Image editing** | Modify existing images with text prompts |
| **Batch generation** | Multiple subjects in one command |
| **Aspect ratios** | 1:1, 16:9, 9:16, and more |

### Prerequisites

1. **Google AI API Key**: https://aistudio.google.com/apikey
2. **Python 3.10+**: Required runtime
3. **uv**: Python package manager (recommended)

### Installation

```bash
# Clone the repository
git clone https://github.com/AI-Engineer-Skool/google-image-gen-api-starter
cd google-image-gen-api-starter

# Install dependencies
uv sync

# Configure API key
cp .env.example .env
# Edit .env: GOOGLE_AI_API_KEY=your_key_here
```

---

## Integration Patterns

### Pattern 1: Documentation Asset Generation

Generate consistent visuals for documentation.

**Use Case**: README banners, architecture diagrams, feature illustrations.

```bash
# Generate architecture diagram
uv run python main.py docs/assets/architecture.png \
  "Clean isometric diagram showing microservices: API Gateway, Auth Service, User Service, Database"

# Generate with style template for consistency
uv run python main.py docs/assets/feature-auth.png \
  "user authentication flow" \
  --style styles/documentation.md
```

**Style Template Example** (`styles/documentation.md`):

```markdown
## Prompt Template

```
Professional technical illustration on white background. Clean, minimal design.
{subject}. Modern flat design style with subtle shadows.
Corporate blue (#0066CC) accent color. No text or labels.
```
```

### Pattern 2: Development Prototyping

Quick visual mockups during development iterations.

**Use Case**: UI component previews, design exploration, stakeholder demos.

```bash
# Generate UI mockup
uv run python main.py mockups/dashboard.png \
  "Modern SaaS dashboard with sidebar navigation, metrics cards, and data table" \
  --aspect 16:9

# Iterate on existing design
uv run python main.py mockups/dashboard-v2.png \
  "Add a dark mode theme" \
  --edit mockups/dashboard.png
```

### Pattern 3: CI/CD Asset Pipeline

Automated asset generation in continuous integration.

**Use Case**: Dynamic documentation, release assets, automated visual testing baselines.

**GitHub Actions Example**:

```yaml
name: Generate Documentation Assets

on:
  push:
    paths:
      - 'docs/**'
      - 'styles/**'

jobs:
  generate-assets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install uv
        run: pip install uv

      - name: Clone image generator
        run: |
          git clone https://github.com/AI-Engineer-Skool/google-image-gen-api-starter /tmp/image-gen
          cd /tmp/image-gen && uv sync

      - name: Generate assets
        env:
          GOOGLE_AI_API_KEY: ${{ secrets.GOOGLE_AI_API_KEY }}
        run: |
          cd /tmp/image-gen
          uv run python main.py $GITHUB_WORKSPACE/docs/assets/banner.png \
            "Project banner for ${GITHUB_REPOSITORY}" \
            --style styles/banner.md

      - name: Commit generated assets
        run: |
          git config user.name github-actions
          git config user.email github-actions@github.com
          git add docs/assets/
          git diff --staged --quiet || git commit -m "🎨 Auto-generate documentation assets"
          git push
```

### Pattern 4: Style Template Library

Maintain consistent visual language across projects.

**Directory Structure**:

```
styles/
├── documentation.md      # Technical diagrams
├── marketing.md          # Promotional assets
├── icons.md              # UI icons
├── diagrams/
│   ├── architecture.md   # System architecture
│   ├── flow.md           # Process flows
│   └── sequence.md       # Sequence diagrams
└── brand/
    ├── primary.md        # Primary brand style
    └── secondary.md      # Secondary variations
```

**Template Anatomy**:

```markdown
# Style: Technical Documentation

## Purpose
Clean, professional diagrams for technical documentation.

## Prompt Template

```
Professional technical illustration. White background. Clean minimal design.
{subject}.
Style: Modern flat design with subtle depth.
Colors: Corporate blue (#0066CC) primary, gray (#666666) secondary.
Constraints: No text, no labels, no watermarks. Centered composition.
```

## Usage Examples
- Architecture diagrams
- Component relationships
- Data flow visualizations

## Reference Images
See `styles/examples/documentation/` for reference outputs.
```

---

## Best Practices

### Prompt Engineering for Images

| Practice | Example |
|----------|---------|
| **Front-load constraints** | "NO text, NO watermarks. Clean white background. Then describe subject..." |
| **Be specific about style** | "Isometric 3D render" vs "illustration" vs "flat design" |
| **Include color codes** | "Corporate blue (#0066CC)" not just "blue" |
| **Specify composition** | "Centered, with 20% padding" |
| **Exclude unwanted elements** | "No people, no text, no gradients" |

### Quality Control

1. **Version control generated assets**: Track in git for history and rollback
2. **Review before publishing**: AI can produce unexpected results
3. **Maintain reference images**: Use `--ref` for style consistency
4. **Document prompts**: Store the prompt that generated each asset

### Cost Management

| Tier | Recommendation |
|------|----------------|
| **Free tier** | Development and testing only (rate limits) |
| **Paid tier** | Production pipelines (recommended) |

**Rate Limit Handling**:
```bash
# Add delay between batch generations
for subject in "cube" "sphere" "pyramid"; do
  uv run python main.py "output_${subject}.png" "$subject" --style styles/icons.md
  sleep 2  # Respect rate limits
done
```

---

## Integration with Claude Code

### Using Image Generation in Claude Code Sessions

Claude Code can invoke the image generator as part of development workflows:

```markdown
## CLAUDE.md Integration

### Image Generation
For visual assets, use the google-image-gen-api-starter tool:

```bash
# Located at: /path/to/google-image-gen-api-starter
uv run python main.py <output> <prompt> [--style <template>]
```

Style templates are in `styles/` directory. Use consistent templates for project assets.
```

### Hook Integration

Generate assets automatically on documentation changes:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "command": "bash .claude/hooks/check-asset-needs.sh"
      }
    ]
  }
}
```

**Hook Script** (`.claude/hooks/check-asset-needs.sh`):
```bash
#!/bin/bash
# Check if documentation was updated and regenerate assets if needed
if echo "$CLAUDE_TOOL_INPUT" | grep -q "docs/"; then
  echo "Documentation updated - consider regenerating assets"
fi
```

---

## Limitations and Mitigations

| Limitation | Mitigation |
|------------|------------|
| **Safety filters** | Rephrase prompts; avoid potentially sensitive content |
| **Resolution caps** | Use vector graphics for print; AI for web only |
| **Style inconsistency** | Use reference images and style templates |
| **Text rendering** | Never rely on AI for text; add text in post-processing |
| **Latency** | Pre-generate assets; don't generate on-demand in production |

---

## Alternative Tools

| Tool | API | Strengths | Weaknesses |
|------|-----|-----------|------------|
| **google-image-gen-api-starter** | Gemini | CLI-native, style templates, editing | Paid tier recommended |
| **DALL-E API** | OpenAI | High quality, wide adoption | No CLI tool, API only |
| **Stable Diffusion** | Local/API | Privacy, customizable | Setup complexity |
| **Midjourney** | Discord | Artistic quality | Not scriptable |

**Recommendation**: google-image-gen-api-starter for developer workflows due to CLI integration and style template support.

---

## SDD Phase Alignment

**Phase**: Tasks + Implement (asset generation as implementation task)

| SDD Phase | Image Generation Application |
|-----------|------------------------------|
| **Specify** | Define visual requirements in specs |
| **Plan** | Identify assets needed, create style templates |
| **Tasks** | List specific images to generate |
| **Implement** | Generate assets, integrate into project |

---

## Related Patterns

- [Tool Ecosystem](./tool-ecosystem.md) - Complementary tools overview
- [Documentation Maintenance](./documentation-maintenance.md) - Keeping docs current
- [Advanced Hooks](./advanced-hooks.md) - Automating asset generation

---

## Anti-Patterns

### ❌ AI for Brand-Critical Assets
**Problem**: Using AI image generation for brand identity, logos, or marketing materials
**Symptom**: Inconsistent brand representation, professional appearance degraded
**Solution**: Reserve AI for development assets; use professional design for brand materials

### ❌ Expecting Reliable Text Rendering
**Problem**: Relying on AI to render text, labels, or captions in images
**Symptom**: Misspelled, garbled, or missing text in generated images
**Solution**: Generate images without text; add text in post-processing with design tools

### ❌ On-Demand Production Generation
**Problem**: Generating images at request time in production applications
**Symptom**: Slow response times, rate limit errors, unpredictable results for users
**Solution**: Pre-generate assets; use AI generation in build/CI pipelines only

### ❌ Ignoring Style Templates
**Problem**: Ad-hoc prompts without consistent style guidance
**Symptom**: Visually inconsistent assets across project
**Solution**: Create and maintain style templates in `styles/` directory

---

## Sources

- [google-image-gen-api-starter](https://github.com/AI-Engineer-Skool/google-image-gen-api-starter) - CLI tool for Gemini image generation
- [Google AI Studio](https://aistudio.google.com) - API key management
- [Gemini API Documentation](https://ai.google.dev/docs) - Official API reference

*Last updated: January 2026*
