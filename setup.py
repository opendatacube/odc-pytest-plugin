#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-odc',
    version='0.1.0',
    author='Damien Ayers',
    author_email='damien@omad.net',
    maintainer='Damien Ayers',
    maintainer_email='damien@omad.net',
    license='Apache Software License 2.0',
    url='https://github.com/opendatacube/pytest-odc',
    description='A pytest plugin for simplifying ODC database tests',
    long_description=read('README.md'),
    packages=['odc.testing'],
    python_requires='>=3.5',
    install_requires=['pytest>=3.5.0', 'docker'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'pytest11': [
            'odc-pytest-database = odc.testing.database',
        ],
    },
)
