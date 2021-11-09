from pathlib import Path
import os
# Added for Heroku start
import dj_database_url
# Added for Heroku end

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q9^csgn!9xwr%atn1r-t^%b$$xxw_!i=vs3oh!k28%ffe#)&jx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# Added for Heroku start
ALLOWED_HOSTS = ['fipsappheroku.herokuapp.com']
# Added for Heroku end

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ipitem.apps.IpitemConfig',
    'user.apps.UserConfig',
]

MIDDLEWARE = [
    # Added for Heroku start
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # Added for Heroku end
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fipsapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'fipsapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'ru-ru'#'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'alekxtt.django@gmail.com'
EMAIL_HOST_PASSWORD = 'ufqmlqcudncfedhj'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Added for Heroku start
PROJECT_ROOT   =   os.path.join(os.path.abspath(__file__))

STATIC_ROOT  =   os.path.join(PROJECT_ROOT, 'staticfiles')

# Added for Heroku end

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    # was changed for Heroku from BASE_DIR / 'static' to:
    os.path.join(PROJECT_ROOT, 'static'),
]

# Added for Heroku start
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# Added for Heroku end

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Added for Heroku start
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
# Added for Heroku end