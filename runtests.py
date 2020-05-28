#!/usr/bin/env python
"""Test run script."""
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner


sys.path.insert(0, "tests")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testapp.settings")
APP_NAME = "django_pagination_bootstrap"

django.setup()
TestRunner = get_runner(settings)
test_runner = TestRunner()
failures = test_runner.run_tests([APP_NAME])
if failures:
    sys.exit(failures)
