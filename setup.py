#!/usr/bin/env python

import pagination_bootstrap

import os
import codecs
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


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
    scripts=[],
    url='https://github.com/staticdev/django-pagination-bootstrap',
    license='LICENSE',
    description="Easy add pagination in Django, using Bootstrap's layout.",
    long_description=readme_text,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='django, bootstrap, pagination',
    install_requires=[
        "Django >= 1.4.0"
    ],
)
