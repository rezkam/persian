"""Constants for Persian language processing utilities."""

from __future__ import annotations

import re
from typing import Final

# Character sets
EN_DIGITS: Final[str] = "0123456789"
FA_DIGITS: Final[str] = "۰۱۲۳۴۵۶۷۸۹"
AR_DIGITS: Final[str] = "٠١٢٣٤٥٦٧٨٩"

# Translation tables (pre-computed)
EN_TO_FA_DIGITS_TABLE: Final = str.maketrans(
    {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
)

FA_TO_EN_DIGITS_TABLE: Final = str.maketrans(
    {
        "۰": "0",
        "۱": "1",
        "۲": "2",
        "۳": "3",
        "۴": "4",
        "۵": "5",
        "۶": "6",
        "۷": "7",
        "۸": "8",
        "۹": "9",
    }
)

AR_TO_FA_DIGITS_TABLE: Final = str.maketrans(
    {
        "٠": "۰",
        "١": "۱",
        "٢": "۲",
        "٣": "۳",
        "٤": "۴",
        "٥": "۵",
        "٦": "۶",
        "٧": "۷",
        "٨": "۸",
        "٩": "۹",
    }
)

EN_TO_FA_KEYBOARD_TABLE: Final = str.maketrans(
    {
        "q": "ض",
        "w": "ص",
        "e": "ث",
        "r": "ق",
        "t": "ف",
        "y": "غ",
        "u": "ع",
        "i": "ه",
        "o": "خ",
        "p": "ح",
        "[": "ج",
        "]": "چ",
        "a": "ش",
        "s": "س",
        "d": "ی",
        "f": "ب",
        "g": "ل",
        "h": "ا",
        "j": "ت",
        "k": "ن",
        "l": "م",
        ";": "ک",
        "'": "گ",
        "z": "ظ",
        "x": "ط",
        "c": "ز",
        "v": "ر",
        "b": "ذ",
        "n": "د",
        "m": "پ",
        ",": "و",
        "?": "؟",
    }
)

AR_TO_FA_CHARS_TABLE: Final = str.maketrans(
    {
        "ك": "ک",
        "ى": "ی",
        "ي": "ی",
    }
)

# Arabic diacritic mappings still require sequential replacements because of composed forms.
AR_DIACRITICS_MAPPING: Final[tuple[tuple[str, str], ...]] = (
    ("دِ", "د"),
    ("بِ", "ب"),
    ("زِ", "ز"),
    ("ذِ", "ذ"),
    ("شِ", "ش"),
    ("سِ", "س"),
)

# Combining diacritics removal table (U+064B..U+0652)
_AR_DIACRITICS = "\u064b\u064c\u064d\u064e\u064f\u0650\u0651\u0652"
AR_DIACRITIC_REMOVAL_TABLE: Final = str.maketrans("", "", _AR_DIACRITICS)

# Pre-compiled regex patterns for spacing fixes
MI_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"((\s\u0645\u06CC)+([\s])+([\u0600-\u06EF]{1,}){1,})"
)
DE_YII_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"(([\u0600-\u06EF]{1,})+([\s])+(ای|ایی|اند|ایم|اید|ام){1})"
)
