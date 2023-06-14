# Configuration file for the Sphinx documentation builder.

# Modules
import datetime
import sphinx_rtd_theme

# -- Project information
project = u'ViciBox'
copyright = u'2005-%d, ViciDial Group' % datetime.datetime.now().year
author = u'James Pearson'
release = u'11.0 Beta'
version = u'11.0 Beta'

# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.blockdiag',
]

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme = 'sphinx_rtd_theme'
html_baseurl = 'https://docs.vicibox.com/'
html_theme_options = { 'style_nav_header_background': '#00AA0D', }
#html_logo = 'images/Vicibox_pixel_green_whitebg_20180921.png'
html_favicon = 'images/favicon.ico'
html_show_sourcelink = False
htmlhelp_basename = 'viciboxdoc'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Font for Block Diagram
blockdiag_fontpath = '/Library/Fonts/Arial.ttf'