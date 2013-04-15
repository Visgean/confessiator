#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getpass, os.path


DEBUG = False
TEMPLATE_DEBUG = DEBUG

location = os.path.dirname(__file__) # this is not Django setting.
TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates"),
    # here you can add another templates directory if you wish.
)


sys.path.append(location)
sys.path.append(location + '../')


import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MEDIA_ROOT = location + "media/"

STATICFILES_DIRS = (location + "static/",)

TEMPLATE_DIRS = (location + "templates/",)


EMAIL_HOST = 'localhost'

