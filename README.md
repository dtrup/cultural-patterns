# 📚 Book-Base: AI-Powered Book Writing System

**The ultimate fork-and-write template for creating professional books with specialized AI assistants.**

Transform your book idea into a complete manuscript using Claude Code's **subagent system** - specialized AI experts that handle research, writing, editing, and thematic analysis. No technical skills required - just fork, customize, and write.

---

## 🤖 What Makes This Different

**Traditional writing tools** give you blank pages and generic AI assistance.

**Book-Base 2.0** gives you **a team of AI specialists**:
- 📚 **chapter-writer** - Expert creative writer trained in your book's voice
- ✍️ **style-editor** - Senior editor ensuring consistency across chapters
- 🔍 **research-assistant** - Research specialist finding authoritative sources
- 🎨 **thematic-analyst** - Cross-chapter coherence expert
- ⚡ **Automated tracking** - Progress updates happen automatically via hooks

**Result**: You focus on ideas. Specialized AI experts handle research, writing, editing, and consistency.

---

## 🚀 Quick Start (5 Minutes)

### 1. Fork & Clone This Repository

```bash
# On GitHub, click "Fork" in the top-right corner
# Then clone your fork:
git clone https://github.com/YOUR-USERNAME/book-base.git
cd book-base
```

### 2. Open in Claude Code

```bash
# If you have Claude Code CLI installed:
claude-code .

# Or open the folder in your Claude Code application
```

### 3. Initialize Your Book

```bash
/setupBook           # Customize book details (title, author, genre, style)
```

Edit `TOC.md` with your chapter structure:
```markdown
# Your Book Title

## Part 1: Foundation
1. Chapter One Title
2. Chapter Two Title
...
```

```bash
/tocToChapters       # Generate chapter files from your TOC
/bookStatus          # Verify everything looks good
```

### 4. Write Your First Chapter

```bash
/prepareChapter 1    # research-assistant does deep research & brainstorming
/writeChapter 1      # chapter-writer transforms brainstorm into polished content
/styleCheck 1        # style-editor reviews for quality & consistency
```

**That's it!** Your first chapter is drafted, and progress is tracked automatically.

---

## 🎯 How It Works: Your AI Writing Team

### The Specialized Subagents

#### 📚 **chapter-writer** - Expert Creative Writer
**What it does:**
- Transforms research into polished, engaging prose
- Writes with your book's specific voice and style
- Crafts compelling hooks, examples, and transitions
- Maintains consistency across all chapters

**Internalized expertise:**
- Your style guide and voice preferences
- Narrative techniques and pacing rules
- Quality standards from `book.config.json`

**Automatically invoked by:** `/writeChapter N`

---

#### ✍️ **style-editor** - Voice Consistency Expert
**What it does:**
- Multi-pass analysis: voice, structure, line-level quality
- Compares against other chapters for consistency
- Detects subtle inconsistencies humans miss
- Provides prioritized, actionable feedback

**Deliverable:**
- Executive summary (Ready/Minor Revision/Major Work needed)
- Specific issues marked with [STYLE], [REVISE], [CLARIFY]
- Prioritized recommendations (Critical → High → Medium → Low)

**Automatically invoked by:** `/styleCheck N`

---

#### 🔍 **research-assistant** - Research & Fact-Checking Specialist
**What it does:**
- 3-stage research process (Landscape → Investigation → Verification)
- Finds authoritative sources (peer-reviewed, expert, primary)
- Discovers compelling examples with full documentation
- Creates comprehensive brainstorm with citations

**Quality assurance:**
- All claims have 2+ authoritative sources
- Statistics traced to original sources
- Confidence levels marked (✅ Verified / ⚠️ Needs verification)

**Automatically invoked by:** `/prepareChapter N`

---

#### 🎨 **thematic-analyst** - Cross-Chapter Coherence Expert
**What it does:**
- Maps thematic threads across entire book
- Tracks concept consistency and terminology
- Identifies missing connections and callbacks
- Analyzes narrative arc and pacing

**Deliverable:**
- Thematic thread mapping (3-7 major themes)
- Concept consistency report
- Cross-chapter connection map
- Prioritized action items

**Automatically invoked by:** `/thematicAnalysis`

---

### ⚡ Automated Progress Tracking

**The `post-tool-use` hook** runs automatically after every file edit:
- ✅ Counts words in chapters (excluding metadata)
- ✅ Updates chapter status (⬜ → 🧠 → 📋 → ✍️ → 🔍 → ✅)
- ✅ Updates `BOOK_SUMMARY.md` with timestamps
- ✅ No manual tracking needed!

**You just write. The system tracks everything.**

---

## ⚡ The Complete Workflow

### Phase 1: Project Setup

```bash
/setupBook              # Customize book details and preferences
```

Edit `TOC.md` to define your chapter structure

