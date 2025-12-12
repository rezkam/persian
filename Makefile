.PHONY: help install test lint format type-check clean build

help:
	@echo "Available commands:"
	@echo "  install      Install package and dev dependencies"
	@echo "  test         Run tests with coverage"
	@echo "  lint         Run linters (flake8)"
	@echo "  format       Format code (black, isort)"
	@echo "  type-check   Run type checker (mypy)"
	@echo "  clean        Remove build artifacts"
	@echo "  build        Build distribution packages"

install:
	pip install -e ".[dev]"

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
	find . -type d -name __pycache__ -exec rm -rf {} +

build: clean
	python -m build
