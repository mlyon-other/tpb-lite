#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='tpblite',
        version='0.1.0',
        description='The Unofficial Pirate Bay Lightweight Python API',
        author='Matt Lyon',
        author_email='matthewlyon18@gmail.com',
        python_requires='>=3.6',
        license='MIT License',
        packages=['tpblite', 'tpblite/models'],
        install_requires=[
            'beautifulsoup4',
            'purl',
        ],
        classifiers=[
            'Programming Language :: Python',
            'Operating System :: Unix',
            'Operating System :: MacOS'
        ],
    )