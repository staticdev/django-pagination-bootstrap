#!/usr/bin/env python
"""Test run script."""
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

APP_NAME = "django_pagination_bootstrap"

# set TEMPLATE_CONTEXT_PROCESSORS or TEMPLATES, based on django version
# http://stackoverflow.com/a/16805125/4126114
settings.configure(
    DEBUG=True,
    DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3"}},
    USE_TZ=True,
    MIDDLEWARE=["pagination_bootstrap.middleware.PaginationMiddleware"],
    SITE_ID=1,
    INSTALLED_APPS=(
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.sites",
        APP_NAME,
    ),
    TEMPLATES=[
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
    ],
)

django.setup()
TestRunner = get_runner(settings)
test_runner = TestRunner()
failures = test_runner.run_tests([APP_NAME])
if failures:
    sys.exit(failures)
