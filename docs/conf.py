# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Py Running Pace"
copyright = "2023, Guilaume Fuchs"
author = "Guillaume Fuchs"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.napoleon"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# https://pradyunsg.me/furo/
html_theme = "furo"

html_static_path = ["_static"]
# html_logo = "_static/logo.png"

# -- Options for MyST parser -------------------------------------------------
# https://myst-parser.readthedocs.io/

extensions += ["myst_parser"]

myst_enable_extensions = [
    "attrs_block",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#block-attributes
    "attrs_inline",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#inline-attributes
    "colon_fence",  # https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#markdown-figures
]

# -- Options for sphinx-autodoc2 ---------------------------------------------
# https://sphinx-autodoc2.readthedocs.io/en/latest/config.html

extensions += ["autodoc2"]  # https://sphinx-autodoc2.readthedocs.io/

autodoc2_output_dir = "apidocs"
autodoc2_packages = [
    "../pyrunpace",
]
autodoc2_render_plugin = "md"

autodoc2_index_template = """
API Documentation
=================

.. toctree::
   :titlesonly:
{% for package in top_level %}
   {{ package }}
{%- endfor %}
"""
