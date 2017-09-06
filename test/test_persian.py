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
