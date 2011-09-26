from __future__ import absolute_import
from .base import *

DEBUG=True
TEMPLATE_DEBUG=DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'iknewit',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# setup email through Postmarkapp
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.postmarkapp.com'
#EMAIL_PORT = '2525'
#EMAIL_HOST_USER = 'ac46783e-31bd-4c35-a50e-f8c83c43e62b'
#EMAIL_HOST_PASSWORD = 'ac46783e-31bd-4c35-a50e-f8c83c43e62b'
POSTMARK_TEST_MODE=True
EMAIL_BACKEND = "postmark.backends.PostmarkBackend"
POSTMARK_API_KEY = 'ac46783e-31bd-4c35-a50e-f8c83c43e62b'

# Celery cofiguration
BROKER_HOST = "localhost"
BROKER_PORT = 6379
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = "/"