# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

from pkg_resources import parse_version
from versioneer import get_version


# -- Project information -----------------------------------------------------

project = 'LIGO/Virgo/KAGRA Public Alerts User Guide'
copyright = '2018-2022, LIGO Scientific Collaboration, Virgo Collaboration, KAGRA Collaboration'
author = 'LIGO Scientific Collaboration, Virgo Collaboration, KAGRA Collaboration'

# The full version, including alpha/beta/rc tags
release = get_version()
# The short X.Y version
version = parse_version(release).base_version


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx_tabs.tabs',
    'matplotlib.sphinxext.plot_directive'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'description': 'Primer on public alerts for astronomers from the LIGO, Virgo, and KAGRA gravitational-wave observatories.',
    'fixed_sidebar': True,
    'show_relbars': True,
    'sidebar_collapse': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'contact.html',
        'searchbox.html',
        'funding.html'
    ]
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'LIGOVirgoKAGRAPublicAlertsUserGuidedoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'LIGOVirgoKAGRAPublicAlertsUserGuide.tex', project,
     'LIGO Scientific Collaboration, Virgo Collaboration, KAGRA Collaboration', 'manual'),
]

latex_elements = {
    'releasename': 'Version'
}

latex_appendices = ['changes', 'glossary']

# LaTeX does not support emoji.
# In LaTeX, replace the sparkle emoji (✨) used in early_warning.rst
# with the text "New: ".
latex_elements['preamble'] = '\DeclareUnicodeCharacter{2728}{New: }'

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'ligovirgokagrapublicalertsuserguide', project,
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'LIGOVirgoKAGRAPublicAlertsUserGuide', project,
     author, 'LIGOVirgoKAGRAPublicAlertsUserGuide', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for autosectionlabel extension -------------------------------

autosectionlabel_prefix_document = True


# -- Options for extlinks extension ------------------------------------------

extlinks = {
    'arxiv': ('https://arxiv.org/abs/%s', 'arXiv:'),
    'dcc': ('https://dcc.ligo.org/%s/public', 'LIGO-'),
    'doi': ('https://doi.org/%s', 'doi:')
}


# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'astroplan': ('https://astroplan.readthedocs.io/en/latest/', None),
    'astropy': ('https://docs.astropy.org/en/stable/', None),
    'astropy-healpix': ('https://astropy-healpix.readthedocs.io/en/stable/', None),
    'astropy-regions': ('https://astropy-regions.readthedocs.io/en/latest', None),
    'conda': ('https://docs.conda.io/projects/conda/en/latest/', None),
    'gamma-astro-data-formats': ('https://gamma-astro-data-formats.readthedocs.io/en/latest/', None),
    'gwcelery': ('https://gwcelery.readthedocs.io/en/latest/', None),
    'healpy': ('https://healpy.readthedocs.io/en/stable/', None),
    'ligo.skymap': ('https://lscsoft.docs.ligo.org/ligo.skymap/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pyregion': ('https://pyregion.readthedocs.io/en/latest/', None),
    'python': ('https://docs.python.org/', None),
    'requests': ('https://docs.python-requests.org/en/stable/', None),
    'voevent-parse': ('https://voevent-parse.readthedocs.io/en/stable/', None)
}


# -- Options for sphinxcontrib.spelling extension ----------------------------

try:
    import sphinxcontrib.spelling
except ImportError:
    pass
else:
    extensions += ['sphinxcontrib.spelling']

    from enchant.tokenize import URLFilter
    spelling_filters = [URLFilter]


# -- Options for plot_directive extension ------------------------------------

plot_formats = [('svg', 300), ('pdf', 300)]
plot_html_show_source_link = False
plot_html_show_formats = False
plot_rcparams = {'font.size': 12}


def setup(app):
    app.add_js_file('copybutton.js')


# -- Image format priority ---------------------------------------------------

# Change image format priority so animated gifs are preferred over static SVGs.

import sphinx.builders.dirhtml
import sphinx.builders.singlehtml
import sphinx.builders.html

for builder_class in [sphinx.builders.dirhtml.DirectoryHTMLBuilder,
                      sphinx.builders.singlehtml.SingleFileHTMLBuilder,
                      sphinx.builders.html.StandaloneHTMLBuilder]:
    builder_class.supported_image_types.remove('image/gif')
    builder_class.supported_image_types.insert(0, 'image/gif')

del builder_class
