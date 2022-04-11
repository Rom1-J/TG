VIRTUAL_ENV := venv
PYTHON_PATH := $(VIRTUAL_ENV)/bin/python

########################################################################################################################
# Stylify code
########################################################################################################################

.PHONY: lint
lint:
	$(PYTHON_PATH) -m pylint core --verbose --output-format=colorized

.PHONY: type
type:
	$(PYTHON_PATH) -m mypy core

.PHONY: flake8
flake8:
	$(PYTHON_PATH) -m flake8 core

.PHONY: isort
isort:
	$(PYTHON_PATH) -m isort core

.PHONY: style
style: isort lint type flake8
