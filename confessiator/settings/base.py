import socket

DEBUG = False
TEMPLATE_DEBUG = DEBUG



if socket.gethostname() in ("Rew", 'rewi'):
    from confessiator.settings.rewitaqia import *
else:
    from confessiator.settings.production import *

from confessiator.credentials import *



ADMINS = (
    ('Visgean Skeloru', 'Visgean@gmail.com'),
)

MANAGERS = ADMINS

AUTH_PROFILE_MODULE = 'secrets.UserProfile'


TIME_ZONE = 'Europe/Prague'

LANGUAGE_CODE = 'cz-cs'

SITE_ID = 1

USE_I18N = True

USE_L10N = False

STATIC_URL = '/static/'
MEDIA_ROOT = location + "media/"
MEDIA_URL = '/media/'
TEMPLATE_DIRS = (
    location + 'templates/',
)

ADMIN_MEDIA_PREFIX = '/static/admin/'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

)


TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.tz",
                               "django.contrib.messages.context_processors.messages",
                                                              )


INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = 'confessiator.urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    "debug_toolbar",
    "social_auth",
    
    "confessiator.secrets",
)

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False
}


LOGIN_URL = "/login/facebook/"
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

FACEBOOK_EXTENDED_PERMISSIONS = ['user_groups', 'manage_pages', 'publish_actions', 'status_update', 'create_note']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


DATE_INPUT_FORMATS = ('%d.%m.%Y',)


AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)


# translations
gettext = lambda s: s
LANGUAGES = (
    ('cs', gettext('Czech')),
    ('en', gettext('English')),
)
