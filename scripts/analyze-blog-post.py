#!/usr/bin/env python3
"""
Analyze Anthropic blog post using Claude API.

Uses Claude API to analyze blog post content and identify:
- New Claude Code patterns or recommendations
- Updates to existing patterns
- Deprecated practices
- Affected pattern files

Requires ANTHROPIC_API_KEY environment variable.

Usage:
    export ANTHROPIC_API_KEY="your-api-key"
    python scripts/analyze-blog-post.py --url https://www.anthropic.com/...
    python scripts/analyze-blog-post.py --url https://... --create-issue
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

try:
    import requests
except ImportError:
    print("⚠️  requests library not found. Install with: pip install requests")
    sys.exit(1)

try:
    from anthropic import Anthropic
except ImportError:
    print("⚠️  anthropic library not found. Install with: pip install anthropic")
    sys.exit(1)


class BlogPostAnalyzer:
    """Analyze blog post using Claude API."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")

        self.client = Anthropic(api_key=self.api_key)
        self.patterns_dir = Path("patterns")

    def fetch_blog_content(self, url: str) -> str:
        """Fetch blog post content."""
        print(f"🌐 Fetching blog post from {url}...")

        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"❌ Error fetching blog post: {e}")
            return ""

        # Extract text content (simplified - in production would use BeautifulSoup)
        content = response.text

        # Remove HTML tags (basic cleaning)
        content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
        content = re.sub(r'<[^>]+>', '', content)
        content = re.sub(r'\s+', ' ', content)

        print(f"   Fetched {len(content)} characters")
        return content[:8000]  # Limit to 8000 chars for API

    def get_pattern_summaries(self) -> str:
        """Get summaries of existing patterns for context."""
        pattern_files = list(self.patterns_dir.glob("*.md"))
        summaries = []

        for pf in pattern_files[:20]:  # Limit to 20 patterns for token efficiency
            name = pf.stem
            # Read first 100 chars of file
            try:
                content = pf.read_text()
                first_line = content.split('\n')[0].replace('#', '').strip()
                summaries.append(f"- {name}: {first_line}")
            except Exception:
                continue

        return "\n".join(summaries)

    def analyze_with_claude(self, blog_content: str, blog_url: str) -> Dict:
        """Use Claude API to analyze blog post."""
        print("🤖 Analyzing with Claude API...")

        pattern_summaries = self.get_pattern_summaries()

        prompt = f"""Analyze this Anthropic blog post for Claude Code best practices updates.

Blog URL: {blog_url}

Blog Content:
{blog_content}

---

Existing Claude Code patterns in this repository:
{pattern_summaries}

---

Your task:
1. Identify NEW patterns or recommendations relevant to Claude Code
2. Identify UPDATES to existing patterns (changes, improvements, deprecations)
3. Identify DEPRECATIONS (practices that should no longer be used)
4. List affected pattern files that should be updated
5. Provide specific recommendations for each update

Respond in this JSON format:
{{
    "relevance_score": 0-10,
    "summary": "Brief summary of blog post",
    "new_patterns": [
        {{
            "name": "Pattern name",
            "description": "What it does",
            "evidence_tier": "A",
            "recommendation": "Specific action to take"
        }}
    ],
    "updates": [
        {{
            "pattern_file": "pattern-name.md",
            "update_type": "enhancement|deprecation|correction",
            "description": "What changed",
            "recommendation": "Specific change to make"
        }}
    ],
    "affected_patterns": ["pattern-name.md", ...],
    "key_quotes": ["Quote 1", "Quote 2"]
}}

Focus on:
- Claude Code CLI and features
- Skills and subagent patterns
- MCP server recommendations
- Tool ecosystem changes
- Model capability updates (Opus 4.6, etc.)
- Performance benchmarks
- Security guidance

If blog post is NOT relevant to Claude Code best practices, set relevance_score to 0-3.
"""

        try:
            message = self.client.messages.create(
                model="claude-opus-4.6",
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}]
            )

            response_text = message.content[0].text

            # Parse JSON from response
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if json_match:
                analysis = json.loads(json_match.group(0))
            else:
                # Fallback: treat entire response as summary
                analysis = {
                    "relevance_score": 5,
                    "summary": response_text[:200],
                    "new_patterns": [],
                    "updates": [],
                    "affected_patterns": [],
                    "key_quotes": [],
                }

            print(f"   Relevance score: {analysis.get('relevance_score', 'N/A')}/10")
            return analysis

        except Exception as e:
            print(f"❌ Error analyzing with Claude API: {e}")
            return {
                "relevance_score": 0,
                "summary": f"Error: {str(e)}",
                "new_patterns": [],
                "updates": [],
                "affected_patterns": [],
                "key_quotes": [],
            }

    def run(self, url: str) -> Dict:
        """Run full analysis pipeline."""
        blog_content = self.fetch_blog_content(url)

        if not blog_content:
            return {
                "error": "Failed to fetch blog content",
                "url": url,
            }

        analysis = self.analyze_with_claude(blog_content, url)
        analysis["url"] = url
        analysis["analyzed_at"] = datetime.now().isoformat()

        return analysis


