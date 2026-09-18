# 🐍 Python Module 4 -- Input & Output

## Overview

This module teaches how Python interacts with users and displays results. We will learn:

1. `print()` and output formatting
2. `input()` and reading user input
3. Type conversion with user input
4. String formatting and f-strings
5. Escape characters and formatted output

---

# 1. `print()` and Output Formatting

The `print()` function is used to display output on the screen.

## Basic example

```python
print("Hello, Python!")
```

Output:
```python
Hello, Python!
```

## Printing variables

```python
name = "Aisha"
print(name)
```

Output:
```python
Aisha
```

## Printing multiple values

```python
print("Name:", "Aisha")
print("Age:", 20)
```

Output:
```python
Name: Aisha
Age: 20
```

## Printing with separators

```python
print("Python", "Java", "C++", sep=",")
```

Output:
```python
Python,Java,C++
```

## Printing without a newline

```python
print("Hello", end=" ")
print("World")
```

Output:
```python
Hello World
```

`end=" "` tells Python to add a space instead of a new line after the first print.

---

# 2. `input()` and User Input

The `input()` function is used to read data entered by the user.

## Basic example

```python
name = input("Enter your name: ")
print("Hello", name)
```

Example output:
```python
Enter your name: Ravi
Hello Ravi
```

## Important note

`input()` always returns a string value.

```python
age = input("Enter your age: ")
print(type(age))
```

Example output:
```python
Enter your age: 18
<class 'str'>
```

Even if the user types a number, Python stores it as a string.

---

# 3. Type Conversion with User Input

Since `input()` returns a string, we often convert it to another type.

## Converting to integer

```python
age = int(input("Enter your age: "))
print("Your age is:", age)
```

Example:
```python
Enter your age: 21
Your age is: 21
```

## Converting to float

```python
price = float(input("Enter price: "))
print(price)
```

## Converting to string

```python
num = 50
text = str(num)
print(text)
print(type(text))
```

Output:
```python
50
<class 'str'>
```

## Example with math

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_value = num1 + num2
print("Sum is:", sum_value)
```

Example:
```python
Enter first number: 10
Enter second number: 20
Sum is: 30
```

## Important warning

If the user enters a non-numeric value for `int()` or `float()`, Python raises an error.

```python
age = int(input("Enter your age: "))
```

If the user enters `abc`, it will cause:
```python
ValueError
```

---

# 4. String Formatting and f-strings

String formatting allows us to insert values inside strings in a neat and readable way.

## Example 1: simple concatenation

```python
name = "Riya"
age = 18
print("My name is " + name + " and I am " + str(age) + " years old.")
```

Output:
```python
My name is Riya and I am 18 years old.
```

This works, but f-strings are easier.

## Example 2: f-string

```python
name = "Riya"
age = 18
print(f"My name is {name} and I am {age} years old.")
```

Output:
```python
My name is Riya and I am 18 years old.
```

## Why use f-strings?

- cleaner code
- easier to read
- simpler than concatenation
- widely used in Python

## Example with calculations

```python
a = 10
b = 20
print(f"The sum of {a} and {b} is {a + b}.")
```

Output:
```python
The sum of 10 and 20 is 30.
```

## Example with user input

```python
name = input("Enter your name: ")
score = int(input("Enter your score: "))

print(f"Student: {name}")
print(f"Score: {score}")
```

---

# 5. Escape Characters and Formatted Output

Escape characters are special sequences used inside strings to format text.

## Common escape characters

| Escape sequence | Meaning |
|-----------------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double quote |
| `\'` | Single quote |

## Example: newline

```python
print("Hello\nWorld")
```

Output:
```python
Hello
World
```

## Example: tab

```python
print("Name\tAge")
print("Ravi\t20")
```

Output:
```python
Name    Age
Ravi    20
```

## Example: quotes inside strings

```python
print("He said, \"Hello!\"")
print('It\'s a test')
```

Output:
```python
He said, "Hello!"
It's a test
```

## Formatted output using `print()`

```python
print("Name: %s" % "Aman")
print("Age: %d" % 25)
print("Price: %.2f" % 12.567)
```

Output:
```python
Name: Aman
Age: 25
Price: 12.57
```

This is an older formatting style, but `f-strings` are preferred in modern Python.

---

# 6. Full Example Program Combining Concepts

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Weight: {weight}")

print("Hello, " + name + "! You are " + str(age) + " years old.")
print("Your details are:\nName: %s\nAge: %d\nWeight: %.2f" % (name, age, weight))
```

Sample output:
```python
Enter your name: Karan
Enter your age: 22
Enter your weight: 65.5
Name: Karan
Age: 22
Weight: 65.5
Hello, Karan! You are 22 years old.
Your details are:
Name: Karan
Age: 22
Weight: 65.50
```

---

# 7. Summary

In this module, we learned:

- `print()` displays information to the user
- `input()` reads user input
- `input()` always gives a string
- We use `int()`, `float()`, and `str()` to convert values
- `f-strings` make output cleaner and easier to read
- Escape characters help format text properly

---

# 8. Quick Revision Questions

1. What does `print()` do?
2. What does `input()` do?
3. Why do we need type conversion with `input()`?
4. What is an f-string?
5. Write an example of using `\n` in Python.
6. What happens if you do `int(input("Age: "))` and the user enters text?
7. What is the difference between `print("A")` and `print('A')`?
8. What is the use of `end=" "` in `print()`?

---

# 9. Practice Exercises

## Exercise 1

```python
name = input("Enter your name: ")
print("Welcome", name)
```

## Exercise 2

```python
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(f"Total: {num1 + num2}")
```

## Exercise 3

```python
message = "Hello\nWorld"
print(message)
```

## Exercise 4

```python
city = "Delhi"
print(f"I live in {city}")
```

---

# Final Note

Input and output are the foundation of interactive programs. Without `print()` and `input()`, programs cannot show results or receive user data. Learning these topics well will help you build simple calculator apps, login forms, and many more interactive programs in the future.
