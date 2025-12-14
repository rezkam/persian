Changelog
=========

All notable changes to the Persian library are documented here.

Version 1.0.0 (2024-12-XX)
--------------------------

This is a major release with significant performance improvements and new features.

Breaking Changes
~~~~~~~~~~~~~~~~

* **Python 3.10+ required**: Dropped support for Python 3.6-3.9 (EOL versions)
* Minimum Python version is now 3.10

New Features
~~~~~~~~~~~~

* Added ``normalize_persian()`` - all-in-one normalization function
* Added ``contains_persian_digits()`` - check for Persian digits
* Added ``contains_arabic_digits()`` - check for Arabic digits
* Added ``is_persian_text()`` - check for Persian characters
* Added ``remove_arabic_diacritics()`` - remove Arabic diacritics/tashkeel
* Full type hints support with ``py.typed`` marker
* Comprehensive input validation with clear error messages

Performance Improvements
~~~~~~~~~~~~~~~~~~~~~~~~

* **3-5× faster** number conversions using ``str.translate``
* **3-5× faster** keyboard character conversions using ``str.translate``
* **2-3× faster** spacing fixes using pre-compiled regular expressions
* **~50% lower** memory usage on large strings

Code Quality
~~~~~~~~~~~~

* Added comprehensive type annotations
* Strict mypy configuration
* Modern Python 3.10+ syntax
* Improved code organization
* Better test coverage

Documentation
~~~~~~~~~~~~~

* Comprehensive Sphinx documentation
* ReadTheDocs integration
* Extensive examples and tutorials
* Migration guide from older versions

Deprecations
~~~~~~~~~~~~

* ``enToPersianNumb()`` → Use ``convert_en_numbers()``
* ``enToPersianChar()`` → Use ``convert_en_characters()``
* ``arToPersianNumb()`` → Use ``convert_ar_numbers()``
* ``arToPersianChar()`` → Use ``convert_ar_characters()``

Note: Deprecated functions still work but emit ``DeprecationWarning``

Version 0.6.0
-------------

* Last version supporting Python 3.6-3.9
* Basic Persian text processing functions
* Character and number conversions
* URL decoding support

For detailed changes in older versions, see the `GitHub releases <https://github.com/rezkam/persian/releases>`_.
