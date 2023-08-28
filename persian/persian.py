# encoding: utf-8

"""
Persian
Simple tool for Persian language localization in Python
Copyright (C) 2017-2020 Reza Kamalifard (mrkamalifard@gmail.com) and others
@rezakamalifard
MIT licensed
https://github.com/itmard/Persian
"""

import re
import urllib.parse


def convert_en_numbers(input_str):
    """
    Converts English numbers to Persian numbers
    :param input_str: String contains English numbers
    :return: New string with Persian numbers
    """
    mapping = {
        '0': '۰',
        '1': '۱',
        '2': '۲',
        '3': '۳',
        '4': '۴',
        '5': '۵',
        '6': '۶',
        '7': '۷',
        '8': '۸',
        '9': '۹',
        '.': '.',
    }
    return _multiple_replace(mapping, input_str)


def convert_en_characters(input_str):
    """
        Assumes that characters written with standard persian keyboard
        not windows arabic layout
    :param input_str: String contains English chars
    :return: New string with related characters on Persian standard keyboard
    """
    mapping = {
        'q': 'ض',
        'w': 'ص',
        'e': 'ث',
        'r': 'ق',
        't': 'ف',
        'y': 'غ',
        'u': 'ع',
        'i': 'ه',
        'o': 'خ',
        'p': 'ح',
        '[': 'ج',
        ']': 'چ',
        'a': 'ش',
        's': 'س',
        'd': 'ی',
        'f': 'ب',
        'g': 'ل',
        'h': 'ا',
        'j': 'ت',
        'k': 'ن',
        'l': 'م',
        ';': 'ک',
        "'": 'گ',
        'z': 'ظ',
        'x': 'ط',
        'c': 'ز',
        'v': 'ر',
        'b': 'ذ',
        'n': 'د',
        'm': 'پ',
        ',': 'و',
        '?': '؟',
    }
    return _multiple_replace(mapping, input_str)


def convert_ar_numbers(input_str):
    """
    Converts Arabic numbers to Persian numbers
    :param input_str: String contains Arabic numbers
    :return: New str and replaces arabic number with persian numbers
    """
    mapping = {
        '١': '۱',  # Arabic 1 is 0x661 and Persian one is 0x6f1
        '٢': '۲',  # More info https://goo.gl/SPiBtn
        '٣': '۳',
        '٤': '۴',
        '٥': '۵',
        '٦': '۶',
        '٧': '۷',
        '٨': '۸',
        '٩': '۹',
        '٠': '۰',
    }
    return _multiple_replace(mapping, input_str)


def convert_fa_numbers(input_str):
    """
    This function convert Persian numbers to English numbers.
    
    Keyword arguments:
    input_str -- It should be string

    Returns: English numbers
    """
    mapping = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9',
        '.': '.',
    }
    return _multiple_replace(mapping, input_str)


def convert_ar_characters(input_str):
    """
    Converts Arabic chars to related Persian unicode char
    :param input_str: String contains Arabic chars
    :return: New str with converted arabic chars
    """
    mapping = {
        'ك': 'ک',
        'دِ': 'د',
        'بِ': 'ب',
        'زِ': 'ز',
        'ذِ': 'ذ',
        'شِ': 'ش',
        'سِ': 'س',
        'ى': 'ی',
        'ي': 'ی'
    }
    return _multiple_replace(mapping, input_str)


def convert_fa_spaces(input_value: str) -> str:
    """
    Convert space between Persian MI and De-Yii to zero-width non-joiner (halfspace) char
    :param input_value: String contains persian chars
    :return: New string with converted space to half space char
    """

    # u200C is the code for unicode zwnj character https://en.wikipedia.org/wiki/Zero-width_non-joiner
    repl = '\\2\u200C\\4'
    # replace space between persian MI.
    mi_pattern = r'((\s\u0645\u06CC)+([\s])+([\u0600-\u06EF]{1,}){1,})'
    result = re.sub(mi_pattern, repl, input_value, 0)
    # replace space between persian De-Yii.
    de_yii_pattern = r'(([\u0600-\u06EF]{1,})+([\s])+(ای|ایی|اند|ایم|اید|ام){1})'
    result = re.sub(de_yii_pattern, repl, result)

    return result


def decode_url(input_str):
    """
    Decode Persian characters in URL
    :param input_str: String contains encoded URL
    :return: New string with decoded URL
    """
    return urllib.parse.unquote(input_str)

def encode_url(input_str):
    """
    Encode non-ASCII characters in URL
    :param input_str: String contains decoded URL
    :return: New string with encoded URL
    """
    return urllib.parse.quote(input_str, safe="/:")


def _multiple_replace(mapping, text):
    """
    Internal function for replace all mapping keys for a input string
    :param mapping: replacing mapping keys
    :param text: user input string
    :return: New string with converted mapping keys to values
    """
    pattern = "|".join(map(re.escape, mapping.keys()))
    return re.sub(pattern, lambda m: mapping[m.group()], str(text))
