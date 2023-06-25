import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-2#h&8pu^z&qo=3p!7a2k#x9ob1s#4=8p*ihocgsy%i+vzu72^#')

DEBUG = bool(os.getenv('DJANGO_DEBUG', 0))

ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '0.0.0.0').split(' ')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'storages',
    'django.contrib.humanize',
    'users',
    'note',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
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


DATABASES = {
    'default': {
        'ENGINE': f'django.db.backends.{os.getenv("DB_BACKEND")}',
        'HOST': os.getenv('DB_HOST'),
        'PORT': int(os.getenv('DB_PORT')),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'OPTIONS': {
            'sslmode': 'require',
        }
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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'vol' / 'static'

MEDIA_ROOT = BASE_DIR / 'vol' / 'media'
MEDIA_URL = '/media/'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True


# Azure Storage
STORAGES = {
    "default": {"BACKEND": "storages.backends.azure_storage.AzureStorage"},
    "staticfiles": {"BACKEND": "storages.backends.azure_storage.AzureStorage"},
}

AZURE_ACCOUNT_NAME = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
AZURE_CONNECTION_STRING = os.getenv("AZURE_CONNECTION_STRING")
AZURE_ACCOUNT_KEY = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
AZURE_CONTAINER = os.getenv("AZURE_CONTAINER_NAME")


CSRF_TRUSTED_ORIGINS = [f"https://{os.getenv('WEBSITE_HOSTNAME')}"]