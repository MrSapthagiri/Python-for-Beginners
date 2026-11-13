"""Demonstrate handling common exceptions with try and except."""

from typing import Any, cast

# pylint: disable=invalid-name
# Module 11: Exception Handling
# Topic 2: try and except
#
# Put a statement that may fail in a try block. Use an except clause to name
# the expected exception and provide a useful response. A caught exception
# does not have to stop the whole program.


# Example 1: Convert valid text to an integer
try:
    count = int("8")
except ValueError:
    print("Example 1 - Enter a whole number.")
else:
    print("Example 1 - Count:", count)
# Output: Example 1 - Count: 8


# Example 2: Handle text that cannot be converted
try:
    count = int("eight")
except ValueError:
    print("\nExample 2 - That is not a whole number.")
# Output: Example 2 - That is not a whole number.


# Example 3: Handle division by zero
try:
    result = 12 / 0
except ZeroDivisionError:
    print("\nExample 3 - A divisor cannot be zero.")
# Output: Example 3 - A divisor cannot be zero.


# Example 4: Handle an index that is not present
colors = ["red", "green"]
try:
    selected_color = colors[5]
except IndexError:
    print("\nExample 4 - No color exists at that position.")
# Output: Example 4 - No color exists at that position.


# Example 5: Handle a missing dictionary key
student = {"name": "Mina"}
try:
    grade = student["grade"]
except KeyError:
    print("\nExample 5 - Grade has not been recorded.")
# Output: Example 5 - Grade has not been recorded.


# Example 6: Get the exception details with "as"
try:
    int("five")
except ValueError as error:
    print("\nExample 6 - Details:", error)
# Output: Example 6 - Details: invalid literal for int() with base 10: 'five'


# Example 7: Continue with a fallback value after a handled exception
try:
    retry_count = int("many")
except ValueError:
    retry_count = 0
print("\nExample 7 - Retry count:", retry_count)
# Output: Example 7 - Retry count: 0


# Example 8: The try block can hold more than one operation
try:
    numerator = int("20")
    denominator = int("4")
    quotient = numerator / denominator
except ValueError:
    print("\nExample 8 - Please use numeric text.")
except ZeroDivisionError:
    print("\nExample 8 - The divisor cannot be zero.")
else:
    print("\nExample 8 - Quotient:", quotient)
# Output: Example 8 - Quotient: 5.0


# Example 9: Only the named exception is handled
try:
    message = "score: " + cast(Any, 10)
except ValueError:
    print("\nExample 9 - This handles invalid values.")
except TypeError:
    print("\nExample 9 - Types cannot be combined this way.")
# Output: Example 9 - Types cannot be combined this way.


# Example 10: Successful try statements skip except
try:
    message = "Python".upper()
except AttributeError:
    print("\nExample 10 - The string operation was unavailable.")
else:
    print("\nExample 10 - Message:", message)
# Output: Example 10 - Message: PYTHON


# Quick review:
# - Match an except clause to the kind of problem you know how to handle.
# - The "as error" form makes the exception object available in the handler.
# - Code after a completed try/except can continue normally.
