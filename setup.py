from __future__ import unicode_literals

import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename) as fh:
        metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", fh.read()))
        return metadata['version']


setup(
    name='Mopidy-Cur8',
    version=get_version('mopidy_cur8/__init__.py'),
    url='https://github.com/gersilex/mopidy-cur8',
    license='Apache License, Version 2.0',
    author='Leroy Foerster',
    author_email='gersilex@gmail.com',
    description='Mopidy extension for automatic playlist curation',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 1.0',
    ],
    entry_points={
        'mopidy.ext': [
            'cur8 = mopidy_cur8:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