```bash
/tocToChapters          # Generate all chapter files automatically
/bookStatus             # Verify project structure
```

---

### Phase 2: Chapter Creation (Repeat for Each Chapter)

```bash
# Step 1: Research & Brainstorm
/prepareChapter 1
```
→ **research-assistant** subagent:
- Conducts 3-stage research process
- Finds authoritative sources and compelling examples
- Creates comprehensive brainstorm in `brainstorms/chapter-01-brainstorm.md`
- Includes: core thesis, hook options, research findings, examples, citations

```bash
# Step 2: Write the Chapter
/writeChapter 1
```
→ **chapter-writer** subagent:
- Loads brainstorm, style guide, previous chapters
- Writes polished content with your established voice
- Deploys researched examples strategically
- Hits word count targets from `book.config.json`

→ **post-tool-use hook**:
- Automatically counts words
- Updates status to "✍️ Drafted"
- Updates `BOOK_SUMMARY.md` with timestamp

```bash
# Step 3: Style Review
/styleCheck 1
```
→ **style-editor** subagent:
- Multi-pass analysis (voice, structure, line-level)
- Compares against other chapters
- Provides prioritized feedback with specific fixes
- Marks issues: [STYLE], [REVISE], [CLARIFY], [CUT]

Review feedback and make edits as needed.

```bash
# Step 4: Finalize Chapter
/completeChapter 1
```
→ Marks chapter as complete and updates tracking

**Repeat for all chapters!**

---

### Phase 3: Book-Level Refinement

```bash
/thematicAnalysis       # Cross-chapter coherence check
```
→ **thematic-analyst** subagent:
- Maps all thematic threads across book
- Checks concept consistency
- Identifies missing connections
- Provides prioritized action items

```bash
/findGaps              # Identify weak areas or missing content
/revisionSweep         # Systematic improvement pass
/finalReview           # Publication readiness check
```

---

## 📋 Complete Command Reference

### Core Writing Commands

| Command | Subagent Used | What It Does |
|---------|---------------|--------------|
| `/prepareChapter N` | research-assistant | Deep research & comprehensive brainstorming |
| `/writeChapter N` | chapter-writer | Transform brainstorm into polished chapter |
| `/styleCheck N` | style-editor | Professional editorial review |
| `/completeChapter N` | (none) | Finalize and mark chapter complete |

### Project Management Commands

| Command | Subagent Used | What It Does |
|---------|---------------|--------------|
| `/bookStatus` | (none) | Progress dashboard and health check |
| `/thematicAnalysis` | thematic-analyst | Cross-chapter consistency analysis |
| `/findGaps` | (none) | Identify weak areas or missing content |
| `/revisionSweep` | (none) | Systematic improvement pass |
| `/finalReview` | (none) | Publication readiness assessment |

### Setup Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/setupBook` | Initialize project | After forking |
| `/tocToChapters` | Generate chapter files | After finalizing TOC |

---

## 🗂️ File Structure

```
your-book/
├── .claude/
│   ├── agents/                        # ← AI Specialist Subagents
│   │   ├── chapter-writer.md          # Creative writing expert
│   │   ├── style-editor.md            # Voice consistency expert
│   │   ├── research-assistant.md      # Research & fact-checking
│   │   └── thematic-analyst.md        # Cross-chapter coherence
│   │
│   ├── hooks/                         # ← Automation Hooks
│   │   └── post-tool-use.py           # Auto progress tracking
│   │
│   └── commands/                      # ← Workflow Commands
│       ├── prepareChapter.md          # → research-assistant
│       ├── writeChapter.md            # → chapter-writer
│       ├── styleCheck.md              # → style-editor
│       ├── thematicAnalysis.md        # → thematic-analyst
│       └── [other commands...]
│
├── chapters/                          # Final chapter content
├── brainstorms/                       # Research & planning
├── outlines/                          # Chapter structure planning
│
├── book.config.json                   # Project settings
├── TOC.md                             # Table of contents
├── style-guide.md                     # Voice & style standards
├── BOOK_SUMMARY.md                    # Progress dashboard (auto-updated!)
│
├── SDK_FEATURES.md                    # Detailed SDK documentation
└── README.md                          # This file
```

---

## 🎨 Customization

### Configure Your Book

Edit `book.config.json`:
```json
{
  "title": "Your Book Title",
  "author": "Your Name",
  "genre": "non-fiction",
  "target_words": 80000,
  "chapter_target": 4000,
  "style": "engaging-authoritative"
}
```

### Define Your Voice & Style

Edit `style-guide.md` to customize:
- **Voice**: Authoritative, conversational, academic, witty
- **Tone**: Serious, warm, analytical, playful
- **Technical level**: Beginner-friendly, intermediate, expert
- **Example style**: Stories, case studies, data, analogies

**The subagents internalize your style guide** and write accordingly!

---

## 💡 Pro Tips

### For Best Results

