#!/usr/bin/env python3
"""
Generate TOOLS-TRACKER.md from patterns/ directory.

This script:
1. Recursively scans patterns/ for tool/pattern mentions
2. Extracts version requirements (v2.1.0+ format)
3. Extracts measurement claims (85%, 4x, etc.)
4. Cross-references SOURCES.md for evidence tiers
5. Generates TOOLS-TRACKER.md with structured recommendations
6. Detects deprecations by comparing with previous version

Usage:
    python scripts/generate-tools-tracker.py
    python scripts/generate-tools-tracker.py --output TOOLS-TRACKER.md
    python scripts/generate-tools-tracker.py --detect-deprecations
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# Configuration
PATTERNS_DIR = Path("patterns")
SOURCES_FILE = Path("SOURCES.md")
TOOLS_TRACKER_FILE = Path("TOOLS-TRACKER.md")
TOOLS_TRACKER_JSON = Path("TOOLS-TRACKER.json")  # Intermediate JSON for diffing


class PatternParser:
    """Parse patterns directory for tool mentions, versions, and measurements."""

    def __init__(self, patterns_dir: Path):
        self.patterns_dir = patterns_dir
        self.tools = defaultdict(list)  # tool_name -> [mentions]
        self.versions = defaultdict(list)  # pattern_file -> [version_requirements]
        self.measurements = defaultdict(list)  # pattern_file -> [measurements]
        self.evidence_tiers = {}  # source_name -> tier (A/B/C/D)

        # Regex patterns
        self.version_regex = re.compile(r'v([0-9]+\.[0-9]+\.?[0-9]*)\+?')
        self.measurement_regex = re.compile(r'(\d+)%|\b(\d+)x\b|(\d+) times')
        self.tool_names = [
            "Claude Code", "MCP", "Playwright", "Aider", "Cursor", "OpenHands",
            "Auto-Claude", "Skills", "Subagent", "CLAUDE.md", "/rewind", "/fast",
            "/clear", "/plugin", "Opus 4.6", "Think tool"
        ]

    def parse_patterns_directory(self) -> Dict:
        """Recursively scan patterns/ for all markdown files."""
        print(f"📂 Scanning {self.patterns_dir}...")

        pattern_files = list(self.patterns_dir.glob("*.md"))
        print(f"   Found {len(pattern_files)} pattern files")

        results = {
            "tools": {},
            "versions": {},
            "measurements": {},
            "component_coverage": self._init_component_coverage(),
            "last_updated": datetime.now().isoformat(),
        }

        for pattern_file in pattern_files:
            self._parse_pattern_file(pattern_file, results)

        return results

    def _init_component_coverage(self) -> Dict:
        """Initialize 8 critical component tracking."""
        return {
            "CLAUDE.md": [],
            "prompts": [],
            "skills": [],
            "tools": [],
            "mcp": [],
            "sub-agents": [],
            "slash-commands": [],
            "marketplaces": [],
        }

    def _parse_pattern_file(self, pattern_file: Path, results: Dict):
        """Parse a single pattern file for tools, versions, measurements."""
        try:
            content = pattern_file.read_text()

            # Extract tool mentions
            self._extract_tool_mentions(pattern_file, content, results)

            # Extract version requirements
            self._extract_version_requirements(pattern_file, content, results)

            # Extract measurement claims
            self._extract_measurement_claims(pattern_file, content, results)

            # Classify into components
            self._classify_component(pattern_file, content, results)

        except Exception as e:
            print(f"   ⚠️  Error parsing {pattern_file}: {e}")

    def _extract_tool_mentions(self, pattern_file: Path, content: str, results: Dict):
        """Find tool/pattern mentions with surrounding context."""
        for tool_name in self.tool_names:
            # Case-insensitive search
            pattern = re.compile(re.escape(tool_name), re.IGNORECASE)
            matches = pattern.finditer(content)

            for match in matches:
                # Get surrounding context (50 chars before/after)
                start = max(0, match.start() - 50)
                end = min(len(content), match.end() + 50)
                context = content[start:end].replace('\n', ' ')

                if tool_name not in results["tools"]:
                    results["tools"][tool_name] = []

                results["tools"][tool_name].append({
                    "file": str(pattern_file),
                    "context": context,
                })

    def _extract_version_requirements(self, pattern_file: Path, content: str, results: Dict):
        """Extract version requirements (v2.1.0+ format)."""
        matches = self.version_regex.finditer(content)

        for match in matches:
            version_str = match.group(0)

            # Get line number
            line_num = content[:match.start()].count('\n') + 1

            # Get surrounding context
            start = max(0, match.start() - 100)
            end = min(len(content), match.end() + 100)
            context = content[start:end].replace('\n', ' ')

            file_key = str(pattern_file)
            if file_key not in results["versions"]:
                results["versions"][file_key] = []

            results["versions"][file_key].append({
                "version": version_str,
                "line": line_num,
                "context": context,
            })

    def _extract_measurement_claims(self, pattern_file: Path, content: str, results: Dict):
        """Extract measurement claims (85%, 4x, etc.)."""
        matches = self.measurement_regex.finditer(content)

        for match in matches:
            # Determine measurement type and value
            if match.group(1):  # Percentage
                value = f"{match.group(1)}%"
            elif match.group(2):  # Multiplier (4x)
                value = f"{match.group(2)}x"
            elif match.group(3):  # Times (4 times)
                value = f"{match.group(3)} times"
            else:
                continue

            # Get line number
            line_num = content[:match.start()].count('\n') + 1

            # Get surrounding context (broader for measurements)
            start = max(0, match.start() - 150)
            end = min(len(content), match.end() + 150)
            context = content[start:end].replace('\n', ' ')

            # Try to extract claim from context
            claim = self._extract_claim_from_context(context)

            file_key = str(pattern_file)
            if file_key not in results["measurements"]:
                results["measurements"][file_key] = []

            results["measurements"][file_key].append({
                "value": value,
                "claim": claim,
                "line": line_num,
                "context": context,
            })

    def _extract_claim_from_context(self, context: str) -> str:
        """Extract the actual claim from surrounding context."""
        # Look for sentences containing the measurement
        sentences = re.split(r'[.!?]', context)
        for sentence in sentences:
            if re.search(r'\d+%|\d+x|\d+ times', sentence):
                return sentence.strip()
        return context[:100]  # Fallback

    def _classify_component(self, pattern_file: Path, content: str, results: Dict):
        """Classify pattern into one of 8 critical components."""
        filename = pattern_file.stem
        content_lower = content.lower()

        # Component classification rules
        if "claude.md" in content_lower or "project instruction" in content_lower:
            results["component_coverage"]["CLAUDE.md"].append(str(pattern_file))

        if "prompt" in content_lower and ("setup" in content_lower or "bootstrap" in content_lower):
            results["component_coverage"]["prompts"].append(str(pattern_file))

        if "skill" in filename or "skill" in content_lower[:500]:
            results["component_coverage"]["skills"].append(str(pattern_file))

        if "tool" in filename or ("built-in" in content_lower and "tool" in content_lower):
            results["component_coverage"]["tools"].append(str(pattern_file))

        if "mcp" in filename or "model context protocol" in content_lower:
            results["component_coverage"]["mcp"].append(str(pattern_file))

        if "subagent" in filename or "sub-agent" in content_lower:
            results["component_coverage"]["sub-agents"].append(str(pattern_file))

        if "slash command" in content_lower or "/commit" in content_lower or "/rewind" in content_lower:
            results["component_coverage"]["slash-commands"].append(str(pattern_file))

        if "marketplace" in content_lower or "plugin" in filename:
            results["component_coverage"]["marketplaces"].append(str(pattern_file))

    def cross_reference_sources(self, results: Dict) -> Dict:
        """Match tool mentions with SOURCES.md evidence tiers."""
        print(f"📚 Cross-referencing with {SOURCES_FILE}...")

        if not SOURCES_FILE.exists():
            print(f"   ⚠️  {SOURCES_FILE} not found, skipping tier assignment")
            return results

        sources_content = SOURCES_FILE.read_text()

        # Extract evidence tiers from SOURCES.md
        # Format: **Evidence Tier**: A|B|C|D
        tier_pattern = re.compile(r'\*\*Evidence Tier\*\*:\s*([ABCD])', re.IGNORECASE)

        # Also look for source names to map tools to tiers
        # This is a simplified heuristic - may need refinement
        tier_matches = tier_pattern.finditer(sources_content)

        # Store tiers (simplified - in production would need better source-to-tier mapping)
        results["evidence_tier_stats"] = {
            "tier_a_count": sources_content.count("Tier A"),
            "tier_b_count": sources_content.count("Tier B"),
            "tier_c_count": sources_content.count("Tier C"),
            "tier_d_count": sources_content.count("Tier D"),
        }

        return results


def generate_tools_tracker_markdown(results: Dict) -> str:
    """Generate TOOLS-TRACKER.md content from parsed results."""
    print("📝 Generating TOOLS-TRACKER.md...")

    md = []
    md.append("# Tools & Patterns Tracker\n")
    md.append(f"**Last Updated**: {datetime.now().strftime('%Y-%m-%d')}\n")
    md.append("**Auto-generated**: By `scripts/generate-tools-tracker.py`\n")
    md.append("**Purpose**: Single source of truth for all Claude Code tool/pattern recommendations\n")
    md.append("\n---\n\n")

    # Status definitions
    md.append("## Status Definitions\n\n")
    md.append("| Status | Meaning |\n")
    md.append("|--------|----------|\n")
    md.append("| ✅ RECOMMENDED | Production-ready with Tier A/B evidence |\n")
    md.append("| ⚠️ CONSIDER | Conditional use cases, trade-offs apply |\n")
    md.append("| 🔬 EMERGING | Promising pattern, needs validation |\n")
    md.append("| ❌ DEPRECATED | Superseded or obsolete |\n")
    md.append("\n---\n\n")

    # Component coverage summary
    md.append("## Component Coverage\n\n")
    md.append("| Component | Pattern Files | Count |\n")
    md.append("|-----------|---------------|-------|\n")

    for component, files in results["component_coverage"].items():
        file_names = ", ".join([Path(f).stem for f in files[:3]])
        if len(files) > 3:
            file_names += f", ... ({len(files)-3} more)"
        md.append(f"| {component} | {file_names} | {len(files)} |\n")

    md.append("\n---\n\n")

    # Top tools by mentions
    md.append("## Most Referenced Tools\n\n")
    md.append("| Tool | Mentions | Pattern Files |\n")
    md.append("|------|----------|---------------|\n")

    sorted_tools = sorted(results["tools"].items(), key=lambda x: len(x[1]), reverse=True)
    for tool, mentions in sorted_tools[:15]:
        files = set(Path(m["file"]).stem for m in mentions)
        file_str = ", ".join(list(files)[:3])
        if len(files) > 3:
            file_str += f" (+{len(files)-3})"
        md.append(f"| {tool} | {len(mentions)} | {file_str} |\n")

    md.append("\n---\n\n")

    # Version requirements
    md.append("## Version Requirements Found\n\n")
    md.append("| Pattern File | Version | Context |\n")
    md.append("|--------------|---------|----------|\n")

    for file, versions in list(results["versions"].items())[:20]:
        file_name = Path(file).stem
        for v in versions[:2]:  # Limit to 2 per file
            context_short = v["context"][:60] + "..."
            md.append(f"| {file_name} | {v['version']} | {context_short} |\n")

    md.append("\n---\n\n")

    # Measurement claims
    md.append("## Measurement Claims Registry\n\n")
    md.append("| Value | Claim | Pattern File | Line |\n")
    md.append("|-------|-------|--------------|------|\n")

    for file, measurements in list(results["measurements"].items())[:20]:
        file_name = Path(file).stem
        for m in measurements[:2]:  # Limit to 2 per file
            claim_short = m["claim"][:50] + "..."
            md.append(f"| {m['value']} | {claim_short} | {file_name} | {m['line']} |\n")

    md.append("\n---\n\n")

    # Evidence tier summary
    md.append("## Evidence Tier Summary\n\n")
    stats = results.get("evidence_tier_stats", {})
    md.append(f"- Tier A sources: {stats.get('tier_a_count', 'N/A')}\n")
    md.append(f"- Tier B sources: {stats.get('tier_b_count', 'N/A')}\n")
    md.append(f"- Tier C sources: {stats.get('tier_c_count', 'N/A')}\n")
    md.append(f"- Tier D sources: {stats.get('tier_d_count', 'N/A')}\n")
    md.append("\n---\n\n")

    md.append("**Generated by**: `scripts/generate-tools-tracker.py`\n")
    md.append(f"**Timestamp**: {results['last_updated']}\n")

    return "".join(md)


def detect_deprecations(current_results: Dict, previous_json: Path) -> List[Dict]:
    """Detect deprecations by comparing with previous TOOLS-TRACKER.json."""
    print("🔍 Detecting deprecations...")

    if not previous_json.exists():
        print("   ℹ️  No previous JSON found, skipping deprecation detection")
        return []

    try:
        with open(previous_json, 'r') as f:
            previous_results = json.load(f)
    except Exception as e:
        print(f"   ⚠️  Error reading previous JSON: {e}")
        return []

    deprecations = []

    # Compare tool mentions
    current_tools = set(current_results["tools"].keys())
    previous_tools = set(previous_results.get("tools", {}).keys())

    removed_tools = previous_tools - current_tools
    for tool in removed_tools:
        deprecations.append({
            "type": "tool_removed",
            "name": tool,
            "previous_mentions": len(previous_results["tools"].get(tool, [])),
        })

    # Significant decrease in mentions (>50% drop)
    for tool in current_tools & previous_tools:
        prev_count = len(previous_results["tools"].get(tool, []))
        curr_count = len(current_results["tools"].get(tool, []))

        if prev_count > 5 and curr_count < prev_count * 0.5:
            deprecations.append({
                "type": "mention_decrease",
                "name": tool,
                "previous_mentions": prev_count,
                "current_mentions": curr_count,
                "decrease_pct": int((1 - curr_count/prev_count) * 100),
            })

    if deprecations:
        print(f"   ⚠️  Found {len(deprecations)} potential deprecations")
    else:
        print("   ✅ No deprecations detected")

    return deprecations


def main():
    parser = argparse.ArgumentParser(description="Generate TOOLS-TRACKER.md from patterns/")
    parser.add_argument("--output", default=str(TOOLS_TRACKER_FILE), help="Output file path")
    parser.add_argument("--detect-deprecations", action="store_true", help="Detect deprecations")
    args = parser.parse_args()

    # Parse patterns directory
    pattern_parser = PatternParser(PATTERNS_DIR)
    results = pattern_parser.parse_patterns_directory()

    # Cross-reference with SOURCES.md
    results = pattern_parser.cross_reference_sources(results)

    # Generate markdown
    markdown_content = generate_tools_tracker_markdown(results)

    # Write output
    output_path = Path(args.output)
    output_path.write_text(markdown_content)
    print(f"✅ Generated {output_path}")

    # Save JSON for deprecation detection
    TOOLS_TRACKER_JSON.write_text(json.dumps(results, indent=2))
    print(f"✅ Saved intermediate JSON to {TOOLS_TRACKER_JSON}")

    # Detect deprecations if requested
    if args.detect_deprecations:
        deprecations = detect_deprecations(results, TOOLS_TRACKER_JSON)
        if deprecations:
            print("\n📊 Deprecation Report:")
            for dep in deprecations:
                print(f"   - {dep['type']}: {dep['name']}")
                if dep['type'] == 'mention_decrease':
                    print(f"     {dep['previous_mentions']} → {dep['current_mentions']} ({dep['decrease_pct']}% decrease)")

    print("\n✨ Done!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
