# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme
import poplar
import os
import sys

sys.path.insert(0, os.path.abspath("../../poplar/"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'poplar'
copyright = '2023, Christian Chapman-Bird'
author = 'Christian Chapman-Bird'
release = poplar.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'numpydoc',
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'autoapi.extension',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# -- Configure autoapi -------------------------------------------------------
autoapi_type = "python"
autoapi_dirs = ["../../poplar"]
autoapi_add_toctree_entry = False
autoapi_options = ["members", "show-inheritance", "show-module-summary"]