import time
import unittest

import persian


class TestPerformance(unittest.TestCase):
    """Performance smoke tests to prevent regressions."""

    def setUp(self) -> None:
        self.small_input = "1234567890" * 10  # 100 chars
        self.medium_input = "1234567890" * 100  # 1,000 chars
        self.large_input = "1234567890" * 10000  # 100,000 chars

    def test_convert_en_numbers_large_string(self) -> None:
        start = time.perf_counter()
        result = persian.convert_en_numbers(self.large_input)
        elapsed = time.perf_counter() - start

        self.assertLess(
            elapsed,
            0.010,
            f"Large string conversion took {elapsed:.3f}s, expected < 0.010s",
        )
        self.assertTrue(all(c in "۰۱۲۳۴۵۶۷۸۹" for c in result))

    def test_convert_fa_spaces_performance(self) -> None:
        test_input = "می روم به خانه ام و می آیم" * 1000
        start = time.perf_counter()
        persian.convert_fa_spaces(test_input)
        elapsed = time.perf_counter() - start

        self.assertLess(
            elapsed,
            0.050,
            f"Space conversion took {elapsed:.3f}s, expected < 0.050s",
        )

    def test_repeated_calls_no_compilation_overhead(self) -> None:
        test_input = "می روم به خانه"
        persian.convert_fa_spaces(test_input)

        start = time.perf_counter()
        for _ in range(1000):
            persian.convert_fa_spaces(test_input)
        elapsed = time.perf_counter() - start

        self.assertLess(
            elapsed,
            0.100,
            f"1000 calls took {elapsed:.3f}s, expected < 0.100s",
        )
