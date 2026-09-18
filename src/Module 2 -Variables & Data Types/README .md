# 🐍 Python Module 2 -- Variables & Data Types

## Overview

This module introduces the basic building blocks of Python programming:

1. Variables and how they store values
2. Naming rules for variables
3. Assignment and dynamic typing
4. Basic data types such as int, float, str, bool, and None
5. Checking data types with `type()`
6. Converting values between data types
7. Multiple assignment and basic memory concepts

---

# 1. Variables

## What is a variable?

A variable is a name used to store data in memory. It helps us save values and use them later in our program.

```python
age = 18
name = "Mr Giri"
```

Here:
- `age` is a variable
- `18` is the value stored in it
- `name` is another variable
- `"Alice"` is a string value

## Why do we use variables?

Variables make programs easier to read and manage.

```python
price = 250
quantity = 3

total = price * quantity
print(total)
```

Output:
```python
750
```

---

# 2. Variable Assignment

Assignment means giving a value to a variable using the `=` operator.

```python
x = 10
y = 20
z = "Python"
```

The variable is on the left side of `=`, and the value is on the right side.

Example:
```python
marks = 90
print(marks)
```

Output:
```python
90
```

---

# 3. Variable Naming Rules

Variable names must follow these rules:

## Valid variable names

```python
name = "Rahul"
age = 25
student_name = "Asha"
_value = 10
```

## Invalid variable names

```python
2name = "A"
my-name = "B"
class = "Python"
```

## Rules to remember

- A variable name can start with a letter or underscore
- It cannot start with a number
- It can contain letters, numbers, and underscores
- It cannot contain spaces
- It cannot use Python keywords like `if`, `else`, `for`, `class`, `True`, `False`, etc.

## Good naming practices

Use meaningful names:

```python
student_name = "Sara"
total_marks = 450
```

Avoid vague names:

```python
x = "Sara"
a = 450
```

For readability, use snake_case:

```python
employee_name = "Kiran"
monthly_salary = 35000
```

---

# 4. Dynamic Typing in Python

Python is a dynamically typed language.

This means you do not have to declare the type of a variable when creating it.

```python
value = 10
print(value)

value = "ten"
print(value)
```

Output:
```python
10
ten
```

Python automatically understands the type based on the value.

Example:
```python
x = 5
x = 5.5
x = "Hello"
```

The same variable can store different types at different times.

---

# 5. Basic Data Types in Python

Python has several built-in data types. The main ones for this module are:

## 5.1 Integer (`int`)

Used for whole numbers.

```python
num1 = 10
num2 = -5
print(type(num1))
```

Output:
```python
<class 'int'>
```

## 5.2 Float (`float`)

Used for decimal numbers.

```python
pi = 3.14
height = 5.8
print(type(pi))
```

Output:
```python
<class 'float'>
```

## 5.3 String (`str`)

Used for text data.

```python
name = "Python"
message = 'Hello, World!'
print(type(name))
```

Output:
```python
<class 'str'>
```

Strings can be enclosed in single quotes or double quotes.

## 5.4 Boolean (`bool`)

Used for true or false values.

```python
is_active = True
is_passed = False
print(type(is_active))
```

Output:
```python
<class 'bool'>
```

## 5.5 `None`

`None` means no value or null value.

```python
result = None
print(result)
print(type(result))
```

Output:
```python
None
<class 'NoneType'>
```

`None` is different from `0`, `False`, or an empty string.

---

# 6. `type()` Function

The `type()` function tells us the type of a value or variable.

```python
x = 25
print(type(x))

y = 7.5
print(type(y))

z = "Python"
print(type(z))

flag = True
print(type(flag))
```

