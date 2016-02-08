try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

INSTALL_REQUIRE = [
    'pytz >= 2013.6',
    'pyyaml >= 3.10',
    'requests >= 2.4.3',
    'simplejson >= 3.1.0',
]

TEST_REQUIRE = [
    'mock >= 1.0.1',
    'nose >= 1.3.6',
    'pep8 >= 1.6.2',
]

setup(
    name='outbrain',
    version='0.0.10',
    author='Brian Mason',
    author_email='bmason@simplereach.com',
    url='https://github.com/bmason/python-outbrain',
    packages=['outbrain'],
    license='LGPL 2.1 or later',
    description='Wrapper for the Outbrain Amplify API',
    install_requires=INSTALL_REQUIRE,
    tests_require=TEST_REQUIRE,
    keywords=['outbrain','api', 'amplify'],
    classifiers=['Intended Audience :: Developers']
)
