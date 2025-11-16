---
description: Review chapter for style consistency and quality
allowed-tools: Task
---

# Style Check for Chapter $1: Delegate to Expert Style Editor

This command delegates style review to the **style-editor** subagent, a specialized voice consistency and quality expert.

## What Happens

The style-editor subagent will:

1. **Load context for comparison**:
   - The chapter to review from @chapters/chapter-$1.md
   - Style guide and standards from @style-guide.md
   - Style preferences from @book.config.json
   - 1-2 other completed chapters for voice comparison
   - Thematic context from BOOK_SUMMARY.md

2. **Conduct multi-pass analysis**:
   - **Voice Consistency**: Compare against established voice
   - **Structural Quality**: Assess hooks, flow, transitions, conclusions
   - **Line-Level Style**: Check rhythm, sentence craft, precision
   - **Content Quality**: Verify every paragraph earns its place
   - **Reader Experience**: Ensure engagement and clarity

3. **Identify issues with precision**:
   - Mark style problems with [STYLE: issue]
   - Flag clarity needs with [CLARIFY: what needs explanation]
   - Note revision opportunities with [REVISE: specific reason]
   - Suggest cuts with [CUT: justification]
   - Highlight voice inconsistencies with [VOICE: deviation]

4. **Provide prioritized recommendations**:
   - **Critical**: Must-fix issues that break immersion
   - **High Priority**: Should-fix for quality improvement
   - **Medium Priority**: Consider-fixing for polish
   - **Low Priority**: Nice-to-have enhancements
   - Specific fixes, not vague suggestions

5. **Deliver comprehensive review**:
   - Executive summary with overall assessment
   - Detailed findings by section
   - Comparative analysis against other chapters
   - Actionable next steps

## Your Command

**Delegate to the style-editor subagent to review chapter $1.**

The style-editor is a senior editor trained on your book's voice, style patterns, and quality standards. It will provide professional-grade editorial feedback with specific, actionable recommendations.

After the review, you can either make the suggested edits yourself or delegate specific revisions to the chapter-writer subagent.