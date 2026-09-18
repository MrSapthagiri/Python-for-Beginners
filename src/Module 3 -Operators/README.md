# 🐍 Python Module 3 -- Operators

## Overview

This module covers the operators used in Python to perform calculations, compare values, combine conditions, and control program logic.

Topics included:

1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators (`and`, `or`, `not`)
5. Membership operators (`in`)
6. Identity operators (`is`)
7. Operator precedence and expressions

---

# 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

## Common arithmetic operators

| Operator | Meaning             | Example   |Result|
|----------|---------------------|-----------|------|
| `+`      | Addition            | `5 + 3`   | `8`  |
| `-`      | Subtraction         | `9 - 4`   | `5`  |
| `*`      | Multiplication      | `6 * 2`   | `12` |
| `/`      | Division            | `10 / 2`  | `5.0`|
| `%`      | Modulus (remainder) | `10 % 3`  | `1`  |
| `**`     | Exponentiation      | `2 ** 3`  | `8`  |
| `//`     | Floor division      | `10 // 3` | `3`  |

## Example

```python
x = 10
y = 3

print(x + y)   # 13
print(x - y)   # 7
print(x * y)   # 30
print(x / y)   # 3.3333333333333335
print(x % y)   # 1
print(x ** y)  # 1000
print(x // y)  # 3
```

## Notes

- `/` always gives a float result
- `//` removes the decimal part and returns an integer value
- `%` gives the remainder after division

---

# 2. Assignment Operators

Assignment operators are used to assign values to variables.

## Basic assignment

```python
x = 5
```

This means: store value `5` in variable `x`.

## Compound assignment operators

These combine assignment with arithmetic.

| Operator | Example | Meaning |
|----------|---------|---------|
| `=` | `x = 5` | Assign `5` to `x` |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 2` | `x = x - 2` |
| `*=` | `x *= 4` | `x = x * 4` |
| `/=` | `x /= 2` | `x = x / 2` |
| `%=` | `x %= 3` | `x = x % 3` |

## Example

```python
x = 10
x += 5
print(x)   # 15

x *= 2
print(x)   # 30

x -= 10
print(x)   # 20
```

## Why use assignment operators?

They make code shorter and easier to read.

---

# 3. Comparison Operators

Comparison operators compare two values and return a boolean result: `True` or `False`.

## Common comparison operators

| Operator | Meaning               |  Example | Result |
|----------|-----------------------|------- --|--------|
|   `==`   | Equal to              | `5 == 5` | `True` |
|   `!=`   | Not equal to          | `5 != 3` | `True` |
|   `>`    | Greater than          | `8 > 3`  | `True` |
|   `<`    | Less than             | `2 < 6`  | `True` |
|   `>=`   | Greater than or equal | `7 >= 7` | `True` |
|   `<=`   | Less than or equal    | `4 <= 5` | `True` |

## Example

```python
a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a > b)    # False
print(a <= 10)  # True
print(b >= 20)  # True
```

## Important point

`==` checks equality, while `=` is used for assignment.

```python
x = 5      # assignment
print(x == 5)   # comparison
```

---

# 4. Logical Operators

Logical operators combine conditions and return `True` or `False`.

## `and`

Returns `True` only if both conditions are true.

```python
age = 25
income = 50000

print(age > 18 and income > 30000)   # True
```

## `or`

Returns `True` if at least one condition is true.

```python
print(age > 18 or income < 1000)      # True
```

## `not`

Reverses the result of a condition.

```python
is_student = False
print(not is_student)   # True
```

## Example table

```python
A = True
B = False

print(A and B)   # False
print(A or B)    # True
print(not A)     # False
print(not B)     # True
```

## Real-world use

```python
marks = 85
attendance = 75

passed = marks >= 70 and attendance >= 75
print(passed)  # True
```

---

# 5. Membership Operators

Membership operators check whether a value exists inside a sequence like a string, list, or tuple.

## `in`

Returns `True` if a value is found.

```python
name = "Python"
print('P' in name)      # True
print('x' in name)      # False
```

```python
numbers = [1, 2, 3, 4]
print(3 in numbers)     # True
print(9 in numbers)     # False
```

## `not in`

Returns `True` if a value is not found.

```python
print(8 not in numbers)   # True
```

## When used?

Membership checks are useful for:
- checking letters in a word
- checking items in a list
- checking usernames in a set

---

# 6. Identity Operators

Identity operators compare whether two objects are the same object in memory.

## `is`

Returns `True` if both variables refer to the same object.

```python
a = [1, 2, 3]
b = a
print(a is b)   # True
```

## `is not`

Returns `True` if they are different objects.

```python
c = [1, 2, 3]
print(a is c)   # False
print(a is not c)  # True
```

## Important note

`==` checks values, while `is` checks identity.

```python
x = [1, 2]
y = [1, 2]

print(x == y)   # True  (same values)
print(x is y)   # False (different objects)
```

---

# 7. Operator Precedence and Expressions

Operator precedence decides the order in which Python evaluates operations in an expression.

## Example

```python
result = 10 + 3 * 2
print(result)  # 16
```

Why?

Python evaluates multiplication before addition.

So:

```python
3 * 2 = 6
10 + 6 = 16
```

## Common precedence order

From highest to lowest:

1. Parentheses `()`
2. Exponentiation `**`
3. Multiplication, division, modulus, floor division `* / % //`
4. Addition and subtraction `+ -`
5. Comparison operators
6. `not`
7. `and`
8. `or`

## Example with precedence

```python
print(5 + 3 * 2)          # 11
print((5 + 3) * 2)        # 16
print(10 > 5 and 3 < 7)   # True
```

## Expression

An expression is a combination of values, variables, and operators.

Examples:

```python
x = 10
y = 5

expr1 = x + y
expr2 = x * 2 + y
expr3 = (x + y) * 3
```

---

# 8. Combined Example Program

```python
x = 10
y = 5

# Arithmetic
print(x + y)      # 15
print(x % y)      # 0

# Assignment
x += 3
print(x)          # 13

# Comparison
print(x > y)      # True

# Logical
print(x > 10 and y < 10)   # True
print(x > 20 or y < 10)    # True
print(not (x < y))         # True

# Membership
letters = "Python"
print('P' in letters)       # True

# Identity
a = [1, 2, 3]
b = a
print(a is b)               # True

# Precedence
result = 2 + 3 * 4
print(result)               # 14
```

---

# 9. Summary

In this module, we learned that:

- Arithmetic operators perform calculations
- Assignment operators store values and update them efficiently
- Comparison operators compare data and return booleans
- Logical operators combine conditions: `and`, `or`, `not`
- Membership operators check whether a value is inside a sequence: `in`
- Identity operators check whether variables refer to the same object: `is`
- Operator precedence decides the order of evaluation in expressions

---

# 10. Quick Revision Questions

1. What is the difference between `=` and `==`?
2. What does `+=` do?
3. Give one example of each logical operator.
4. What does the `in` operator check?
5. What is the difference between `==` and `is`?
6. Why is operator precedence important?
7. What is the result of `10 // 3`?
8. What is the output of `not True`?

---

# 11. Practice Exercises

## Exercise 1

```python
x = 15
y = 4
print(x + y)
print(x % y)
```

## Exercise 2

```python
age = 21
print(age >= 18 and age <= 30)
```

## Exercise 3

```python
name = "Python"
print('y' in name)
```

## Exercise 4

```python
x = 10
print(x == 10)
print(x is 10)
```

---

# Final Note

Operators are one of the most important parts of Python because they help us do calculations, compare values, and make decisions in programs. Once you understand operators clearly, the next topics like conditions, loops, and functions become much easier.
