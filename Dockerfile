FROM python:3.13-alpine AS builder

# Install UV for dependency management
RUN pip install uv

# Copy site into builder image
WORKDIR /site/
COPY . /site/

# Install dependencies and build site
RUN uv sync && uv run pelican content -s publishconf.py

# Copy site into httpd image
FROM docker.io/library/httpd:alpine3.20

# Enable required modules and copy config
RUN sed -i \
    -e 's/^#LoadModule headers_module/LoadModule headers_module/' \
    -e 's/^#LoadModule deflate_module/LoadModule deflate_module/' \
    -e 's/^#LoadModule expires_module/LoadModule expires_module/' \
    /usr/local/apache2/conf/httpd.conf

COPY httpd-custom.conf /usr/local/apache2/conf/extra/
RUN echo "Include conf/extra/httpd-custom.conf" >> /usr/local/apache2/conf/httpd.conf

COPY --from=builder /site/output /usr/local/apache2/htdocs/
