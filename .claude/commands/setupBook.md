---
description: Initialize a forked book-base for your specific book project
allowed-tools: Read, Write, Edit
---

# Setup Your Book Project

Customize this forked book-base template for your specific book.

## Your Task

1. **Gather book details** from user:
   - Book title and subtitle
   - Author name  
   - Genre (non-fiction, memoir, technical, etc.)
   - Target word count and chapter count
   - Writing style preference (academic, narrative, conversational, etc.)

2. **Update configuration**:
   - Customize @book.config.json with book details
   - Set realistic word targets per chapter
   - Configure publishing preferences (GitHub Pages, etc.)

3. **Create initial files**:
   - **TOC.md**: Basic table of contents template for user to customize if it is not already there
   - **style-guide.md**: Personalized style guide based on genre and preferences
   - **BOOK_SUMMARY.md**: Progress tracking template

4. **Setup GitHub Pages infrastructure** (if publishing to GitHub):
   - Create **.github/workflows/jekyll.yml** for automated deployment
   - Create **Gemfile** with Jekyll dependencies
   - Create **_config.yml** with site configuration (baseurl, title, etc.)
   - Create **_layouts/default.html** to prevent unwanted navigation
   - Create **_includes/header.html** with clean header (title only)
   - Ensure these files prevent the common GitHub Pages navigation issues

5. **Verify structure**:
   - Ensure chapters/, brainstorms/, outlines/ directories exist
   - Check that .claude/commands/ has all workflow commands
   - Create .gitignore if repository will be used
   - Confirm GitHub Pages files are in place

6. **Guide next steps**:
   - Explain the workflow: TOC → /tocToChapters → /prepareChapter → /writeChapter → /completeChapter
   - Suggest starting with TOC.md customization if the file is blank
   - Point to key commands they'll use

Transform generic template into personalized book writing system.