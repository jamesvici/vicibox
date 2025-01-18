# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------
import datetime

# -- Project information -----------------------------------------------------
project = "ViciBox"
copyright = "2005-%d, ViciDial Group" % datetime.datetime.now().year
author = "James Pearson"
release = "12.0"
version = "12.0"
language = 'en'
locale_dirs = ['locale/']
gettext_compact = False

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_rtd_dark_mode",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
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
html_theme_options = {
    'style_nav_header_background': '#00AA0D',
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'collapse_navigation': True,
    'analytics_id': 'G-XXXXXXXXXX'  # Replace with your GA ID
}
#html_logo = 'images/Vicibox_pixel_green_whitebg_20180921.png'
html_favicon = "images/favicon.ico"
html_show_sourcelink = False
htmlhelp_basename = "viciboxdoc"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# SEO Options
html_context = {
    'display_github': True,
    'github_user': 'jamesvici',
    'github_repo': 'vicibox',
    'github_version': 'main/',
    'conf_py_path': 'docs/source/',
}

# Documentation options
html_show_sphinx = False
html_copy_source = False
html_show_sourcelink = False
