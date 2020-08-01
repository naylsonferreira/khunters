from decouple import config as get_env
from django.conf import settings
import os

SECRET_KEY = get_env('SECRET_KEY')
DEBUG = get_env('DEBUG')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_env('K_NAME'),
        'USER': get_env('K_USER'),
        'PASSWORD': get_env('K_PASSWORD'),
        'HOST': get_env('K_HOST'),
        'PORT': '5432',
    }
}

settings.INSTALLED_APPS.append('corsheaders')
settings.INSTALLED_APPS.append('rest_framework')
settings.INSTALLED_APPS.append('rest_framework.authtoken')
settings.INSTALLED_APPS.append('core.apps.CoreConfig')

settings.MIDDLEWARE.append('core.middleware.core_middleware')
DEFAULT_APP = 'website_app'
DEFAULT_APP_LABEL = 'Khunters'
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
ALLOWED_HOSTS = ['*']
ADMINS = [('Naylson Ferreira', 'naylsonfsa@gmail.com')]
EMAIL_HOST_USER = 'naylsonfsa@gmail.com'
EMAIL_HOST = get_env('EMAIL_HOST')
EMAIL_HOST_PASSWORD = get_env('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = get_env('EMAIL_HOST_USER')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'contato.overloadlab@gmail.com'
LOGIN_URL = get_env('LOGIN_URL')
LOGIN_REDIRECT_URL = '/'
if DEBUG:
    STATICFILES_DIRS = [os.path.join(settings.BASE_DIR, "static")]
else:
    STATIC_URL = get_env('STATIC_URL')
    STATIC_ROOT = get_env('STATIC_ROOT')
MEDIA_URL = get_env('MEDIA_URL')
MEDIA_ROOT = os.path.join(settings.BASE_DIR, get_env('MEDIA_ROOT'))
FTP_STORAGE_LOCATION = get_env('FTP_STORAGE_LOCATION')
CORS_ORIGIN_ALLOW_ALL = True

from corsheaders.defaults import default_headers
CORS_ALLOW_HEADERS = list(default_headers) + [
    'access-control-allow-origin',
    'access-control-allow-headers',
]
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}