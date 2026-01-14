Installation
============

Install from PyPI
-----------------

The easiest way to install Persian is from PyPI using pip:

.. code-block:: bash

   pip install persian

This will install the latest stable version.

Upgrading
~~~~~~~~~

To upgrade to the latest version:

.. code-block:: bash

   pip install --upgrade persian

Install from Source
-------------------

For development or to get the latest unreleased changes:

Clone the Repository
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/rezkam/persian.git
   cd persian

Install in Development Mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using uv (recommended):

.. code-block:: bash

   uv sync --extra dev

Using pip:

.. code-block:: bash

   pip install -e ".[dev]"

This installs the package in editable mode with development dependencies including:

* pytest (testing)
* pytest-cov (coverage)
* pytest-benchmark (performance testing)
* ty (type checking)
* ruff (linting and formatting)

Install Documentation Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To build the documentation locally:

Using uv:

.. code-block:: bash

   uv sync --extra docs

Using pip:

.. code-block:: bash

   pip install -e ".[docs]"

Verify Installation
-------------------

After installation, verify that Persian is installed correctly:

.. code-block:: python

   import persian
   print(persian.convert_en_numbers("123"))  # Should print: ۱۲۳

Or from the command line:

.. code-block:: bash

   python -c "import persian; print(persian.convert_en_numbers('123'))"

Check Version
~~~~~~~~~~~~~

To check the installed version:

.. code-block:: python

   import persian
   # Check if package is properly installed
   print(persian.__version__)

Virtual Environments
--------------------

We strongly recommend using virtual environments to avoid dependency conflicts.

Using venv (Built-in)
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Create virtual environment
   python -m venv myenv

   # Activate (Linux/macOS)
   source myenv/bin/activate

   # Activate (Windows)
   myenv\Scripts\activate

   # Install Persian
   pip install persian

Using conda
~~~~~~~~~~~

.. code-block:: bash

   # Create conda environment
   conda create -n myenv python

   # Activate environment
   conda activate myenv

   # Install Persian
   pip install persian

Using poetry
~~~~~~~~~~~~

.. code-block:: bash

   # Add Persian to your project
   poetry add persian

Using pipenv
~~~~~~~~~~~~

.. code-block:: bash

   # Install Persian with pipenv
   pipenv install persian

Troubleshooting
---------------

Import Errors
~~~~~~~~~~~~~

If you encounter import errors:

.. code-block:: python

   ModuleNotFoundError: No module named 'persian'

Make sure:

1. Persian is installed: ``pip list | grep persian``
2. You're using the correct Python interpreter
3. Your virtual environment is activated (if using one)

Version Conflicts
~~~~~~~~~~~~~~~~~

If you have version conflicts:

.. code-block:: bash

   # Uninstall old version
   pip uninstall persian

   # Install latest version
   pip install persian

Permission Errors
~~~~~~~~~~~~~~~~~

If you get permission errors on Linux/macOS:

.. code-block:: bash

   # Use --user flag
   pip install --user persian

   # Or use a virtual environment (recommended)
   python -m venv .venv
   source .venv/bin/activate
   pip install persian

Next Steps
----------

* Continue to :doc:`quickstart` for a quick introduction
* See :doc:`examples` for comprehensive examples
* Check the :doc:`../api/core` for detailed API reference
