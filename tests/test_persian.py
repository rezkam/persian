import unittest

import persian


class TestEnglish(unittest.TestCase):
    def test_convert_english_numbers(self):
        self.assertEqual("۱۲۳۴۵۶۷۸۹۰",
                         persian.convert_en_numbers("1234567890"))

    def test_convert_english_chars(self):
        self.assertEqual("ضصثقفغعهخحجچگکمنتالبیسشظطزرذدپو./؟",
                         persian.convert_en_characters(
                             "qwertyuiop[]';lkjhgfdsazxcvbnm,./?"))


class TestArabic(unittest.TestCase):
    def test_convert_arabic_numbers(self):
        self.assertEqual("۱۲۳۴۵۶۷۸۹۰",
                         persian.convert_ar_numbers("١٢٣٤٥٦٧٨٩٠"))

    def test_convert_arabic_chars(self):
        self.assertEqual("کدبزذشسیی",
                         persian.convert_ar_characters("كدبزذشسىي"))


class TestPersian(unittest.TestCase):
    def test_convert_fa_numbers(self):
        self.assertEqual("1234567890", persian.convert_fa_numbers("۱۲۳۴۵۶۷۸۹۰"))

    def test_remove_halfspace(self):
        self.assertEqual('آمده‌ای ولی من رفته‌ام و می‌آییم', persian.convert_fa_spaces(
            'آمده ای ولی من رفته ام و می آییم'))
