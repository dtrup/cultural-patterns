# Contributing to Book-Base

Thank you for helping make book-base the best LLM-powered writing system! 

## 🎯 What We're Building

A **simple, powerful system** that transforms book writing from overwhelming to systematic. We focus on:

- **LLM-optimized workflows** that leverage AI strengths  
- **Minimal complexity** with maximum functionality
- **Quality-focused processes** that produce professional results
- **Flexibility** for different book types and writing styles

## 🚀 How to Contribute

### Improve Commands
The heart of book-base is the `.claude/commands/` system. Great commands:

- **Give clear direction** to the LLM about what to accomplish
- **Reference specific files** using @filename syntax  
- **Include quality criteria** so LLMs know what "good" looks like
- **Chain together logically** with other commands in the workflow

### Command Quality Standards
```markdown
---
description: Brief, clear description of command purpose
allowed-tools: List of tools the LLM needs
thinking-mode: long (for complex tasks)
---

# Clear, Action-Oriented Title

Brief explanation of what this command accomplishes.

## Your Task
1. Numbered steps that are specific and actionable
2. Reference files with @filename for context
3. Include quality criteria and standards
4. Specify exact outputs and updates needed
```

### New Command Ideas
We're always looking for commands that:
- **Fill workflow gaps** - steps that aren't covered yet
- **Improve quality** - better review and refinement processes  
- **Add flexibility** - support for different book types or workflows
- **Enhance automation** - reduce manual tracking and updates

## 📝 Types of Contributions

### 1. New Commands
**Great additions**:
- Genre-specific commands (memoir, technical, academic)
- Quality assurance commands (fact-check, citation-check)
- Workflow variants (fast-draft, research-heavy)
- Publication commands (format for different outputs)

### 2. Template Improvements  
**Core templates** in root directory:
- `TOC.md` - make it work for more book types
- `style-guide.md` - better customization guidance
- `book.config.json` - additional useful configuration options

### 3. Documentation
- **README improvements** - clearer instructions, better examples
- **Command documentation** - usage examples and tips
- **Workflow guides** - specialized approaches for different book types

### 4. Bug Fixes
- Commands that don't work as expected
- File reference issues
- Template placeholder problems

## 🧪 Testing Contributions

### Before Submitting
1. **Test your command** with a real book project
2. **Verify file references** work correctly (@filename syntax)
3. **Check for clear output** - does the command produce what it promises?
4. **Test integration** - does it work well with existing commands?

### Command Testing Checklist
- [ ] Command runs without errors
- [ ] Produces expected files/updates  
- [ ] Integrates with existing workflow
- [ ] Clear, actionable output for users
- [ ] Follows established patterns

## 💭 Design Philosophy

### Keep It Simple
- **LLMs handle complexity** - commands provide structure
- **No overengineering** - resist adding unnecessary features
- **Minimal dependencies** - works out of the box
- **Clear patterns** - consistent command design

### Focus on Workflow  
- **Guide, don't automate** - LLMs make decisions, commands guide process
- **Quality over speed** - better to write well than fast
- **Progress visibility** - users always know where they stand
- **Flexible structure** - adapt to different writing styles

## 📬 How to Submit

### Pull Request Process
1. **Fork book-base** repository
2. **Create feature branch** (`git checkout -b command/new-feature`)
3. **Test thoroughly** with real book project
4. **Submit PR** with clear description of improvement
5. **Include example** of command in use

### PR Description Template
```
## What This Adds
Brief description of the new command or improvement

## Why It's Needed  
What gap this fills or problem it solves

## How It Works
Example usage and integration with existing workflow

## Testing Done
How you verified this works correctly
```

---

## 🙏 Recognition

Contributors who improve book-base help writers worldwide create better books with AI assistance. Every improvement compounds across all future books written with this system.

**That's pretty amazing impact for a simple command file!**

---

*Questions? Open an issue or submit a PR with your ideas.*