#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Production configuration for 128bit.io"""

# Import all settings from development config
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Production URL
import os

# Netlify Context: 'production', 'deploy-preview', 'branch-deploy', or None (local)
NETLIFY_CONTEXT = os.environ.get('CONTEXT')

if NETLIFY_CONTEXT == 'production':
    SITEURL = 'https://128bit.io'
    RELATIVE_URLS = False
elif NETLIFY_CONTEXT == 'deploy-preview':
    # Use the Deploy Prime URL (e.g. https://deploy-preview-123--site.netlify.app)
    SITEURL = os.environ.get('DEPLOY_PRIME_URL', '')
    RELATIVE_URLS = False
else:
    # Local development or Docker (no context)
    SITEURL = ''
    RELATIVE_URLS = True

# Enable feeds for production
FEED_ALL_ATOM = 'index.xml'
FEED_MAX_ITEMS = 20

# Keep output directory (Netlify handles cleanup)
DELETE_OUTPUT_DIRECTORY = True
