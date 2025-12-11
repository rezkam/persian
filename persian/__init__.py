from __future__ import annotations

"""Public API exports for the Persian package."""

from .core import (
    contains_arabic_digits,
    contains_persian_digits,
    convert_ar_characters,
    convert_ar_numbers,
    convert_en_characters,
    convert_en_numbers,
    convert_fa_numbers,
    convert_fa_spaces,
    decode_url,
    is_persian_text,
    normalize_persian,
    remove_arabic_diacritics,
)

# Deprecated helpers are still importable for backward compatibility
from .deprecation import *  # noqa: F401,F403

__all__ = [
    "convert_en_numbers",
    "convert_en_characters",
    "convert_ar_numbers",
    "convert_fa_numbers",
    "convert_ar_characters",
    "convert_fa_spaces",
    "decode_url",
    "normalize_persian",
    "contains_persian_digits",
    "contains_arabic_digits",
    "is_persian_text",
    "remove_arabic_diacritics",
]
