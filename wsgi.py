
import os
import sys, getpass, os.path


location = os.path.dirname(__file__) # this is not Django setting.)


sys.path.append(location)
sys.path.append(location + '../')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "confessiator.settings.base")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
