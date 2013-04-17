#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import getpass
import os.path
import os
import urlparse


DEBUG = True
TEMPLATE_DEBUG = DEBUG

location = os.environ['OPENSHIFT_REPO_DIR'] + 'confessiator/'


sys.path.append(location)

MEDIA_ROOT = location + "media/"


if 'OPENSHIFT_REPO_DIR' in os.environ:
    MEDIA_ROOT= os.environ['OPENSHIFT_REPO_DIR'] + '/wsgi/media/'
else:
    MEDIA_ROOT = location + "media/"


STATICFILES_DIRS = (location + "static/",)
TEMPLATE_DIRS = (location + "templates/",)

EMAIL_HOST = 'localhost'

DATABASES = {'default':
            {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'dev.db',
                'USER': '',
                'PASSWORD': '',
                'HOST': '',
                'PORT': '',
            },
}


if 'OPENSHIFT_MYSQL_DB_URL' in os.environ:
    url = urlparse.urlparse(os.environ.get('OPENSHIFT_MYSQL_DB_URL'))
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['OPENSHIFT_APP_NAME'],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
elif 'OPENSHIFT_POSTGRESQL_DB_URL' in os.environ:
    url = urlparse.urlparse(os.environ.get('OPENSHIFT_POSTGRESQL_DB_URL'))
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['OPENSHIFT_APP_NAME'],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
