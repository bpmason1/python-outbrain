export NOSE_INIT_MODULE=tests.nose_init
export PYTHONPATH=.
export TZ=UTC

build:
	$(NOOP)

test:
	nosetests ./test -v

lint:
	pep8 outbrain --ignore=E123,E126,E128,E265,E501

clean:
	python setup.py clean
	find . -name '*.py[cox]' -delete
	rm -rf build/ dist/ *outbrain.egg-info

.PHONY:	test lint clean
