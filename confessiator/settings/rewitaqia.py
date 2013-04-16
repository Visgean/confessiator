#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getpass

#sys.path.append("/home/visgean/scripty/pymodules/") # django modules like django_filters

USER_HOME_FOLDER = 'visgean'
PROJECT_NAME = 'restaurator'
location = "/home/visgean/scripty/confessiator_source/confessiator/"

DATABASES = {
	"default" : {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': location + '../sqlite3.db',                      # Or path to database file if using sqlite3.
        'USER': 'django',                      # Not used with sqlite3.
        'PASSWORD': 'WpmMMCo7GiWK',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = location + "media/"

STATICFILES_DIRS = (location + "static/",)

TEMPLATE_DIRS = (location + "templates/",)

DEBUG = True

EMAIL_HOST = 'localhost'



