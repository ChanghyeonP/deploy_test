import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@1lo*@^rb7!gzisk+end#+)@rp9s%p4ozvjvm$6#ed-^&93fnl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['nurigo.site', 'www.nurigo.site']

CSRF_TRUSTED_ORIGINS = ['https://nurigo.site', 'http://nurigo.site']

# HTTPS를 사용하는 경우에만 설정
CSRF_COOKIE_SECURE = True  # HTTPS를 사용하는 경우 True
SESSION_COOKIE_SECURE = True  # HTTPS를 사용하는 경우 True

# CSRF 쿠키 관련 추가 설정
CSRF_COOKIE_HTTPONLY = True  # CSRF 쿠키는 JavaScript에서 접근 불가
CSRF_USE_SESSIONS = True  # 세션을 사용한 CSRF 검증 비활성화

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'detail_page',
    'account',
    'channels',
]

ASGI_APPLICATION = 'myproject.asgi.application'

# Channels 설정
CHANNEL_LAYERS = {
    'default': {
	'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
   	 },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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
		'django.template.context_processors.csrf',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'account',
        'USER': 'chang',
        'PASSWORD': 'Rkswl159!',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

#DATABASES['mongodb'] = {
#    'ENGINE': 'djongo',
#    'NAME': 'your_mongodb_name',
#    'ENFORCE_SCHEMA': False,
#    'CLIENT': {
#        'host': 'your_mongodb_host',
#        'port': 27017,
#        'username': 'your_mongodb_user',
#        'password': 'your_mongodb_password',
#        'authSource': 'admin',
#        'authMechanism': 'SCRAM-SHA-1',
#    },
#}

AUTH_USER_MODEL = 'account.CustomUser'


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
