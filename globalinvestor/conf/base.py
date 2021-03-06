"""
Django settings for globalinvestor project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)
sys.path.insert(0,os.path.join(BASE_DIR,'../apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fixa)xa!=fy1%%j52tqe_8+4fs)p!2cf(76y7)8yaysc-%ra2%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'globalinvestor',
    'cn_a_stocks.apps.CnAStocksConfig',
    'cn_hk_stocks',
    'us_stocks',
    'cryptocurrency',

    # xadmin
    'xadmin',
    'crispy_forms',
    'reversion',

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

ROOT_URLCONF = 'globalinvestor.urls'

THEME = 'default'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'themes', THEME, 'templates')],
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

WSGI_APPLICATION = 'globalinvestor.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = False
DATE_FORMAT = 'Y/m/d'  # 如要生效，需设置USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# python manager.py collectstatic 收集静态文件的目录
STATIC_ROOT = os.path.join(BASE_DIR, 'themes', THEME,'tmp', 'static/')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'themes', THEME, 'static/')
]


# 分页数据展示数量
PAGINATOR_NUM = 16

# xadmin主题设置
XADMIN_TITLE = 'Global Investor'
XADMIN_FOOTER_TITLE = 'Global Investor'


# logging 日志设置
BASE_LOG_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.join(BASE_LOG_DIR):
    os.mkdir(BASE_LOG_DIR)
LOGGING = {
    'version': 1,  # 保留字
    'disable_existing_loggers': False,  # 禁用已经存在的logger实例
    # 日志文件格式
    'formatters': {
        # 详细的日志格式
        'standard': {
            'format': '[%(asctime)s]'
                      '[%(filename)s:%(lineno)d][%(levelname)s][%(message)s]'
        },
        # 简单的日志格式
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d][%(message)s]'
        },
        # 定义一个特殊的日志格式
        'collect': {
            'format': '%(message)s'
        }
    },

    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },

    # 处理器
    'handlers': {
        # '在终端打印'
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],   # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 默认的
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, 'gi_info.log'),
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8'
        },

        # 专门用来记录错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, 'gi_error.log'),
            'maxBytes': 1024*1024*50,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8'
        },
        # 专门处理收集特定信息的日志
        'collect': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, 'gi_collect.log'),
            'maxBytes': 1025*1024*50,
            'backupCount': 3,
            'formatter': 'collect',
            'encoding': 'utf-8'
        }
    },
    'loggers':{
        # 默认的logger应用配置
        '': {
            'handlers': ['default', 'error'],  # 上线后可以把console移除
            'level': 'DEBUG',
            'propagate': True,  # 向不向最高级别的logger传递
        },
        # 名为'collect'的logger单独处理
        'collect': {
            'handlers': ['console', 'collect'],
            'level': 'INFO'
        }
    }
}


# redis config

# celery中间人
BROKER_URL = 'redis://localhost:6379/0'

# celery结果返回，可用于跟踪结果
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# celery内容的消息的格式设置

CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# celery时区设置， 使用settings中的TIME_ZONE同样的时区
CELERY_TIMEZONE = TIME_ZONE


