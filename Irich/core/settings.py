# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from decouple import config
from unipath import Path
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("===========================", CORE_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# load production server froim .env
#ALLOWED_HOSTS = ['localhost', '127.0.0.1', '13.232.49.240' config('SERVER', default='13.232.49.240')]
ALLOWED_HOSTS = ['*']
# Application definition
AWS_ACCESS_KEY_ID = 'AKIARVG45XWQYPC3KPYN'
AWS_SECRET_ACCESS_KEY= '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'
AWS_SNS_REGION_NAME='US East (N. Virginia)'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'app',
    'authentication',
    'django_google_maps',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'rest_framework',
    'corsheaders',
     
    
   
      
      
]
# AWS_ACCESS_KEY_ID = 
# AWS_SECRET_ACCESS_KEY= 
# AWS_SNS_REGION_NAME=

# IOS_PLATFORM_APPLICATION_ARN=
# ANDROID_PLATFORM_APPLICATION_ARN=
CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'authentication.urls'
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]
AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend'),
)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'qr-code': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'qr-code-cache',
        'TIMEOUT': 100000
    }
}
RAZOR_KEY_ID = "rzp_test_a6qBA77iGvUz3f"
RAZOR_KEY_SECRET = "eMcOH6gU2W90ye7vmrZusatO"

QR_CODE_CACHE_ALIAS = 'qr-code'
ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"   # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "core/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'

ASGI_APPLICATION = 'core.asgi.application'
# ASGI_APPLICATION = 'routing.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD':'mypassword',
        'HOST':'irich.cvhij6lkelzp.ap-south-1.rds.amazonaws.com'
        
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SELERLIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, 'static')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'core/static'),
)
print(STATICFILES_DIRS)
MEDIA_ROOT = os.path.join(CORE_DIR, 'media')
print("++++++++++++++++", MEDIA_ROOT)
MEDIA_URL = '/media/'

PAYMENT_API_KEY = 'pk_test_51K1UzDC28elAkKFnzO563cwDKV7RESRNiNaP9Zb6ORvd8l3H8shfU4ootf3bKii3xD7G39wty93wqu6pRNEiqDFZ00xvV7Tdmo'
PAYMENT_API_SECRET = 'sk_test_51K1UzDC28elAkKFn4MGLA1ogZ0XS1bdPp1a9KBTB24gpi6l0PhDOVcoUq7OxjMcNjspxsADfrZshFyN36rT9iwGn00k42geJ35'
#############################################################


REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #         'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    
}