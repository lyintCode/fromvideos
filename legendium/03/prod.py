import os
from .base import *

DEBUG = False
ALOOWED_HOSTS = ['www.example.ru', 'example.ru']

# Database settings for production
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
        'OPTIONS': {
            "pool": True
        },
    }
}

DEV_MODE = False
