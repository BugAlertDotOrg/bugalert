#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Base URL of your website. If not specified, feeds will not be generated with
# properly-formed URLs. Include http:// and your domain, with no trailing slash
# at the end.
# SITEURL = 'https://www.example.com'
SITEURL = os.getenv('SITEURL', 'https://www.bugalert.org')
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'
FEED_RSS = 'feeds/rss.xml'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

CATEGORY_FEED_ATOM = 'feeds/category-%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/category-%s.rss.xml'
TAG_FEED_ATOM = 'feeds/tag-%s.atom.xml'
TAG_FEED_RSS = 'feeds/tag-%s.rss.xml'

# RSS_FEED_SUMMARY_ONLY = True

DELETE_OUTPUT_DIRECTORY = False 

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