Output:
```python
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

## Why is `type()` important?

It helps us know what kind of data we are working with before performing operations.

Example:
```python
sample = "100"
print(type(sample))
```

This is a string, not a number.

---

# 7. Type Conversion and Type Casting

Type conversion means changing one data type into another.

Python has built-in functions for this:

## `int()`

Converts a value into an integer.

```python
print(int("10"))
print(int(3.9))
print(int(True))
```

Output:
```python
10
3
1
```

## `float()`

Converts a value into a float.

```python
print(float("3.5"))
print(float(7))
```

Output:
```python
3.5
7.0
```

## `str()`

Converts a value into a string.

```python
print(str(25))
print(str(True))
```

Output:
```python
25
True
```

## `bool()`

Converts a value into a boolean.

```python
print(bool(1))
print(bool(0))
print(bool("hello"))
print(bool(""))
```

Output:
```python
True
False
True
False
```

## Important note

Not every conversion is possible.

```python
int("hello")
```

This will raise an error because Python cannot convert the text `hello` into an integer.

## Example of conversion in real use

```python
age = "18"
print(type(age))

converted_age = int(age)
print(converted_age)
print(type(converted_age))
```

Output:
```python
<class 'str'>
18
<class 'int'>
```

---

# 8. Multiple Variable Assignment

Python allows assigning multiple variables in one line.

## Same value to multiple variables

```python
a = b = c = 10
print(a)
print(b)
print(c)
```

Output:
```python
10
10
10
```

## Different values to different variables

```python
x, y, z = 10, 20, 30
print(x)
print(y)
print(z)
```

Output:
```python
10
20
30
```

## Swapping values

```python
p, q = 10, 20
p, q = q, p
print(p)
print(q)
```

Output:
```python
20
10
```

This is a common technique used in programming.

---

# 9. Basic Memory Concepts

Variables are stored in memory. Python keeps track of them using names.

## Example

```python
num = 10
print(num)
```

Here:
- `num` is the variable name
- `10` is stored in memory
- the variable points to the value in memory

## Memory idea

Think of a variable as a label attached to a value.

```python
x = 5
y = x
```

Now both `x` and `y` are associated with the same value `5`.

## `id()` function

The `id()` function shows the memory address of an object.

```python
x = 10
y = 10
print(id(x))
print(id(y))
```

Python may store small integer values in the same memory location for optimization.

---

# 10. Example Program Using Variables and Data Types

```python
name = "Riya"
age = 19
height = 5.5
is_student = True
result = None

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print(result, type(result))

num_str = "50"
num_int = int(num_str)
print(num_int + 10)
```

Output:
```python
Riya <class 'str'>
19 <class 'int'>
5.5 <class 'float'>
True <class 'bool'>
None <class 'NoneType'>
60
```

---

# 11. Summary

In this module, we learned:

- Variables store data in memory
- Variable names must follow naming rules
- Python is dynamically typed
- Basic types include `int`, `float`, `str`, `bool`, and `None`
- The `type()` function tells us the type of a variable
- Type conversion helps us change data types
- Multiple variable assignment saves time and simplifies code
- Variables are linked to memory locations

---

# 12. Quick Revision Questions

1. What is a variable?
2. List 5 naming rules for variables.
3. What does dynamic typing mean in Python?
4. Name the five basic data types learned in this module.
5. What does `type()` do?
6. Why do we use type conversion?
7. What is the difference between `int`, `float`, and `str`?
8. What is `None` used for?
9. How do we assign multiple variables in one line?
10. What is basic memory concept in variables?

---

# 13. Practice Exercises

## Exercise 1
```python
name = "Dev"
age = 22
print(name)
print(age)
```

## Exercise 2
```python
x = 10
y = "20"
print(x + int(y))
```

## Exercise 3
```python
a, b, c = 5, 10, 15
print(a + b + c)
```

## Exercise 4
```python
is_pass = True
print(type(is_pass))
```

---

# Final Note

Variables and data types are the foundation of Python programming. Learning them well will make every future topic easier, such as operators, conditions, loops, functions, and lists.

Practice is the best way to understand these concepts. Write code daily and test different data types in Python.
