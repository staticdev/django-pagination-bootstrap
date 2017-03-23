#!/usr/bin/env python

import sys
import os
import django
from django.conf import settings


APP_NAME = 'pagination_bootstrap'

if django.VERSION < (1, 8):
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        USE_TZ=True,
        ROOT_URLCONF='{0}.tests'.format(APP_NAME),
        MIDDLEWARE_CLASSES=(
            'pagination_bootstrap.middleware.PaginationMiddleware',
        ),
        SITE_ID=1,
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.admin',
            'django.contrib.sites',
            APP_NAME,
        ),
        TEMPLATE_CONTEXT_PROCESSORS = (
            "django.contrib.auth.context_processors.auth",
            "django.core.context_processors.debug",
            "django.core.context_processors.i18n",
            "django.core.context_processors.media",
            "django.core.context_processors.request",
        ),
    )
else:
    settings.configure(
        DEBUG=True,
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        USE_TZ=True,
        ROOT_URLCONF='{0}.tests'.format(APP_NAME),
        MIDDLEWARE=[
            'pagination_bootstrap.middleware.PaginationMiddleware',
        ],
        SITE_ID=1,
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.admin',
            'django.contrib.sites',
            APP_NAME,
        ),
        TEMPLATES = [
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [
                    os.path.join(os.path.dirname(__file__), "templates"),
                ],
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
            },
        ]
    )

from django.test.utils import get_runner

if hasattr(django, 'setup'):
    django.setup()
TestRunner = get_runner(settings)
test_runner = TestRunner()
failures = test_runner.run_tests([APP_NAME])
if failures:
    sys.exit(failures)
