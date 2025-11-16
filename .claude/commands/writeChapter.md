---
description: Write complete chapter content from brainstorm plan
allowed-tools: Task
---

# Write Chapter $1: Delegate to Expert Chapter Writer

This command delegates chapter writing to the **chapter-writer** subagent, a specialized creative writing expert.

## What Happens

The chapter-writer subagent will:

1. **Load minimal necessary context**:
   - Brainstorm plan from @brainstorms/chapter-$1-brainstorm.md
   - Narrative continuity from @CHAPTER_SUMMARIES.md (prior chapters' summaries)
   - Style guide from @style-guide.md
   - Word count targets from @book.config.json
   - Existing chapter from @chapters/chapter-$1.md

2. **Write with expertise**:
   - Transform brainstorm into polished content
   - Use compelling narrative hooks
   - Deploy researched examples strategically
   - Maintain consistent voice and style
   - Hit word count targets
   - Create smooth transitions

3. **Ensure quality**:
   - Every paragraph advances the argument
   - Examples illuminate, not just decorate
   - Voice matches established style
   - Claims are properly supported
   - Structure works for navigation

4. **Add Chapter Summary section at end** (REQUIRED):
   After the main chapter content, add:
   ```markdown
   ---

   ## Chapter Summary (for continuity tracking)

   **Core Argument**: [2-3 sentence summary of chapter's main thesis]

   **Key Concepts Introduced**:
   - [Concept 1 with brief description]
   - [Concept 2 with brief description]
   - [etc.]

   **Major Examples Used**:
   - [Example 1: brief description]
   - [Example 2: brief description]
   - [etc.]

   **Transition to Next Chapter**: [1-2 sentences on how this sets up the next chapter]
   ```

   This summary will be copied to CHAPTER_SUMMARIES.md and used by subagents for continuity.

5. **Auto-update progress** (via update script):
   - Word count tracked automatically
   - Chapter status updated to "✍️ Drafted"
   - BOOK_SUMMARY.md synced with current state

## Your Command

**Delegate to the chapter-writer subagent to write chapter $1.**

The chapter-writer has been trained on your book's specific voice, style guide, and quality standards. It will handle the writing process autonomously while maintaining consistency with your previous chapters.

**CRITICAL: Jekyll Front Matter Requirement**

The chapter-writer MUST ensure the chapter file starts with proper Jekyll YAML front matter:
```yaml
---
layout: chapter
title: "Chapter X: [Title]"
---
```

This is required for GitHub Pages to render the chapter as HTML instead of raw markdown. The front matter must be:
- At the very beginning of the file (line 1)
- Include `layout: chapter` (required for template)
- Include `title` with chapter number and title

After writing, consider running `/styleCheck $1` to have the style-editor subagent review for voice consistency.