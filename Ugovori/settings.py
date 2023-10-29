

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-k0&mi&!#r*w$8os#d+@*#$w$_a8fh9yh(lo82m-e$h!7smb8sf'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','autougovori.herokuapp.com', '192.168.0.198', 'autougovori-b3a868c4d123.herokuapp.com']

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kupoprodaja',
    #'invoice',
    
    #third party apps
    #'report_builder',
    #'albums',
    'reportbro',
    'report',
    'crispy_forms',
    'crispy_tailwind',
    'xhtml2pdf',
    'bootstrap_datepicker_plus',
    'num2words'
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
ROOT_URLCONF = 'Ugovori.urls'

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
                'django.template.context_processors.static'
            ],

        },
    },
]

AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.RemoteUserBackend',
        'django.contrib.auth.backends.ModelBackend',
)
WSGI_APPLICATION = 'Ugovori.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




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

LOCALE_NAME="sr-Ltn"
LANGUAGE_CODE = 'sr-latn'

TIME_ZONE = 'Europe/Sarajevo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS= [
    BASE_DIR / "static"
]

STATIC_ROOT = "static_root"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'kupoprodaja.User'
LOGIN_REDIRECT_URL='/ugovori'
LOGIN_URL='/login'
LOGOUT_REDIRECT_URL='/login'
USE_THOUSAND_SEPARATOR = True
DATE_INPUT_FORMATS="%d.%m.%Y"
DATE_FORMAT = "%d.%m.%Y"
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK='tailwind'
REPORTBRO_STORAGE = 'django.core.files.storage.FileSystemStorage'
REPORTBRO_STORAGE_KWARGS = {'location': os.path.join(BASE_DIR, 'report_files')}
