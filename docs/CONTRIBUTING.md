# Contributing

Thank you for helping improve the Persian language tools! This document summarizes
how to get started and the quality expectations for contributions.

## Development Environment

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   make install
   ```
3. Run the full suite before sending a pull request:
   ```bash
   make format lint type-check test
   ```

## Coding Standards

- Follow PEP 8/PEP 257 and keep lines ≤ 100 characters.
- Use type hints everywhere and keep the code mypy-clean.
- Prefer `str.translate`/translation tables and pre-compiled regex objects when manipulating text.
- Write docstrings in Google style and include a short example where meaningful.
- Keep helper functions private (`_helper_name`) unless part of the public API.

## Tests

- Add unit tests for every bug fix and feature in `tests/`.
- Maintain >95% coverage (checked automatically via CI).
- Performance-sensitive code should include a benchmark in `tests/test_performance.py`.

## Git & Pull Requests

- Use descriptive commit messages referencing issues when available.
- Update `docs/CHANGELOG.md` with a short entry under the “Unreleased” heading.
- Document user-facing changes in `README.md` if needed.
- Ensure CI passes for all supported Python versions (stable 3.10 – 3.14) and the cross-platform Python 3.15 pre-release job (currently `3.15.0-alpha.2` listed in GitHub’s `versions-manifest.json`).

## Reporting Bugs

When filing an issue, include:

- Steps to reproduce
- Expected vs. actual behavior
- Sample input data
- Python version / OS information

We appreciate detailed reports—they make fixing problems significantly faster.
