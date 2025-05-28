import os
import sys
import subprocess

# Run Doxygen automatically (optional)
subprocess.call('doxygen', shell=True)

extensions = [
    'breathe',
]

project = 'My Project'
author = 'Your Name'
release = '1.0'

breathe_projects = {
    "myproject": "../doxy_files/xml/"
}
breathe_default_project = "myproject"

html_theme = 'sphinx_rtd_theme'
