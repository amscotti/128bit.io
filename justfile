# 128bit.io task runner

default:
    @just --list

# Run Pelican dev server with autoreload
dev:
    uv run pelican --autoreload --listen

# Build development site
build:
    uv run pelican content -s pelicanconf.py

# Build production site
prod:
    CONTEXT=production uv run pelican content -s publishconf.py

# Build production site and generate Pagefind search index
search: prod
    npx --yes pagefind --site output

# Run linters and production build checks
check:
    uv run ruff check pelicanconf.py publishconf.py plugins scripts
    uv run djlint --lint theme/minimal128/templates/
    CONTEXT=production uv run pelican content -s publishconf.py

# Scaffold a new blog post (e.g. just new "My Post Title" --tags "Python, Systems")
new title *args:
    uv run python scripts/new_post.py "{{title}}" {{args}}

# Build Docker image locally
docker:
    docker build -t 128bit .
