#!/usr/bin/env python
"""Production configuration for 128bit.io"""

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# Netlify Context: 'production', 'deploy-preview', 'branch-deploy', or None (local/Docker)
NETLIFY_CONTEXT = os.environ.get('CONTEXT')

if NETLIFY_CONTEXT in ('deploy-preview', 'branch-deploy'):
    SITEURL = os.environ.get('DEPLOY_PRIME_URL', '').rstrip('/')
    RELATIVE_URLS = False
elif os.environ.get('RELATIVE_URLS') == '1':
    SITEURL = ''
    RELATIVE_URLS = True
else:
    # Production Netlify, Docker, or local production builds
    SITEURL = os.environ.get('SITEURL', 'https://128bit.io').rstrip('/')
    RELATIVE_URLS = False

# Enable feeds for production
FEED_ALL_ATOM = 'index.xml'
FEED_MAX_ITEMS = 20

# Clean output directory before regenerating production build
DELETE_OUTPUT_DIRECTORY = True
