# minimal128

A terminal-aesthetic Pelican theme designed for 128bit.io.

## Features

- **Terminal aesthetic**: Command-line inspired design with prompts, cursors, and file listings
- **Responsive design**: Mobile-first with breakpoints at 768px and 480px
- **Syntax highlighting**: Pygments integration with github-dark style
- **SEO optimized**: Open Graph and Twitter Card meta tags
- **Accessibility**: Supports `prefers-reduced-motion`
- **Pagination**: Built-in support for paginated archive listings

## Requirements

- Pelican 4.11+
- Python 3.11+

## Installation

Set in your `pelicanconf.py`:

```python
THEME = 'theme/minimal128'
```

## Required Settings

Add these to your `pelicanconf.py`:

```python
# Required
AUTHOR = 'Your Name'
SITENAME = 'Your Site Name'

# Optional but recommended
BIO = 'Your bio text...'
AVATAR = '/images/avatar.webp'
SOCIAL = (
    ('GitHub', 'https://github.com/username'),
    ('LinkedIn', 'https://linkedin.com/in/username'),
    ('X', 'https://x.com/username'),
)
X_HANDLE = '@username'

# Syntax highlighting
PYGMENTS_STYLE = 'github-dark'
```

## Template Structure

```
templates/
├── base.html              # Base template with common structure
├── index.html             # Homepage with whoami section
├── article.html           # Single post page
├── archives.html          # Paginated post listing
├── tag.html               # Posts filtered by tag
├── tags.html              # All tags listing
├── period_archives.html   # Year/month archive pages
└── includes/
    ├── head.html          # Common head elements (meta, styles)
    ├── header.html        # Terminal header component
    ├── footer.html        # Site footer
    ├── article-meta.html  # Article title, date, tags
    ├── article-preview.html # Article preview for listings
    ├── pagination.html    # Prev/next page navigation
    └── social-links.html  # Social media links
```

## Customization

### Terminal Prompt

The terminal prompt displays as `[amscotti@128bit.io ~]#`. To customize for your own site, modify:

1. `templates/includes/header.html` - Main prompt
2. `templates/index.html` - Whoami section prompt

### Colors

CSS variables are defined in `static/css/main.css`:

```css
:root {
  --bg-primary: #0d1117;
  --bg-secondary: #161b22;
  --text-primary: #f0f6fc;
  --text-secondary: #7d8590;
  --text-accent: #58a6ff;
  --terminal-accent: #7c3aed;
  --border-color: #30363d;
}
```

### Adding New Templates

1. Create your template extending `base.html`
2. Use `{% set header_path %}` and `{% set header_command %}` before including header
3. Use existing includes for consistency:
   - `{% include "includes/article-preview.html" %}` for post listings
   - `{% include "includes/pagination.html" %}` for navigation

## Include Components

### header.html

Variables:
- `header_path`: Path shown in prompt (default: `~`)
- `header_command`: Command text shown after prompt

Example:
```jinja
{% set header_path = "~/posts" %}
{% set header_command = "head *.md" %}
{% include "includes/header.html" %}
```

### article-preview.html

Requires `article` variable in scope. Displays:
- Title as filename link
- Publication date
- Tags
- Summary

### pagination.html

Automatically uses Pelican pagination variables:
- `articles_page`
- `articles_previous_page`
- `articles_next_page`

## License

MIT License
