"""Django test settings."""
import os

SECRET_KEY = "$%ffv#zpca%a#bdxtl&)&=5k20egnwcwjdg665r-lsr+s5zdw#"  # nosec

APP_NAME = "django_pagination_bootstrap"

DEBUG = True

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

USE_TZ = True

MIDDLEWARE = ["pagination_bootstrap.middleware.PaginationMiddleware"]

SITE_ID = 1

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    APP_NAME,
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(os.path.dirname(__file__), "templates")],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    }
]
