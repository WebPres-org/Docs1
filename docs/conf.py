# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from datetime import datetime



# -- Project information -----------------------------------------------------

#project = 'WebPres'
#copyright = '2021, bigwebx.com'
#author = 'bigwebx.com'
project = u'WebPres'
year = datetime.now().year
copyright = u"%d bigwebx.com" % year



# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- Project Sponsored -----------------------------------------------------




# Sidebar
html_sidebars = {
    '**': [
        'about.html',
        'localtoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html',
    ]
}

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# Them option.
html_theme = 'alabaster'
html_static_path = ['_static']
html_logo = ['_static/webpres-logo.png']
donate_url =
extra_nav_links =
fixed_sidebar = false
html_theme_options = {
    
    'logo': 'webpres-logo.png',
    'description': 'An opnen source cms site builder.',
    'display_version': True,
    'logo_only':False,
    'logo_name':True,
    'show_powered_by': True,
    'github_user': 'WebPres-org',
    'github_repo': 'Docs',
    'github_banner': False,
    'show_related': False,
    'note_bg': '#FFF59C'
    
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
