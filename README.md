# 128bit.io

Source code for [https://128bit.io](https://128bit.io).

## Tech Stack

- **Static Site Generator:** [Pelican](https://getpelican.com/) (Python 3.13)
- **Dependency Management:** [uv](https://github.com/astral-sh/uv)
- **Theme:** Custom "minimal128" terminal aesthetic
- **Deployment:** Netlify

## Local Development

To run the development server with auto-reload and live listening:

```bash
uv run pelican --autoreload --listen
```

The site will typically be available at `http://127.0.0.1:8000`.

## Building for Production

To perform a production build:

```bash
uv run pelican content -s publishconf.py
```