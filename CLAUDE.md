# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Pelican-based static blog site (128bit.io) that publishes technical content about software development. The site uses a custom "minimal128" theme with a terminal aesthetic and is deployed via Netlify.

## Build and Development Commands

### Local Development
```bash
# Run development server with auto-reload
uv run pelican --autoreload --listen

# Or build then serve
uv run pelican content -s pelicanconf.py && uv run pelican --listen
```

### Production Build
```bash
uv run pelican content -s publishconf.py
```

### Docker
```bash
# Build and run locally
docker build -t 128bit . && docker run -p 8080:80 128bit
```

## Architecture

### Content Structure
- **Blog posts**: Markdown files in `content/posts/`
- **Images**: `content/images/`
- **Favicons/extras**: `content/extra/`
- **Configuration**: `pelicanconf.py` (dev), `publishconf.py` (production)

### Theme (minimal128)
Located in `theme/minimal128/`:
- **Templates**: Jinja2 templates in `templates/`
  - Base templates: `base.html`, `index.html`, `article.html`, `archives.html`, `tags.html`, `tag.html`, `404.html`
  - Includes: `templates/includes/` (head, header, footer, article-meta, article-preview, pagination, social-links)
- **Styles**: `static/css/main.css` (includes Pygments github-dark theme)

### Deployment
- **Netlify**: Configured via `netlify.toml`, uses UV for dependency management
- **Docker**: Apache httpd with custom config in `httpd-custom.conf`
- **Python Version**: 3.13

## Key Configuration

### URL Structure (Preserved from Hugo migration)
- Newer posts: `/posts/{slug}/`
- Older posts: `/{YYYY}/{MM}/{DD}/{slug}/` (via `Slug`, `Save_as`, `URL` metadata)
- Tags: `/tags/{slug}/`

### Article Metadata
```markdown
Title: Post Title
Date: 2026-01-01 12:00
Slug: post-slug
Tags: Tag1, Tag2
Summary: Brief description for listings and SEO.
```

### Pagination
- 10 posts per page
- Archives at `/posts/`, paginated at `/posts/page/{n}/`

## Dependencies

Managed via UV (`pyproject.toml`):
- `pelican[markdown]>=4.11.0`
- `pygments>=2.17.0`
- `pyyaml>=6.0`
