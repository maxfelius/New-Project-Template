.PHONY: run test install-pre-commit

PYTHON ?= python3

run:
	@$(PYTHON) -m app.src.main

test:
	@$(PYTHON) -m pytest app/test/ -v

install-pre-commit:
	pre-commit install
