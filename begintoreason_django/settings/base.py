"""
Django base settings for begintoreason_django project.

This file contains the settings that are shared in development
and production modes. See `development.py` and `production.py`
for specific settings.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l46i#coubyfrpmlk2%h#kp^t_^w_kv8xpwtxm&5#x361wieb@f'

# client keys and secret for google auth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '611944294175-bbmqfpu7gemb6bjeacgrdtqg0qq6arcg.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'tqfQvS7M_TnxDTM0PO4T_GAe'

# Application definition

INSTALLED_APPS = [
    # Django Applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Our own applications
    'accounts',
    'core',
    'data_analysis',
    'educator',
    'think_aloud',
    'tutor',

    # External Plugins
    'social_django',
    'django_ace',
    'compressor',
    'crispy_forms',
    'mathfilters'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'begintoreason_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'begintoreason_django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../../db.sqlite3'),
    }
}

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin
    'django.contrib.auth.backends.ModelBackend',

    # google oauth2
    'social_core.backends.google.GoogleOAuth2',
]


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../../static')

# django-compressor
# https://django-compressor.readthedocs.io/en/stable/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    # other finders..
    'compressor.finders.CompressorFinder'
]

# django-libsass
# https://github.com/torchbox/django-libsass

COMPRESS_PRECOMPILERS = [
    ('text/x-scss', 'django_libsass.SassCompiler')
]

# Python Social Auth
# https://python-social-auth.readthedocs.io/en/latest/

LOGIN_URL = '/auth/login/google-oauth2/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

# Django 3.2 introduced a customization of primary keys. Since I don't believe that's a priority at the moment,
# this setting makes all unset primary keys default to what replaced the only option before (i.e. no change)
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'