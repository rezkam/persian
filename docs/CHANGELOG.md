# Changelog

All notable changes to this project will be documented here. The project adheres
to semantic versioning.

## [0.6.0] - 2025-01-01

### ⚠️ Breaking Changes

- **Minimum Python version is now 3.10+** (previously 3.6+)
  - Python 3.6 reached end-of-life in December 2021
  - Python 3.7 reached end-of-life in June 2023
  - Python 3.8 reached end-of-life in October 2024
  - Python 3.9 reached end-of-life in October 2025 (3.9.25 was the final release)
  - This change was necessary to support modern type hints and align with currently supported Python versions
  - If you must use Python 3.6-3.9, please pin to `persian<0.6.0`

### Added

- Full type annotations for every public function.
- Strict runtime validation for all string-based parameters.
- `normalize_persian`, detection helpers, and diacritic removal utilities.
- Comprehensive documentation in `docs/` plus `py.typed` for PEP 561 compliance.
- Performance benchmarks and CI jobs guarding against regressions.

### Changed

- Core conversions now rely on `str.translate` and pre-compiled regex patterns,
  delivering 3–5× faster execution with lower memory usage.
- Packaging moved to `pyproject.toml` with modern tool configurations.
- README expanded with performance, type safety, and migration guidance.

### Fixed

- License metadata now consistently references MIT across the project.
- Regex compilation overhead removed from `convert_fa_spaces`.
- Arabic diacritics are handled deterministically and removable on demand.

## [0.5.0] - 2021-08-15

- Previous stable release with basic conversion utilities and deprecated CamelCase wrappers.
