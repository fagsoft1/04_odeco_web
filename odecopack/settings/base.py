"""
Django settings for DrAmor project.
Generated by 'django-admin startproject' using Django 1.11.
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from sys import path


def str_to_bool(s):
    if s == 'True':
        return True
    elif s == 'False':
        return False
    else:
        raise ValueError


# Quick-start development perfil - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Absolute filesystem path to the top-level project folder:
SITE_ROOT = os.path.dirname(DJANGO_ROOT)
# Site name:
SITE_NAME = os.path.basename(DJANGO_ROOT)
# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


# Application definition

########## APP CONFIGURATION
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
MY_APPS = [
    'web',
    'web_configurations',
    'web_soluciones',
    'web_empresa',
    'web_clientes',
    'web_contactos',
    'web_casos_exito',
]

THIRD_PART_APPS = [
    'import_export',
    'solo',
    'tinymce',
    'imagekit',
    'redisboard',
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + MY_APPS + THIRD_PART_APPS
########## END APP CONFIGURATIO

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware'
]

########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_ROOT, 'templates'),
        ]
        ,
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

WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

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

LANGUAGE_CODE = 'es'

USE_THOUSAND_SEPARATOR = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'odecopackdb',
    }
}

########## STATIC FILE CONFIGURATION
STATICFILES_DIRS = [
    os.path.normpath(os.path.join(SITE_ROOT, "static"))
]
########## END STATIC FILE CONFIGURATION


############ TINYMCE CONFIGURATION
TINYMCE_DEFAULT_CONFIG = {
    'selector': 'textarea',
    'height': 300,
    'theme': 'modern',
    'plugins': [
        'advlist autolink lists link image charmap print preview hr anchor pagebreak',
        'searchreplace wordcount visualblocks visualchars code fullscreen',
        'insertdatetime media nonbreaking save table contextmenu directionality',
        'emoticons template paste textcolor colorpicker textpattern imagetools',
        'autoresize'
    ],
    'toolbar1': 'insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
}
############ END TINYMCE CONFIGURATION


IMAGEKIT_WATERMARK_IMAGE = os.path.join(SITE_ROOT, 'static/web/img/marca_agua.png')
IMAGEKIT_WATERMARK_IMAGE_ORANGE = os.path.join(SITE_ROOT, 'static/web/img/marca_agua_orange.png')
