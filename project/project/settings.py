"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 1.11.14.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o9ek3%9#!3ts7vmmiuxt^f&^m7xtlgdkx1ov16ouq+4u(20&30'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


LOG_LEVEL = 'INFO'
# LOG_LEVEL = 'DEBUG' if DEBUG else 'INFO'
LOGFILE_SIZE = 10 * 1024 * 1024  # 10 MB max log size
LOGFILE_COUNT = 2
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'rq_console': {
        'format': '%(asctime)s %(message)s',
        'datefmt': '%H:%M:%S',
        },
        'verbose': {
        'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
        'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
        'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file-django': {
        'level': LOG_LEVEL,
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': '/srv/logs/scada_site.log',
        'maxBytes': LOGFILE_SIZE,
        'backupCount': LOGFILE_COUNT,
        'formatter': 'verbose'
        },
        'file-testing': {
        'level': 'INFO',
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': '/srv/logs/testing.log',
        'maxBytes': LOGFILE_SIZE,
        'backupCount': LOGFILE_COUNT,
        'formatter': 'verbose'
        },
        'file-management': {
        'level': LOG_LEVEL,
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': '/srv/logs/scada_management.log',
        'maxBytes': LOGFILE_SIZE,
        'backupCount': LOGFILE_COUNT,
        'formatter': 'verbose'
        },
        'console': {
        'level': LOG_LEVEL,
        'class': 'logging.StreamHandler',
        'formatter': 'verbose'
        }
    },
    'loggers': {
        'django': {
        'handlers': ['file-django'],
        'propagate': True,
        'level': LOG_LEVEL,
        },
        'testing': {
        'handlers': ['file-testing'],
        'propagate': True,
        'level': LOG_LEVEL,
        },
        'management': {
        'handlers': ['file-management'],
        'propagate': True,
        'level': LOG_LEVEL,
        },
        'console': {
        'handlers': ['console'],
        'propagate': True,
        'level': LOG_LEVEL,
        },
    }
}
