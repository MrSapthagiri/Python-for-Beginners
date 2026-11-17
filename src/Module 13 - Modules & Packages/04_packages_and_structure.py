"""Demonstrate importing reusable functions from a package."""

# Module 13: Modules & Packages
# Topic 4: Packages and basic project structure
#
# course_utils is a package directory. Its __init__.py exposes selected
# functions, and text_tools.py contains their implementations.


from course_utils import count_words, normalize_name
from course_utils.text_tools import normalize_name as normalize_from_module


# Example 1: Import names exposed by the package.
print("Example 1 - Normalized name:", normalize_name("  ADA   LOVELACE "))
# Output: Example 1 - Normalized name: Ada Lovelace

# Example 2: Use another name exposed by the package.
print("Example 2 - Word count:", count_words("Packages organize related modules"))
# Output: Example 2 - Word count: 4

# Example 3: Import directly from a module inside the package.
print("Example 3 - Direct module import:", normalize_from_module("grace hopper"))
# Output: Example 3 - Direct module import: Grace Hopper


# Quick review:
# - A package groups related modules in a directory.
# - __init__.py can define the names the package makes convenient to import.
