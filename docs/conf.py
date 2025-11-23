# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lógica computacional grado 8'
copyright = '2026, Julian Camilo Fonseca Romero, IE John F. Kennedy'
author = 'Julian Camilo Fonseca Romero'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser","sphinx_design"]

myst_enable_extensions = [
    #"amsmath",
    "dollarmath", #ecuaciones matematicas con $
    "tasklist", # listas con casillas de verificacion pero como hacer para que sea editable?
    "colon_fence", #bloques con ::: en vez de ```
    "attrs_inline", # para agregar atributos en linea ejemplo: IMAGENES
    "smartquotes", #comillas inteligentes
    #"linkify", # convierte URLs en enlaces automaticamente
    "fieldlist" # listas de campos
]

myst_number_code_blocks = ["python", "c++"] # Numera bloques de código en los lenguajes especificados
myst_links_external_new_tab = True # Abre enlaces externos en una nueva pestaña
myst_enable_checkboxes = True # Habilita casillas de verificación en las listas de tareas
myst_heading_anchors = 3 # Genera enlaces ancla para los encabezados (niveles 1 a 3)

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
