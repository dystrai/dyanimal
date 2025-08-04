from csv import DictReader
from pathlib import Path

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

conf_path: Path = Path(__file__)
emojis_path: Path = conf_path.parent/"_static"/"animais-emojis.csv"
if emojis_path.exists() and emojis_path.is_file():
    reader = DictReader(emojis_path.open(mode='r', encoding='utf-8'))
    myst_substitutions = {line["nome"]:line["emoji"] for line in reader}

project = 'Dyanimal'
copyright = '2025, Jurandy Soares'
author = 'Jurandy Soares'
release = '2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [    
    'myst_parser',
    'sphinx_tabs.tabs',
    'sphinxcontrib.youtube'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = html_short_title = project

myst_enable_extensions = {
#    "amsmath",
    "attrs_inline",
#    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
#    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",    
}

myst_url_schemes = {
    "asciinema": "https://asciinema.org/a/{{path}}?{{query}}",
    "http": None,
    "https": None,
    "wikien": "https://en.wikipedia.org/wiki/{{path}}#{{fragment}}",
    "wikies": "https://es.wikipedia.org/wiki/{{path}}#{{fragment}}",
    "wikipt": "https://pt.wikipedia.org/wiki/{{path}}#{{fragment}}",
    "doi": "https://doi.org/{{path}}",
    # "gh-issue": {
    #     "url": "https://github.com/executablebooks/MyST-Parser/issue/{{path}}#{{fragment}}",
    #     "title": "Issue #{{path}}",
    #     "classes": ["github"],
    # },
}


