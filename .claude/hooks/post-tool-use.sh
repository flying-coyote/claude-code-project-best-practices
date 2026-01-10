#!/bin/bash
# .claude/hooks/post-tool-use.sh
# Auto-regenerate INDEX.md when file structure changes
# Auto-format code files after Write/Edit (Boris Cherny pattern)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$PROJECT_ROOT" || exit 0

# Read hook input (JSON from stdin)
read -r input 2>/dev/null || input=""

# Extract tool name if available
TOOL=$(echo "$input" | jq -r '.tool // "unknown"' 2>/dev/null || echo "unknown")

# --- Code Formatting (Boris Cherny Pattern) ---
if [ "$TOOL" = "Write" ] || [ "$TOOL" = "Edit" ]; then
    FILE_PATH=$(echo "$input" | jq -r '.parameters.file_path // .parameters.filePath // ""' 2>/dev/null || echo "")

    if [ -n "$FILE_PATH" ] && [ -f "$FILE_PATH" ]; then
        EXT="${FILE_PATH##*.}"

        case "$EXT" in
            js|jsx|ts|tsx|json)
                if command -v prettier &> /dev/null; then
                    prettier --write "$FILE_PATH" 2>/dev/null && \
                        echo "✨ Formatted: $(basename "$FILE_PATH")"
                fi
                ;;
            py)
                if command -v black &> /dev/null; then
                    black --quiet "$FILE_PATH" 2>/dev/null && \
                        echo "✨ Formatted: $(basename "$FILE_PATH")"
                fi
                ;;
            go)
                if command -v gofmt &> /dev/null; then
                    gofmt -w "$FILE_PATH" 2>/dev/null && \
                        echo "✨ Formatted: $(basename "$FILE_PATH")"
                fi
                ;;
            rs)
                if command -v rustfmt &> /dev/null; then
                    rustfmt "$FILE_PATH" 2>/dev/null && \
                        echo "✨ Formatted: $(basename "$FILE_PATH")"
                fi
                ;;
        esac
    fi
fi

# --- INDEX.md Regeneration ---

# Check if this might be a file structure change
STRUCTURE_CHANGED=false

case "$TOOL" in
    "Write"|"NotebookEdit")
        STRUCTURE_CHANGED=true
        ;;
    "Bash")
        COMMAND=$(echo "$input" | jq -r '.parameters.command // ""' 2>/dev/null || echo "")
        if [[ "$COMMAND" =~ ^(mkdir|mv|cp|rm|touch) ]]; then
            STRUCTURE_CHANGED=true
        fi
        ;;
    *)
        # Unknown tool, check anyway if we have a .md file change
        STRUCTURE_CHANGED=true
        ;;
esac

# Regenerate INDEX.md if structure might have changed
if [ "$STRUCTURE_CHANGED" = true ] && [ -f "automation/generate_index.py" ]; then
    # Capture current INDEX.md hash
    OLD_HASH=$(md5sum INDEX.md 2>/dev/null | cut -d' ' -f1 || echo "none")

    # Regenerate silently
    python3 automation/generate_index.py > /dev/null 2>&1

    # Check if it changed
    NEW_HASH=$(md5sum INDEX.md 2>/dev/null | cut -d' ' -f1 || echo "none")

    if [ "$OLD_HASH" != "$NEW_HASH" ]; then
        echo "INDEX.md automatically regenerated"
    fi
fi

exit 0  # Non-blocking
