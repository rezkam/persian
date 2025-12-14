Persian - Fast Python Toolkit for Persian Language Localization
===============================================================

.. image:: https://github.com/rezkam/persian/workflows/Tests/badge.svg
   :target: https://github.com/rezkam/persian/actions
   :alt: Tests

A fast Python toolkit for Persian (Farsi) text normalization, number/character conversion, and localization utilities.

Key Features
------------

* **Fast**: 3-5× faster number and character conversions using ``str.translate``
* **Type-Safe**: Ships with native type hints (``py.typed``) and strict ``mypy`` configuration
* **Modern Python**: Requires Python 3.10+ with full support for 3.10-3.15
* **Comprehensive**: Complete set of utilities for Persian text processing
* **Well-Tested**: Extensive test coverage with pytest
* **Zero Dependencies**: No external runtime dependencies

Installation
------------

.. code-block:: bash

   pip install persian

**Requirements:** Python 3.10 or higher

For older Python versions (3.6-3.9):

.. code-block:: bash

   pip install "persian<1.0.0"

Quick Start
-----------

.. code-block:: python

   import persian

   # Convert Arabic characters to Persian
   persian.convert_ar_characters("علي")  # 'علی'

   # Convert Persian numbers to English
   persian.convert_fa_numbers("۱۳۷۱")    # '1371'

   # Convert English numbers to Persian
   persian.convert_en_numbers("345")     # '۳۴۵'

   # Convert English keyboard to Persian
   persian.convert_en_characters("sghl") # 'سلام'

   # Fix Persian spacing
   persian.convert_fa_spaces("آمده ای")  # 'آمده‌ای'

   # Decode Persian URLs
   persian.decode_url("https://example.com/%D8%B5%D9%81%D8%AD%D9%87")
   # 'https://example.com/صفحه'

   # Normalize Persian text (one-stop helper)
   persian.normalize_persian("سلام ٣٤٥ می آیم")  # 'سلام ۳۴۵ می‌آیم'

Performance
-----------

Version 1.0.0 includes major speedups:

* 3–5× faster number and keyboard conversions via ``str.translate``
* 2–3× faster spacing fixes using pre-compiled regular expressions
* ~50% lower memory usage on large strings thanks to fewer temporary objects

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   user-guide/overview
   user-guide/installation
   user-guide/quickstart
   user-guide/examples

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/core
   api/utilities

.. toctree::
   :maxdepth: 1
   :caption: Additional Information

   migration
   contributing

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
