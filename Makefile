.PHONY: help install install-docs setup-hooks test lint format type-check clean build docs docs-linkcheck

# Sphinx documentation variables
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs/sphinx
BUILDDIR      = docs/sphinx/_build

help:
	@echo "Available commands:"
	@echo "  install         Install package and dev dependencies"
	@echo "  install-docs    Install documentation dependencies"
	@echo "  setup-hooks     Configure git to use .githooks directory"
	@echo "  test            Run tests with coverage"
	@echo "  lint            Run linters (flake8)"
	@echo "  format          Format code (black, isort)"
	@echo "  type-check      Run type checker (mypy)"
	@echo "  docs            Build documentation"
	@echo "  docs-linkcheck  Check documentation for broken links"
	@echo "  clean           Remove all build and documentation artifacts"
	@echo "  build           Build distribution packages"

install:
	pip install -e ".[dev]"

install-docs:
	pip install -e ".[docs]"

setup-hooks:
	git config core.hooksPath .githooks
	@echo "Git hooks configured! Hooks in .githooks/ will now run automatically."

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
	@$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

build: clean
	python -m build

docs:
	@echo "Building documentation..."
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
	@echo "Documentation built! Open docs/sphinx/_build/html/index.html"

docs-linkcheck:
	@echo "Checking documentation for broken links..."
	@$(SPHINXBUILD) -M linkcheck "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
