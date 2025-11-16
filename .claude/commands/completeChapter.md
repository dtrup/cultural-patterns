---
description: Finalize chapter and update project progress
allowed-tools: Read, Write, Edit, Bash
---

# Complete Chapter $1: Finalize and Publish

Mark chapter as complete and update all project tracking.

## Your Task

1. **Final quality check**:
   - Read @chapters/chapter-$1.md to verify it's complete
   - Count words (use Bash wc -w, exclude YAML front matter)
   - Verify meets targets in @book.config.json (~4,750 words)
   - Check for any [TODO], [RESEARCH], or [REVISE] markers
   - Ensure smooth transitions into and out of chapter

2. **Update progress tracking** (CRITICAL - Do these in order):

   a. **Update chapter file** (Edit tool):
   - Ensure proper Jekyll front matter exists at the top:
     ```yaml
     ---
     layout: chapter
     title: "Chapter X: [Title]"
     status: complete
     completed_date: [YYYY-MM-DD]
     ---
     ```
   - If front matter is missing `layout: chapter`, add it
   - Add/update `status: complete` and `completed_date`
   - This ensures GitHub Pages renders the chapter properly

   b. **Run progress sync script** (Bash):
   ```bash
   python3 scripts/update_progress.py
   ```
   This automatically:
   - Scans all chapters and counts words
   - Updates BOOK_SUMMARY.md with all current statuses
   - Updates overall stats and completion percentage
   - Zero token cost (runs outside Claude context)

   c. **Extract and copy chapter summary** (Edit tool):
     - Read the "Chapter Summary (for continuity tracking)" section from the chapter file
     - Copy it to the appropriate section in @CHAPTER_SUMMARIES.md
     - Update status and word count in the CHAPTER_SUMMARIES entry
     - This provides narrative continuity for future chapters

3. **Report completion** to user:
   ```
   ✅ Chapter $1 Complete!

   📊 Stats:
   - Word Count: [actual count]
   - Target: ~4,750 words ([under/on/over] target)
   - Completed: [YYYY-MM-DD]

   📈 Book Progress:
   - Chapters Complete: X of 21
   - Total Words: [sum] / 100,000+
   - Overall Progress: XX%

   📌 Next Steps:
   - [Suggest next chapter to work on based on TOC]
   - Or run `/bookStatus` for full health check
   ```

## Quality Standards

- Chapter must have substantial content (3,000+ words minimum)
- No [TODO], [RESEARCH], or placeholder markers
- All citations and sources verified
- Narrative flows smoothly from prior chapter (check CHAPTER_SUMMARIES.md)

## Integration Notes

This command **explicitly updates BOOK_SUMMARY.md** instead of relying on the legacy post-tool-use hook. This is the modern SDK workflow approach—active commands rather than passive hooks.