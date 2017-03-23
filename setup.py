#!/usr/bin/env python

import pagination_bootstrap

import os
import codecs
import uuid
from pip.req import parse_requirements
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


def get_requirements(source):

    try:
        install_reqs = parse_requirements(source, session=uuid.uuid1())
    except TypeError:
        # Older version of pip.
        install_reqs = parse_requirements(source)
    required = set([str(ir.req) for ir in install_reqs])
    return required


with open('README.rst', 'rb') as readme:
    readme_text = readme.read().decode('utf-8')


setup(
    name='django-pagination-bootstrap',
    version=pagination_bootstrap.__version__,
    maintainer='Thiago Carvalho D Avila',
    maintainer_email='thiagocavila@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/staticdev/django-pagination-bootstrap',
    license='LICENSE',
    description="Easy add pagination in Django, using Bootstrap's layout.",
    long_description=readme_text,
    keywords='django, bootstrap, pagination',
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: JavaScript",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