✅ **Trust the specialists** - Let subagents work autonomously
- The research-assistant knows how to find authoritative sources
- The chapter-writer knows your voice after reading the style guide
- The style-editor has decades of editorial experience (in training)

✅ **Review subagent output** - You're still the author
- Review brainstorms before writing
- Review drafts before finalizing
- Make decisions on style-editor suggestions

✅ **Use the workflow** - It's optimized for quality
- Research → Write → Review → Finalize
- Don't skip the brainstorm phase
- Run `/styleCheck` proactively

✅ **Check consistency regularly**
- Run `/thematicAnalysis` every 3-4 chapters
- Use `/bookStatus` to see overall progress
- Track issues as they emerge, not at the end

### Advanced Usage

**Explicit subagent invocation:**
```
"Use the research-assistant to fact-check the claims in chapter 3"
"Use the chapter-writer to expand section 2 of chapter 5"
"Use the style-editor to compare voice in chapters 1-3"
```

**Collaborate with subagents:**
```
"I need help with chapter 4. Use the research-assistant to find
examples about [topic], then we'll discuss the best approach
together before writing."
```

---

## 🆘 Troubleshooting

### Commands Not Working?
1. Verify you're in the project root directory
2. Check required files exist: `TOC.md`, `book.config.json`
3. Run `/bookStatus` to see project health

### Subagents Not Being Invoked?
1. Commands should automatically delegate to subagents
2. If not, try explicit: "Use the chapter-writer subagent to write chapter 5"
3. Check `.claude/agents/` directory exists with subagent files

### Progress Not Auto-Updating?
1. Verify `.claude/hooks/post-tool-use.py` exists and is executable
2. Hook only tracks chapters in `chapters/chapter-*.md` format
3. Check `BOOK_SUMMARY.md` has a table with chapter rows

### Writer's Block?
- Try `/findGaps` to identify what's missing
- Run `/thematicAnalysis` to see the big picture
- Use research-assistant for more research: "Use the research-assistant to find more examples about [topic]"

### Quality Concerns?
- Run `/styleCheck N` on problem chapters
- Use style-editor for targeted review: "Use the style-editor to review the opening of chapter 3"
- Compare against other chapters: "Use the style-editor to compare chapters 1 and 5"

---

## 🌟 Why This Works

### The Power of Specialized AI

**Generic AI assistance:**
- One model tries to do everything
- No accumulated expertise
- Inconsistent results
- You manage the process

**Book-Base subagent system:**
- ✅ Specialized experts with deep training
- ✅ Separate context windows for focused work
- ✅ Consistent, high-quality output
- ✅ Autonomous workflows with automatic delegation
- ✅ Automated progress tracking

### The Result

**You focus on:**
- Big ideas and insights
- Strategic decisions
- Creative direction
- Final editorial choices

**The AI team handles:**
- Research and fact-checking
- Writing with your voice
- Style consistency
- Cross-chapter coherence
- Progress tracking

---

## 🌐 Publishing to GitHub Pages

**Your book automatically becomes a website!**

### Setup (2 steps)
1. **Enable GitHub Pages**: Settings → Pages → "Deploy from a branch" → main
2. **Your book is live**: `https://YOUR-USERNAME.github.io/your-book-title/`

### Features
✅ **Zero configuration** - just markdown files
✅ **Clean styling** - GitHub's default theme
✅ **Mobile-friendly** - responsive automatically
✅ **Instant updates** when you push

See `PUBLISHING.md` for complete instructions.

---

## 📚 Learn More

### Documentation
- **`SDK_FEATURES.md`** - Deep dive into the subagent system
- **`CLAUDE.md`** - Instructions for Claude about the system
- **`PUBLISHING.md`** - GitHub Pages publishing guide
- **`CONTRIBUTING.md`** - How to contribute improvements

### Official Resources
- [Claude Code Subagents Docs](https://docs.claude.com/en/docs/claude-code/sub-agents)
- [Claude Code Hooks Guide](https://docs.claude.com/en/docs/claude-code/hooks-guide)
- [Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview)

---

## 🎉 You're Ready!

**Book-Base gives you a professional AI writing environment with:**
- ✅ 4 specialized AI experts (research, writing, editing, analysis)
- ✅ Automated progress tracking (no manual updates)
- ✅ Intelligent task delegation (commands route to right expert)
- ✅ Quality-focused workflows (brainstorm → write → review)
- ✅ Publication-ready output (consistent voice, proper structure)

### Start Writing Now

```bash
/prepareChapter 1    # Let research-assistant build your foundation
/writeChapter 1      # Let chapter-writer craft your content
/styleCheck 1        # Let style-editor ensure quality
```

**Your book, powered by a team of AI specialists.** 🚀📚

---

*Questions? Issues? Check `SDK_FEATURES.md` for detailed documentation or open an issue on GitHub.*
