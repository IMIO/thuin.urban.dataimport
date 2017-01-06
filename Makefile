#!/usr/bin/make
#
all: run

.PHONY: bootstrap buildout run test cleanall
bootstrap:
	virtualenv-2.7 .
	./bin/easy_install -U setuptools==28.2.0
	./bin/python bootstrap.py -v 2.5.3

buildout:
	if ! test -f bin/buildout;then make bootstrap;fi
	bin/buildout -Nt 5

run:
	if ! test -f bin/instance;then make buildout;fi
	bin/instance fg

test:
	if ! test -f bin/test;then make buildout;fi
	rm -fr htmlcov
	bin/coverage.sh

cleanall:
	rm -fr bin develop-eggs htmlcov include .installed.cfg lib .mr.developer.cfg parts downloads eggs
