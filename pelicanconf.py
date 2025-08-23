#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pelican configuration for 128bit.io"""

AUTHOR = 'Anthony Scotti'
SITENAME = '128bit.io'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation
FEED_ALL_ATOM = 'index.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL Settings - Critical for preserving existing URLs
# Default pattern for posts without explicit URL (newer posts)
ARTICLE_URL = 'posts/{slug}/'
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

# Index/Archives - Homepage at root, post listing at /posts/
INDEX_SAVE_AS = 'index.html'  # Homepage
ARCHIVES_SAVE_AS = 'posts/index.html'  # Post listing

# Tags
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

# Disable categories (Hugo site only uses tags)
CATEGORY_URL = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

# Disable author pages
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

# Pagination
DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Direct templates for homepage
DIRECT_TEMPLATES = ['index', 'archives', 'tags']
PAGINATED_TEMPLATES = {'index': None, 'archives': 10}

# Template pages (404, etc.)
TEMPLATE_PAGES = {
    '404.html': '404.html',
}

# Plugins - liquid_tags auto-discovered, but must enable specific tags
LIQUID_TAGS = ["youtube"]

# Theme
THEME = 'theme/minimal128'

# Syntax highlighting
PYGMENTS_STYLE = 'github-dark'

# Markdown settings
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'linenums': True,
            'guess_lang': False,
        },
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.tables': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

# Site parameters (accessible in templates)
BIO = "I'm a software engineer with a passion for learning new technologies, techniques, and building reliable systems. This is my personal blog where I explore various topics ranging from functional programming languages to a few thoughts on AI and reflections on technology."
AVATAR = '/images/amscotti.webp'
SOCIAL = (
    ('GitHub', 'https://github.com/amscotti'),
    ('LinkedIn', 'https://www.linkedin.com/in/amscotti/'),
    ('X', 'https://x.com/amscotti'),
)
X_HANDLE = '@amscotti'

# Static paths
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extra/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extra/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
}

# Don't copy source files
OUTPUT_SOURCES = False

# Delete output directory before regenerating
DELETE_OUTPUT_DIRECTORY = True

# Relative URLs for development
RELATIVE_URLS = True
