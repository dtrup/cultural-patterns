# GitHub Pages Publishing Guide

**Super Simple Setup** - Just markdown files, no configuration needed.

## Setup (2 steps)

1. **Enable GitHub Pages**:
   - Go to Settings → Pages
   - Source: "Deploy from a branch"  
   - Branch: `main` / `(root)`
   - Save

2. **Done!** Your book is live at: `https://[username].github.io/[repository-name]`

## How It Works

GitHub automatically renders your markdown files:
- `index.md` becomes your homepage
- `chapters/chapter-01.md` becomes `/chapters/chapter-01.html`
- Uses GitHub's default markdown styling (clean and readable)

## File Structure

Dead simple:
```
your-repo/
├── index.md          # Book homepage with TOC
└── chapters/         # Chapter markdown files
    ├── chapter-01.md
    ├── chapter-02.md
    └── ...
```

## Publishing Process

1. Write in plain markdown files
2. Push to GitHub: `git push`
3. Site updates automatically

## Features

✅ **Zero configuration** - just markdown  
✅ **GitHub's clean styling** - professional by default  
✅ **Mobile friendly** - responsive automatically  
✅ **Fast** - static files, no processing  

## Troubleshooting

### **Chapter changes not updating on the live site?**

This is the most common issue. Try these in order:

1. **Wait 2-3 minutes** after pushing - GitHub Pages needs time to rebuild
2. **Check build status**: Go to your repo → Actions tab → look for "pages build and deployment"
3. **Force refresh**: Clear browser cache or try incognito mode
4. **Check the commit**: Make sure your changes actually pushed to the main branch

### **Still not updating?**
- Go to Settings → Pages → Save (even if no changes) to trigger a rebuild
- Check that you're editing files in the `main` branch, not another branch

### **Links not working?**
- Use relative links: `[Chapter 1](chapters/chapter-01.md)`
- GitHub converts `.md` to `.html` automatically

### **Want to verify it's working?**
1. Make a small change to `index.md` (add a period somewhere)
2. Commit and push: `git add . && git commit -m "test update" && git push`
3. Watch the Actions tab for the build to complete
4. Check your live site in 2-3 minutes

**This is the simplest approach that actually works.** 📚