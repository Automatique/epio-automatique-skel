from unipath import FSPath as Path
import sys

# do celery
import djcelery
djcelery.setup_loader()

sys.path.append('lib')

PROJECT_DIR = Path(__file__).absolute().ancestor(2)

ADMINS = (
    ("Tijs Teulings", "tijs@automatique.nl"),
)

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Amsterdam'
LANGUAGE_CODE = 'nl-NL'
SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = PROJECT_DIR.parent.child('data')
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_DIR.child('static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    str(PROJECT_DIR.child('static')),
    #str(PROJECT_DIR.parent.child('data')),
)
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'i5txu^^&i0h9=yl&1=+uy^ik0u8nja2dno#es*hvff#cuo6c@n'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    PROJECT_DIR.child('templates'),
)

MIDDLEWARE_CLASSES = (
    'annoying.middlewares.StaticServe',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    # tools
    'south',
    'debug_toolbar',
    'djcelery',
    'epio_commands',

    # helper apps
    'sorl.thumbnail',
    'postmark',

    # main app
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

# Setup for templated-email app
EMAIL_APP_FROM = 'tijs@automatique.nl'
TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'
TEMPLATED_EMAIL_DJANGO_SUBJECTS = {
#        'new_prediction' : 'Somebody predicted one of your topics in I Knew It',
      }

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

# Celery config
CELERY_IGNORE_RESULT = True
CELERY_DISABLE_RATE_LIMITS = True
#CELERY_IMPORTS = ("predictions.tasks", "scoreboard.tasks", )

# Cached sessions
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"