.PHONY: help install install-docs setup-hooks test lint format type-check clean build docs docs-linkcheck check

# Sphinx documentation variables
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = docs/sphinx
BUILDDIR      = docs/sphinx/_build

help:
	@echo "Available commands:"
	@echo "  install         Install package and dev dependencies with uv"
	@echo "  install-docs    Install documentation dependencies with uv"
	@echo "  setup-hooks     Configure git to use .githooks directory"
	@echo "  test            Run tests with coverage"
	@echo "  lint            Run linter (ruff check)"
	@echo "  format          Format code (ruff format)"
	@echo "  type-check      Run type checker (ty)"
	@echo "  check           Run all checks (lint, format --check, type-check)"
	@echo "  docs            Build documentation"
	@echo "  docs-linkcheck  Check documentation for broken links"
	@echo "  clean           Remove all build and documentation artifacts"
	@echo "  build           Build distribution packages"

install:
	uv sync --extra dev

install-docs:
	uv sync --extra docs

setup-hooks:
	git config core.hooksPath .githooks
	@echo "Git hooks configured! Hooks in .githooks/ will now run automatically."

test:
	uv run pytest

lint:
	uv run ruff check persian tests

format:
	uv run ruff format persian tests
	uv run ruff check --fix persian tests

type-check:
	uv run ty check persian

check: lint type-check
	uv run ruff format --check persian tests

clean:
	rm -rf build dist *.egg-info
	rm -rf .pytest_cache .ruff_cache .coverage htmlcov coverage.xml
	rm -rf $(BUILDDIR)
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name ".DS_Store" -delete 2>/dev/null || true

build: clean
	uv build

docs:
	@echo "Building documentation..."
	@uv run $(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
	@echo "Documentation built! Open docs/sphinx/_build/html/index.html"

docs-linkcheck:
	@echo "Checking documentation for broken links..."
	@uv run $(SPHINXBUILD) -M linkcheck "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
