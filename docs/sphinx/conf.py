"""Sphinx configuration for Persian package documentation."""

import os
import sys
from datetime import datetime

# Add the project root to the path
sys.path.insert(0, os.path.abspath("../.."))

# Get version dynamically from the package
try:
    from persian import __version__
    version = __version__
    release = __version__
except ImportError:
    version = "dev"
    release = "dev"

# Project information
project = "Persian"
copyright = f"{datetime.now().year}, Reza Kamali"
author = "Reza Kamali"

# General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx_autodoc_typehints",
]

# Napoleon settings (for Google/NumPy style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# Autodoc settings
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"

# Autosummary settings
autosummary_generate = True

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# Templates path
templates_path = ["_templates"]

# List of patterns to ignore
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# HTML output options
html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "github_url": "https://github.com/rezkam/persian",
    "use_edit_page_button": True,
    "show_toc_level": 2,
}

html_static_path = []
html_context = {
    "github_user": "rezkam",
    "github_repo": "persian",
    "github_version": "main",
    "doc_path": "docs/sphinx",
}

# HTML additional options
html_show_sourcelink = True
html_show_sphinx = False
html_show_copyright = True

# Output file base name for HTML help builder
htmlhelp_basename = "Persiandoc"
