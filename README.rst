python-outbrain |build-status|
===============

Python wrapper for Outbrain Amplify API


Copy over yaml file for outbrain credentials

  cp outbrain.yml.example outbrain.yml

Edit usename and password (note that this is the outbrain username and not the user email).

.. |build-status| image:: https://travis-ci.org/bpmason1/python-outbrain.svg?branch=master
   :target: https://travis-ci.org/bpmason1/python-outbrain
   :alt: Build status


linting
===============
At present, the module complies with all pep8 style rules except limiting lines to 80 characters.
Eventually I will try to figure out how to change the limit from 80 to 110 characters but
for now I simply ignore the check.  Use the following command to lint your code.
  pep8 --ignore=E501 outbrain/__init__.py
