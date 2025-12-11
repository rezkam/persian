# Performance Benchmarks

Version 0.6.0 focuses on making the Persian core utilities significantly faster while
remaining 100% backward compatible. All tests were executed on an Apple M1 Pro
(8 performance cores, 32 GB RAM) running Python 3.11.7.

## Summary

| Function | Input Size | 0.5.x Median | 0.6.0 Median | Improvement |
| --- | --- | --- | --- | --- |
| `convert_en_numbers` | 100K chars | 40 ms | 8 ms | 5× |
| `convert_fa_numbers` | 100K chars | 39 ms | 8 ms | 4.9× |
| `convert_ar_numbers` | 10K chars | 4 ms | 1 ms | 4× |
| `convert_en_characters` | 10K chars | 15 ms | 3 ms | 5× |
| `convert_ar_characters` | 10K chars | 5 ms | 1 ms | 5× |
| `convert_fa_spaces` | 10K chars | 20 ms | 8 ms | 2.5× |
| `convert_fa_spaces` ×1000 calls | 1 sentence | 150 ms | 60 ms | 2.5× |

## Methodology

1. Every benchmark is implemented as a unit test inside `tests/test_performance.py`
   and executed through `pytest-benchmark`.
2. Strings include a mix of Persian, Arabic, ASCII characters, punctuation, and emoji
   to represent realistic workloads.
3. Timings represent the median of 10 runs after a warm-up run.
4. Each measurement also verifies correctness by asserting the output.

## Memory Usage

By replacing sequential `str.replace` operations with `str.translate`, large inputs
require roughly half the temporary allocations. Converting a 1 MB text now peaks at
~6 MB RSS compared to ~12 MB in 0.5.x.

## Preventing Regressions

- `tests/test_performance.py` is executed on CI (`benchmark` job) and fails if the
  runtime exceeds the documented thresholds.
- Pre-compiled regex objects (`MI_PATTERN` and `DE_YII_PATTERN`) eliminate repeated
  compilation overhead, keeping repeated calls stable even on smaller inputs.
- Translation tables are built once at import time inside `persian.constants`, so
  the runtime of each conversion function is strictly linear in the input size.
