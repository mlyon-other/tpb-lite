#!/usr/bin/env python3

from setuptools import setup
from os import path

this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = '0.3.0'

setup(name = 'tpblite',
        version = version,
        description = 'The Unofficial Pirate Bay Lightweight Python API',
        author = 'Matt Lyon',
        author_email = 'matthewlyon18@gmail.com',
        python_requires = '>=3.6',
        url = 'https://github.com/mattlyon93/tpb-lite',
        download_url = 'https://github.com/mattlyon93/tpb-lite/archive/v{}.tar.gz'.format(version),
        long_description = long_description,
        long_description_content_type='text/markdown',
        license = 'MIT License',
        packages = ['tpblite', 'tpblite/models'],
        install_requires = [
            'beautifulsoup4',
            'purl'],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python',
            'Operating System :: Unix',
            'Operating System :: MacOS',
            'Topic :: Internet :: WWW/HTTP :: Browsers',
            'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
            'Topic :: Utilities'],
        keywords = ['ThePirateBay', 'PirateBay', 'torrent']
    )