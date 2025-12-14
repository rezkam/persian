"""Legacy module maintained for backwards compatibility.

Historically, consumers imported helpers via ``import persian.persian``.
This shim simply re-exports the new core implementations so the older
import path continues to function without modification.
"""

from __future__ import annotations

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
