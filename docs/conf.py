#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# MSMBuilder documentation build configuration file.
#
# The docs are narrative pages only (no autodoc), so building them does not
# require msmbuilder to be installed or compiled.

import os
import re

# -- General configuration ------------------------------------------------

extensions = []

templates_path = []
source_suffix = '.rst'
master_doc = 'index'

project = 'MSMBuilder'
copyright = '2016, Stanford University and the Authors'


def _read_version():
    """Read VERSION from setup.py without importing msmbuilder."""
    setup_py = os.path.join(os.path.dirname(__file__), '..', 'setup.py')
    with open(setup_py) as f:
        match = re.search(r"^VERSION\s*=\s*['\"]([^'\"]+)['\"]", f.read(),
                          re.MULTILINE)
    return match.group(1) if match else 'unknown'


release = _read_version()
version = '.'.join(release.split('.')[:2])

exclude_patterns = ['_build', 'package-guide']

pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

try:
    import sphinx_rtd_theme  # noqa: F401
    html_theme = 'sphinx_rtd_theme'
except ImportError:
    html_theme = 'alabaster'

html_logo = '_static/logo-200px.png'
html_static_path = ['_static']
htmlhelp_basename = 'MSMBuilderdoc'
