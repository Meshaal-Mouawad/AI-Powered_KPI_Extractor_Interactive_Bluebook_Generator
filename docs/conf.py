# Configuration file for the Sphinx documentation builder.
import os
import sys

sys.path.insert(0, os.path.abspath(".."))  # To find project modules if needed

# -- Project information -----------------------------------------------------
project = "KPI Bluebook"
copyright = "2025, Meshaal Mouawad"
author = "Meshaal Mouawad"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",  # required to render .. math:: blocks
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Force MathJax v3 (works regardless of Sphinx default)
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

# MathJax v3 config (used by modern Sphinx)
mathjax3_config = {
    "tex": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
    },
    "options": {
        # Only process elements with this class (matches your template)
        "processHtmlClass": "math-equation",
        "ignoreHtmlClass": "tex2jax_ignore",
    },
}

# MathJax v2 fallback (used by older Sphinx)
mathjax_config = {
    "tex2jax": {
        "inlineMath": [["$", "$"], ["\\(", "\\)"]],
        "displayMath": [["$$", "$$"], ["\\[", "\\]"]],
        "processClass": "math-equation",
        "ignoreClass": "tex2jax_ignore",
    }
}

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


def setup(app):
    app.add_css_file("custom.css")
