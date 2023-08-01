# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Summoning Frontier'
copyright = '2023, Kai Sforza'
author = 'Kai Sforza'
release = '1.0'
version = release
language = 'en'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.extlinks',
    'sphinx.ext.todo'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'Ideas/bad', 'README.rst', '.venv']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_title = f'Summoning Frontier {release}'
html_css_files = ['style/customs.css',]

# -- Options for epub output
suppress_warnings = [
    'epub.unknown_project_files'
]
epub_cover = ('_static/cover.png', '')

## Okay this is hacky af
exclude_epub = []
for root, dirs, files in os.walk('_images/examples/'):
  exclude_epub += ['_build/epub/' + root + f for f in files]
epub_exclude_files = exclude_epub
epub_max_image_width = 1236
epub_fix_images = True

# For skipping unicode stuff.
latex_engine = 'lualatex'
