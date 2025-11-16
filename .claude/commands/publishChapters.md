---
description: Commit and push completed chapters to GitHub for publication
allowed-tools: Bash, Read, Glob
---

# Publish Chapters to GitHub

Commit and push your completed chapters and related files to GitHub for online publication.

## Your Task

1. **Check repository status**:
   - Run `git status` to see current changes
   - Identify which chapters have been modified or are new
   - Check for any untracked files that should be included

2. **Stage relevant files**:
   - Add all completed chapter files (chapters/*.md)
   - Add any new brainstorm files (brainstorms/*.md)
   - Add updated project tracking files (BOOK_SUMMARY.md, CHAPTER_SUMMARIES.md)
   - Add any configuration or style guide updates
   - DO NOT add temporary files, logs, or local settings

3. **Create meaningful commit**:
   - Review the staged changes with `git diff --cached`
   - Create a descriptive commit message that summarizes:
     - Which chapters were completed or updated
     - Key improvements or additions
     - Any structural changes to the book
   - Follow format: "Complete Chapter N: Title - brief description of contents and word count"

4. **Push to GitHub**:
   - Push the commit to the main branch
   - Verify the push was successful
   - Provide the GitHub Pages URL if applicable

5. **Publication status**:
   - Confirm which chapters are now live on GitHub
   - Note any next steps for publication workflow
   - Update user on overall book progress

## Example Workflow

```bash
# Check what's changed
git status

# Add relevant files
git add chapters/chapter-04.md
git add brainstorms/chapter-04-brainstorm.md  
git add BOOK_SUMMARY.md
git add CHAPTER_SUMMARIES.md

# Review staged changes
git diff --cached

# Commit with descriptive message
git commit -m "Complete Chapter 4: Method & Quality Bar - 5,847 words establishing rigorous methodology framework with five-test validation system and evidence hierarchy"

# Push to GitHub
git push origin main
```

## Important Notes

- Only commit files that are ready for public viewing
- Ensure chapter quality meets publication standards
- Include word counts in commit messages for progress tracking
- Don't commit local settings or temporary files
- Verify GitHub Pages deployment if enabled

Present a clear summary of what was published and provide any relevant URLs for viewing the content online.