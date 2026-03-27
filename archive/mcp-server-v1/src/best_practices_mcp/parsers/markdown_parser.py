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

    # Related patterns pattern: patterns/xxx.md or ./xxx.md or [Pattern Name](./xxx.md)
    RELATED_PATTERN = re.compile(r'(?:patterns/|\./|/)([a-z0-9-]+)\.md')

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
        seen_urls = set()

        # Method 1: Look for ## Sources section (most common format)
        sources_section_match = re.search(
            r'^##\s+Sources?\s*\n((?:[-*]\s+.+\n?)+)',
            content,
            re.MULTILINE
        )
        if sources_section_match:
            sources_text = sources_section_match.group(1)
            for line in sources_text.strip().split('\n'):
                line_text = line.lstrip('-* ').strip()
                if not line_text:
                    continue
                link_match = self.LINK_PATTERN.search(line)
                if link_match:
                    title, url = link_match.groups()
                    if url not in seen_urls:
                        seen_urls.add(url)
                        tier_match = self.EVIDENCE_TIER_PATTERN.search(line)
                        tier = None
                        if tier_match:
                            tier = tier_match.group(1) or tier_match.group(2)
                        sources.append({
                            "title": title,
                            "url": url,
                            "tier": tier
                        })
                else:
                    # Plain text source (no URL)
                    sources.append({
                        "title": line_text,
                        "url": None,
                        "tier": None
                    })

        # Method 2: Look for **Sources**: or **Source**: inline format
        inline_sources_match = re.search(
            r'\*\*Sources?\*\*:\s*(.+?)(?:\n\n|\n##|\Z)',
            content,
            re.DOTALL
        )
        if inline_sources_match:
            sources_text = inline_sources_match.group(1)
            for link_match in self.LINK_PATTERN.finditer(sources_text):
                title, url = link_match.groups()
                if url.startswith('http') and url not in seen_urls:
                    seen_urls.add(url)
                    sources.append({
                        "title": title,
                        "url": url,
                        "tier": None
                    })

        # Method 3: Look for **Tier X Sources**: format (used in some patterns)
        tier_sources_matches = re.finditer(
            r'\*\*Tier ([A-D]) Sources?\*\*:\s*\n((?:[-*]\s+.+\n?)+)',
            content
        )
        for match in tier_sources_matches:
            tier = match.group(1)
            sources_text = match.group(2)
            for line in sources_text.strip().split('\n'):
                # Extract title from line (may not have URL)
                line = line.lstrip('-* ').strip()
                link_match = self.LINK_PATTERN.search(line)
                if link_match:
                    title, url = link_match.groups()
                    if url not in seen_urls:
                        seen_urls.add(url)
                        sources.append({
                            "title": title,
                            "url": url,
                            "tier": tier
                        })
                elif line and ':' in line:
                    # Non-link source like "Author: Title"
                    sources.append({
                        "title": line,
                        "url": None,
                        "tier": tier
                    })

        # Method 4: Look for ## Further Reading section
        further_reading_match = re.search(
            r'^##\s+Further Reading\s*\n((?:.*\n)*?)(?=^##|\Z)',
            content,
            re.MULTILINE
        )
        if further_reading_match:
            section_text = further_reading_match.group(1)
            for link_match in self.LINK_PATTERN.finditer(section_text):
                title, url = link_match.groups()
                if url.startswith('http') and url not in seen_urls:
                    seen_urls.add(url)
                    sources.append({
                        "title": title,
                        "url": url,
                        "tier": None
                    })

        # Method 5: Extract header **Source**: description (no URL, common at file top)
        # Only use if no other sources found (fallback)
        if not sources:
            header_source_match = re.search(
                r'^\*\*Source\*\*:\s*(.+?)$',
                content,
                re.MULTILINE
            )
            if header_source_match:
                description = header_source_match.group(1).strip()
                # Check if it contains a link
                link_match = self.LINK_PATTERN.search(description)
                if link_match:
                    title, url = link_match.groups()
                    sources.append({
                        "title": title,
                        "url": url,
                        "tier": None
                    })
                else:
                    # Plain text source description
                    sources.append({
                        "title": description,
                        "url": None,
                        "tier": None
                    })

        return sources

    def parse_all(self) -> list[PatternMetadata]:
        """Parse all pattern files in the directory."""
        patterns = []
        for file_path in sorted(self.patterns_dir.glob('*.md')):
            patterns.append(self.parse_file(file_path))
        return patterns
