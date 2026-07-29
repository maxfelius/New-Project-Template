.PHONY: run test

PYTHON ?= python3

run:
	@$(PYTHON) -m app.src.main

test:
	@$(PYTHON) -m pytest app/test/ -v
