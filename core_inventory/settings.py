import os
from pathlib import Path
import core_inventory.db_config as db
from decouple import config
from core_inventory.jazzmin_settings import JAZZMIN_SETTINGS, JAZZMIN_UI_TWEAKS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Jazzmin config
JAZZMIN_SETTINGS
JAZZMIN_UI_TWEAKS

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','core-inventory.azurewebsites.net', 'coreinventory.software']
CSRF_TRUSTED_ORIGINS = ['https://*.core-inventory.azurewebsites.net']

AUTH_USER_MODEL = 'Users.User'

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'core_inventory.apps.CustomAdminConfig',
    'django.contrib.humanize',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'MyApps.Users',
    'MyApps.Orders',
    'MyApps.Products',
    'MyApps.Purchases',
    'MyApps.Sales',
    'MyApps.Carts',
    'MyApps.ShippingAddresses',
    'MyApps.Providers',
    'MyApps.PromoCodes',
    'MyApps.BillingProfiles',
    'MyApps.Charts' 
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]
ROOT_URLCONF = 'core_inventory.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'core_inventory.wsgi.application'


LOGOUT_REDIRECT_URL = 'login'

# Database
DATABASES = db.MYSQL

# Media Files
MEDIA_URL = 'media/'
MEDIAFILES_DIRS = (
    os.path.join(BASE_DIR,'media'),
)

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
LANGUAGE_CODE = 'es-co'
TIME_ZONE = 'America/Bogota'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Development
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR,'static'),
# )

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings
EMAIL_HOST = 'smtp.googlemail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
STRIPE_PUBLIC_KEY = 'pk_test_51M1Fq2BQSHmCnrdvv3HwVGsD7cN3GUIgOCVR8fJAVTOIDQ152dOefmyefjIPSpaD8A75B61hG8HyWjLBhxA4bNGG00PieTdNrc'
STRIPE_PRIVATE_KEY = config('STRIPE_PRIVATE_KEY')