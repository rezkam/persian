.PHONY: help install install-docs test lint format type-check clean build docs docs-clean

help:
	@echo "Available commands:"
	@echo "  install       Install package and dev dependencies"
	@echo "  install-docs  Install documentation dependencies"
	@echo "  test          Run tests with coverage"
	@echo "  lint          Run linters (flake8)"
	@echo "  format        Format code (black, isort)"
	@echo "  type-check    Run type checker (mypy)"
	@echo "  docs          Build documentation"
	@echo "  docs-clean    Clean documentation build artifacts"
	@echo "  clean         Remove build artifacts"
	@echo "  build         Build distribution packages"

install:
	pip install -e ".[dev]"

install-docs:
	pip install -e ".[docs]"

test:
	pytest

lint:
	flake8 persian tests

format:
	black persian tests
	isort persian tests

type-check:
	mypy persian

clean:
	rm -rf build dist *.egg-info
	rm -rf .pytest_cache .mypy_cache .coverage htmlcov
	rm -rf docs/sphinx/_build docs/sphinx/_static docs/sphinx/_templates
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name ".DS_Store" -delete

build: clean
	python -m build

docs:
	@echo "Building documentation..."
	cd docs/sphinx && $(MAKE) html
	@echo "Documentation built! Open docs/sphinx/_build/html/index.html"

docs-clean:
	cd docs/sphinx && $(MAKE) clean
