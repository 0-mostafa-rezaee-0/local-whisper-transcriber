# Markdown Formatting Command

Fix formatting issues in Markdown files by removing trailing spaces, fixing multiple spaces, converting tabs to spaces, and removing excessive empty lines.

## Usage

Type `/markdown-formatting` in Cursor chat to fix the currently open Markdown file.

## What it does

- Removes trailing spaces from all lines
- Fixes multiple spaces (replaces with single space)
- Converts tabs to 4 spaces
- Removes excessive empty lines (keeps max 2 consecutive)

## Command

```bash
if [ -n "$CURSOR_FILE" ] && [[ "$CURSOR_FILE" == *.md ]]; then
    echo "🔧 Fixing formatting in: $CURSOR_FILE"
    sed -i 's/[[:space:]]*$//' "$CURSOR_FILE"
    sed -i 's/  \+/ /g' "$CURSOR_FILE"
    sed -i 's/\t/    /g' "$CURSOR_FILE"
    sed -i '/^$/N;/^\n$/d' "$CURSOR_FILE"
    echo "✅ Fixed formatting issues in: $CURSOR_FILE"
else
    echo "❌ No Markdown file is currently open"
fi
```
