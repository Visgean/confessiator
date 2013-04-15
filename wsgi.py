#!/usr/bin/env python
 
import os
import sys
 
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR']))
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'confessiator.settings.base'
 
virtenv = os.environ['OPENSHIFT_HOMEDIR'] + 'python-2.7/virtenv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.7/site-packages')
 
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()