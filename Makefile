VIRTUAL_ENV := venv
PYTHON_PATH := $(VIRTUAL_ENV)/bin/python

########################################################################################################################
# Stylify code
########################################################################################################################

.PHONY: lint
lint:
	$(PYTHON_PATH) -m pylint main.py --verbose --output-format=colorized
	$(PYTHON_PATH) -m pylint core --verbose --output-format=colorized

.PHONY: type
type:
	$(PYTHON_PATH) -m mypy main.py
	$(PYTHON_PATH) -m mypy core

.PHONY: flake8
flake8:
	$(PYTHON_PATH) -m flake8 main.py
	$(PYTHON_PATH) -m flake8 core

.PHONY: isort
isort:
	$(PYTHON_PATH) -m isort main.py
	$(PYTHON_PATH) -m isort core

.PHONY: style
style: isort lint type flake8
