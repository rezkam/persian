"""Core Persian language processing utilities."""

from __future__ import annotations

import urllib.parse

from .constants import (
    AR_DIACRITIC_REMOVAL_TABLE,
    AR_DIACRITICS_MAPPING,
    AR_DIGITS,
    AR_TO_FA_CHARS_TABLE,
    AR_TO_FA_DIGITS_TABLE,
    DE_YII_PATTERN,
    EN_TO_FA_DIGITS_TABLE,
    EN_TO_FA_KEYBOARD_TABLE,
    FA_DIGITS,
    FA_TO_EN_DIGITS_TABLE,
    MI_PATTERN,
)

MappingType = tuple[tuple[str, str], ...]


def _validate_string_input(input_str: str, param_name: str = "input_str") -> None:
    """Validate that the provided input is a non-None string."""
    if input_str is None:
        raise ValueError(f"{param_name} cannot be None")
    if not isinstance(input_str, str):
        raise TypeError(f"{param_name} must be str, got {type(input_str).__name__}")


def _multiple_replace(mapping: MappingType, text: str) -> str:
    """Replace all mapping keys within a text sequentially (legacy helper)."""
    result = text
    for old, new in mapping:
        result = result.replace(old, new)
    return result


def convert_en_numbers(input_str: str) -> str:
    """Convert English digits to Persian digits.

    Args:
        input_str: Text that may contain English digits.

    Returns:
        A copy of the text with English digits replaced by Persian digits.

    Raises:
        TypeError: If `input_str` is not a string.
        ValueError: If `input_str` is None.

    Examples:
        >>> convert_en_numbers("Phone 123")
        'Phone ۱۲۳'
    """
    _validate_string_input(input_str)
    return input_str.translate(EN_TO_FA_DIGITS_TABLE)


def convert_en_characters(input_str: str) -> str:
    """Convert English keyboard characters to standard Persian characters.

    Args:
        input_str: Text typed using an English keyboard layout.

    Returns:
        New text containing the mapped Persian characters.

    Raises:
        TypeError: If `input_str` is not a string.
        ValueError: If `input_str` is None.

    Examples:
        >>> convert_en_characters("sghl")
        'سلام'
    """
    _validate_string_input(input_str)
    return input_str.translate(EN_TO_FA_KEYBOARD_TABLE)


def convert_ar_numbers(input_str: str) -> str:
    """Convert Arabic digits to Persian digits.

    Args:
        input_str: Text that may contain Arabic digits.

    Returns:
        Text with Arabic digits replaced by Persian digits.

    Raises:
        TypeError: If `input_str` is not a string.
        ValueError: If `input_str` is None.

    Examples:
        >>> convert_ar_numbers("٣٤٥")
        '۳۴۵'
    """
    _validate_string_input(input_str)
    return input_str.translate(AR_TO_FA_DIGITS_TABLE)


def convert_fa_numbers(input_str: str) -> str:
    """Convert Persian digits to English digits.

    Args:
        input_str: Text that may contain Persian digits.

    Returns:
        Text containing English digits instead of Persian digits.

    Raises:
        TypeError: If `input_str` is not a string.
        ValueError: If `input_str` is None.

    Examples:
        >>> convert_fa_numbers("۱۲۳")
        '123'
    """
    _validate_string_input(input_str)
    return input_str.translate(FA_TO_EN_DIGITS_TABLE)


def convert_ar_characters(input_str: str) -> str:
    """Convert Arabic characters to their Persian equivalents.

    Args:
        input_str: Text that may contain Arabic characters.

    Returns:
        Text where Arabic characters are replaced with Persian characters.

    Raises:
        TypeError: If `input_str` is not a string.
        ValueError: If `input_str` is None.

    Examples:
        >>> convert_ar_characters("علي")
        'علی'
    """
    _validate_string_input(input_str)
    result = _multiple_replace(AR_DIACRITICS_MAPPING, input_str)
    return result.translate(AR_TO_FA_CHARS_TABLE)


