## Project Overview
This is a book writing project that transforms a Table of Contents into a complete book with individual chapter files, progress tracking, and consistent writing style.

## Book Structure
```
/book-project
├── CLAUDE.md           # This file - project configuration
├── TOC.md             # Table of Contents input file
├── BOOK_SUMMARY.md    # Progress tracking and summaries
├── style-guide.md     # Writing style reference
├── /chapters/         # Individual chapter files
│   ├── chapter-01.md
│   ├── chapter-02.md
│   └── ...
├── /brainstorms/      # Pre-writing thoughts for each chapter
│   ├── chapter-01-brainstorm.md
│   ├── chapter-02-brainstorm.md
│   └── ...
└── /outlines/         # Detailed outlines per chapter
    ├── chapter-01-outline.md
    ├── chapter-02-outline.md
    └── ...
```

## Writing Style Guidelines

### Core Style Principles
- **Genre**: Non-fiction with narrative flair
- **Tone**: Engaging yet precise - think Malcolm Gladwell meets Mary Roach meets David Sedaris Richard Feynman 
- **Voice**: Authoritative but approachable, occasionally self-aware
- **Precision**: Every claim must be exact and verifiable
- **Elegance**: Aim for literary moments without sacrificing clarity

### Style Elements
- **Humor**: Dry wit, unexpected analogies, clever observations - never forced
- **Sharpness**: Incisive analysis, cutting through complexity to core insights
- **Pacing**: Vary sentence length. Short punches. Then flowing, contemplative passages that give readers space to think
- **Metaphors**: Use sparingly but memorably - prefer fresh over familiar
- **Technical Terms**: Define gracefully in context, never condescend

### Writing Rules
- Open chapters with a hook - anecdote, paradox, or provocative question
- Use concrete examples before abstract principles
- Show tension between competing ideas
- End sections with insights, not summaries
- Avoid clichés like the plague (yes, that was intentional)
- Never use "utilize" when "use" will do

## Workflow Commands

### Initialize Book Project
When starting with a new TOC:
1. Read TOC.md to understand book structure
2. Create chapter directories if they don't exist
3. Generate BOOK_SUMMARY.md with chapter status tracking
4. Create individual chapter files with proper headings

### Write Chapter Workflow
For each chapter in the TOC:
1. **Brainstorm Phase**
   - Create `/brainstorms/chapter-XX-brainstorm.md`
   - Include: key themes, potential examples, narrative arc, unique angles
   - Consider: What makes this chapter essential? What's the "aha" moment?
   - Time: 5-10 minutes of free association

2. **Outline Phase**
   - Create `/outlines/chapter-XX-outline.md`
   - Structure: Hook → Context → Core Concepts → Examples → Insights → Bridge
   - Include word count targets per section (typical: 3,000-5,000 words/chapter)

3. **Writing Phase**
   - Write to `/chapters/chapter-XX.md`
   - Follow style guide rigorously
   - Include section headers for navigation
   - Add footnote placeholders for citations [^1]

4. **Progress Update**
   - Update BOOK_SUMMARY.md with:
     - Chapter status (brainstormed/outlined/drafted/revised)
     - Word count
     - Key themes covered
     - Notes for revision
     - Connections to other chapters

## File Templates

### Chapter File Template
```markdown
# Chapter [Number]: [Title]

## Opening Hook
[Compelling anecdote or question - 200-300 words]

## Section 1: [Concept Introduction]
[Build from concrete to abstract - 800-1000 words]

## Section 2: [Deep Dive]
[Core analysis with examples - 1000-1200 words]

## Section 3: [Complications/Nuance]
[Address counterarguments or edge cases - 800-1000 words]

## Section 4: [Synthesis]
[Tie together insights - 600-800 words]

## Bridge to Next Chapter
[Transitional paragraph - 100-200 words]

---
### Chapter Notes
- Key sources:
- Revision priorities:
- Cross-references:
```

### BOOK_SUMMARY.md Template
```markdown
# Book Progress Summary

## Overview
- Total Chapters: [X]
- Completed: [X]
- In Progress: [X]
- Total Word Count: [X]

## Chapter Status

### Chapter 1: [Title]
- Status: [Brainstormed/Outlined/Drafted/Revised/Complete]
- Word Count: [X]
- Last Updated: [Date]
- Summary: [One paragraph capturing the essence]
- Key Concepts: [Bullet list]
- Revision Notes: [What needs attention]

[Repeat for each chapter]

## Thematic Threads
- Thread 1: Appears in chapters [X, Y, Z]
- Thread 2: Develops from chapter [A] to [B]

## Style Consistency Notes
- Recurring metaphors:
- Terminology decisions:
- Tone calibrations:
```

## Specific Instructions

### When Reading TOC.md
- Parse chapter numbers and titles precisely
- Identify any part/section divisions
- Note any special formatting requirements
- Preserve hierarchy if present

### When Creating Files
- Always create parent directories first
- Use consistent naming: `chapter-01.md` not `ch1.md`
- Include YAML front matter for metadata if needed
- Ensure proper Markdown formatting

### When Writing Content
- Check previous chapters for established terminology
- Maintain consistent character/example references
- Build on concepts progressively
- Flag areas needing fact-checking with [VERIFY]
- Mark placeholders with [TODO: specific need]

### When Updating Progress
- Update BOOK_SUMMARY.md after EVERY writing session
- Include timestamp of last edit
- Note any blocking issues or research needs
- Track narrative momentum and pacing

## Advanced Features

### Cross-Chapter Continuity
- Maintain a "story bible" of examples, characters, and concepts
- Track callbacks and forward references
- Ensure terminology consistency

### Research Integration
```markdown
[RESEARCH: topic] - Placeholder for needed research
[CITE: source] - Placeholder for citation
[FACT-CHECK] - Mark claims needing verification
```

### Revision Markers
```markdown
[REVISE: too technical] - Style issue
[EXPAND: needs example] - Content gap
[CUT: redundant] - Suggested deletion
[BRIDGE: weak transition] - Flow issue
```
