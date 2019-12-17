#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name = 'tpblite',
        version = '0.2.2',
        description = 'The Unofficial Pirate Bay Lightweight Python API',
        author = 'Matt Lyon',
        author_email = 'matthewlyon18@gmail.com',
        python_requires = '>=3.6',
        url = 'https://github.com/mattlyon93/tpb-lite',
        download_url = 'https://github.com/mattlyon93/tpb-lite/archive/v0.2.2.tar.gz',
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