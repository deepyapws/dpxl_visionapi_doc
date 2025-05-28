import os
import sys
import subprocess

# Optional: run Doxygen automatically when building docs
subprocess.call('doxygen', shell=True)

extensions = [
    'breathe',
    # Add other Sphinx extensions as needed
]
