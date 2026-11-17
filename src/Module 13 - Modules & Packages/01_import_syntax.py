"""Demonstrate import, from-import, and aliases."""

# Module 13: Modules & Packages
# Topic 1: Modules, import, and from ... import
#
# Import a module to access its names through the module, or import selected
# names directly. Aliases can make names shorter or clearer.


# Example 1: Import a module and qualify the name with its module.
import math

print("Example 1 - math.pi:", round(math.pi, 4))
# Output: Example 1 - math.pi: 3.1416

# Example 2: Import a selected function directly.
from math import sqrt

print("Example 2 - sqrt(81):", sqrt(81))
# Output: Example 2 - sqrt(81): 9.0

# Example 3: Give an imported module a readable alias.
import datetime as dt

fixed_date = dt.date(2026, 1, 15)
print("Example 3 - Date:", fixed_date)
# Output: Example 3 - Date: 2026-01-15

# Example 4: Give an imported function an alias.
from math import factorial as find_factorial

print("Example 4 - 5 factorial:", find_factorial(5))
# Output: Example 4 - 5 factorial: 120


# Quick review:
# - Explicit imports show where names come from.
# - Avoid wildcard imports such as "from math import *".
