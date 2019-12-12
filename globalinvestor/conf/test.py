from .base import *

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'globalinvestor',
        'USER': 'admin',
        'PASSWORD': 'admin@20191201',
        'HOST': 'localhost',
        'PORT': 3306
    }
}

