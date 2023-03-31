"""
Django settings for communication_system project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import ssl
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!8)7sh84)no#c_rgd26f=_^7@q$horu%b12gn6@3r##-$3cqs%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
""" 
# Enable TLS 1.2
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_context.load_cert_chain('cert.pem', 'key.pem')

# Pass the SSL context object to the runsslserver command
RUNSERVERPLUS_SERVER_ADDRESS_PORT = 'localhost:8000'
RUNSERVERPLUS_SERVER_CERT = ssl_context
"""
if not DEBUG:
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
# Set the SSL certificate and key paths


ALLOWED_HOSTS = ['127.0.0.1']
# Application definition

INSTALLED_APPS = [
    'login_system',
    "sslserver",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

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
"""
# Relevant to the non secure version
AUTHENTICATION_BACKENDS = [
    'login_system.PlainTextBackend.PlainTextBackend',
    'django.contrib.auth.backends.ModelBackend',
]
"""

ROOT_URLCONF = 'communication_system.urls'

AUTH_USER_MODEL = 'login_system.Account'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'communication_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Communication_system',
        'USER': 'root',
        'PASSWORD': 'til96544',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

""" DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Communication_system',
        'USER': 'remote',
        'PASSWORD': '123456',
        'HOST': 'ec2-3-21-159-201.us-east-2.compute.amazonaws.com',
        'PORT': '3306',
    }
}
"""


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
