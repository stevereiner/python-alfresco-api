# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('../../..'))

project = 'Python Alfresco API'
copyright = '2025, Developer'
author = 'Developer'
release = '1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_autodoc_typehints',
    'sphinx.ext.viewcode',        # Add source code links
    'sphinx.ext.intersphinx',     # Cross-reference other docs
    'sphinx.ext.autosummary',     # Generate summary tables
    'sphinx.ext.coverage',        # Documentation coverage
]

templates_path = ['_templates']
exclude_patterns = []

# -- Napoleon Settings (Google/NumPy docstring support) --------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = False
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

# -- Autodoc Settings -------------------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Type hints configuration
typehints_fully_qualified = False
always_document_param_types = True
typehints_document_rtype = True

# -- Autosummary Settings ---------------------------------------------------
autosummary_generate = True

# -- Options for HTML output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # Professional Read the Docs theme
html_static_path = ['_static']

html_theme_options = {
    'analytics_id': '',  # Google Analytics (optional)
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Add custom CSS
html_css_files = [
    'custom.css',
]

# Add favicon and logo
html_favicon = 'favicon.ico'
html_logo = 'logo.png'

# Output file base name for HTML help builder
htmlhelp_basename = 'PythonAlfrescoAPIdoc'

# -- Intersphinx mapping ----------------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'pydantic': ('https://docs.pydantic.dev/', None),
    'httpx': ('https://www.python-httpx.org/', None),
}

# -- Custom CSS to make v1.1 documentation stand out -----------------------
def setup(app):
    app.add_css_file('custom.css')  # Custom styling for v1.1 docs