def generate_issue_body(analysis: Dict) -> str:
    """Generate GitHub issue body from analysis."""
    body = []
    body.append("## Blog Post Analysis: Claude Code Updates\n\n")
    body.append(f"**URL**: {analysis['url']}\n")
    body.append(f"**Analyzed**: {analysis['analyzed_at']}\n")
    body.append(f"**Relevance Score**: {analysis.get('relevance_score', 'N/A')}/10\n\n")

    # Summary
    body.append("### Summary\n\n")
    body.append(f"{analysis.get('summary', 'No summary available')}\n\n")

    # New patterns
    new_patterns = analysis.get("new_patterns", [])
    if new_patterns:
        body.append(f"### 🆕 New Patterns ({len(new_patterns)})\n\n")
        for pattern in new_patterns:
            body.append(f"#### {pattern['name']}\n\n")
            body.append(f"**Description**: {pattern['description']}\n\n")
            body.append(f"**Evidence Tier**: {pattern['evidence_tier']}\n\n")
            body.append(f"**Recommendation**: {pattern['recommendation']}\n\n")
            body.append("---\n\n")

    # Updates
    updates = analysis.get("updates", [])
    if updates:
        body.append(f"### 🔄 Updates to Existing Patterns ({len(updates)})\n\n")
        for update in updates:
            body.append(f"#### {update['pattern_file']}\n\n")
            body.append(f"**Update Type**: {update['update_type']}\n\n")
            body.append(f"**Description**: {update['description']}\n\n")
            body.append(f"**Recommendation**: {update['recommendation']}\n\n")
            body.append("---\n\n")

    # Affected patterns
    affected = analysis.get("affected_patterns", [])
    if affected:
        body.append(f"### 📄 Affected Pattern Files ({len(affected)})\n\n")
        for pattern in affected:
            body.append(f"- [ ] `patterns/{pattern}`\n")
        body.append("\n")

    # Key quotes
    quotes = analysis.get("key_quotes", [])
    if quotes:
        body.append("### 📌 Key Quotes\n\n")
        for quote in quotes:
            body.append(f"> {quote}\n\n")

    # Action items
    body.append("### ✅ Action Items\n\n")
    body.append("- [ ] Review blog post in full\n")
    body.append("- [ ] Update affected pattern files\n")
    body.append("- [ ] Add URL to SOURCES.md with evidence tier A\n")
    body.append("- [ ] Run dogfooding audit if new patterns apply to this repo\n")
    body.append("- [ ] Update TOOLS-TRACKER.md if tool recommendations changed\n")
    body.append("- [ ] Check DEPRECATIONS.md if any deprecations identified\n\n")

    body.append("---\n\n")
    body.append("**Generated by**: `scripts/analyze-blog-post.py`\n")
    body.append(f"**Model**: Claude Opus 4.6\n")

    return "".join(body)


def main():
    parser = argparse.ArgumentParser(description="Analyze Anthropic blog post with Claude API")
    parser.add_argument("--url", required=True, help="Blog post URL")
    parser.add_argument("--create-issue", action="store_true", help="Create GitHub issue from analysis")
    args = parser.parse_args()

    # Check for API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("❌ ANTHROPIC_API_KEY environment variable not set")
        print("   Set it with: export ANTHROPIC_API_KEY='your-key'")
        return 1

    # Run analysis
    try:
        analyzer = BlogPostAnalyzer()
        analysis = analyzer.run(args.url)
    except Exception as e:
        print(f"❌ Analysis failed: {e}")
        return 1

    # Print summary
    print(f"\n📊 Analysis Summary:")
    print(f"   Relevance: {analysis.get('relevance_score', 'N/A')}/10")
    print(f"   New patterns: {len(analysis.get('new_patterns', []))}")
    print(f"   Updates: {len(analysis.get('updates', []))}")
    print(f"   Affected files: {len(analysis.get('affected_patterns', []))}")

    # Generate issue body
    issue_body = generate_issue_body(analysis)

    if args.create_issue:
        # Write issue body to file
        issue_file = Path("blog-analysis-issue.md")
        issue_file.write_text(issue_body)
        print(f"\n✅ Issue body written to {issue_file}")

        # Also save full analysis as JSON
        json_file = Path("blog-analysis.json")
        with open(json_file, 'w') as f:
            json.dump(analysis, f, indent=2)
        print(f"✅ Full analysis saved to {json_file}")

    else:
        print("\n📝 Issue Body Preview:")
        print("=" * 60)
        print(issue_body)
        print("=" * 60)
        print("\n💡 Run with --create-issue to generate issue file")

    print("\n✅ Analysis complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
