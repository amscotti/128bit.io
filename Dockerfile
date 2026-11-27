# syntax=docker/dockerfile:1

FROM python:3.14-alpine3.24 AS builder

# Monospace font for Pillow OG image rendering
RUN apk add --no-cache font-dejavu

# Copy pinned uv binary from official distroless image
COPY --from=ghcr.io/astral-sh/uv:0.13.10 /uv /bin/

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /site

# Install locked production dependencies in a cached layer before copying site content
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-dev --no-install-project

# Copy build sources and generate production site
COPY pelicanconf.py publishconf.py ./
COPY plugins/ ./plugins/
COPY theme/ ./theme/
COPY content/ ./content/

RUN SITEURL=https://128bit.io uv run --no-sync pelican content -s publishconf.py

# Runtime image
FROM docker.io/library/httpd:2.4-alpine3.24

# Enable required modules and copy Apache config
RUN sed -i \
    -e 's/^#LoadModule headers_module/LoadModule headers_module/' \
    -e 's/^#LoadModule deflate_module/LoadModule deflate_module/' \
    -e 's/^#LoadModule expires_module/LoadModule expires_module/' \
    /usr/local/apache2/conf/httpd.conf

COPY httpd-custom.conf /usr/local/apache2/conf/extra/
RUN echo "Include conf/extra/httpd-custom.conf" >> /usr/local/apache2/conf/httpd.conf

COPY --from=builder /site/output /usr/local/apache2/htdocs/

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget -qO- http://127.0.0.1/ >/dev/null || exit 1
