from __future__ import absolute_import
from .base import *
from bundle_config import config

DEBUG=False
TEMPLATE_DEBUG=DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config['postgres']['database'],
        'USER': config['postgres']['username'],
        'PASSWORD': config['postgres']['password'],
        'HOST': config['postgres']['host'],
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '{host}:{port}'.format(
                host=config['redis']['host'],
                port=int(config['redis']['port'])
        ),
        'OPTIONS': {
            'PASSWORD': config['redis']['password']
        },
        'VERSION': config['core']['version'],
    },
}

# Use Postmark for email
EMAIL_APP_FROM = "info@automatique.com"
POSTMARK_TEST_MODE=False
POSTMARK_API_USER = "USERNAME"
POSTMARK_API_PASSWORD = "PASSWORD"
EMAIL_BACKEND = "postmark.backends.PostmarkBackend"
POSTMARK_API_KEY = 'API-KEY'

# Celery configuration
CELERY_RESULT_BACKEND = "redis"
REDIS_HOST = CELERY_REDIS_HOST = config['redis']['host']
REDIS_PORT = CELERY_REDIS_PORT = int(config['redis']['port'])
REDIS_PASSWORD = CELERY_REDIS_PASSWORD = config['redis']['password']
REDIS_CONNECT_RETRY = True

BROKER_BACKEND = "redis"
BROKER_TRANSPORT = "redis"
BROKER_HOST = config['redis']['host']
BROKER_PORT = int(config['redis']['port'])
BROKER_PASSWORD = config['redis']['password']

# django-redis-sessions
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = config['redis']['host']
SESSION_REDIS_PORT = int(config['redis']['port'])