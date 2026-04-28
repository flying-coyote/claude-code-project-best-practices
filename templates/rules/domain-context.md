<!-- .claude/rules/domain-context.md
     Domain-specific knowledge that helps Claude make informed decisions.
     This is the most project-specific template — replace everything below. -->

# Domain Context

## Terminology
<!-- Define terms Claude might misinterpret or not know.
     Only include terms that affect code correctness. -->

| Term | Meaning | Code Usage |
|------|---------|------------|
| {{term}} | {{definition}} | {{where it appears in code}} |

## Data Model
<!-- Describe the key entities and relationships.
     Focus on what's non-obvious from the code alone. -->

{{Brief description of the data model and key relationships.}}

## External System Conventions
<!-- Field names, API conventions, or protocol details that come from
     external systems and must be used exactly as specified. -->

- {{Convention: e.g., "Zeek field id.orig_h means source IP, id.resp_p means dest port"}}
- {{Convention: e.g., "SIEM index names use underscores, not hyphens"}}
