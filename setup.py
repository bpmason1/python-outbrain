try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os

with open('requirements.txt') as f:
    PACKAGE_INSTALL_REQUIRES = [line[:-1] for line in f]

with open('README.md') as file:
    PACKAGE_LONG_DESCRIPTION = file.read()

setup(
    name='outbrain',
    version='0.0.2',
    author='Alan Anders',
    author_email='aanders@simplereach.com',
    url='https://github.com/andessen/python-outbrain',
    packages=['outbrain'],
    license='LGPL 2.1 or later',
    description='Wrapper for the Outbrain Amplify API',
    long_description=PACKAGE_LONG_DESCRIPTION,
    install_requires=PACKAGE_INSTALL_REQUIRES,
)
