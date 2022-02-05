.PHONY: help

help:
	@echo "Usage"
	@echo "~~~~~"
	@echo "install : Install requirements"
	@echo "lint    : Run pre-commit"
	@echo ""

install:
	@poetry install

lint:
	@poetry run pre-commit run -a
