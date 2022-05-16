define USAGE

TP Software Testing - GL4 2021/2022

Commands:
  init                           Initialize by installing required packages
  unit-tests                     Run unit tests
  integration-tests              Run integration tests
endef

export USAGE

SHELL := /bin/bash

help:
	@echo "$$USAGE"

init:
	python3 -m pip install -r requirements-dev.txt

.PHONY: unit-tests
unit-tests:
	python3 -m pytest -vvv --cov=app unit-tests

.PHONY: integration-tests
integration-tests:
	python3 -m pytest --cov=app integration-tests
