# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os

from datetime import datetime

ROOT_BASE = os.path.abspath(os.path.dirname(__file__))
 
html_context = {
    'current_year': datetime.now().year, # Set the Copyright year of footer
    "show_sphinx": False, # remove 'Powered by Sphinx' at the bottom
}

project = 'RTKIOT GUI'
author = 'RTKIOT GUI'
release = 'v0.0.0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["breathe", 
              "myst_parser", 
              "sphinx_rtd_theme",
              "sphinx.ext.intersphinx",
              "sphinxcontrib.mermaid",
              "sphinx_copybutton"]

myst_enable_extensions = [
    # "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    # "deflist",
    # "dollarmath",
    # "fieldlist",
    # "html_admonition",
    # "html_image",
    "linkify",
    # "replacements",
    # "smartquotes",
    # "strikethrough",
    # "substitution",
    # "tasklist",
]

intersphinx_mapping = {
    'api_en': ('', (os.path.join(ROOT_BASE, '_build', 'en', 'html', 'objects.inv'), None)),
    'api_cn': ('', (os.path.join(ROOT_BASE, '_build', 'cn', 'html', 'objects.inv'), None)),
}

exclude_patterns = []

# The default language to highlight source code in. The default is 'python'.
# The value should be a valid Pygments lexer name, see Showing code examples for more details.
highlight_language = 'c'

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

source_encoding = "utf-8"

# The master toctree document.
master_doc = "index"

# The templates path
templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_show_sourcelink = False
html_show_copyright = False

html_static_path = ['_static']
html_js_files = [
    'js/auth.js',
    'js/custom.js',
    'js/versions.js',
    'js/imgmodal.js',
]

html_logo = './_static/image/logo.png'
html_favicon = "./_static/image/favicon.ico"

html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes"]
html_theme_options = {
    'collapse_navigation' : False,
    'logo_only': True,
    # 在侧边栏显示版本
    'display_version': True,
    'navigation_depth': 10,
}


# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'xelatex'
latex_use_xindy = False
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
    'figure_align': 'H',

    'inputenc': '',
    'utf8extra': '',
    'classoptions': ',openany,oneside',
    'babel': '\\usepackage{babel}',
    'passoptionstopackages': r'''
        \PassOptionsToPackage{bookmarksdepth=5}{hyperref}% depth of pdf bookmarks
    ''',
    'preamble': r'''
        \usepackage{fontspec}
        \setmonofont{DejaVu Sans Mono}
        \usepackage{silence}
        \WarningsOff*
        \usepackage[pipeTables=true]{markdown}
    ''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'RTKIOT GUI.tex', 'RTKIOT GUI Documentation',
     'RTKIOT GUI community', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'RTKIOT GUI', 'RTKIOT GUI Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'RTKIOT GUI', 'RTKIOT GUI Documentation',
     author, 'Contributors of RTKIOT GUI', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Breathe ----------------------------------------------------

breathe_projects = {"HoneyGUI": os.path.join(os.path.dirname(__file__), r"./doxyxml/xml")}
breathe_default_project = "HoneyGUI"
breathe_domain_by_extension = {"h" : "c"}
breathe_implementation_filename_extensions = ['.c', '.cc', '.cpp']


# Example configuration for intersphinx: refer to the Python standard library.

def setup(app):
    from recommonmark.transform import AutoStructify
    app.add_config_value('recommonmark_config', {
            'enable_eval_rst': True,
            'enable_auto_toc_tree': 'True',
            }, True)
    app.add_transform(AutoStructify)
    app.add_css_file('css/custom.css')
    app.add_css_file('css/fontawesome.min.css')
    app.add_css_file('css/auto.number.title.css')
