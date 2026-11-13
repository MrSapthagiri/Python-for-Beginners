# Module 11: Exception Handling
# Topic 5: raise and basic custom exception handling
#
# Use raise when a function cannot perform its job with the supplied value.
# Built-in exceptions are suitable for many invalid arguments. A custom
# exception is a named class derived from Exception for an application rule.


# Example 1: Raise ValueError when a number is below zero
def set_temperature(celsius):
    if celsius < 0:
        raise ValueError("temperature must not be below zero")
    return celsius


try:
    print("Example 1 - Temperature:", set_temperature(20))
    set_temperature(-5)
except ValueError as error:
    print("Example 1 - ValueError:", error)
# Output:
# Example 1 - Temperature: 20
# Example 1 - ValueError: temperature must not be below zero


# Example 2: Raise TypeError when an argument has the wrong type
def show_name(name):
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    return name.title()


try:
    show_name(7)
except TypeError as error:
    print("\nExample 2 - TypeError:", error)
# Output: Example 2 - TypeError: name must be a string


# Example 3: Use a condition instead of an exception for normal branching
discount_code = ""
if discount_code:
    print("\nExample 3 - Apply the code.")
else:
    print("\nExample 3 - No discount code was entered.")
# Output: Example 3 - No discount code was entered.


# Example 4: Define and raise a custom exception
class InvalidAgeError(Exception):
    """Raised when an age is outside the accepted range."""


def validate_age(age):
    if age < 0:
        raise InvalidAgeError("age cannot be negative")
    return age


try:
    validate_age(-1)
except InvalidAgeError as error:
    print("\nExample 4 - InvalidAgeError:", error)
# Output: Example 4 - InvalidAgeError: age cannot be negative


# Example 5: Give the custom exception a docstring and catch its own type
class OutOfStockError(Exception):
    """Raised when a requested quantity is not available."""


available = 3
requested = 5
try:
    if requested > available:
        raise OutOfStockError("not enough items in stock")
except OutOfStockError as error:
    print("\nExample 5 - Order rejected:", error)
# Output: Example 5 - Order rejected: not enough items in stock


# Example 6: Catch a custom exception separately from a built-in exception
class InvalidCodeError(Exception):
    """Raised when a code does not match the required format."""


def read_code(text):
    if not text.isdigit():
        raise InvalidCodeError("code must contain digits only")
    return int(text)


for code_text in ("42", "four"):
    try:
        print("\nExample 6 - Code:", read_code(code_text))
    except InvalidCodeError as error:
        print("\nExample 6 - Invalid code:", error)
# Output:
# Example 6 - Code: 42
# Example 6 - Invalid code: code must contain digits only


# Example 7: Raise a built-in exception with a clear message
def calculate_average(total, count):
    if count == 0:
        raise ZeroDivisionError("cannot average zero items")
    return total / count


try:
    calculate_average(0, 0)
except ZeroDivisionError as error:
    print("\nExample 7 - Average unavailable:", error)
# Output: Example 7 - Average unavailable: cannot average zero items


# Example 8: Re-raise an exception after recording a simple message
try:
    int("invalid")
except ValueError:
    print("\nExample 8 - Conversion failed; passing the problem onward.")
    try:
        raise
    except ValueError as error:
        print("Example 8 - Re-raised type:", type(error).__name__)
# Output:
# Example 8 - Conversion failed; passing the problem onward.
# Example 8 - Re-raised type: ValueError


# Example 9: A custom exception may inherit from a more specific exception
class InvalidScoreError(ValueError):
    """Raised when a score is outside the 0-to-100 range."""


def validate_score(score):
    if not 0 <= score <= 100:
        raise InvalidScoreError("score must be from 0 to 100")
    return score


try:
    validate_score(101)
except ValueError as error:
    print("\nExample 9 - Caught as ValueError:", type(error).__name__)
# Output: Example 9 - Caught as ValueError: InvalidScoreError


# Example 10: Handle validation at the point where a useful response is possible
class EmptyNameError(Exception):
    """Raised when a required name is empty."""


def make_greeting(name):
    if not name.strip():
        raise EmptyNameError("name cannot be empty")
    return f"Hello, {name.strip()}!"


try:
    greeting = make_greeting("   ")
except EmptyNameError as error:
    print("\nExample 10 - Please provide a name:", error)
else:
    print("\nExample 10 -", greeting)
# Output: Example 10 - Please provide a name: name cannot be empty


# Quick review:
# - Use raise to state that an operation cannot continue with its input.
# - Custom exceptions should have descriptive names and inherit from
#   Exception (or a suitable specific exception).
# - Catch exceptions where you can recover or explain the problem usefully.
