try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os

this_dir = os.path.dirname(__file__)
readme_filename = os.path.join(this_dir, 'README.md')
requirements_filename = os.path.join(this_dir, 'requirements.txt')

PACKAGE_NAME = 'python-outbrain'
PACKAGE_VERSION = '0.0.1'
PACKAGE_AUTHOR = 'Alan Anders'
PACKAGE_AUTHOR_EMAIL = ''
PACKAGE_URL = 'https://github.com/andessen/python-outbrain'
PACKAGES = ['outbrain']
PACKAGE_LICENSE = 'LGPL 2.1 or later'
PACKAGE_DESCRIPTION = 'Wrapper for the Outbrain Amplify API'

with open(readme_filename) as f:
    PACKAGE_LONG_DESCRIPTION = f.read()

with open(requirements_filename) as f:
    PACKAGE_INSTALL_REQUIRES = [line[:-1] for line in f]

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    author=PACKAGE_AUTHOR,
    author_email=PACKAGE_AUTHOR_EMAIL,
    url=PACKAGE_URL,
    packages=PACKAGES,
    license=PACKAGE_LICENSE,
    description=PACKAGE_DESCRIPTION,
    long_description=PACKAGE_LONG_DESCRIPTION,
    install_requires=PACKAGE_INSTALL_REQUIRES,
)
