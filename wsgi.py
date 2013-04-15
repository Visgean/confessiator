from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


#!/usr/bin/env python
 
# some original codes we need
import os
 
virtenv = os.environ['APPDIR'] + '/virtenv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.6/site-packages')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except:
    pass
 
# new codes we adding for Django
import sys
import django.core.handlers.wsgi
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "confessiator.settings.base")
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi' ))
application = django.core.handlers.wsgi.WSGIHandler()