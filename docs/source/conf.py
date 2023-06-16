# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------
import datetime

# -- Project information -----------------------------------------------------
project = "ViciBox"
copyright = "2005-%d, ViciDial Group" % datetime.datetime.now().year
author = "James Pearson"
release = "11.0 Beta"
version = "11.0 Beta"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_baseurl = "https://docs.vicibox.com/"
html_theme_options = { 'style_nav_header_background': '#00AA0D', }
#html_logo = 'images/Vicibox_pixel_green_whitebg_20180921.png'
html_favicon = "images/favicon.ico"
html_show_sourcelink = False
htmlhelp_basename = "viciboxdoc"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
