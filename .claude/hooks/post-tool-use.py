#!/usr/bin/env python3
"""
Post-Tool-Use Hook for Book-Base
Automatically tracks progress, updates word counts, and maintains BOOK_SUMMARY.md

This hook runs after every tool use and:
1. Detects chapter file modifications (Write/Edit to chapters/*.md)
2. Calculates word counts automatically
3. Updates BOOK_SUMMARY.md with progress
4. Timestamps modifications
5. Tracks chapter status transitions
"""

import json
import sys
import os
import re
from pathlib import Path
from datetime import datetime

def count_words(file_path):
    """Count words in a markdown file, excluding front matter and metadata."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove YAML front matter if present
        content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)

        # Remove markdown formatting but keep text
        content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)  # Code blocks
        content = re.sub(r'`[^`]+`', '', content)  # Inline code
        content = re.sub(r'!\[.*?\]\(.*?\)', '', content)  # Images
        content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)  # Links
        content = re.sub(r'[#*_~`]', '', content)  # Markdown symbols

        # Count words
        words = content.split()
        return len(words)
    except FileNotFoundError:
        return 0
    except Exception as e:
        print(f"Error counting words in {file_path}: {e}", file=sys.stderr)
        return 0

def extract_chapter_number(file_path):
    """Extract chapter number from filename like 'chapter-01.md'."""
    match = re.search(r'chapter-(\d+)\.md', file_path)
    return int(match.group(1)) if match else None

def get_chapter_status(file_path):
    """Determine chapter status based on word count and markers."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        word_count = count_words(file_path)

        # Check for status markers in content
        if '✅ Complete' in content or 'Status: Complete' in content:
            return '✅ Complete'
        elif '🔍 Revised' in content or 'Status: Revised' in content:
            return '🔍 Revised'
        elif word_count > 1000:  # Substantial content
            return '✍️ Drafted'
        elif word_count > 100:  # Some content
            return '📋 Outlined'
        elif '[brainstorm' in content.lower() or file_path.replace('chapters/', 'brainstorms/').replace('.md', '-brainstorm.md'):
            # Check if brainstorm exists
            brainstorm_path = file_path.replace('chapters/', 'brainstorms/').replace('.md', '-brainstorm.md')
            if os.path.exists(brainstorm_path):
                return '🧠 Brainstormed'

        return '⬜ Not Started'
    except:
        return '⬜ Not Started'

def update_book_summary(chapter_file):
    """Update BOOK_SUMMARY.md with latest chapter progress."""
    project_root = Path.cwd()
    summary_file = project_root / 'BOOK_SUMMARY.md'

    if not summary_file.exists():
        return  # Summary not created yet

    chapter_num = extract_chapter_number(chapter_file)
    if not chapter_num:
        return

    word_count = count_words(chapter_file)
    status = get_chapter_status(chapter_file)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')

    # Read current summary
    try:
        with open(summary_file, 'r', encoding='utf-8') as f:
            summary_content = f.read()
    except:
        return

    # Try to find and update the chapter row in the progress table
    # Format: | 01 | [Chapter Title] | Status | Words | Date |
    chapter_pattern = rf'\|\s*{chapter_num:02d}\s*\|([^|]+)\|[^|]*\|[^|]*\|[^|]*\|'

    def replace_row(match):
        title = match.group(1).strip()
        return f'| {chapter_num:02d} | {title} | {status} | {word_count:,} | {timestamp} |'

    updated_content = re.sub(chapter_pattern, replace_row, summary_content)

    # If content changed, write it back
    if updated_content != summary_content:
        try:
            with open(summary_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"📊 Updated BOOK_SUMMARY.md: Chapter {chapter_num} - {status} ({word_count:,} words)", file=sys.stderr)
        except Exception as e:
            print(f"Error updating BOOK_SUMMARY.md: {e}", file=sys.stderr)

def main():
    """Main hook execution."""
    # Read hook input from stdin
    try:
        hook_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)  # Silent failure if no JSON input

    # Extract tool name and inputs
    tool_name = hook_data.get('tool_name', '')
    tool_input = hook_data.get('tool_input', {})

    # Only process Write and Edit tools
    if tool_name not in ['Write', 'Edit']:
        sys.exit(0)

    # Get file path
    file_path = tool_input.get('file_path', '')

    # Only process chapter files
    if not file_path or 'chapters/chapter-' not in file_path:
        sys.exit(0)

    # Update progress tracking
    update_book_summary(file_path)

    sys.exit(0)

if __name__ == '__main__':
    main()
