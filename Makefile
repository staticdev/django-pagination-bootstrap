.PHONY: flake8 test coverage

flake8:
	flake8 debug_toolbar example tests

test:
	DJANGO_SETTINGS_MODULE=tests.settings \
		django-admin test tests

coverage:
	python --version
	coverage erase
	DJANGO_SETTINGS_MODULE=tests.settings \
		coverage run `which django-admin` test -v2 tests
	coverage report
	coverage html
