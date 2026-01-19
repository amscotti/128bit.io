# GEMINI.md

This file provides context for Gemini when working with the **128bit.io** codebase.

## Project Overview

**128bit.io** is a personal technical blog built with the **Pelican** static site generator.
It features a custom theme ("minimal128") with a terminal-inspired aesthetic and is written in Python (v3.13).
The site is deployed to Netlify and can also be containerized using Docker.

## Environment & Dependencies

*   **Language:** Python 3.13+
*   **Dependency Manager:** `uv` (replaces pip/poetry/etc.)
*   **Configuration Files:**
    *   `pyproject.toml`: Dependency definitions.
    *   `uv.lock`: Locked dependency versions.
    *   `.python-version`: Specifies Python version (3.13).

## Building and Running

### Local Development
To run the development server with auto-reload and live listening:

```bash
uv run pelican --autoreload --listen
```
*   Server will typically be available at `http://128.0.0.1:8000`.

To perform a one-off build for development:
```bash
uv run pelican content -s pelicanconf.py
```

### Production Build
To build the site for production (applying `publishconf.py` settings):

```bash
uv run pelican content -s publishconf.py
```
Output is generated in the `output/` directory.

### Docker
The project includes a multi-stage `Dockerfile`:
1.  **Builder**: Python 3.13 alpine image using `uv` to build the static site.
2.  **Runtime**: Apache httpd alpine image serving the `output/` folder.

**Build and Run:**
```bash
docker build -t 128bit .
docker run -p 8080:80 128bit
```

## Directory Structure

*   **`content/`**: Source content for the site.
    *   `posts/`: Markdown files for blog entries.
    *   `images/`: Static image assets.
    *   `extra/`: Miscellaneous static files (favicons, CNAME, etc.).
*   **`theme/minimal128/`**: Custom Pelican theme.
    *   `templates/`: Jinja2 HTML templates.
    *   `static/`: CSS and other theme-specific assets.
*   **`output/`**: (Git-ignored) Generated static site artifacts.
*   **`pelicanconf.py`**: Main Pelican configuration for development.
*   **`publishconf.py`**: Production overrides for Pelican configuration.
*   **`netlify.toml`**: Netlify deployment configuration.

## Development Conventions

### Content Creation
*   **Format**: Markdown (`.md`).
*   **Metadata**: Files must include standard Pelican metadata at the top:
    ```markdown
    Title: My Post Title
    Date: YYYY-MM-DD HH:MM
    Slug: my-post-slug
    Tags: tag1, tag2
    Summary: A brief summary for the index page.
    ```
*   **Legacy URLs**: The project supports legacy URL structures (from a previous migration). Newer posts generally follow `/posts/{slug}/`.

### Theme Development
*   Modifications to the look and feel should be done in `theme/minimal128/`.
*   **CSS**: Located in `theme/minimal128/static/css/`.
*   **Templates**: Located in `theme/minimal128/templates/`.

### Deployment
*   **Netlify**: Automatically builds using `uv` defined in `netlify.toml`.
*   **Headers**: Security headers are configured in `netlify.toml` and `httpd-custom.conf`.
