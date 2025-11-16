---
description: Deep brainstorm and research planning for a specific chapter
allowed-tools: Task
---

# Prepare Chapter $1: Delegate to Expert Research Assistant

**Model**: Switch to haiku for efficient research
```
/model haiku
```

This command delegates research and brainstorming to the **research-assistant** subagent, a specialized expert in research methodology and planning.

## What Happens

The research-assistant subagent will:

1. **Load minimal context**:
   - This chapter's specs from @TOC.md (lines for chapter only)
   - Continuity from @BOOK_SUMMARY.md (not full prior chapters)
   - Voice from @style-guide.md
   - Targets from @book.config.json

2. **Conduct efficient research**:
   - Identify key concepts and 2-3 authoritative sources per claim
   - Find strong examples (quality over quantity)
   - Verify accuracy of examples and key statistics

3. **Create focused brainstorm** in `brainstorms/chapter-$1-brainstorm.md`:
   - Core thesis (1 sentence)
   - Opening hooks (2-3 options)
   - Research findings with essential sources
   - Best examples (3-5 with details)
   - Narrative arc
   - Cross-chapter connections
   - Citations

4. **Quality standards**:
   - 2+ authoritative sources for major claims
   - Examples verified (✅/⚠️/❓)
   - Foundation for ~4,750 word chapter

## Your Instructions

**Create a CONCISE delegation prompt** for the research-assistant subagent:

### Efficient Prompt Template:

```
Research Chapter $1: "[CHAPTER TITLE from TOC]"

**Context**: Read @CHAPTER_SUMMARIES.md for narrative continuity (what came before), @style-guide.md for voice, @book.config.json for targets. Check TOC.md only for this chapter's specs (lines X-Y).

**Mission**: Create focused brainstorm in `brainstorms/chapter-$1-brainstorm.md`:
- Core thesis (1 sentence)
- Opening hooks (2-3)
- Key research (2-3 authoritative sources per major claim, not exhaustive)
- Best examples (3-5 with essentials, ✅/⚠️/❓)
- Narrative arc
- Cross-chapter links
- Citations

**Research approach**: Efficient, not exhaustive. Find solid foundation, not every source. Focus on:
- Core concepts & definitions
- 2-3 classic citations per claim
- Strong concrete examples
- Practical measures

**Brainstorm constraints**: Keep brainstorm file under 6-8k tokens. Be focused and concise.

**Report back**: SUMMARY ONLY (location, source count, example count, confidence, gaps, ready status)
```

### Key Optimization:
- Keep prompt under 500 words
- Trust subagent expertise (avoid over-specifying)
- Request summary report only (not full content)
- Full brainstorm stays in file for chapter-writer to read

After delegation completes:
- Review summary
- User can read brainstorm file if needed
- Use `/writeChapter $1` when ready

**Reset Model**: Switch back to sonnet for writing phase
```
/model sonnet
```