"""Parser for SOURCES.md file."""

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class SourceEntry:
    """A source entry from SOURCES.md."""
    id: str
    name: str
    url: Optional[str] = None
    tier: Optional[str] = None
    source_type: Optional[str] = None
    section: Optional[str] = None
    key_insights: list[str] = field(default_factory=list)
    pattern_refs: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "tier": self.tier,
            "source_type": self.source_type,
            "section": self.section,
            "key_insights": self.key_insights,
            "pattern_refs": self.pattern_refs,
        }


class SourcesParser:
    """Parser for SOURCES.md file."""

    # Section headers: ## Primary Sources (Tier A)
    SECTION_PATTERN = re.compile(r'^##\s+(.+?)(?:\s+\(Tier ([A-D])\))?$', re.MULTILINE)

    # Subsection: ### Title
    SUBSECTION_PATTERN = re.compile(r'^###\s+(.+)$', re.MULTILINE)

    # Sub-subsection: #### Title
    SUBSUBSECTION_PATTERN = re.compile(r'^####\s+(.+)$', re.MULTILINE)

    # URL pattern
    URL_PATTERN = re.compile(r'\*\*(?:URL|Source)\*\*:\s*(https?://[^\s]+)')

    # Link pattern
    LINK_PATTERN = re.compile(r'\[([^\]]+)\]\((https?://[^)]+)\)')

    # Key insights pattern
    INSIGHTS_PATTERN = re.compile(r'\*\*Key Insights?\*\*:\s*\n((?:\s+[-*].+\n?)+)')

    # Pattern references pattern
    PATTERN_REF = re.compile(r'patterns/([a-z0-9-]+)\.md')

    # Evidence tier inline
    TIER_INLINE = re.compile(r'\*\*Evidence Tier\*\*:\s*([A-D])')

    def __init__(self, sources_file: Path):
        self.sources_file = sources_file

    def parse(self) -> list[SourceEntry]:
        """Parse the SOURCES.md file."""
        if not self.sources_file.exists():
            return []

        content = self.sources_file.read_text(encoding='utf-8')
        entries = []

        # Split by main sections
        sections = self._split_by_sections(content)

        for section_name, section_tier, section_content in sections:
            # Parse each section
            subsections = self._split_by_subsections(section_content)

            for subsection_name, subsection_content in subsections:
                # Check for sub-subsections (e.g., individual blog posts)
                subsubsections = self._split_by_subsubsections(subsection_content)

                if subsubsections:
                    for subsubsection_name, subsubsection_content in subsubsections:
                        entry = self._parse_entry(
                            name=subsubsection_name,
                            content=subsubsection_content,
                            section=section_name,
                            default_tier=section_tier
                        )
                        if entry:
                            entries.append(entry)
                else:
                    entry = self._parse_entry(
                        name=subsection_name,
                        content=subsection_content,
                        section=section_name,
                        default_tier=section_tier
                    )
                    if entry:
                        entries.append(entry)

        return entries

    def _split_by_sections(self, content: str) -> list[tuple[str, Optional[str], str]]:
        """Split content by ## headers."""
        sections = []
        matches = list(self.SECTION_PATTERN.finditer(content))

        for i, match in enumerate(matches):
            section_name = match.group(1).strip()
            section_tier = match.group(2)
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            section_content = content[start:end]
            sections.append((section_name, section_tier, section_content))

        return sections

    def _split_by_subsections(self, content: str) -> list[tuple[str, str]]:
        """Split content by ### headers."""
        subsections = []
        matches = list(self.SUBSECTION_PATTERN.finditer(content))

        for i, match in enumerate(matches):
            subsection_name = match.group(1).strip()
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            subsection_content = content[start:end]
            subsections.append((subsection_name, subsection_content))

        return subsections

    def _split_by_subsubsections(self, content: str) -> list[tuple[str, str]]:
        """Split content by #### headers."""
        subsubsections = []
        matches = list(self.SUBSUBSECTION_PATTERN.finditer(content))

        for i, match in enumerate(matches):
            subsubsection_name = match.group(1).strip()
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            subsubsection_content = content[start:end]
            subsubsections.append((subsubsection_name, subsubsection_content))

        return subsubsections

    def _parse_entry(
        self,
        name: str,
        content: str,
        section: str,
        default_tier: Optional[str]
    ) -> Optional[SourceEntry]:
        """Parse a single source entry."""
        # Generate ID from name
        entry_id = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

        # Extract URL
        url_match = self.URL_PATTERN.search(content)
        url = url_match.group(1) if url_match else None

        # Fallback: look for first link
        if not url:
            link_match = self.LINK_PATTERN.search(content)
            if link_match:
                url = link_match.group(2)

        # Extract tier (inline overrides section tier)
        tier_match = self.TIER_INLINE.search(content)
        tier = tier_match.group(1) if tier_match else default_tier

        # Determine source type from section
        source_type = self._infer_source_type(section)

        # Extract key insights
        insights_match = self.INSIGHTS_PATTERN.search(content)
        key_insights = []
        if insights_match:
            insights_text = insights_match.group(1)
            for line in insights_text.strip().split('\n'):
                line = line.strip()
                if line.startswith(('-', '*')):
                    key_insights.append(line.lstrip('-* ').strip())

        # Extract pattern references
        pattern_refs = list(set(self.PATTERN_REF.findall(content)))

        return SourceEntry(
            id=entry_id,
            name=name,
            url=url,
            tier=tier,
            source_type=source_type,
            section=section,
            key_insights=key_insights,
            pattern_refs=pattern_refs,
        )

    def _infer_source_type(self, section: str) -> str:
        """Infer source type from section name."""
        section_lower = section.lower()
        if 'primary' in section_lower:
            return 'primary'
        elif 'secondary' in section_lower or 'peer' in section_lower:
            return 'peer-reviewed'
        elif 'industry' in section_lower or 'community' in section_lower:
            return 'industry'
        elif 'opinion' in section_lower or 'speculation' in section_lower:
            return 'opinion'
        else:
            return 'unknown'
