#!/bin/bash/
.DEFAULT_GOAL: help

VIRTUALENVDIR := env
ACTIVATE := . $(VIRTUALENVDIR)/bin/activate
VIRTUALENV := virtualenv
MANAGE := ./manage.py


.PHONY: help
help:
	@echo "Please use \ 'make <target>' where <target> is one of"
	@echo "<base_command> build virtualenv, install requirements and conf nginx, uwsgi"
	@echo "<runserver> it will activate vitualenv and runserver"
	@echo "<runglobal> you can use it when you runserver on webserver "
	@echo "<check_mig> will do makemigrations and migrate"


.PHONY: runserver
runserver:
	$(ACTIVATE); \
	./manage.py runserver; \

.PHONY: runglobal
runglobal:
	$(ACTIVATE); \
	gunicorn glotechsol.wsgi:application -b 127.0.0.1:8000

.PHONY: check_mig
check_mig:
	./manage.py makemigratins; \
	./manage.py migrate; \

.PHONY: base_commad
base_command:
	$(VIRTUALENV) -p python3  env --no-site-packages; \
	$(ACTIVATE); \
	pip install -r requirements.txt; \
	chmod +x manage.py; \
	$(MANAGE) migrate; \
	$(MANAGE) runserver; \
