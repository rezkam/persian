Migration Guide
===============

This guide helps you migrate from older versions of the Persian library to version 1.0.0.

Migration to v1.0.0
-------------------

Overview
~~~~~~~~

Version 1.0.0 is a major release that brings significant improvements while maintaining backward compatibility for supported Python versions.

Breaking Changes
~~~~~~~~~~~~~~~~

Python Version Requirement
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Version 1.0.0 requires Python 3.10 or higher** (previously 3.6+).

**Reason**: Python 3.6-3.9 have all reached end-of-life and no longer receive security updates.

**Migration Path**:

* If you're on Python 3.10+: No code changes needed, just update the package
* If you're on Python 3.6-3.9: Either upgrade Python or pin to ``persian<1.0.0``

.. code-block:: bash

   # For Python 3.10+
   pip install --upgrade persian

   # For Python 3.6-3.9 (legacy)
   pip install "persian<1.0.0"

What's New in v1.0.0
~~~~~~~~~~~~~~~~~~~~

Performance Improvements
^^^^^^^^^^^^^^^^^^^^^^^^

Major performance enhancements:

* **3-5× faster** number and keyboard conversions using ``str.translate``
* **2-3× faster** spacing fixes with pre-compiled regex
* **~50% lower** memory usage on large strings

No code changes needed - your code automatically benefits from these improvements.

Type Hints
^^^^^^^^^^

Full type hints support with ``py.typed`` marker:

.. code-block:: python

   from persian import convert_en_numbers

   result: str = convert_en_numbers("123")  # ✔️ mypy is satisfied

Input Validation
^^^^^^^^^^^^^^^^

All functions now validate inputs and raise clear exceptions:

.. code-block:: python

   import persian

   # Before v1.0.0: might crash or give unexpected results
   # After v1.0.0: clear error messages
   try:
       persian.convert_en_numbers(None)
   except ValueError as e:
       print(e)  # "input_str cannot be None"

   try:
       persian.convert_en_numbers(123)
   except TypeError as e:
       print(e)  # "input_str must be str, got int"

New Functions
^^^^^^^^^^^^^

Several new utility functions:

.. code-block:: python

   import persian

   # Normalize Persian text (all-in-one)
   persian.normalize_persian("سلام ٣٤٥ می آیم")

   # Check for Persian digits
   persian.contains_persian_digits("۱۲۳")  # True

   # Check for Arabic digits
   persian.contains_arabic_digits("٣٤٥")  # True

   # Check for Persian text
   persian.is_persian_text("سلام")  # True

   # Remove Arabic diacritics
   persian.remove_arabic_diacritics("مَرحَباً")  # "مرحبا"

Deprecated Functions
~~~~~~~~~~~~~~~~~~~~

CamelCase function names are deprecated but still work with warnings:

.. code-block:: python

   import persian

   # Deprecated (still works but shows warning)
   persian.enToPersianNumb("123")  # DeprecationWarning

   # Recommended
   persian.convert_en_numbers("123")  # No warning

Deprecation Mapping
^^^^^^^^^^^^^^^^^^^

Replace deprecated functions with their modern equivalents:

+---------------------------+-----------------------------+
| Deprecated                | Use Instead                 |
+===========================+=============================+
| ``enToPersianNumb()``     | ``convert_en_numbers()``    |
+---------------------------+-----------------------------+
| ``enToPersianChar()``     | ``convert_en_characters()`` |
+---------------------------+-----------------------------+
| ``arToPersianNumb()``     | ``convert_ar_numbers()``    |
+---------------------------+-----------------------------+
| ``arToPersianChar()``     | ``convert_ar_characters()`` |
+---------------------------+-----------------------------+

Migration Example
^^^^^^^^^^^^^^^^^

Before:

.. code-block:: python

   import persian

   # Old style (still works with warnings)
   result = persian.enToPersianNumb("123")
   text = persian.arToPersianChar("علي")

After:

.. code-block:: python

   import persian

   # New style (recommended)
   result = persian.convert_en_numbers("123")
   text = persian.convert_ar_characters("علي")

Upgrading from Specific Versions
---------------------------------

From v0.x to v1.0.0
~~~~~~~~~~~~~~~~~~~

1. **Check Python version**:

   .. code-block:: bash

      python --version  # Must be 3.10+

2. **Update package**:

   .. code-block:: bash

      pip install --upgrade persian

3. **Replace deprecated functions** (optional but recommended):

   .. code-block:: python

      # Find deprecated usage
      grep -r "enToPersianNumb\|arToPersianChar" .

4. **Add type hints** (optional):

   .. code-block:: python

      from persian import convert_en_numbers

      def process_text(text: str) -> str:
          return convert_en_numbers(text)

5. **Run tests** to ensure everything works.

Common Migration Issues
-----------------------

Issue: Import Error
~~~~~~~~~~~~~~~~~~~

**Problem**:

.. code-block:: python

   ModuleNotFoundError: No module named 'persian'

**Solution**:

Ensure Persian is installed for the correct Python version:

.. code-block:: bash

   python3.10 -m pip install persian
   # Or
   python3.11 -m pip install persian

Issue: Python Version Too Old
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**:

.. code-block:: text

   ERROR: Package 'persian' requires a different Python: 3.9.0 not in '>=3.10'

**Solution**:

Either upgrade Python or use the legacy version:

.. code-block:: bash

   # Option 1: Upgrade Python (recommended)
   # Install Python 3.10+ from python.org

   # Option 2: Use legacy version
   pip install "persian<1.0.0"

Issue: Type Errors with mypy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**:

.. code-block:: text

   error: Skipping analyzing 'persian': found module but no type hints

**Solution**:

Update to v1.0.0+ which includes ``py.typed``:

.. code-block:: bash

   pip install --upgrade persian

Issue: Deprecation Warnings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**:

.. code-block:: text

   DeprecationWarning: enToPersianNumb is deprecated, use convert_en_numbers

**Solution**:

Replace with modern function names:

.. code-block:: python

   # Before
   persian.enToPersianNumb("123")

   # After
   persian.convert_en_numbers("123")

Testing Your Migration
-----------------------

Run this test script to verify your migration:

.. code-block:: python

   import persian

   def test_migration():
       """Test that Persian library works correctly after migration."""

       # Test number conversions
       assert persian.convert_en_numbers("123") == "۱۲۳"
       assert persian.convert_fa_numbers("۱۲۳") == "123"
       assert persian.convert_ar_numbers("٣٤٥") == "۳۴۵"

       # Test character conversions
       assert persian.convert_en_characters("sghl") == "سلام"
       assert persian.convert_ar_characters("علي") == "علی"

       # Test text processing
       assert "می‌روم" == persian.convert_fa_spaces("می روم")

       # Test normalization
       result = persian.normalize_persian("سلام ٣٤٥ می آیم")
       assert "۳۴۵" in result
       assert "‌" in result  # ZWNJ

       # Test detection
       assert persian.contains_persian_digits("۱۲۳") is True
       assert persian.is_persian_text("سلام") is True

       print("✅ All migration tests passed!")

   if __name__ == "__main__":
       test_migration()

Save this as ``test_migration.py`` and run:

.. code-block:: bash

   python test_migration.py

Getting Help
------------

If you encounter migration issues:

1. **Check the documentation**: https://persian.readthedocs.io
2. **Search existing issues**: https://github.com/rezkam/persian/issues
3. **Create a new issue**: Include Python version, Persian version, and error message

Next Steps
----------

* Read the :doc:`user-guide/quickstart` for v1.0.0 features
* Check :doc:`api/core` for complete API reference
* See :doc:`user-guide/examples` for practical examples
