#!/usr/bin/env python
# from distutils.core import setup
from setuptools import setup

with open("README.rst", "rt") as f:
    DESCRIPTION = f.read()

url = 'https://github.com/carlok/fss3wrap'
version='0.1.21'

setup(
  name = 'fss3wrap',
  packages = ['fss3wrap'],
  version = version,
  license='MIT',
  description = 'A python class to wrap fs and fs-s3fs (WIP)',
  long_description = DESCRIPTION,
  author = 'Carlo Perassi',
  author_email = 'carlo.perassi@kiwifarm.it',
  url = url,
  download_url = url + '/archive/v_' + version + '.tar.gz',
  keywords = ['fs', 's3', 'wrapper'],
  install_requires=[
      'fs',
      'fs-s3fs-ng'
  ],
  classifiers=[
    'Development Status :: 3 - Alpha',  # "3 - Alpha", "4 - Beta", "5 - Production/Stable"
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
  ],
)
