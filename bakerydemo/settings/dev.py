from .base import *

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# BASE_URL required for notification emails
BASE_URL = 'http://localhost:8000'

# INSTALLED_APPS += [
#     # Tips: https://github.com/korfuri/django-prometheus
#     'CHANGE_ME'
# ]

# MIDDLEWARE = [
#     'django_prometheus.middleware.PrometheusBeforeMiddleware',
#     *MIDDLEWARE,
#     'bakerydemo.middleware.BakeryMiddleware',
#     'django_prometheus.middleware.PrometheusAfterMiddleware'
# ]

# DATABASES['default']['ENGINE'] = 'django_prometheus.db.backends.sqlite3'
