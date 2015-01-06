#!/usr/bin/env python

from distutils.core import setup
version = '0.0.1'

setup(
    name='outbrain',
    version=version,
    packages=['outbrain'],
    description='Wrapper for the Outbrain Amplify API',
    url='https://github.com/andessen/python_outbrain',
    license='LGPL 2.1 or later',
    long_description=\
    """
    Python wrapper to allow easier access to Outbrain's Apmlify API.
    """,
)
