# encoding: utf-8

"""
Persian
Simple tool for Persian language localization in Python
Copyright (C) 2017-2020 Reza Kamalifard (mrkamalifard@gmail.com) and others
@rezakamalifard
MIT licensed
https://github.com/itmard/Persian

These functions will be deprecated on version 0.6.0

"""

import warnings

from .persian import (convert_en_numbers, convert_en_characters,
                      convert_ar_numbers, convert_ar_characters)


def enToPersianNumb(input_str):
    warnings.warn("deprecated use convert_en_numbers", DeprecationWarning)
    return convert_en_numbers(input_str)


def enToPersianChar(input_str):
    warnings.warn("deprecated use convert_en_characters", DeprecationWarning)
    return convert_en_characters(input_str)


def arToPersianNumb(input_str):
    warnings.warn("deprecated use convert_ar_numbers", DeprecationWarning)
    return convert_ar_numbers(input_str)


def arToPersianChar(input_str):
    warnings.warn("deprecated use convert_ar_characters", DeprecationWarning)
    return convert_ar_characters(input_str)
