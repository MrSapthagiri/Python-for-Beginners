# Module 10: Functions

## Module overview

Functions are named, reusable blocks of code. This module explains how to
define and call functions, pass information into them, return results, and
organize code into small reusable pieces.

## Learning outcomes

After completing this module, you should be able to:

- Define and call a function using `def`.
- Explain the difference between a parameter and an argument.
- Return one or more values from a function.
- Use multiple parameters, default values, and keyword arguments.
- Pass positional arguments and understand local and global variables.
- Collect extra arguments with `*args` and `**kwargs`.
- Write simple lambda functions and design reusable functions.

## Topics and files

1. [Creating and calling functions, parameters, and arguments](01_creating_and_calling_functions.py)
2. [Return values, multiple parameters, default and keyword arguments](02_return_values_and_arguments.py)
3. [Positional arguments and local/global variables](03_positional_and_scope.py)
4. [`*args` and `**kwargs`](04_args_and_kwargs.py)
5. [Lambda functions and reusable function design](05_lambda_and_reusable_functions.py)

Each Python file contains ten runnable examples with explanations and sample
outputs. Run a file with Python 3 to see its examples.

## Key ideas

- A **parameter** is a name written in a function definition; an **argument**
  is a value supplied when calling the function.
- `return` gives a result back to the caller. `print()` only displays it.
- Default arguments make a value optional. Keyword arguments identify values
  by parameter name.
- Local variables belong to a function call. Prefer parameters and return
  values over changing global variables.
- `*args` collects extra positional arguments in a tuple; `**kwargs` collects
  extra keyword arguments in a dictionary.
- Use `lambda` for a short expression. Use `def` for clear, reusable,
  multi-step behavior.
