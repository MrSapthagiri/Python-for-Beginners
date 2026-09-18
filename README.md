# Python for Beginners

This is the complete beginner-friendly Python course notes for the learning path covered in this workspace.

## Course Modules

- Module 1: Python Installation & Environment
- Module 2: Variables & Data Types
- Module 3: Operators
- Module 4: Input & Output

## Module 1: Python Installation & Environment

### Overview

This module covers the basic Python environment needed before starting programming:

1. Python introduction and features
2. Python installation and environment setup
3. VS Code setup and Python extension
4. Running Python programs
5. Using pip and virtual environments

### What is Python?

Python is a high-level, general-purpose programming language known for:

- Simple and readable syntax
- Easy learning curve
- Cross-platform support
- Large library ecosystem
- Use in web development, automation, data science, AI, and scripting

### Common Python features

- Easy syntax
- Readable code
- Dynamic typing
- Object-oriented programming
- Large standard library

### Python use cases

- Automation and scripting
- Web development
- Data science
- AI and machine learning
- DevOps and cloud tasks

### Python versions

Use Python 3 for all new projects.

### Installation checks

```bash
python --version
```

or

```bash
python3 --version
```

### Basic setup flow

1. Download Python
2. Install Python
3. Add Python to PATH
4. Open VS Code
5. Install Python extension
6. Create a .py file
7. Run the program

### Example

```python
name = "Giri"
age = 30

print(name)
print(age)
```

### Important note

Python is interpreted, meaning code is executed line by line by the Python interpreter.

See module notes: [src/Module 1 -Python Installation & Environment/README .md](src/Module%201%20-Python%20Installation%20&%20Environment/README%20.md)

---

## Module 2: Variables & Data Types

### Overview

This module introduces the basic building blocks of Python programming:

1. Variables and how they store values
2. Naming rules for variables
3. Assignment and dynamic typing
4. Basic data types: int, float, str, bool, None
5. Using type()
6. Type conversion
7. Multiple assignment and memory concepts

### Variables

A variable stores a value in memory so it can be used later.

```python
age = 18
name = "Alice"
```

### Variable assignment

Use the = operator:

```python
x = 10
y = 20
```

### Naming rules

Valid examples:

```python
name = "Rahul"
age = 25
student_name = "Asha"
_value = 10
```

Invalid examples:

```python
2name = "A"
my-name = "B"
class = "Python"
```

Rules:

- Start with a letter or underscore
- Cannot start with a number
- Cannot contain spaces
- Cannot use Python keywords

### Dynamic typing

Python automatically decides the variable type.

```python
value = 10
value = "ten"
```

### Basic data types

#### int

```python
num = 10
```

#### float

```python
pi = 3.14
```

#### str

```python
name = "Python"
```

#### bool

```python
is_active = True
```

#### None

```python
result = None
```

### type()

```python
x = 25
print(type(x))
```

Output:

```python
<class 'int'>
```

### Type conversion

```python
num = "20"
print(int(num))
print(float(num))
print(str(20))
```

### Multiple assignment

```python
x, y, z = 10, 20, 30
```

or

```python
a = b = c = 10
```

### Memory idea

Variables are labels attached to values stored in memory.

See module notes: [src/Module 2 -Variables & Data Types/README .md](src/Module%202%20-Variables%20&%20Data%20Types/README%20.md)

---

## Module 3: Operators

### Overview

This module focuses on operators used in Python to calculate, compare, and combine conditions.

### Topics covered

1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Membership operators
6. Identity operators
7. Operator precedence

### Arithmetic operators

```python
x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
```

### Assignment operators

```python
x = 10
x += 5
print(x)
```

### Comparison operators

```python
print(5 == 5)
print(5 != 3)
print(8 > 3)
print(2 < 6)
```

### Logical operators

```python
print(True and False)
print(True or False)
print(not True)
```

### Membership operator

```python
name = "Python"
print('P' in name)
```

### Identity operator

```python
a = [1, 2, 3]
b = a
print(a is b)
```

### Operator precedence

Python evaluates expressions based on precedence.

```python
result = 10 + 3 * 2
print(result)
```

Because multiplication is evaluated before addition, the answer is:

```python
16
```

See module notes: [src/Module 3 -Operators/README.md](src/Module%203%20-Operators/README.md)

---

## Module 4: Input & Output

### Overview

This module covers how Python interacts with users by taking input and displaying output.

### Topics covered

1. `print()` and output formatting
2. `input()` and user input
3. Type conversion with input
4. String formatting with f-strings
5. Escape characters and formatted output

### `print()`

```python
print("Hello, Python!")
```

### `input()`

```python
name = input("Enter your name: ")
print("Hello", name)
```

### Type conversion with user input

```python
age = int(input("Enter your age: "))
print(age)
```

### F-strings

```python
name = "Riya"
print(f"Hello {name}!")
```

### Escape characters

```python
print("Hello\nWorld")
print("Name\tAge")
```

See module notes: [src/Module 4 -Input & Output/README.md](src/Module%204%20-Input%20&%20Output/README.md)

---

## Learning Progress

The beginner course in this workspace covers:

- Python environment setup
- Variables and data types
- Operators and expressions

These concepts are the foundation for future modules like:

- Conditional statements
- Loops
- Functions
- Lists and strings
- Files and modules

---

## Final Notes

Python is a beginner-friendly language that becomes powerful when you practice daily. Start with small examples, understand each concept carefully, and write code regularly to build confidence.
