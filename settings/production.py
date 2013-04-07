#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getpass

DEBUG = False
TEMPLATE_DEBUG = DEBUG


location = "/home/apps/app_00078/app/restaurator/"

sys.path.append(location)
sys.path.append(location + '../')

DATABASE_SCHEMA = 'restaurator'

import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MEDIA_ROOT = location + "media/"

STATICFILES_DIRS = (location + "static/",)

TEMPLATE_DIRS = (location + "templates/",)


EMAIL_HOST = 'localhost'