def convert_fa_spaces(input_value: str) -> str:
    """Replace improper spaces around Persian affixes with zero-width non-joiners.

    Args:
        input_value: Persian text that may include incorrect spaces.

    Returns:
        Text where required affix boundaries use half-space characters.

    Raises:
        TypeError: If `input_value` is not a string.
        ValueError: If `input_value` is None.

    Examples:
        >>> convert_fa_spaces("می روم به خانه")
        'می‌روم به خانه'
    """
    _validate_string_input(input_value, "input_value")
    repl = "\\2\u200c\\4"
    result = MI_PATTERN.sub(repl, input_value)
    return DE_YII_PATTERN.sub(repl, result)


def decode_url(input_str: str) -> str:
    """Decode percent-encoded Persian characters in URLs.

    Args:
        input_str: URL containing percent-encoded segments.

    Returns:
        Decoded URL string.

    Raises:
        TypeError: If `input_str` is not a string.
        ValueError: If `input_str` is None.

    Examples:
        >>> decode_url("https://example/%D8%B5%D9%81%D8%AD%D9%87")
        'https://example/صفحه'
    """
    _validate_string_input(input_str)
    return urllib.parse.unquote(input_str)


def normalize_persian(
    input_str: str,
    *,
    convert_numbers: bool = True,
    convert_characters: bool = True,
    fix_spacing: bool = True,
) -> str:
    """Normalize Persian text by applying optional conversions.

    Args:
        input_str: Text to normalize.
        convert_numbers: Whether to convert Arabic digits to Persian.
        convert_characters: Whether to convert Arabic characters to Persian.
        fix_spacing: Whether to fix improper spaces with ZWNJ.

    Returns:
        Normalized Persian text.

    Raises:
        TypeError: If `input_str` is not a string.
        ValueError: If `input_str` is None.

    Examples:
        >>> normalize_persian("سلام ٣٤٥ می آیم")
        'سلام ۳۴۵ می‌آیم'
    """
    _validate_string_input(input_str)
    result = input_str
    if convert_numbers:
        result = convert_ar_numbers(result)
    if convert_characters:
        result = convert_ar_characters(result)
    if fix_spacing:
        result = convert_fa_spaces(result)
    return result


def contains_persian_digits(input_str: str) -> bool:
    """Check whether the text contains Persian digits.

    Args:
        input_str: Text to inspect.

    Returns:
        True if at least one Persian digit exists, otherwise False.

    Raises:
        TypeError: If `input_str` is not a string.
        ValueError: If `input_str` is None.
    """
    _validate_string_input(input_str)
    return any(char in FA_DIGITS for char in input_str)


def contains_arabic_digits(input_str: str) -> bool:
    """Check whether the text contains Arabic digits.

    Args:
        input_str: Text to inspect.

    Returns:
        True if at least one Arabic digit exists, otherwise False.

    Raises:
        TypeError: If `input_str` is not a string.
        ValueError: If `input_str` is None.
    """
    _validate_string_input(input_str)
    return any(char in AR_DIGITS for char in input_str)


def is_persian_text(input_str: str) -> bool:
    """Determine whether the text contains Persian characters.

    Args:
        input_str: Text to inspect.

    Returns:
        True if the unicode range includes at least one Persian character.

    Raises:
        TypeError: If `input_str` is not a string.
        ValueError: If `input_str` is None.
    """
    _validate_string_input(input_str)
    return any("\u0600" <= char <= "\u06ff" for char in input_str)


def remove_arabic_diacritics(input_str: str) -> str:
    """Remove Arabic diacritic (tashkeel) characters from the text.

    Args:
        input_str: Text that may include combining Arabic diacritics.

    Returns:
        Text without Arabic diacritics.

    Raises:
        TypeError: If `input_str` is not a string.
        ValueError: If `input_str` is None.
    """
    _validate_string_input(input_str)
    return input_str.translate(AR_DIACRITIC_REMOVAL_TABLE)


__all__ = [
    "contains_arabic_digits",
    "contains_persian_digits",
    "convert_ar_characters",
    "convert_ar_numbers",
    "convert_en_characters",
    "convert_en_numbers",
    "convert_fa_numbers",
    "convert_fa_spaces",
    "decode_url",
    "is_persian_text",
    "normalize_persian",
    "remove_arabic_diacritics",
]
