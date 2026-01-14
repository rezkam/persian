Contributing
============

Thank you for your interest in contributing to the Persian library! This document provides guidelines and instructions for contributing.

Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

* Python 3.10 or higher
* `uv <https://docs.astral.sh/uv/>`_ (modern Python package manager)
* Git
* Familiarity with pytest for testing
* Understanding of Persian language processing

Setting Up Development Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Fork the repository** on GitHub

2. **Clone your fork**:

   .. code-block:: bash

      git clone https://github.com/YOUR_USERNAME/persian.git
      cd persian

3. **Install uv** (if not already installed):

   .. code-block:: bash

      # macOS/Linux
      curl -LsSf https://astral.sh/uv/install.sh | sh

      # Windows
      powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

4. **Install development dependencies**:

   .. code-block:: bash

      uv sync --extra dev

5. **Set up pre-commit hooks** (optional but recommended):

   .. code-block:: bash

      make setup-hooks

6. **Verify installation**:

   .. code-block:: bash

      make test
      make type-check

Development Workflow
--------------------

Creating a Feature Branch
~~~~~~~~~~~~~~~~~~~~~~~~~

Always create a new branch for your work:

.. code-block:: bash

   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix

Code Style
~~~~~~~~~~

We use **Ruff** for both linting and formatting, providing a fast, unified tool for code quality:

**Format code**:

.. code-block:: bash

   make format
   # Or directly:
   uv run ruff format persian tests
   uv run ruff check --fix persian tests

**Check linting**:

.. code-block:: bash

   make lint
   # Or directly:
   uv run ruff check persian tests

**Run all checks** (lint, format check, type check):

.. code-block:: bash

   make check

Type Checking
~~~~~~~~~~~~~

All code must pass ty type checking:

.. code-block:: bash

   make type-check
   # Or directly:
   uv run ty check persian

Add type hints to all functions:

.. code-block:: python

   def convert_en_numbers(input_str: str) -> str:
       """Convert English digits to Persian digits."""
       # Implementation

Writing Tests
~~~~~~~~~~~~~

All new features and bug fixes must include tests.

**Test file structure**:

.. code-block:: text

   tests/
   ├── test_persian.py
   └── test_performance.py

**Write a test**:

.. code-block:: python

   import pytest
   import persian

   def test_convert_en_numbers():
       """Test English to Persian number conversion."""
       assert persian.convert_en_numbers("123") == "۱۲۳"
       assert persian.convert_en_numbers("") == ""

   def test_convert_en_numbers_validation():
       """Test input validation."""
       with pytest.raises(TypeError):
           persian.convert_en_numbers(123)

       with pytest.raises(ValueError):
           persian.convert_en_numbers(None)

**Run tests**:

.. code-block:: bash

   # Run all tests
   make test
   # Or directly:
   uv run pytest

   # Run specific test
   uv run pytest tests/test_persian.py::test_convert_en_numbers

Documentation
~~~~~~~~~~~~~

Update documentation for any changes:

1. **Docstrings**: Use Google style docstrings

   .. code-block:: python

      def my_function(input_str: str) -> str:
          """One-line summary.

          Longer description if needed.

          Args:
              input_str: Description of parameter.

          Returns:
              Description of return value.

          Raises:
              TypeError: If input_str is not a string.
              ValueError: If input_str is None.

          Examples:
              >>> my_function("test")
              'result'
          """

2. **Update relevant .rst files** in ``docs/sphinx/``

3. **Build documentation locally**:

   .. code-block:: bash

      make install-docs  # Install docs dependencies
      make docs
      # View at docs/sphinx/_build/html/index.html

Committing Changes
------------------

Commit Message Format
~~~~~~~~~~~~~~~~~~~~~

Write clear, descriptive commit messages:

.. code-block:: text

   Short summary (50 chars or less)

   More detailed explanation if necessary. Wrap at 72 characters.

   - Bullet points are okay
   - Use present tense: "Add feature" not "Added feature"
   - Reference issues: "Fixes #123" or "Relates to #456"

**Examples**:

.. code-block:: text

   Add support for removing Arabic diacritics

   Implement remove_arabic_diacritics() function to strip tashkeel
   characters from Arabic/Persian text.

   Fixes #42

