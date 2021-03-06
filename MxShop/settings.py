"""
Django settings for MxShop project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR,'apps'))
sys.path.insert(0, os.path.join(BASE_DIR,'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+9&$3sdan^d=ash6v1f-kk$*ql%dx+&$h0h=4e7(d4x@67*tjl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# 自定义User
AUTH_USER_MODEL = 'users.UserProfile'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DjangoUeditor',
    'users.apps.UsersConfig',
    'goods.apps.GoodsConfig',
    'trade.apps.TradeConfig',
    'useroperation.apps.UseroperationConfig',
    'crispy_forms', # xadmin需要
    'xadmin',
    'django_filters',
    'rest_framework',
    'corsheaders', # 跨域
    'rest_framework.authtoken', # token验证,记得migrate
    'social_django',  # 第三方登录,记得migrate
    'raven.contrib.django.raven_compat',  # sentry
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 放在CsrfViewMiddleware之前
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True # 允许所有跨域请求

ROOT_URLCONF = 'MxShop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 第三方登录
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'MxShop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mxshop',
        'USER': 'root',
        'PASSWORD': 'basketBALL91',
        'HOST': '123.206.229.93',
        # 'HOST': '127.0.0.1',
        'OPTIONS': { 'init_command':'SET default_storage_engine=INNODB;'}
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

AUTHENTICATION_BACKENDS = (
    'users.views.CustomAuth',

    # 第三方登陆认证
    'social_core.backends.weibo.WeiboOAuth2',
    'social_core.backends.weixin.WeixinOAuth2',
    'social_core.backends.qq.QQOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)
# 自定义认证函数

# rest-framework配置
REST_FRAMEWORK = {
    # DEFAULT_PERMISSION_CLASSES表示所有api都需要登陆才能使用
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    # 验证用户
    # 多种验证方式可以共存
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication', # 用户名密码认证（需要用户名密码）
        'rest_framework.authentication.SessionAuthentication',  # session认证（需要sessionid）
        # 'rest_framework.authentication.TokenAuthentication',  # 验证request中的token并获取相应用户
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # json web token方式获取用户
    ),
    # 限速类（设置在settings是全局，可单独设置在viewset中）
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle', # 未登录（通过ip判断）
        'rest_framework.throttling.UserRateThrottle' # 已登录（通过token判断）
    ),
    # 限制速率（day，hour，minute）
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/minute',
        'user': '5/minute'
    }
}


# JWT设置
# http://getblimp.github.io/django-rest-framework-jwt/

import datetime
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7), # 过期时间
    'JWT_AUTH_HEADER_PREFIX': 'JWT', # header的值对应的前缀
}

# 手机号码验证
MOBILE_REGEX = '^(13[0-9]|15[0-9]|17[0-9]|18[0-9]|14[0-9])[0-9]{8}$'

# 云片网APIKEY
APIKEY = '93af765b45a8d5cd804c6c83e1150fcc'

# 支付宝key
alipay_private_key = os.path.join(BASE_DIR,'apps/trade/keys/private_2048.txt')
alipay_pub_key = os.path.join(BASE_DIR,'apps/trade/keys/alipay_key_2048.txt')

# rest_framework_extensions缓存时间设置（秒）
REST_FRAMEWORK_EXTENSIONS = {
    # 'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60 * 15
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 60
}

# 配置缓存系统为redis缓存（django默认使用内存做缓存）
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }

# 第三方登录
SOCIAL_AUTH_WEIBO_KEY = '3366751802'
SOCIAL_AUTH_WEIBO_SECRET = 'fb16ae76810aad7452f4aba8cfe8db08'
SOCIAL_AUTH_QQ_KEY = 'foobar'
SOCIAL_AUTH_QQ_SECRET = 'bazqux'
SOCIAL_AUTH_WEIXIN_KEY = 'foobar'
SOCIAL_AUTH_WEIXIN_SECRET = 'bazqux'
# 登录后的跳转页面
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index/'

import raven
# sentry设置
RAVEN_CONFIG = {
    'dsn': "http://8d8598f5461949bdb8e113eab19344c9:f089949a985f472d87d9ac491bc6d8aa@120.79.48.216:9000//7",
}