# Persian

A fast Python toolkit for Persian (Farsi) text normalization, number/character conversion, and localization utilities.

[![Tests](https://github.com/rezkam/persian/workflows/Tests/badge.svg)](https://github.com/rezkam/persian/actions)

## Installation

```bash
pip install persian
```

## Quick Start

```python
import persian

persian.convert_ar_characters("علي")  # 'علی'
persian.convert_fa_numbers("۱۳۷۱")    # '1371'
persian.convert_en_numbers("345")     # '۳۴۵'
persian.convert_en_characters("sghl") # 'سلام'
persian.convert_fa_spaces("آمده ای")  # 'آمده‌ای'
persian.decode_url("https://.../%D8%B5%D9%81%D8%AD%D9%87")  # 'https://.../صفحه'
```

Need a one-stop helper? Use `normalize_persian("سلام ٣٤٥ می آیم")`
to get `سلام ۳۴۵ می‌آیم`.

## Performance

Version 1.0.0 includes major speedups:

- 3–5× faster number and keyboard conversions via `str.translate`
- 2–3× faster spacing fixes using pre-compiled regular expressions
- ~50% lower memory usage on large strings thanks to fewer temporary objects

See [docs/PERFORMANCE.md](docs/PERFORMANCE.md) for benchmark methodology and charts.

## Type Safety & Tooling

The package ships with native type hints (`py.typed`) and strict type checking.
Static analyzers know the exact return type of every function:

```python
from persian import convert_en_numbers

result: str = convert_en_numbers("123")  # ✔️ type checker is satisfied
```

## Error Handling

All public functions validate inputs and raise clear exceptions:

```python
import persian

persian.convert_en_numbers(None)  # ValueError: input_str cannot be None
persian.convert_en_numbers(123)   # TypeError: input_str must be str, got int
```

Empty strings are accepted and return empty strings.

## API Overview

| Category | Functions |
| --- | --- |
| Numbers | `convert_en_numbers`, `convert_fa_numbers`, `convert_ar_numbers` |
| Characters | `convert_en_characters`, `convert_ar_characters`, `remove_arabic_diacritics` |
| Spacing & URLs | `convert_fa_spaces`, `decode_url` |
| Utilities | `normalize_persian`, `contains_persian_digits`, `contains_arabic_digits`, `is_persian_text` |

A detailed description is available in [docs/API.md](docs/API.md).

## Deprecated Functions

CamelCase helpers remain available but emit `DeprecationWarning`:

- `enToPersianNumb()` → `convert_en_numbers()`
- `enToPersianChar()` → `convert_en_characters()`
- `arToPersianNumb()` → `convert_ar_numbers()`
- `arToPersianChar()` → `convert_ar_characters()`

## Documentation

- [Performance Benchmarks](docs/PERFORMANCE.md)
- [API Reference](docs/API.md)
- [Changelog](docs/CHANGELOG.md)
- [Contributing Guide](docs/CONTRIBUTING.md)

## Contributors

- [Reza Kamlifard](https://github.com/rezakamalifard/)
- [Keyvan Hedayati](https://github.com/k1-hedayati)
- [Bahram Aghaei](https://github.com/GreatBahram)
- [Hasan Ramezani](https://github.com/hramezani)
- [Farhad Mortezapour](https://github.com/farhadmpr)

## Contributing

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for setup instructions and code style rules.
