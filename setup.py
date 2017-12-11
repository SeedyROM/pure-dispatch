#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of pure-dispatch.
# https://github.com/someuser/somepackage

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Zack Kollar <zackkollar@gmail.com>

from setuptools import setup, find_packages
from pure_dispatch import __version__

TESTS_REQUIRE = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
    'pylint'
]

setup(
    name='pure-dispatch',
    version=__version__,
    description='an incredible python package',
    long_description='''
an incredible python package
''',
    keywords='',
    author='Zack Kollar',
    author_email='zackkollar@gmail.com',
    url='https://github.com/someuser/somepackage',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'aiohttp',
        'sqlalchemy',
    ],
    extras_require={
        'tests': TESTS_REQUIRE,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'pure-dispatch=pure_dispatch.cli:main',
        ],
    },
)
