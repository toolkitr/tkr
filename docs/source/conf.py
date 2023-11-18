# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'tkr'
copyright = '2023, toolkitr'
author = 'tlkr.'

release = '0.1.6'
version = '0.1.8'

# -- General configuration

extensions = [
    'tkr.ext.driver',
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
