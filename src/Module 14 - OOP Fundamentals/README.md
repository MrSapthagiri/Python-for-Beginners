# Module 14: OOP Fundamentals

## Module overview

Object-oriented programming (OOP) organizes a program around objects that
combine related data and behavior. This module introduces classes, objects,
attributes, methods, constructors, instance variables, and class variables.

## Learning outcomes

After completing this module, you should be able to:

- Explain the difference between a class and an object.
- Create objects and define attributes.
- Define instance methods and call them through objects.
- Use `__init__()` to initialize objects.
- Explain what `self` represents.
- Distinguish instance variables from class variables.
- Create and work with multiple objects.
- Avoid sharing mutable state unintentionally between objects.

## Important definitions

### Object-oriented programming

**Object-oriented programming** is a style that models related data and
actions as objects. It can make a program easier to organize, extend, and
reason about.

### Class

A **class** is a blueprint or template for creating objects. It defines
attributes and methods that its objects can use.

### Object

An **object** is a concrete instance of a class. Different objects made from
the same class can contain different instance data.

### Attribute

An **attribute** is data associated with a class or object. An instance
attribute belongs to one object; a class attribute belongs to the class and
is shared unless an object overrides it.

### Method

A **method** is a function defined inside a class. Instance methods receive
the current object as their first parameter, conventionally named `self`.

## Topics and files

### 1. OOP concepts, classes, and objects

File: [`01_oop_concepts_classes_and_objects.py`](01_oop_concepts_classes_and_objects.py)

A class defines a type of object, while an object is created from that class:

```python
class Student:
    pass


student = Student()
student.name = "Asha"
print(student.name)
```

Use `isinstance(object, ClassName)` to check whether an object was created
from a class or is compatible with it.

### 2. Attributes, methods, and object creation

File: [`02_attributes_methods_and_object_creation.py`](02_attributes_methods_and_object_creation.py)

Attributes store data. Methods describe behavior and can read or update
attributes:

```python
class Rectangle:
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```

Create an object with `ClassName()`, set or read its attributes, and call a
method with `object.method()`.

### 3. Constructor, `__init__()`, and `self`

File: [`03_constructor_init_and_self.py`](03_constructor_init_and_self.py)

The special method `__init__()` runs automatically when a new object is
created. It usually initializes instance variables:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Asha", 20)
```

`self` is a reference to the object receiving the method call. It is a
convention, not a Python keyword, but all instance methods should use this
name consistently.

### 4. Instance variables and instance methods

File: [`04_instance_variables_and_methods.py`](04_instance_variables_and_methods.py)

Instance variables are generally created through `self` and belong to one
object:

```python
class Counter:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1
```

Instance methods receive `self`, so they can act on the object that called
the method. Each object's instance variables remain separate.

### 5. Class variables and multiple objects

File: [`05_class_variables_and_multiple_objects.py`](05_class_variables_and_multiple_objects.py)

A class variable is declared in the class body and is shared by objects:

```python
class Employee:
    company = "Tech Academy"

    def __init__(self, name):
        self.name = name
```

Both `Employee.company` and `employee.company` can read a class variable,
but assigning `employee.company = "Other"` creates an instance attribute
only on that employee. Use instance variables for mutable data that belongs
to each object.

## Good practices

- Use a capitalized class name according to Python naming conventions.
- Initialize instance variables in `__init__()` when possible.
- Name the first instance-method parameter `self`.
- Keep methods short and focused on one object behavior.
- Prefer instance variables for mutable, object-specific data.
- Use class variables for values truly shared by the class.
- Create and test several objects to verify that instance state remains
  independent.

## Practice ideas

1. Create a `Pet` class with a name and age, then create two pets.
2. Add a method that formats a pet's details as a string.
3. Create a `BankAccount` constructor with an owner and starting balance.
4. Add `deposit()` and `withdraw()` instance methods.
5. Add a class variable for a shared bank name.
6. Create a `Team` class with a separate member list for every team.
7. Explain whether each variable in a program should be an instance or class
   variable.

## Running the examples

Run each lesson file from this directory with Python 3:

```bash
python 01_oop_concepts_classes_and_objects.py
python 02_attributes_methods_and_object_creation.py
python 03_constructor_init_and_self.py
python 04_instance_variables_and_methods.py
python 05_class_variables_and_multiple_objects.py
```
