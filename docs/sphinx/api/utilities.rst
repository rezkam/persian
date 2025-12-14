Utility Functions
=================

Helper functions for detecting and validating Persian text.

Detection Functions
-------------------

contains_persian_digits
~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: persian.contains_persian_digits

**Examples:**

.. code-block:: python

   import persian

   # Check for Persian digits
   persian.contains_persian_digits("۱۲۳")  # True
   persian.contains_persian_digits("123")  # False

   # Mixed content
   persian.contains_persian_digits("سلام ۱۲۳")  # True
   persian.contains_persian_digits("سلام 123")  # False

   # Use in validation
   text = "قیمت: ۱۵۰۰۰"
   if persian.contains_persian_digits(text):
       print("Text contains Persian digits")
   else:
       print("No Persian digits found")

contains_arabic_digits
~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: persian.contains_arabic_digits

**Examples:**

.. code-block:: python

   import persian

   # Check for Arabic digits
   persian.contains_arabic_digits("٣٤٥")  # True
   persian.contains_arabic_digits("۳۴۵")  # False (Persian digits)

   # Mixed content
   persian.contains_arabic_digits("النص ٩٨٧")  # True
   persian.contains_arabic_digits("متن ۹۸۷")  # False

   # Conditional conversion
   text = "العدد ٣٤٥"
   if persian.contains_arabic_digits(text):
       text = persian.convert_ar_numbers(text)
   print(text)  # 'العدد ۳۴۵'

is_persian_text
~~~~~~~~~~~~~~~

.. autofunction:: persian.is_persian_text

**Examples:**

.. code-block:: python

   import persian

   # Pure Persian text
   persian.is_persian_text("سلام")  # True

   # English text
   persian.is_persian_text("Hello")  # False

   # Mixed content (returns True if ANY Persian character exists)
   persian.is_persian_text("Hello سلام")  # True

   # Numbers don't count as Persian characters
   persian.is_persian_text("123")  # False
   persian.is_persian_text("۱۲۳")  # True (Persian digits are Persian characters)

   # Use in content filtering
   def process_text(text):
       if persian.is_persian_text(text):
           return persian.normalize_persian(text)
       return text

   process_text("سلام دنیا")  # Returns normalized text
   process_text("Hello World")  # Returns unchanged

Practical Examples
------------------

Combining Detection and Conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import persian

   def smart_normalize(text):
       """Intelligently normalize text based on its content."""
       if not persian.is_persian_text(text):
           return text

       # Convert Arabic numbers if present
       if persian.contains_arabic_digits(text):
           text = persian.convert_ar_numbers(text)

       # Always normalize Persian text
       return persian.normalize_persian(text)

   # Examples
   smart_normalize("سلام ٣٤٥")  # 'سلام ۳۴۵'
   smart_normalize("Hello 123")  # 'Hello 123' (unchanged)

Input Validation
~~~~~~~~~~~~~~~~

.. code-block:: python

   import persian

   def validate_persian_input(text):
       """Validate that input contains Persian characters."""
       if not isinstance(text, str):
           raise TypeError("Input must be a string")

       if not text:
           raise ValueError("Input cannot be empty")

       if not persian.is_persian_text(text):
           raise ValueError("Input must contain Persian characters")

       return True

   # Usage
   try:
       validate_persian_input("سلام")  # Returns True
       validate_persian_input("Hello")  # Raises ValueError
   except ValueError as e:
       print(f"Validation error: {e}")

Content Detection
~~~~~~~~~~~~~~~~~

.. code-block:: python

   import persian

   def analyze_text(text):
       """Analyze text content and return statistics."""
       return {
           "is_persian": persian.is_persian_text(text),
           "has_persian_digits": persian.contains_persian_digits(text),
           "has_arabic_digits": persian.contains_arabic_digits(text),
           "length": len(text),
       }

   # Example
   text = "سال ۱۴۰۲ میلادی"
   stats = analyze_text(text)
   print(stats)
   # {
   #     'is_persian': True,
   #     'has_persian_digits': True,
   #     'has_arabic_digits': False,
   #     'length': 16
   # }
