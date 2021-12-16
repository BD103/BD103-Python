# -- Project information --
project = "BD103-Python"
author = "BD103"
copyright = "2021, BD103"
version = "2.0.0"
release = version


# -- General configuration --
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "_cache"]
templates_path = ["_templates"]
pygments_style = "stata-dark"
autodoc_default_options = {"members": True, "undoc-members": True}
todo_include_todos = True
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "trio": ("https://trio.readthedocs.io/en/stable/", None),
}


# -- Options for HTML output --
html_theme = "basic"
html_static_path = ["_static"]
html_baseurl = "https://bd103.github.io/BD103-Python"
html_permalink_icon = "#"
