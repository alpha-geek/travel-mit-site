# Django settings for travelsite project.
import os
from os import environ
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('marcelar', 'marcelar@mit.edu','travelmit785@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'traveldb',
        'USER': 'dev',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
  }
#import psycopg2
#import urlparse

#urlparse.uses_netloc.append("postgres")
#url = urlparse.urlparse(os.environ["DATABASE_URL"])

#conn = psycopg2.connect(
#    database=url.path[1:],
#    user=url.username,
#    password=url.password,
#    host=url.hostname,
#    port=url.port
#)

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/' #Will change
# Example: "/home/media/media.lawrence.com/static/"STATIC_ROOT = ''


# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".

STATIC_ROOT ='travelsite/static/'

STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/__scripts/django/media/'


# List of (WHAT WAS HERE?) 
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



SECRET_KEY = 'f6%agbk_m8u-o_p8jjeiy29bq!zt#r4bsnd)%apxq=gkto1ehx'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
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

# URL prefix for admin static files -- CSS, JavaScript and images.
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'travelsite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'travelsite.wsgi.application'
#import os.path
PROJECT_DIR = os.path.dirname(__file__)
TEMPLATE_DIRS = (
 # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, "mytemplates"),
    os.path.join(PROJECT_DIR, "mytemplates/admin"),
    os.path.join(PROJECT_DIR, "mytemplates/destinations"),
    "/Users/marcelar/djangosites/travel-mit-site/travelsite/mytemplates",
    "/Users/marcelar/djangosites/travel-mit-site/travelsite/mytemplates/admin",
    "/Users/marcelar/djangosites/travel-mit-site/travelsite/mytemplates/destinations",
    "/Users/marcelar/djangosites/travel-mit-site/travelsite/mytemplates/css",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.admin',
    'travelsite',
    'travelsite.destinations',
#    'travelsite.forum',
    'travelsite.registration',
    'travelsite.profiles',
    'storages',
    'boto'
#    'askbot',
#    'travelsite.haystack',
#    'south',
)

LOGIN_REDIRECT_URL = 'http://agile-bastion-8951.herokuapp.com'
AUTH_PROFILE_MODULE = 'profiles.Profile' #May have to change back
ACCOUNT_ACTIVATION_DAYS = 7


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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



#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = os.environ.get('app18949432@heroku.com')
EMAIL_HOST = environ.get('smtp.sendgrid.net')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ.get('csfyhi6z')
#SERVER_EMAIL = 'travelmit785@gmail.com'
# Parse database configuration from $DATABASE_URL for Heroku use
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
AWS_ACCESS_KEY_ID = 'AKIAI447NW4T5C6OMHDQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'travelsite'


DEFAULT_FILE_STORAGE = 'travelsite.s3utils.MediaS3BotoStorage' 
STATICFILES_STORAGE = 'travelsite.s3utils.StaticS3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_DIRECTORY = '/static/'
MEDIA_DIRECTORY = '/media/'
STATIC_URL = S3_URL + STATIC_DIRECTORY
MEDIA_URL = S3_URL + MEDIA_DIRECTORY