# python-outbrain [![Build Status](https://travis-ci.org/bpmason1/python-outbrain.svg?branch=master)](https://travis-ci.org/bpmason1/python-outbrain)

Python wrapper for Outbrain Amplify API

## install

In production environments run `make install`.
For development run `make install-dev`.
The dev install includes everything in the production install as well as libraries for linting and unittesting

Copy over yaml file for outbrain credentials
`cp outbrain.yml.example outbrain.yml`

Edit usename and password (note that this is the outbrain username and not the user email).

## linting
`make lint`

## testing
`make test`

## usage
```python
outbrain = OutbrainAmplifyApi()
for marketer_id in outbrain.get_marketer_ids():
    marketer = outbrain.get_marketer(marketer_id)

campaigns = outbrain.get_campaigns()
```
