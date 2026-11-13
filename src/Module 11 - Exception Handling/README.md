# Module 11: Exception Handling

## Module overview

Programs can encounter problems while they run: a user may enter text where a
number is expected, a list index may not exist, or a calculation may divide by
zero. **Exception handling** lets a program recognize expected runtime
problems, respond clearly, and continue or stop in a controlled way.

This module explains the difference between syntax errors and runtime
exceptions, the `try` and `except` statements, handling several exception
types, the `else` and `finally` clauses, common built-in exceptions, `raise`,
and basic custom exceptions.

## Learning outcomes

After completing this module, you should be able to:

- Distinguish a syntax error from an exception raised while a program runs.
- Explain the purpose of `try` and `except`.
- Catch a specific exception instead of hiding every possible problem.
- Handle more than one exception type with separate or grouped handlers.
- Describe when `else` and `finally` run.
- Recognize `ValueError`, `TypeError`, `IndexError`, `KeyError`, and
  `ZeroDivisionError`.
- Raise a suitable exception when a function receives invalid data.
- Define and handle a simple custom exception.

## Important definitions

### Error and exception

An **error** is a general term for a problem that prevents a program from doing
what was intended. Python uses different exception types to describe many
problems. In everyday conversation, people may call all problems "errors";
in Python code, the specific exception type tells us what kind of problem
occurred.

A **syntax error** means Python cannot parse the code, for example because a
colon or closing parenthesis is missing. It is normally reported before the
affected program starts running. An **exception** is an event raised while
Python executes code. An exception that is not handled stops the current
program flow and displays a traceback.

### Exception handling

**Exception handling** is the process of responding to exceptions using
`try`, `except`, `else`, and `finally`. It does not mean ignoring problems:
handle only exceptions for which the program has a useful response, and give
the user or caller an accurate result.

```python
try:
    quantity = int("12")
except ValueError:
    print("Please provide a whole number.")
else:
    print("Quantity:", quantity)
finally:
    print("Input check finished.")
```

Output:

```text
Quantity: 12
Input check finished.
```

### The exception hierarchy

Most built-in exceptions inherit from `Exception`. A handler for `Exception`
can therefore catch many different programming and runtime problems. Beginners
should usually catch the specific exception they expect, such as `ValueError`,
rather than catch `Exception` broadly. `BaseException` is above `Exception`;
it also includes process-control exceptions such as `KeyboardInterrupt` and
`SystemExit`, so it is rarely appropriate to catch.

## Topics and files

### 1. Errors, exceptions, and common Python errors

File: [`01_errors_and_exceptions.py`](01_errors_and_exceptions.py)

Introduces syntax errors, runtime exceptions, tracebacks, and common
programming mistakes. It demonstrates how to inspect a syntax error safely
using `compile()` without putting invalid syntax directly into the lesson
file.

### 2. `try` and `except`

File: [`02_try_and_except.py`](02_try_and_except.py)

Place the statements that may raise an expected exception inside `try`. Place
the response in an `except` clause that names the exception type.

```python
try:
    age = int("not a number")
except ValueError:
    print("Age must be a whole number.")
```

### 3. Multiple exceptions, `else`, and `finally`

File: [`03_multiple_exceptions_else_finally.py`](03_multiple_exceptions_else_finally.py)

- Use multiple `except` clauses when each kind of failure needs a different
  response.
- Use `except (TypeError, ValueError)` when different exception types need
  the same response.
- `else` runs only if the `try` block raised no exception handled by these
  clauses.
- `finally` runs whether the `try` block succeeds or raises an exception.
  It is useful for cleanup that must happen either way. A `finally` block
  does not make an exception disappear.

### 4. Common exceptions

File: [`04_common_exceptions.py`](04_common_exceptions.py)

| Exception | Typical cause |
|---|---|
| `ValueError` | A value has the right general type but is not acceptable, such as `int("hello")`. |
| `TypeError` | An operation or function receives an incompatible type, such as `"3" + 3`. |
| `IndexError` | A sequence index is outside the available positions. |
| `KeyError` | A dictionary key is missing. |
| `ZeroDivisionError` | A number is divided by zero. |
| `NameError` | A name is used before it has been defined. |
| `AttributeError` | An object does not have the requested attribute or method. |
| `FileNotFoundError` | An operation tries to open a file that cannot be found. |

These are not the only exception types in Python. Use the exception named by
the traceback and consider what input or operation caused it.

### 5. `raise` and custom exceptions

File: [`05_raise_and_custom_exceptions.py`](05_raise_and_custom_exceptions.py)

Use `raise` to signal that an operation cannot continue under the supplied
conditions. A **custom exception** is a class derived from `Exception` that
gives an application-specific problem a meaningful name.

```python
class InvalidAgeError(Exception):
    """Raised when an age is outside the accepted range."""


def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    return age
```

Catch a custom exception at the point where the program can give a useful
response. Do not use `raise` as a replacement for normal decisions such as
checking whether a value is present.

## Good practices

- Keep the `try` block small: include only statements that may raise the
  exception you intend to handle.
- Catch specific exception classes and order handlers from more specific to
  more general.
- Do not use a bare `except:` or silently ignore exceptions; doing so can hide
  bugs and interrupts.
- Keep error messages clear and avoid claiming an operation succeeded when
  it did not.
- Use `else` for success-only work and `finally` for cleanup needed on both
  success and failure.
- Raise a suitable built-in exception for ordinary invalid arguments. Create
  a custom exception when a distinct application-level condition deserves a
  clear name.
- Read the traceback from the last line upward: the last line gives the
  exception type and message, while earlier lines show where execution led
  to it.

## Practice ideas

1. Change the text passed to `int()` and observe which input succeeds.
2. Try a valid and invalid list index and handle only `IndexError`.
3. Look up both existing and missing dictionary keys.
4. Add a success message in `else` and confirm it is skipped after an
   exception.
5. Add a cleanup message in `finally` and observe it on both paths.
6. Write a function that rejects a negative number with `raise`.
7. Define a custom exception for an invalid product quantity and handle it
   where the user-facing message belongs.

## Running the examples

Run each lesson file with Python 3 from this directory. For example:

```bash
python 02_try_and_except.py
```

Each file contains definitions, explanations, ten runnable examples, and
expected output comments.
