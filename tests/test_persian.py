import unittest

import persian


class TestInputValidation(unittest.TestCase):
    def test_none_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            persian.convert_en_numbers(None)  # type: ignore[arg-type]

    def test_non_string_input_raises_type_error(self):
        with self.assertRaises(TypeError):
            persian.convert_en_numbers(123)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            persian.convert_fa_spaces(["test"])  # type: ignore[arg-type]

    def test_empty_string_returns_empty(self):
        self.assertEqual("", persian.convert_en_numbers(""))
        self.assertEqual("", persian.convert_fa_numbers(""))
        self.assertEqual("", persian.convert_ar_numbers(""))


class TestNumberConversions(unittest.TestCase):
    def test_convert_english_numbers(self):
        self.assertEqual("۱۲۳۴۵۶۷۸۹۰", persian.convert_en_numbers("1234567890"))

    def test_convert_arabic_numbers(self):
        self.assertEqual("۱۲۳۴۵۶۷۸۹۰", persian.convert_ar_numbers("١٢٣٤٥٦٧٨٩٠"))

    def test_convert_fa_numbers(self):
        self.assertEqual("1234567890", persian.convert_fa_numbers("۱۲۳۴۵۶۷۸۹۰"))

    def test_mixed_content(self):
        self.assertEqual("سلام ۱۲۳", persian.convert_en_numbers("سلام 123"))

    def test_floating_point_numbers(self):
        self.assertEqual("۱۲۳.۴۵", persian.convert_en_numbers("123.45"))

    def test_idempotency(self):
        self.assertEqual("۱۲۳", persian.convert_en_numbers("۱۲۳"))


class TestCharacterConversions(unittest.TestCase):
    def test_convert_keyboard_layout(self):
        self.assertEqual(
            "ضصثقفغعهخحجچگکمنتالبیسشظطزرذدپو./؟",
            persian.convert_en_characters("qwertyuiop[]';lkjhgfdsazxcvbnm,./?"),
        )

    def test_convert_arabic_chars(self):
        self.assertEqual("کدبزذشسیی", persian.convert_ar_characters("كدبزذشسىي"))

    def test_remove_diacritics(self):
        self.assertEqual("دب", persian.remove_arabic_diacritics("دِبِ"))

    def test_arabic_diacritics_preserved(self):
        text = "مُحَمَّد"
        self.assertEqual(text, persian.convert_ar_characters(text))


class TestSpacingAndUrl(unittest.TestCase):
    def test_convert_fa_spaces(self):
        self.assertEqual(
            "آمده‌ای ولی من رفته‌ام و می‌آییم",
            persian.convert_fa_spaces("آمده ای ولی من رفته ام و می آییم"),
        )

    def test_decode_url(self):
        encoded_url = (
            "https://fa.wikipedia.org/wiki/%D8%B5%D9%81%D8%AD%D9%87%D9%94_%D8%A7%D8%B5%D9%84%DB%8C"
        )
        self.assertEqual(
            "https://fa.wikipedia.org/wiki/صفحهٔ_اصلی",
            persian.decode_url(encoded_url),
        )


class TestNormalizationAndDetection(unittest.TestCase):
    def test_normalize_persian(self):
        self.assertEqual("سلام ۳۴۵ می‌آیم", persian.normalize_persian("سلام ٣٤٥ می آیم"))

    def test_detection_helpers(self):
        text = "سال ۱۳۹۹"
        self.assertTrue(persian.contains_persian_digits(text))
        self.assertFalse(persian.contains_arabic_digits(text))
        self.assertTrue(persian.is_persian_text(text))


class TestBackwardCompatibility(unittest.TestCase):
    """Ensure legacy examples from README continue to work."""

    def test_original_examples(self):
        self.assertEqual("علی", persian.convert_ar_characters("علي"))
        self.assertEqual("1371", persian.convert_fa_numbers("۱۳۷۱"))
        self.assertEqual("۳۴۵", persian.convert_ar_numbers("٣٤٥"))
        self.assertEqual("۳۴۵", persian.convert_en_numbers("345"))
        self.assertEqual("سلام", persian.convert_en_characters("sghl"))


class TestLegacyModule(unittest.TestCase):
    def test_persian_persian_import(self):
        import importlib

        legacy = importlib.import_module("persian.persian")
        self.assertEqual("۱۲۳", legacy.convert_en_numbers("123"))
