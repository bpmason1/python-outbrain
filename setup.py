try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os

setup(
    name='outbrain',
    version='0.0.6',
    author='Brian Mason',
    author_email='bmsaon@simplereach.com',
    url='https://github.com/andessen/python-outbrain',
    packages=['outbrain'],
    license='LGPL 2.1 or later',
    description='Wrapper for the Outbrain Amplify API',
    install_requires=[
        'python-dateutil >= 2.1',
        'requests >= 2.4.3',
        'pyyaml >= 3.10',
        'simplejson >= 3.1.0',
    ],
    keywords=['outbrain','api', 'amplify'],
    classifiers=['Intended Audience :: Developers']
)
