Overview
========

What is Persian?
----------------

**Persian** is a fast Python toolkit for Persian (Farsi) text normalization, number/character conversion, and localization. It provides a comprehensive set of utilities for converting and processing Persian text, including:

* Number conversions (English ↔ Persian, Arabic → Persian)
* Character conversions (English keyboard → Persian, Arabic → Persian)
* Text processing (spacing fixes, URL decoding, diacritic removal)
* Detection utilities (check for Persian/Arabic content)

The library is a Python implementation of the popular `Persian.js <https://github.com/usablica/persian.js>`_ JavaScript library.

Why Use Persian?
----------------

**Performance**
  Version 1.0.0 includes major performance improvements:

  * 3-5× faster number and character conversions using ``str.translate``
  * 2-3× faster spacing fixes with pre-compiled regex patterns
  * ~50% lower memory usage on large strings

**Type Safety**
  Ships with native type hints (``py.typed``) and strict ``mypy`` configuration:

  .. code-block:: python

     from persian import convert_en_numbers

     result: str = convert_en_numbers("123")  # ✔️ mypy is satisfied

**Modern Python**
  Requires Python 3.10+ with full support through Python 3.15, including:

  * Modern syntax and features
  * Comprehensive type annotations
  * Excellent IDE support

**Zero Dependencies**
  No external runtime dependencies - just pure Python stdlib

**Well-Tested**
  Extensive test coverage with pytest and continuous integration across:

  * Python 3.10, 3.11, 3.12, 3.13, 3.14, 3.15
  * Linux, macOS, and Windows

Use Cases
---------

Web Applications
~~~~~~~~~~~~~~~~

Perfect for Django, Flask, FastAPI applications that need to handle Persian content:

.. code-block:: python

   from persian import normalize_persian

   def process_user_input(text: str) -> str:
       """Clean and normalize Persian user input."""
       return normalize_persian(text)

Data Processing
~~~~~~~~~~~~~~~

Clean and standardize Persian text in data pipelines:

.. code-block:: python

   import persian
   import pandas as pd

   # Normalize a DataFrame column
   df['persian_text'] = df['persian_text'].apply(persian.normalize_persian)

Content Management
~~~~~~~~~~~~~~~~~~

Process Persian content in CMS systems:

.. code-block:: python

   import persian

   def prepare_persian_article(content: str) -> str:
       """Prepare Persian article for publication."""
       # Fix spacing issues
       content = persian.convert_fa_spaces(content)

       # Convert Arabic chars to Persian
       content = persian.convert_ar_characters(content)

       # Convert Arabic numbers to Persian
       content = persian.convert_ar_numbers(content)

       return content

URL Processing
~~~~~~~~~~~~~~

Decode Persian URLs for display or logging:

.. code-block:: python

   import persian

   encoded_url = "https://example.com/%D9%85%D9%82%D8%A7%D9%84%D9%87"
   readable_url = persian.decode_url(encoded_url)
   print(readable_url)  # https://example.com/مقاله

API Design
----------

All public functions follow a consistent design:

**Input Validation**
  All functions validate inputs and raise clear exceptions:

  .. code-block:: python

     persian.convert_en_numbers(None)  # ValueError: input_str cannot be None
     persian.convert_en_numbers(123)   # TypeError: input_str must be str, got int

**Empty String Handling**
  Empty strings are accepted and return empty strings:

  .. code-block:: python

     persian.convert_en_numbers("")  # ''
     persian.normalize_persian("")   # ''

**No Side Effects**
  All functions return new strings without modifying inputs:

  .. code-block:: python

     original = "123"
     result = persian.convert_en_numbers(original)
     # original is unchanged

**Type Hints**
  All functions include comprehensive type annotations:

  .. code-block:: python

     def convert_en_numbers(input_str: str) -> str: ...
     def normalize_persian(
         input_str: str,
         *,
         convert_numbers: bool = True,
         convert_characters: bool = True,
         fix_spacing: bool = True,
     ) -> str: ...

Comparison with Persian.js
---------------------------

The Python Persian library maintains API compatibility with Persian.js while adding Python-specific improvements:

**Similarities**
  * Same core functionality
  * Compatible naming conventions
  * Similar behavior and output

**Python Enhancements**
  * Type hints for better IDE support
  * Keyword-only arguments for clarity
  * Python-style error handling
  * Modern Python performance optimizations
  * Comprehensive test coverage

License
-------

The Persian library is released under the MIT License. See the `LICENSE <https://github.com/rezkam/persian/blob/main/LICENSE>`_ file for details.

Community & Support
-------------------

* **GitHub**: `github.com/rezkam/persian <https://github.com/rezkam/persian>`_
* **Issues**: `github.com/rezkam/persian/issues <https://github.com/rezkam/persian/issues>`_
* **PyPI**: `pypi.org/project/persian <https://pypi.org/project/persian/>`_
