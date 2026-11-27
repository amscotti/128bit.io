# minimal128

A modern, accessible terminal-aesthetic Pelican theme designed for 128bit.io.

## Features

- **Terminal aesthetic**: Command-line inspired layout with prompts, cursors, and file listings
- **Light & dark themes**: Built on CSS `color-scheme` and `light-dark()` with an interactive `[theme]` toggle and adaptive Pygments syntax highlighting
- **WCAG AA contrast & semantics**: Proper `<h1>`/`<h2>` hierarchy, skip-to-content link, `<time>` elements, ARIA labels, `prefers-reduced-motion` support, and print styles
- **Modern CSS architecture**: Structured with `@layer` cascade layers, logical properties, `color-mix()`, `:has()` wide-screen sticky Table of Contents, and responsive breakpoints at 768px and 480px
- **Reader utilities**: Zero-dependency CSP-safe `terminal.js` for copy-code buttons, language badges, light/dark toggle, and a Pagefind-powered terminal `grep` search `<dialog>` (`/` or `Cmd/Ctrl+K`)
- **SEO & syndication**: Canonical URLs, Open Graph + Twitter Cards, JSON-LD (`WebSite`, `Person`, `BlogPosting`), Atom feed discovery, and `llms.txt` / raw `.md` links

## Requirements

- Pelican 4.11+
- Python 3.11+

## Optional Pelican Settings

```python
AUTHOR = 'Your Name'
SITENAME = 'Your Site Name'
BIO = 'Your bio text...'
AVATAR = '/images/avatar.webp'
SOCIAL = (
    ('GitHub', 'https://github.com/username'),
    ('LinkedIn', 'https://linkedin.com/in/username'),
    ('X', 'https://x.com/username'),
)
X_HANDLE = '@username'
CURRENT_YEAR = 2026
DEFAULT_OG_IMAGE = '/og/default.png'
MAIN_CSS_URL = 'theme/css/main.css'      # Supports fingerprinted asset paths
MAIN_JS_URL = 'theme/js/terminal.js'     # Supports fingerprinted asset paths
```

## Template Structure

```
theme/minimal128/
├── static/
│   ├── css/main.css          # Layered light/dark terminal stylesheet
│   └── js/terminal.js        # CSP-safe theme toggle, copy-code, Pagefind modal
└── templates/
    ├── base.html             # Base layout, SEO meta, skip link, search <dialog>
    ├── index.html            # Homepage with whoami and recent posts
    ├── article.html          # Article view with TOC, related posts, prev/next, JSON-LD
    ├── archives.html         # Paginated post listing
    ├── tag.html              # Posts filtered by tag
    ├── tags.html             # All tags listing
    ├── period_archives.html  # Year/month archive pages
    ├── 404.html              # Terminal 404 page
    └── includes/
        ├── head.html         # Meta, stylesheet, feed discovery, favicons
        ├── header.html       # Terminal prompt + primary nav + search/theme controls
        ├── footer.html       # Copyright, RSS, llms.txt
        ├── article-meta.html # Title, date/updated, reading time, raw .md, tags
        ├── article-preview.html # Listing preview card
        ├── pagination.html   # Prev/next page navigation
        └── social-links.html # Social + RSS links
```

## License

MIT License
