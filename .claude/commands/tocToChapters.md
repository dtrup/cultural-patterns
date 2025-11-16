---
description: Convert TOC to individual chapter files and initialize project
allowed-tools: Read, Write, MultiEdit, Glob
---

# Initialize Book Project from TOC

Read TOC.md and create the complete project structure with individual chapter files.

## Your Task

1. **Read project files**:
   - @TOC.md - book structure and chapters
   - @book.config.json - project configuration 
   - @style-guide.md - writing guidelines (if exists)

2. **Create chapter files** in chapters/ directory:
   - File naming: `chapter-01.md`, `chapter-02.md`, etc.
   - Include chapter title as H1 heading
   - Add structured placeholder content
   - Include word count target from config

3. **Initialize BOOK_SUMMARY.md** with:
   - **Book's core ambition**: What is this book's central thesis/purpose?
   - **Reader transformation**: How will readers change after reading this?
   - **Unique value**: What makes this book different/essential?
   - Complete chapter listing with "Not Started" status
   - Progress tracking setup
   - Word count targets
   - Thematic thread placeholders

4. **Verify structure**:
   - Ensure brainstorms/ and outlines/ directories exist
   - Check all chapters are accounted for
   - Report total chapter count and targets

## Chapter Template Structure

**CRITICAL**: Every chapter file MUST start with Jekyll YAML front matter for GitHub Pages:

```markdown
---
layout: chapter
title: "Chapter X: [Title from TOC]"
---

# Chapter X: [Title from TOC]

> **Target**: [N] words | **Status**: Not Started | **Last Updated**: [Date]

## Planning Notes
*Use /prepareChapter X to brainstorm this chapter*

## Content
*Use /writeChapter X to write this chapter*

---
**Progress**: ⬜ Brainstorm → ⬜ Outline → ⬜ Draft → ⬜ Review → ⬜ Complete

<script src="https://hypothes.is/embed.js" async></script>
```

**Front matter requirements**:
- Must be at line 1 (very beginning)
- Must include `layout: chapter` (for template)
- Must include `title` with chapter number and name
- Without this, GitHub Pages will serve raw markdown instead of HTML

Also create **index.md** for GitHub Pages with:
- **CRITICAL**: Start with YAML front matter: `---\nlayout: default\ntitle: Home\n---`
- Book title and author
- Table of contents with links to completed chapters
- Progress indicator showing completion status
- Hypothesis commenting enabled

**IMPORTANT**: Without YAML front matter, Jekyll will NOT process the file to HTML and GitHub Pages will fail with 404 errors.

Focus on clean structure that sets up the entire workflow.