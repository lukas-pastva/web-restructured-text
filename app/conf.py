html_show_sourcelink = False

project = '{NAME}'
copyright = '{NAME}'
author = '{NAME}'
version = ''
release = '1.0'

extensions = [
]

templates_path = ['_templates']
source_suffix = '.rst'

master_doc = 'index'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = None
html_theme = '{THEME}'
html_static_path = ['_static']
htmlhelp_basename = 'dashboarddoc'
latex_elements = {
}
latex_documents = [
    (master_doc, 'dashboard.tex', '{NAME}',
     '{NAME}', 'manual'),
]

man_pages = [
    (master_doc, 'dashboard', '{NAME}',
     [author], 1)
]

texinfo_documents = [
    (master_doc, '{NAME}', 'v',
     author, '{NAME}', '.',
     'Miscellaneous'),
]

epub_title = project
epub_exclude_files = ['search.html']
