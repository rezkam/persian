"""Backward compatible wrappers for deprecated helper names."""

from __future__ import annotations

import warnings

from .core import (
    convert_ar_characters,
    convert_ar_numbers,
    convert_en_characters,
    convert_en_numbers,
)


def enToPersianNumb(input_str: str) -> str:
    """Deprecated wrapper for convert_en_numbers."""
    warnings.warn("deprecated use convert_en_numbers", DeprecationWarning, stacklevel=2)
    return convert_en_numbers(input_str)


def enToPersianChar(input_str: str) -> str:
    """Deprecated wrapper for convert_en_characters."""
    warnings.warn("deprecated use convert_en_characters", DeprecationWarning, stacklevel=2)
    return convert_en_characters(input_str)


def arToPersianNumb(input_str: str) -> str:
    """Deprecated wrapper for convert_ar_numbers."""
    warnings.warn("deprecated use convert_ar_numbers", DeprecationWarning, stacklevel=2)
    return convert_ar_numbers(input_str)


def arToPersianChar(input_str: str) -> str:
    """Deprecated wrapper for convert_ar_characters."""
    warnings.warn("deprecated use convert_ar_characters", DeprecationWarning, stacklevel=2)
    return convert_ar_characters(input_str)
