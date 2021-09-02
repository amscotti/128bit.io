FROM ubuntu:21.10 AS builder

# Install git and hugo
RUN apt-get update && apt-get install -y git hugo

# Copy site into builder image
WORKDIR /site/
COPY . /site/

# Build site
RUN git submodule update --init --recursive
RUN hugo --gc --minify -b "/"

# Copy site into httpd image
FROM httpd:2.4-alpine
COPY --from=0 /site/public /usr/local/apache2/htdocs/