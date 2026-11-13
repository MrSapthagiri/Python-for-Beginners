# Module 11: Exception Handling
# Topic 3: Multiple exceptions, else, and finally
#
# Use separate except clauses for different responses or a tuple of exception
# types for one shared response. The optional else runs after a successful
# try block; finally runs whether the try succeeds or raises an exception.


# Example 1: Different handlers respond to different exception types
def divide_text(top_text, bottom_text):
    try:
        return int(top_text) / int(bottom_text)
    except ValueError:
        return "Please enter whole-number text."
    except ZeroDivisionError:
        return "The divisor cannot be zero."


print("Example 1 - Invalid number:", divide_text("ten", "2"))
print("Example 1 - Zero divisor:", divide_text("10", "0"))
# Output:
# Example 1 - Invalid number: Please enter whole-number text.
# Example 1 - Zero divisor: The divisor cannot be zero.


# Example 2: Two exception types can share one handler
try:
    int("not a number")
except (TypeError, ValueError) as error:
    print("\nExample 2 - Invalid input:", type(error).__name__)
# Output: Example 2 - Invalid input: ValueError


# Example 3: Catch the specific exception you expect
try:
    {"present": "value"}["missing"]
except KeyError:
    print("\nExample 3 - The requested key is missing.")
# Output: Example 3 - The requested key is missing.


# Example 4: else runs when the try block succeeds
try:
    total = int("17")
except ValueError:
    print("\nExample 4 - Conversion failed.")
else:
    print("\nExample 4 - Conversion succeeded:", total)
# Output: Example 4 - Conversion succeeded: 17


# Example 5: else is skipped when the try block raises a handled exception
try:
    total = int("seventeen")
except ValueError:
    print("\nExample 5 - Conversion failed.")
else:
    print("\nExample 5 - This does not run:", total)
# Output: Example 5 - Conversion failed.


# Example 6: finally runs after a successful try block
try:
    print("\nExample 6 - Work completed.")
finally:
    print("Example 6 - Final step always runs.")
# Output:
# Example 6 - Work completed.
# Example 6 - Final step always runs.


# Example 7: finally also runs after a handled exception
try:
    3 / 0
except ZeroDivisionError:
    print("\nExample 7 - Could not divide.")
finally:
    print("Example 7 - Final step always runs.")
# Output:
# Example 7 - Could not divide.
# Example 7 - Final step always runs.


# Example 8: Combine try, except, else, and finally
try:
    score = int("92")
except ValueError:
    print("\nExample 8 - Score must be a whole number.")
else:
    print("\nExample 8 - Saved score:", score)
finally:
    print("Example 8 - Score check finished.")
# Output:
# Example 8 - Saved score: 92
# Example 8 - Score check finished.


# Example 9: A finally block does not hide an unhandled exception
try:
    try:
        5 / 0
    except ValueError:
        print("\nExample 9 - This handler does not match.")
    finally:
        print("\nExample 9 - Finally runs before the exception continues.")
except ZeroDivisionError as error:
    print("Example 9 - Exception still exists:", type(error).__name__)
# Output:
# Example 9 - Finally runs before the exception continues.
# Example 9 - Exception still exists: ZeroDivisionError


# Example 10: Handle expected conversion errors, then use else for success
def describe_number(text):
    try:
        value = float(text)
    except (TypeError, ValueError):
        return "Not a number"
    else:
        return f"Number: {value:g}"


print("\nExample 10 - Valid:", describe_number("3.5"))
print("Example 10 - Invalid:", describe_number("three"))
# Output:
# Example 10 - Valid: Number: 3.5
# Example 10 - Invalid: Not a number


# Quick review:
# - Use separate handlers if the recovery actions differ.
# - else belongs to the no-exception success path.
# - finally is for work that should happen on both success and failure.
