# API Reference

The Persian package exposes a small set of focused utilities for handling numbers,
characters, spacing, and URL decoding. All functions reside in the top-level
`persian` package and are fully typed.

## Number Conversion

- `convert_en_numbers(text: str) -> str`  
  Convert ASCII digits (`0-9`) to Persian digits.

- `convert_fa_numbers(text: str) -> str`  
  Convert Persian digits to ASCII digits.

- `convert_ar_numbers(text: str) -> str`  
  Convert Arabic-Indic digits to Persian digits.

## Character Conversion

- `convert_en_characters(text: str) -> str`  
  Map characters typed on an English keyboard layout to Persian characters.

- `convert_ar_characters(text: str) -> str`  
  Convert Arabic characters and remove diacritics where appropriate.

- `remove_arabic_diacritics(text: str) -> str`  
  Strip combining tashkeel characters without modifying the rest of the text.

## Spacing and Normalization

- `convert_fa_spaces(text: str) -> str`  
  Replace incorrect spaces around Persian prefixes/suffixes with zero-width
  non-joiners.

- `normalize_persian(text: str, *, convert_numbers=True, convert_characters=True, fix_spacing=True) -> str`  
  Convenience wrapper that applies the most common conversions in a single call.

## Detection Helpers

- `contains_persian_digits(text: str) -> bool`  
  Return `True` if at least one Persian digit exists.

- `contains_arabic_digits(text: str) -> bool`  
  Return `True` if at least one Arabic-Indic digit exists.

- `is_persian_text(text: str) -> bool`  
  Return `True` if any character falls inside the Persian Unicode block.

## URL Helpers

- `decode_url(text: str) -> str`  
  Decode percent-encoded segments in URLs containing Persian characters.

## Deprecated Wrappers

The CamelCase helpers (`enToPersianNumb`, `enToPersianChar`, `arToPersianNumb`,
`arToPersianChar`) continue to work but raise `DeprecationWarning`. They will be removed
in v1.0.0—use the snake_case equivalents listed above.
