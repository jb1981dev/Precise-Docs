# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Precise Tools Documentation'
copyright = '2025, Precise Tools'
author = 'Jeroen Backx'

release = '1.0'
version = '1.0.0'

# -- General configuration
html_title = 'Precise Tools Documentation'
html_short_title = 'Precise Tools'
html_show_sourcelink = False
html_show_sphinx = False

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),    
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# This dictionary is ONLY for theme-specific options
html_theme_options = {
    'display_version': False,
    # other theme-specific options would go here
}
