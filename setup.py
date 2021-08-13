#!/usr/bin/env python3

import os.path
from distutils.core import setup

exec(open('./eodapi/version.py').read())

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='eodapi',
      version=__version__,
      description='Wrapper for EOD stock API https://eodhistoricaldata.com',
      long_description=read('README.md'),
      author='Dennis Greguhn',
      author_email='',
      url=__url__,
      install_requires=[
          'requests>=2.18.2,<3'
      ],
      packages=['eodapi'],
      python_requires='>=3.6',
      classifiers=[
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
)
