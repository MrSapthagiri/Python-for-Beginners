"""Demonstrate importing and using a custom module."""

# Module 13: Modules & Packages
# Topic 3: Creating and using custom modules
#
# calculator_tools.py is a neighboring Python file. Its functions can be
# imported and reused here without copying their implementations.


import calculator_tools
from calculator_tools import add, rectangle_area


# Example 1: Access a function through the module name.
print("Example 1 - Sum:", calculator_tools.add(8, 5))
# Output: Example 1 - Sum: 13

# Example 2: Call a directly imported function.
print("Example 2 - Area:", rectangle_area(4, 6))
# Output: Example 2 - Area: 24

# Example 3: Use another directly imported function.
print("Example 3 - Add:", add(12, 3))
# Output: Example 3 - Add: 15


# Quick review:
# - Put reusable definitions in a separate .py file.
# - Importing runs top-level statements; use the main guard for demo code.
