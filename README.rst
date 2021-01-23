Django Pagination Bootstrap
===========================

**MAINTAINER NEEDED: this project is complete but won't be updated until further notice. If you have interest in improving it, please contact me by creating an** `issue here`_ **.**

.. badges-begin

|PyPI| |Python Version| |License|

|Tests| |Codecov|

|Black| |pre-commit|

.. |PyPi| image:: https://badge.fury.io/py/django-pagination-bootstrap.svg
   :target: https://badge.fury.io/py/django-pagination-bootstrap
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/django-pagination-bootstrap
   :target: https://pypi.org/project/django-pagination-bootstrap
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/django-pagination-bootstrap
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Tests| image:: https://github.com/staticdev/django-pagination-bootstrap/workflows/Tests/badge.svg
   :target: https://github.com/staticdev/django-pagination-bootstrap/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/staticdev/django-pagination-bootstrap/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/staticdev/django-pagination-bootstrap
   :alt: Codecov
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

Django-pagination-bootstrap is an app to easy add pagination in Django_, using `Bootstrap`_'s layout.

Note: This library currently works with Python 3.6+, Django 2.0+ and Bootstrap 3+. For older versions, please use version 1.3.0.

Installation
------------

To install ``django-pagination-bootstrap`` simply run:

.. code:: console

   pip install django-pagination-bootstrap

Configuration
-------------

We need to hook ``django-pagination-bootstrap`` into our project.

1. Put ``django-pagination-bootstrap`` into your ``INSTALLED_APPS`` at settings module:

.. code-block:: python

   INSTALLED_APPS = (
       # other apps
       "django_pagination_bootstrap",
   )

2. Install the pagination middleware. Your settings file might look something like:

.. code-block:: python

   MIDDLEWARE_CLASSES = (
       # other middleware
       "django_pagination_bootstrap.middleware.PaginationMiddleware",
   )

3. Guarantee you have ``django.template.context_processors.request`` on settings.py:

.. code-block:: python

   TEMPLATES = [
       {
           # ...
           "OPTIONS": {
               "context_processors": [
                   # ...
                   "django.template.context_processors.request"
                   # ...
               ],
           },
       },
   ]

4. Add this line at the top of your template to load the pagination tags:

.. code-block:: python

   {% load pagination_tags %}

5. Decide on a variable that you would like to paginate, and use the autopaginate tag on that variable before iterating over it. This could take one of two forms (using the canonical object_list as an example variable):

.. code-block:: python

   {% autopaginate object_list %}


This assumes that you would like to have the default 20 results per page. If you would like to specify your own amount of results per page, you can specify that like so:

.. code-block:: python

   {% autopaginate object_list 10 %}

Note that this replaces object_list with the list for the current page, so you can iterate over the object_list like you normally would.

6. Now you want to display the current page and the available pages, so somewhere after having used autopaginate. If you are using Bootstrap 3, use the paginate inclusion tag:

.. code-block:: python

   {% paginate %}

This does not take any arguments, but does assume that you have already called autopaginate, so make sure to do so first.

That's it! You have now paginated object_list and given users of the site a way to navigate between the different pages--all without touching your views.

Side effects
------------

A django-paginator_ instance will be injected in the template context as ``paginator``. You can access it as usual:

.. code-block:: python

   page {{ page }} of {{ paginator.num_pages }}

Optional Settings
-----------------

In django-pagination, there are no required settings. There are, however, a small set of optional settings useful for changing the default behavior of the pagination tags. Here's an overview:

* PAGINATION_DEFAULT_PAGINATION

The default amount of items to show on a page if no number is specified.

* PAGINATION_DEFAULT_WINDOW

The number of items to the left and to the right of the current page to display (accounting for ellipses).

* PAGINATION_DEFAULT_ORPHANS

The number of orphans allowed. According to the Django documentation, orphans are defined as:

   The minimum number of items allowed on the last page, defaults to zero.

* PAGINATION_INVALID_PAGE_RAISES_404

Determines whether an invalid page raises an Http404 or just sets the invalid_page context variable.  True does the former and False does the latter.

Credits
-------

This is based on Eric Florenzano's django-pagination 1.0.7 and is an updated version of https://github.com/tgdn/django-bootstrap-pagination for Django 1.7 or higher.

.. _issue here: https://github.com/staticdev/staticdev/issues
.. _Django: https://www.djangoproject.com/
.. _Bootstrap: http://getbootstrap.com/
.. _django-pagination: https://pypi.python.org/pypi/django-pagination
.. _django-paginator: https://docs.djangoproject.com/en/dev/topics/pagination/#paginator-objects
