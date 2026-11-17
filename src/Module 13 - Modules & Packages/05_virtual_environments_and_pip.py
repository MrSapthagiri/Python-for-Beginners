"""Explain how to identify a virtual environment and manage packages."""

import sys

# Module 13: Modules & Packages
# Topic 5: pip, virtual environments, and requirements.txt
#
# This example does not install anything. It shows which interpreter is
# running and whether it appears to be inside a virtual environment.


inside_virtual_environment = sys.prefix != sys.base_prefix
print("Python executable:", sys.executable)
print("Running in a virtual environment:", inside_virtual_environment)


# Typical workflow from a project's root directory:
#
# Windows PowerShell:
#   py -m venv .venv
#   .\.venv\Scripts\Activate.ps1
#   python -m pip install package-name
#   python -m pip freeze > requirements.txt
#   deactivate
#
# macOS or Linux:
#   python3 -m venv .venv
#   source .venv/bin/activate
#   python -m pip install package-name
#   python -m pip freeze > requirements.txt
#   deactivate
#
# Restore recorded dependencies in a newly created environment with:
#   python -m pip install -r requirements.txt
#
# Add .venv/ to .gitignore; share requirements.txt instead of the environment.
