"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

# flake8: off
from pathlib import Path
from django.utils.translation import gettext_lazy as _

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [".vercel.app", ".now.sh"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "shop.apps.ShopConfig",
    "cart.apps.CartConfig",
    "orders.apps.OrdersConfig",
    "payment.apps.PaymentConfig",
    "coupons.apps.CouponsConfig",
    "rosetta",
    "parler",
    "localflavor",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myshop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "myshop.wsgi.app"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "verceldb",
        "USER": "default",
        "PASSWORD": "qVCN4jf2xTBU",
        "HOST": "ep-odd-sound-a48au2ec-pooler.us-east-1.aws.neon.tech",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en"

LANGUAGES = [("en", _("English")), ("es", _("Spanish"))]

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"


CART_SESSION_ID = "cart"

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# # Настроечные параметры Stripe
# STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY")
# STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
# # Секретный ключ
# STRIPE_API_VERSION = os.environ.get("STRIPE_API_VERSION")
# STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET")

STRIPE_PUBLISHABLE_KEY = "pk_test_51NGONAKmP5dRHdeh964H8d70iOYbVEn5ukMnbs0HdwCSkD59ZzwplXBsXvTRa4kWx0GiNePT0gwaGkMlRWUFVb3C00twXVZ9GJ"
STRIPE_SECRET_KEY = "sk_test_51NGONAKmP5dRHdehxfUtMw7q595dCkVw9bKCN3uG1YrFbC8GAvJ8qmBpaLJyZsLgTThae8qYwB1lOy4huI49cAsP0044mmpRzZ"
STRIPE_API_VERSION = "2022-08-01"
SECRET_KEY = "django-insecure-urzwkpumet#ali!ybcdwi_#p-0g6ay2bk069uqg-+4=59=y5g&"
STRIPE_WEBHOOK_SECRET = "whsec_b34a7dd28ccf3b47d441415e5c22125ba60b1519307eef388ea8e79f63244954"


REDIS_HOST = "upright-colt-51668.upstash.io"
REDIS_PORT = 6379
REDIS_DB = 1


PARLER_LANGUAGES = {
    None: (
        {"code": "en"},
        {"code": "es"},
    ),
    "default": {
        "fallback": "en",
        "hide_untranslated": False,
    },
}
