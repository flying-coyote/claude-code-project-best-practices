"""Parser for pattern markdown files."""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class PatternMetadata:
    """Metadata extracted from a pattern file."""
    id: str
    name: str
    file_path: str
    sources: list[dict] = field(default_factory=list)
    evidence_tier: Optional[str] = None
    sdd_phase: Optional[str] = None
    related_patterns: list[str] = field(default_factory=list)
    sections: list[str] = field(default_factory=list)
    internal_links: list[str] = field(default_factory=list)
    external_links: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "file_path": self.file_path,
            "sources": self.sources,
            "evidence_tier": self.evidence_tier,
            "sdd_phase": self.sdd_phase,
            "related_patterns": self.related_patterns,
            "sections": self.sections,
            "internal_links": self.internal_links,
            "external_links": self.external_links,
        }


class MarkdownParser:
    """Parser for pattern markdown files."""

    # Evidence tier pattern: (Evidence Tier A) or **Evidence Tier**: A
    EVIDENCE_TIER_PATTERN = re.compile(
        r'(?:\(Evidence Tier ([A-D])\)|\*\*Evidence Tier\*\*:\s*([A-D]))',
        re.IGNORECASE
    )

    # SDD Phase pattern: **SDD Phase**: Specify
    SDD_PHASE_PATTERN = re.compile(
        r'\*\*SDD Phase\*\*:\s*(\w+)',
        re.IGNORECASE
    )

    # Source link pattern: [title](url)
    LINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    # Section header pattern: ## Header
    SECTION_PATTERN = re.compile(r'^##\s+(.+)$', re.MULTILINE)

    # Related patterns pattern: patterns/xxx.md or [Pattern Name](patterns/xxx.md)
    RELATED_PATTERN = re.compile(r'patterns/([a-z0-9-]+)\.md')

    def __init__(self, patterns_dir: Path):
        self.patterns_dir = patterns_dir

    def _strip_code_blocks(self, content: str) -> str:
        """Remove code blocks from content to avoid false link detection."""
        # Remove fenced code blocks (```...```)
        content = re.sub(r'```[\s\S]*?```', '', content)
        # Remove inline code (`...`)
        content = re.sub(r'`[^`]+`', '', content)
        return content

    def parse_file(self, file_path: Path) -> PatternMetadata:
        """Parse a single pattern file."""
        content = file_path.read_text(encoding='utf-8')

        # Extract pattern ID from filename
        pattern_id = file_path.stem

        # Extract title from first H1
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        name = title_match.group(1) if title_match else pattern_id.replace('-', ' ').title()

        # Extract evidence tier
        tier_match = self.EVIDENCE_TIER_PATTERN.search(content)
        evidence_tier = None
        if tier_match:
            evidence_tier = tier_match.group(1) or tier_match.group(2)

        # Extract SDD phase
        phase_match = self.SDD_PHASE_PATTERN.search(content)
        sdd_phase = phase_match.group(1).lower() if phase_match else None

        # Extract sources
        sources = self._extract_sources(content)

        # Extract sections
        sections = self.SECTION_PATTERN.findall(content)

        # Strip code blocks before extracting links to avoid false positives
        content_without_code = self._strip_code_blocks(content)

        # Extract all links (from content without code blocks)
        all_links = self.LINK_PATTERN.findall(content_without_code)
        internal_links = []
        external_links = []
        for title, url in all_links:
            if url.startswith('http://') or url.startswith('https://'):
                external_links.append(url)
            else:
                internal_links.append(url)

        # Extract related patterns (from content without code blocks)
        related_patterns = list(set(self.RELATED_PATTERN.findall(content_without_code)))
        # Remove self-reference
        related_patterns = [p for p in related_patterns if p != pattern_id]

        return PatternMetadata(
            id=pattern_id,
            name=name,
            file_path=str(file_path.relative_to(self.patterns_dir.parent)),
            sources=sources,
            evidence_tier=evidence_tier,
            sdd_phase=sdd_phase,
            related_patterns=related_patterns,
            sections=sections,
            internal_links=internal_links,
            external_links=external_links,
        )

    def _extract_sources(self, content: str) -> list[dict]:
        """Extract source references from content."""
        sources = []

        # Look for Sources section
        sources_match = re.search(
            r'\*\*Sources?\*\*:\s*\n((?:[-*]\s+.+\n?)+)',
            content
        )
        if sources_match:
            sources_text = sources_match.group(1)
            for line in sources_text.strip().split('\n'):
                link_match = self.LINK_PATTERN.search(line)
                if link_match:
                    title, url = link_match.groups()
                    tier_match = self.EVIDENCE_TIER_PATTERN.search(line)
                    tier = None
                    if tier_match:
                        tier = tier_match.group(1) or tier_match.group(2)
                    sources.append({
                        "title": title,
                        "url": url,
                        "tier": tier
                    })

        return sources

    def parse_all(self) -> list[PatternMetadata]:
        """Parse all pattern files in the directory."""
        patterns = []
        for file_path in sorted(self.patterns_dir.glob('*.md')):
            patterns.append(self.parse_file(file_path))
        return patterns
