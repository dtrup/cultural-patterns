---
description: Complete end-to-end chapter workflow - prepare, write, style check, and finalize
allowed-tools: Task, Read, Write, Edit, Bash, SlashCommand
---

# Do Chapter $1: Complete Automated Workflow

Execute all phases of chapter creation in sequence:
1. **Prepare** (research & brainstorm)
2. **Write** (polished content)
3. **Style Check** (editorial review)
4. **Complete** (finalize & update progress)

## Your Task

Run all four phases sequentially for chapter $1. After each phase, provide a brief status update before proceeding to the next phase.

### Phase 1: Prepare Chapter $1

Switch to haiku for efficient research:
```
/model haiku
```

Execute: `/prepareChapter $1`

**After completion:**
- Confirm brainstorm file created in `brainstorms/chapter-$1-brainstorm.md`
- Brief summary: research quality, example count, confidence level
- Status: ✅ Phase 1 Complete - Research & Brainstorm Ready

---

### Phase 2: Write Chapter $1

Switch back to sonnet for writing:
```
/model sonnet
```

Execute: `/writeChapter $1`

**After completion:**
- Confirm chapter file written to `chapters/chapter-$1.md`
- Verify Jekyll front matter exists (layout: chapter, title)
- Check word count (target ~4,750 words)
- Status: ✅ Phase 2 Complete - Chapter Drafted

---

### Phase 3: Style Check Chapter $1

Execute: `/styleCheck $1`

**After completion:**
- Review style-editor feedback summary
- Note critical/high-priority issues (if any)
- Ask user: "Apply suggested edits now? (yes/no)"
  - If yes: Make recommended changes using Edit tool
  - If no or minor issues: Proceed to completion
- Status: ✅ Phase 3 Complete - Editorial Review Done

---

### Phase 4: Complete Chapter $1

Execute: `/completeChapter $1`

**After completion:**
- Update chapter YAML front matter with `status: complete`
- Run progress sync script
- Extract chapter summary to CHAPTER_SUMMARIES.md
- Report final stats and book progress
- Status: ✅ Phase 4 Complete - Chapter Finalized

---

## Final Report

Provide a comprehensive completion summary:

```
🎉 Chapter $1 Complete: Full Workflow Finished!

📋 Phases Completed:
✅ Research & Brainstorm (haiku)
✅ Chapter Writing (sonnet)
✅ Style Review (editorial)
✅ Finalization & Progress Update

📊 Chapter Stats:
- Word Count: [actual]
- Target: ~4,750 words
- Status: Complete
- Completed: [date]

📈 Book Progress:
- Chapters Complete: X of 21
- Total Words: [sum]
- Overall: XX%

📌 Next Steps:
- Review chapter $1 in `chapters/chapter-$1.md`
- Continue with `/doChapter [next number]`
- Or run `/bookStatus` for full dashboard
```

## Quality Standards

Each phase must meet quality thresholds:
- **Prepare**: 2+ authoritative sources per major claim, 3-5 verified examples
- **Write**: ~4,750 words, proper front matter, chapter summary section included
- **Style Check**: Voice consistency confirmed, critical issues addressed
- **Complete**: No TODO markers, Jekyll front matter verified, progress synced

## Error Handling

If any phase fails:
1. Report the specific phase and error
2. Provide troubleshooting steps
3. Allow user to resume from failed phase
4. Do NOT proceed to next phase until current phase succeeds

## User Interaction

- Minimal interaction required (designed for autonomous execution)
- Only pause for style check edits if critical issues found
- User can interrupt between phases if needed
- Full transparency: show what's happening at each step
