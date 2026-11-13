# Module 11: Exception Handling
# Topic 1: Errors, exceptions, and common Python errors
#
# An error is a general problem; an exception is a Python event describing a
# problem during execution. Syntax errors prevent code from being parsed.
# Runtime exceptions can be handled if the program has a useful response.


# Example 1: A syntax error is detected before the invalid code can run
source = "if True print('missing colon')"
try:
    compile(source, "<example>", "exec")
except SyntaxError as error:
    print("Example 1 - Syntax problem:", error.msg)
# Output: Example 1 - Syntax problem: invalid syntax


# Example 2: Convert a string containing a number
try:
    number = int("25")
    print("\nExample 2 - Converted:", number)
except ValueError:
    print("Example 2 - The text is not an integer.")
# Output: Example 2 - Converted: 25


# Example 3: Invalid numeric text raises ValueError
try:
    int("twenty")
except ValueError as error:
    print("\nExample 3 - Exception type:", type(error).__name__)
# Output: Example 3 - Exception type: ValueError


# Example 4: Adding incompatible types raises TypeError
try:
    _ = "score: " + 10  # type: ignore[operator]
except TypeError as error:
    print("\nExample 4 - Exception type:", type(error).__name__)
# Output: Example 4 - Exception type: TypeError


# Example 5: Use an index within the list's valid range
colors = ["red", "blue"]
print("\nExample 5 - Color:", colors[1])
# Output: Example 5 - Color: blue


# Example 6: Looking up a missing dictionary key raises KeyError
try:
    {"name": "Asha"}["age"]
except KeyError as error:
    print("\nExample 6 - Missing key:", error.args[0])
# Output: Example 6 - Missing key: age


# Example 7: Dividing a number by zero raises ZeroDivisionError
try:
    _ = 10 / 0
except ZeroDivisionError as error:
    print("\nExample 7 - Exception type:", type(error).__name__)
# Output: Example 7 - Exception type: ZeroDivisionError


# Example 8: Using a name that has not been defined raises NameError
try:
    print(undefined_course_name)  # type: ignore[name-defined, reportUndefinedVariable]
except NameError as error:
    print("\nExample 8 - Exception type:", type(error).__name__)
# Output: Example 8 - Exception type: NameError


# Example 9: Calling a string-only method on an integer raises AttributeError
try:
    _ = (42).upper()  # type: ignore[attr-defined, reportAttributeAccessIssue]
except AttributeError as error:
    print("\nExample 9 - Exception type:", type(error).__name__)
# Output: Example 9 - Exception type: AttributeError


# Example 10: A traceback identifies the exception that stopped execution
try:
    int("3.5")
except ValueError as error:
    print("\nExample 10 - Traceback's exception:", type(error).__name__)
    print("Example 10 - Message is available:", bool(str(error)))
# Output:
# Example 10 - Traceback's exception: ValueError
# Example 10 - Message is available: True


# Quick review:
# - Syntax errors concern invalid Python structure; runtime exceptions happen
#   as an operation is being executed.
# - Exception names help explain the cause, but inspect the traceback and code.
# - The next lessons show how to respond to expected exceptions.
