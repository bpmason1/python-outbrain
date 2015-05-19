try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='outbrain',
    version='0.0.10',
    author='Brian Mason',
    author_email='bmsaon@simplereach.com',
    url='https://github.com/bmason/python-outbrain',
    packages=['outbrain'],
    license='LGPL 2.1 or later',
    description='Wrapper for the Outbrain Amplify API',
    install_requires=[
        'pytz >= 2013.6',
        'pyyaml >= 3.10',
        'requests >= 2.4.3',
        'simplejson >= 3.1.0',
    ],
    keywords=['outbrain','api', 'amplify'],
    classifiers=['Intended Audience :: Developers']
)
