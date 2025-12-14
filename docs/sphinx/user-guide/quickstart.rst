Quick Start Guide
=================

This guide will get you started with the Persian library in minutes.

Basic Import
------------

Start by importing the library:

.. code-block:: python

   import persian

All functions are available directly from the ``persian`` module.

Number Conversions
------------------

English to Persian
~~~~~~~~~~~~~~~~~~

Convert English digits to Persian digits:

.. code-block:: python

   persian.convert_en_numbers("123")
   # '۱۲۳'

   persian.convert_en_numbers("Price: 1500")
   # 'Price: ۱۵۰۰'

Persian to English
~~~~~~~~~~~~~~~~~~

Convert Persian digits to English digits:

.. code-block:: python

   persian.convert_fa_numbers("۱۲۳")
   # '123'

   persian.convert_fa_numbers("قیمت: ۱۵۰۰")
   # 'قیمت: 1500'

Arabic to Persian
~~~~~~~~~~~~~~~~~

Convert Arabic digits to Persian digits:

.. code-block:: python

   persian.convert_ar_numbers("٣٤٥")
   # '۳۴۵'

Character Conversions
---------------------

English Keyboard to Persian
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Convert text typed with English keyboard to Persian:

.. code-block:: python

   persian.convert_en_characters("sghl")
   # 'سلام'

   persian.convert_en_characters("sghl Hkd Hvhgdk")
   # 'سلام خوب حوالیک'

Arabic to Persian Characters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Convert Arabic characters to Persian equivalents:

.. code-block:: python

   persian.convert_ar_characters("علي")
   # 'علی'

   persian.convert_ar_characters("مرحبا يا صديقي")
   # 'مرحبا یا صدیقی'

Text Processing
---------------

Fix Persian Spacing
~~~~~~~~~~~~~~~~~~~

Replace improper spaces with zero-width non-joiners (ZWNJ):

.. code-block:: python

   persian.convert_fa_spaces("می روم")
   # 'می‌روم'

   persian.convert_fa_spaces("کتاب های من")
   # 'کتاب‌های من'

Decode Persian URLs
~~~~~~~~~~~~~~~~~~~

Decode percent-encoded Persian characters in URLs:

.. code-block:: python

   url = "https://example.com/%D8%B5%D9%81%D8%AD%D9%87"
   persian.decode_url(url)
   # 'https://example.com/صفحه'

Remove Arabic Diacritics
~~~~~~~~~~~~~~~~~~~~~~~~

Remove Arabic diacritics (harakat/tashkeel) from text:

.. code-block:: python

   persian.remove_arabic_diacritics("مَرحَباً")
   # 'مرحبا'

All-in-One Normalization
-------------------------

Use ``normalize_persian()`` to apply multiple conversions at once:

.. code-block:: python

   persian.normalize_persian("سلام ٣٤٥ می آیم")
   # 'سلام ۳۴۵ می‌آیم'

This function:

1. Converts Arabic digits to Persian
2. Converts Arabic characters to Persian
3. Fixes spacing issues

Custom Normalization
~~~~~~~~~~~~~~~~~~~~

You can control which conversions to apply:

.. code-block:: python

   # Only convert numbers
   persian.normalize_persian(
       "سلام ٣٤٥",
       convert_characters=False,
       fix_spacing=False
   )
   # 'سلام ۳۴۵'

   # Only fix spacing
   persian.normalize_persian(
       "می آیم",
       convert_numbers=False,
       convert_characters=False
   )
   # 'می‌آیم'

Detection Utilities
-------------------

Check for Persian Digits
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   persian.contains_persian_digits("۱۲۳")  # True
   persian.contains_persian_digits("123")  # False

Check for Arabic Digits
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   persian.contains_arabic_digits("٣٤٥")  # True
   persian.contains_arabic_digits("۳۴۵")  # False

Check for Persian Text
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   persian.is_persian_text("سلام")  # True
   persian.is_persian_text("Hello")  # False

Practical Examples
------------------

Clean User Input
~~~~~~~~~~~~~~~~

.. code-block:: python

   def clean_persian_input(text: str) -> str:
       """Clean and normalize Persian user input."""
       return persian.normalize_persian(text)

   user_input = "سلام من می روم به خانه"
   clean_text = clean_persian_input(user_input)
   # 'سلام من می‌روم به خانه'

Process Mixed Content
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def process_text(text: str) -> str:
       """Process text containing both Persian and English."""
       # First, convert Arabic to Persian
       text = persian.convert_ar_characters(text)
       text = persian.convert_ar_numbers(text)

       # Fix spacing
       text = persian.convert_fa_spaces(text)

       return text

   mixed = "كتاب شماره ٣ را می خوانم"
   result = process_text(mixed)
   # 'کتاب شماره ۳ را می‌خوانم'

Validate Persian Content
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def validate_persian(text: str) -> bool:
       """Check if text contains Persian characters."""
       if not persian.is_persian_text(text):
           raise ValueError("Text must contain Persian characters")
       return True

   try:
       validate_persian("سلام")  # OK
       validate_persian("Hello")  # Raises ValueError
   except ValueError as e:
       print(f"Error: {e}")

Common Patterns
---------------

Web Forms
~~~~~~~~~

Clean Persian input from web forms:

.. code-block:: python

   from persian import normalize_persian

   def process_form_data(form_data: dict) -> dict:
       """Normalize all Persian text fields in form data."""
       for key, value in form_data.items():
           if isinstance(value, str):
               form_data[key] = normalize_persian(value)
       return form_data

Database Storage
~~~~~~~~~~~~~~~~

Normalize before storing in database:

.. code-block:: python

   import persian

   class Article:
       def __init__(self, title: str, content: str):
           self.title = persian.normalize_persian(title)
           self.content = persian.normalize_persian(content)

Display URLs
~~~~~~~~~~~~

Decode URLs for display:

.. code-block:: python

   import persian

   encoded_urls = [
       "https://example.com/%D8%B5%D9%81%D8%AD%D9%87",
       "https://example.com/%D9%85%D9%82%D8%A7%D9%84%D9%87",
   ]

   readable_urls = [persian.decode_url(url) for url in encoded_urls]
   # [
   #     'https://example.com/صفحه',
   #     'https://example.com/مقاله'
   # ]

Error Handling
--------------

All functions validate inputs and raise clear exceptions:

Type Errors
~~~~~~~~~~~

.. code-block:: python

   try:
       persian.convert_en_numbers(123)
   except TypeError as e:
       print(e)  # "input_str must be str, got int"

Value Errors
~~~~~~~~~~~~

.. code-block:: python

   try:
       persian.convert_en_numbers(None)
   except ValueError as e:
       print(e)  # "input_str cannot be None"

Empty Strings
~~~~~~~~~~~~~

Empty strings are accepted and return empty strings:

.. code-block:: python

   persian.convert_en_numbers("")  # ''
   persian.normalize_persian("")   # ''

Next Steps
----------

* See :doc:`examples` for more comprehensive examples
* Check the :doc:`../api/core` for detailed function documentation
* Read about :doc:`../migration` if upgrading from an older version
