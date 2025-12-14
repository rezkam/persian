Core Functions
==============

The Persian package provides a comprehensive set of functions for converting and processing Persian text.

Number Conversion
-----------------

convert_en_numbers
~~~~~~~~~~~~~~~~~~

.. autofunction:: persian.convert_en_numbers

**Examples:**

.. code-block:: python

   import persian

   # Basic usage
   persian.convert_en_numbers("123")  # '۱۲۳'

   # In sentences
   persian.convert_en_numbers("I have 5 apples")  # 'I have ۵ apples'

   # Mixed text
   persian.convert_en_numbers("سال 2024")  # 'سال ۲۰۲۴'

   # Phone numbers
   persian.convert_en_numbers("09123456789")  # '۰۹۱۲۳۴۵۶۷۸۹'

convert_fa_numbers
~~~~~~~~~~~~~~~~~~

.. autofunction:: persian.convert_fa_numbers

**Examples:**

.. code-block:: python

   import persian

   # Basic usage
   persian.convert_fa_numbers("۱۲۳")  # '123'

   # In sentences
   persian.convert_fa_numbers("من ۵ سیب دارم")  # 'من 5 سیب دارم'

   # Dates
   persian.convert_fa_numbers("۱۴۰۲/۰۱/۱۵")  # '1402/01/15'

   # Mixed content
   persian.convert_fa_numbers("قیمت: ۱۵۰۰۰ تومان")  # 'قیمت: 15000 تومان'

convert_ar_numbers
~~~~~~~~~~~~~~~~~~

.. autofunction:: persian.convert_ar_numbers

**Examples:**

.. code-block:: python

   import persian

   # Arabic digits to Persian
   persian.convert_ar_numbers("٣٤٥")  # '۳۴۵'

   # Mixed Arabic and English
   persian.convert_ar_numbers("٣٤٥ and 678")  # '۳۴۵ and 678'

   # In Arabic text with numbers
   persian.convert_ar_numbers("العدد ٩٨٧")  # 'العدد ۹۸۷'

Character Conversion
--------------------

convert_en_characters
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: persian.convert_en_characters

**Examples:**

.. code-block:: python

   import persian

   # English keyboard to Persian
   persian.convert_en_characters("sghl")  # 'سلام'

   # Complete sentence
   persian.convert_en_characters("sghl Hkd Hvhgdk")  # 'سلام خوب حوالیک'

   # Mixed content (only converts English keyboard chars)
   persian.convert_en_characters("sghl 123")  # 'سلام 123'

convert_ar_characters
~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: persian.convert_ar_characters

**Examples:**

.. code-block:: python

   import persian

   # Arabic to Persian characters
   persian.convert_ar_characters("علي")  # 'علی'

   # Complete text
   persian.convert_ar_characters("مرحبا يا صديقي")  # 'مرحبا یا صدیقی'

   # Fix common Arabic characters in Persian text
   persian.convert_ar_characters("كيك خوشمزه")  # 'کیک خوشمزه'

remove_arabic_diacritics
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: persian.remove_arabic_diacritics

**Examples:**

.. code-block:: python

   import persian

   # Remove Arabic diacritics (harakat/tashkeel)
   persian.remove_arabic_diacritics("مَرحَباً")  # 'مرحبا'

   # Clean text with various diacritics
   persian.remove_arabic_diacritics("الْحَمْدُ لِلَّهِ")  # 'الحمد لله'

Text Processing
---------------

convert_fa_spaces
~~~~~~~~~~~~~~~~~

.. autofunction:: persian.convert_fa_spaces

**Examples:**

.. code-block:: python

   import persian

   # Fix spaces with Persian affixes
   persian.convert_fa_spaces("می روم")  # 'می‌روم'

   # Multiple fixes in one sentence
   persian.convert_fa_spaces("من می روم به خانه ام")  # 'من می‌روم به خانه‌ام'

   # Common prefixes
   persian.convert_fa_spaces("نمی دانم")  # 'نمی‌دانم'

   # Common suffixes
   persian.convert_fa_spaces("کتاب های من")  # 'کتاب‌های من'

decode_url
~~~~~~~~~~

.. autofunction:: persian.decode_url

**Examples:**

.. code-block:: python

   import persian

   # Decode Persian in URL
   url = "https://example.com/%D8%B5%D9%81%D8%AD%D9%87"
   persian.decode_url(url)  # 'https://example.com/صفحه'

   # Full URL with multiple Persian segments
   url = "https://example.com/%D9%85%D9%82%D8%A7%D9%84%D9%87/%D8%A2%D9%85%D9%88%D8%B2%D8%B4"
   persian.decode_url(url)  # 'https://example.com/مقاله/آموزش'

   # Query parameters
   url = "https://example.com/search?q=%D8%AC%D8%B3%D8%AA%D8%AC%D9%88"
   persian.decode_url(url)  # 'https://example.com/search?q=جستجو'

normalize_persian
~~~~~~~~~~~~~~~~~

.. autofunction:: persian.normalize_persian

**Examples:**

.. code-block:: python

   import persian

   # Normalize everything (default)
   persian.normalize_persian("سلام ٣٤٥ می آیم")  # 'سلام ۳۴۵ می‌آیم'

   # Only convert numbers
   persian.normalize_persian("سلام ٣٤٥", convert_characters=False, fix_spacing=False)
   # 'سلام ۳۴۵'

   # Only fix spacing
   persian.normalize_persian("می آیم", convert_numbers=False, convert_characters=False)
   # 'می‌آیم'

   # Custom combination
   persian.normalize_persian(
       "علي ٣٤٥ می آید",
       convert_numbers=True,
       convert_characters=True,
       fix_spacing=False
   )  # 'علی ۳۴۵ می آید'

   # Complete text normalization
   text = "كتاب شماره ٣ را می خوانم"
   persian.normalize_persian(text)  # 'کتاب شماره ۳ را می‌خوانم'