.. code-block:: text

   Fix spacing issue in convert_fa_spaces

   The function was not handling multiple consecutive spaces correctly.
   Updated regex pattern to match all cases.

   Fixes #67

Pre-commit Checklist
~~~~~~~~~~~~~~~~~~~~

Before committing, ensure:

- [ ] Code follows style guidelines (``make format``)
- [ ] All linting passes (``make lint``)
- [ ] All tests pass (``make test``)
- [ ] Type checking passes (``make type-check``)
- [ ] Coverage doesn't decrease
- [ ] Documentation is updated
- [ ] Commit message is clear

Submitting a Pull Request
--------------------------

Preparing Your PR
~~~~~~~~~~~~~~~~~

1. **Update your branch**:

   .. code-block:: bash

      git fetch upstream
      git rebase upstream/main

2. **Push to your fork**:

   .. code-block:: bash

      git push origin feature/your-feature-name

3. **Create pull request** on GitHub

PR Description Template
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: markdown

   ## Description
   Brief description of changes

   ## Motivation
   Why is this change needed?

   ## Changes
   - List of changes made
   - Each on a new line

   ## Testing
   How was this tested?

   ## Checklist
   - [ ] Tests added/updated
   - [ ] Documentation updated
   - [ ] Type hints added
   - [ ] All tests pass
   - [ ] Code follows style guidelines

Code Review Process
~~~~~~~~~~~~~~~~~~~

1. Maintainers will review your PR
2. Address any requested changes
3. Once approved, your PR will be merged

Types of Contributions
----------------------

Bug Fixes
~~~~~~~~~

Found a bug? Please:

1. **Check existing issues** to avoid duplicates
2. **Create an issue** describing the bug
3. **Submit a PR** with the fix and tests

Feature Requests
~~~~~~~~~~~~~~~~

Have an idea for a new feature?

1. **Create an issue** to discuss the feature
2. **Wait for approval** before implementing
3. **Submit a PR** with implementation and tests

Documentation
~~~~~~~~~~~~~

Documentation improvements are always welcome:

* Fix typos
* Improve examples
* Add missing documentation
* Clarify existing docs

Performance Improvements
~~~~~~~~~~~~~~~~~~~~~~~~

Performance PRs should include:

* Benchmarks showing improvement
* Explanation of the optimization
* Tests ensuring correctness

Testing
-------

Running the Full Test Suite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Run all tests with coverage
   make test

   # Run benchmarks
   uv run pytest tests/test_performance.py --benchmark-only

Writing Good Tests
~~~~~~~~~~~~~~~~~~

* Test both success and failure cases
* Use descriptive test names
* Include edge cases
* Test error handling

.. code-block:: python

   def test_convert_en_numbers_empty_string():
       """Empty string should return empty string."""
       assert persian.convert_en_numbers("") == ""

   def test_convert_en_numbers_no_digits():
       """String without digits should be unchanged."""
       assert persian.convert_en_numbers("hello") == "hello"

   def test_convert_en_numbers_mixed_content():
       """Mixed content should only convert digits."""
       assert persian.convert_en_numbers("test 123") == "test ۱۲۳"

Community Guidelines
--------------------

Code of Conduct
~~~~~~~~~~~~~~~

* Be respectful and inclusive
* Welcome newcomers
* Provide constructive feedback
* Focus on the code, not the person

Getting Help
~~~~~~~~~~~~

* **GitHub Issues**: For bugs and feature requests
* **GitHub Discussions**: For questions and general discussion
* **Documentation**: Check docs first

Recognition
~~~~~~~~~~~

Contributors will be:

* Listed in the README
* Credited in release notes
* Thanked in the project

Release Process
---------------

For Maintainers
~~~~~~~~~~~~~~~

1. Create release tag (version auto-detected by setuptools-scm)
2. GitHub Actions will automatically build and publish to PyPI
3. Create GitHub release with changelog

Resources
---------

* **Repository**: https://github.com/rezkam/persian
* **Documentation**: https://persian.readthedocs.io
* **Issue Tracker**: https://github.com/rezkam/persian/issues
* **PyPI**: https://pypi.org/project/persian

Thank You!
----------

Your contributions make this project better. Thank you for taking the time to contribute!
