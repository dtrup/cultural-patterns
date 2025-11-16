# Book-Base 2.0: AI Writing System

Professional book writing template with **4 specialized subagent experts** and automated progress tracking.

## 🤖 Subagents

1. **chapter-writer** - Creative writing, voice consistency
2. **style-editor** - Editorial review, quality control
3. **research-assistant** - Research, source evaluation, citations
4. **thematic-analyst** - Cross-chapter coherence

**Progress Tracking**: Modern SDK workflow uses explicit commands (`/completeChapter`, `/updateProgress`) instead of legacy hooks.

---

## 📋 Workflow Commands

### Phase 1: Setup
- `/setupBook` - Customize for your book
- `/tocToChapters` - Generate chapter files from TOC.md

### Phase 2: Per Chapter (Repeat)
- `/prepareChapter N` → research-assistant (3-stage research, creates brainstorm) - auto-switches to Haiku
- `/writeChapter N` → chapter-writer (polished content from brainstorm)
- `/styleCheck N` → style-editor (multi-pass review, prioritized feedback)
- `/completeChapter N` - Mark complete, update BOOK_SUMMARY.md

### Phase 3: Book-Level
- `/updateProgress` - Sync BOOK_SUMMARY.md with all chapter states
- `/bookStatus` - Progress dashboard
- `/thematicAnalysis` → thematic-analyst (map themes across book)
- `/findGaps` - Identify weak areas
- `/revisionSweep` - Systematic improvements
- `/finalReview` - Publication readiness
- `/publishChapters` - Git commit & push

---

## 🎯 Subagent Delegation

**Auto-delegate** when user runs these commands:
- `/prepareChapter N` → research-assistant
- `/writeChapter N` → chapter-writer
- `/styleCheck N` → style-editor
- `/thematicAnalysis` → thematic-analyst

**Manual invoke** when user requests explicitly:
- "Use research-assistant to fact-check chapter 3"
- "Use chapter-writer to expand section 2"
- "Use style-editor to compare chapters 1-3"

**Command prompts tell you when to delegate.** Follow them.

---

## 📁 Key Files (Reference, Don't Duplicate)

### Configuration
- `@book.config.json` - Title, author, targets, style preferences
- `@style-guide.md` - Voice, tone, forbidden patterns, quality standards

### Content
- `@TOC.md` - Chapter structure
- `@chapters/chapter-NN.md` - Chapter content
- `@brainstorms/chapter-NN-brainstorm.md` - Research & planning
- `@outlines/chapter-NN-outline.md` - Detailed outlines (optional)

### Tracking
- `@BOOK_SUMMARY.md` - Progress dashboard (updated by `/updateProgress` and `/completeChapter`)
- `@CHAPTER_SUMMARIES.md` - Narrative continuity (extracted from chapter summary sections)

**Subagents read these files directly.** Reference by name (`@style-guide.md`) instead of copying content into prompts.

---

## ⚡ Progress Tracking (Modern SDK Workflow)

**Explicit commands** update BOOK_SUMMARY.md:
- `/completeChapter N` - Updates specific chapter to ✅ Complete with word counts
- `/updateProgress` - Scans all chapters and syncs BOOK_SUMMARY.md with current state

**Status progression**:
⬜ Not Started (<100 words) → 🧠 Brainstormed (brainstorm exists) → 📋 Outlined (100-999 words) → ✍️ Drafted (1,000-2,999 words) → 🔍 Revised (3,000+ words) → ✅ Complete (YAML: status: complete)

**Legacy**: `.claude/hooks/post-tool-use.py` exists but is not used in modern workflow. Explicit commands are preferred for clarity and reliability.

---

## 🎨 Quality Standards

**Workflow**: brainstorm → write → review → finalize

**Subagent roles**:
- research-assistant: Authoritative sources, proper citations
- chapter-writer: Voice consistency, example deployment, target word counts
- style-editor: Inconsistency detection, specific fixes
- thematic-analyst: Book-level coherence

**Prioritize**: Quality over speed, consistency over volume, publication-ready over draft.

---

## 📄 Jekyll/GitHub Pages Requirements

**CRITICAL**: All chapter files MUST have proper YAML front matter for GitHub Pages to render them as HTML.

**Required front matter** (at very beginning of file):
```yaml
---
layout: chapter
title: "Chapter X: [Title]"
---
```

**Why this matters**: Without front matter, Jekyll serves raw markdown instead of rendered HTML. The `layout: chapter` field is required for the template system.

**When to add**:
- `/tocToChapters` should create files with front matter
- `/writeChapter` must ensure front matter exists
- `/completeChapter` must verify front matter

---

## ✅ DO / ❌ DON'T

### DO:
- Delegate when commands instruct
- Trust subagent expertise
- Use `/completeChapter` or `/updateProgress` to sync BOOK_SUMMARY.md
- Reference `@style-guide.md` for voice
- Maintain quality standards
- **ALWAYS add Jekyll front matter** to chapter files (layout + title)

### DON'T:
- Manually edit BOOK_SUMMARY.md (use commands instead)
- Skip brainstorm phase (research foundation critical)
- Ignore subagent feedback (especially style-editor)
- Rush quality checks (consistency > speed)
- Copy file contents into prompts (reference by @filename)
- **Skip Jekyll front matter** (breaks GitHub Pages rendering)

---

## 🚀 Subagent Benefits

**Separate contexts**: Each has own context window, no pollution
**Autonomous**: Load own context, make decisions, report back
**Specialized**: Deep domain training (narrative, editorial, research, literary analysis)

---

## 🎯 Your Role

Coordinate subagent specialists, make high-level decisions, ensure user's vision is realized through quality, consistent, publication-ready content.

**You conduct. Subagents perform. Commands track. User writes.**

---

*Powered by Claude Code SDK with specialized subagents and intelligent automation.*
