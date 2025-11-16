---
description: Comprehensive book project health check and progress report
allowed-tools: Read, Glob, Grep
---

# Book Project Status Report

Generate a comprehensive overview of your book's progress and health.

## Your Task

1. **Read project configuration**:
   - @book.config.json - targets and settings
   - @BOOK_SUMMARY.md - current progress tracking
   - @TOC.md - planned structure

2. **Analyze chapter progress**:
   - Check all chapters/ files for completion status
   - Count words in each chapter
   - Identify chapters at different stages (brainstormed, outlined, drafted, complete)
   - Calculate overall progress percentage

3. **Quality assessment**:
   - Scan for [TODO], [RESEARCH], [REVISE] markers across all files
   - Check for chapters that are significantly over/under target length
   - Identify missing brainstorms or outlines
   - Note any broken cross-references between chapters

4. **Generate comprehensive report**:
   - **Progress Dashboard**: Chapter completion stats, word counts, percentage complete
   - **Quality Metrics**: Outstanding TODOs, research needs, revision notes
   - **Project Health**: Are chapters balanced? Any structural issues?
   - **Next Actions**: What should be prioritized next?
   - **Timeline Estimate**: Based on current pace, when might book be complete?

5. **Visual progress indicator**:
   Create a progress bar like: `[████████░░] 80% (8/10 chapters complete)`

Present the status as a clear, actionable dashboard that guides next steps.