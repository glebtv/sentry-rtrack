#!/usr/bin/env python
"""
sentry-rtrack
=============

An extension for Sentry which integrates with Rtrack. Specifically, it allows
you to easily create issues from events within Sentry.

:copyright: (c) 2012 Pancentric Ltd, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


tests_require = [
    'nose',
]

install_requires = [
    'sentry>=7.0.0',
    'requests>=2.0',
]

setup(
    name='sentry-rtrack',
    version='0.1.0',
    author='glebtv',
    author_email='glebtv@gmail.com',
    url='http://github.com/glebtv/sentry-rtrack',
    description='A Sentry extension which integrates with Rtrack.',
    long_description=__doc__,
    license='BSD',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
    include_package_data=True,
    entry_points={
        'sentry.apps': [
            'rtrack = sentry_rtrack',
        ],
        'sentry.plugins': [
            'rtrack = sentry_rtrack.plugin:RtrackPlugin'
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)

