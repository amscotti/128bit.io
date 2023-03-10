FROM alpine:3.17 AS builder

ENV HUGO_VERSION 0.111.2
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux-64bit

# Install pygments (for syntax highlighting) and git
RUN apk update && apk add --no-cache py-pygments git

# Download and Install hugo
RUN mkdir /usr/local/hugo
ADD https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz /usr/local/hugo/
RUN tar xzf /usr/local/hugo/${HUGO_BINARY}.tar.gz -C /usr/local/hugo/ \
	&& ln -s /usr/local/hugo/hugo /usr/local/bin/hugo \
	&& rm /usr/local/hugo/${HUGO_BINARY}.tar.gz

# Copy site into builder image
WORKDIR /site/
COPY . /site/

# Build site
RUN git submodule update --init --recursive
RUN hugo --gc --minify -b "/"

# Copy site into httpd image
FROM docker.io/library/httpd:alpine3.17
COPY --from=0 /site/public /usr/local/apache2/htdocs/ 