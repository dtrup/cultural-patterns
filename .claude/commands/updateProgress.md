---
description: Sync BOOK_SUMMARY.md with actual chapter file states
allowed-tools: Bash
---

# Update Progress: Sync BOOK_SUMMARY.md

Scan all chapter files and update BOOK_SUMMARY.md with current word counts and statuses.

**Token-efficient**: Runs standalone Python script outside Claude's context.

## Your Task

1. **Run the standalone script**:
   ```bash
   python3 scripts/update_progress.py
   ```

2. **Report the output** to the user (the script prints its own summary)

That's it! The script:
- Scans all 21 chapters
- Counts words (excludes YAML/code/markdown)
- Determines status for each chapter
- Updates BOOK_SUMMARY.md directly
- Prints progress summary

## When to Use

- After writing multiple chapters without using /completeChapter
- To sync BOOK_SUMMARY.md when it's out of date
- When you want a quick health check of all chapters
- After manual edits to chapter files outside the workflow

## Token Efficiency

This command uses **ZERO context tokens** for chapter content because the Python script runs independently. Only the brief output is returned to Claude.

Compare to naive approach:
- ❌ Bad: Read 21 chapters into context (50k+ tokens)
- ✅ Good: Run script, see 10-line summary (~100 tokens)

## Notes

This is a utility command for the modern SDK workflow. It replaces relying on the legacy post-tool-use hook for progress tracking.
