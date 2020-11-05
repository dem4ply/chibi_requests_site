#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "chibi-requests>=0.6.3"
]

setup(
    author="dem4ply",
    author_email='dem4ply@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="snippets para tropicalizar sitios web a objectos en python",
    install_requires=requirements,
    license="WTFPL",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='chibi_requests_site',
    name='chibi_requests_site',
    packages=find_packages(include=['chibi_requests_site', 'chibi_requests_site.*']),
    url='https://github.com/dem4ply/chibi_requests_site',
    version='0.0.1',
    zip_safe=False,
)
