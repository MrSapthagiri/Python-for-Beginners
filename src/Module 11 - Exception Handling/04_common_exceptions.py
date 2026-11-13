# Module 11: Exception Handling
# Topic 4: Common built-in exceptions
#
# Python exceptions describe different kinds of problems. Learn the cause
# indicated by the type, then handle the expected case specifically.


# Example 1: ValueError - text cannot be converted to an integer
try:
    int("hello")
except ValueError:
    print("Example 1 - ValueError: use digits for an integer.")
# Output: Example 1 - ValueError: use digits for an integer.


# Example 2: ValueError - a number is outside an application's allowed range
def set_percent(percent):
    """Return percent if it is between 0 and 100; otherwise raise ValueError."""
    if not 0 <= percent <= 100:
        raise ValueError("percent must be from 0 to 100")
    return percent


try:
    set_percent(120)
except ValueError as error:
    print("\nExample 2 - ValueError:", error)
# Output: Example 2 - ValueError: percent must be from 0 to 100


# Example 3: TypeError - incompatible types used together
try:
    message = "age: " + 18  # type: ignore[operator]
except TypeError:
    print("\nExample 3 - TypeError: convert the number or use an f-string.")
# Output: Example 3 - TypeError: convert the number or use an f-string.


# Example 4: TypeError - a function receives the wrong kind of value
try:
    len(25)  # type: ignore[arg-type]
except TypeError:
    print("\nExample 4 - TypeError: this object has no length.")
# Output: Example 4 - TypeError: this object has no length.


# Example 5: IndexError - a list position does not exist
try:
    fruits = ["apple", "pear"]
    print(fruits[2])
except IndexError:
    print("\nExample 5 - IndexError: choose an existing list position.")
# Output: Example 5 - IndexError: choose an existing list position.


# Example 6: KeyError - a dictionary key does not exist
try:
    prices = {"tea": 3}
    print(prices["coffee"])
except KeyError:
    print("\nExample 6 - KeyError: that item has no saved price.")
# Output: Example 6 - KeyError: that item has no saved price.


# Example 7: ZeroDivisionError - denominator is zero
try:
    average = 10 / 0
except ZeroDivisionError:
    print("\nExample 7 - ZeroDivisionError: divisor cannot be zero.")
# Output: Example 7 - ZeroDivisionError: divisor cannot be zero.


# Example 8: NameError - a variable name has not been defined
try:
    raise NameError("name 'student_total' is not defined")
except NameError:
    print("\nExample 8 - NameError: define the name before using it.")
# Output: Example 8 - NameError: define the name before using it.


# Example 9: AttributeError - the requested method is not on this object
try:
    number = 12
    number.append(13)  # type: ignore[attr-defined]
except AttributeError:
    print("\nExample 9 - AttributeError: integers do not have append().")
# Output: Example 9 - AttributeError: integers do not have append().


# Example 10: FileNotFoundError - the requested file does not exist
try:
    open("this_file_is_not_part_of_the_lesson.txt", encoding="utf-8")
except FileNotFoundError:
    print("\nExample 10 - FileNotFoundError: the file was not found.")
# Output: Example 10 - FileNotFoundError: the file was not found.


# Quick review:
# - ValueError: correct general type, unacceptable value.
# - TypeError: incompatible type for an operation.
# - IndexError and KeyError: missing sequence position or mapping key.
# - ZeroDivisionError: division by zero.
# - NameError, AttributeError, and FileNotFoundError have different causes.
