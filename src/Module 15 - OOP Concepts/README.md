# Module 15: OOP Concepts

## Module overview

Building on basic OOP, this module explains encapsulation, inheritance,
polymorphism, abstraction, class methods, static methods, and basic object
design. These concepts help organize larger Python programs around clear
responsibilities and replaceable behavior.

## Learning outcomes

After completing this module, you should be able to:

- Explain encapsulation and distinguish public, protected, and private naming
  conventions.
- Protect object state with methods and properties.
- Create parent and child classes and reuse behavior with inheritance.
- Use `super()` to call parent behavior.
- Implement polymorphism through overriding and compatible method interfaces.
- Create abstract classes and abstract methods with `abc`.
- Define class methods and static methods.
- Choose inheritance or composition for a basic design.

## Important definitions

### Encapsulation

**Encapsulation** combines data and operations in an object and limits direct
access to implementation details. Python uses naming conventions rather than
true access keywords: `_name` indicates protected data and `__name` activates
name mangling.

### Inheritance

**Inheritance** lets a child class reuse and specialize behavior from a parent
class. Use inheritance for a genuine is-a relationship.

### Polymorphism

**Polymorphism** lets different objects respond to the same method call.
Different implementations may produce different behavior.

### Abstraction

**Abstraction** exposes essential behavior while hiding implementation
details. An abstract base class declares methods that concrete subclasses
must implement.

## Topics and files

### 1. Encapsulation and data protection

File: [`01_encapsulation_public_private_and_data_protection.py`](01_encapsulation_public_private_and_data_protection.py)

Use methods or properties to control access and validate changes:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
```

### 2. Inheritance and `super()`

File: [`02_inheritance_reuse_and_super.py`](02_inheritance_reuse_and_super.py)

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors
```

`super()` delegates to the next implementation in the method resolution order,
which is especially useful for initializing parent state.

### 3. Polymorphism and overriding

File: [`03_polymorphism_and_method_overriding.py`](03_polymorphism_and_method_overriding.py)

Two or more classes can provide the same method name with different behavior:

```python
class CardPayment:
    def pay(self, amount):
        return f"Paid {amount} by card"


class CashPayment:
    def pay(self, amount):
        return f"Paid {amount} by cash"
```

Python also supports duck typing: code can accept any object that provides
the needed behavior, regardless of inheritance.

### 4. Abstraction

File: [`04_abstraction_abstract_classes_and_methods.py`](04_abstraction_abstract_classes_and_methods.py)

Use `ABC` and `@abstractmethod` to require subclasses to implement an
interface:

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

An abstract class cannot be instantiated while abstract methods remain
unimplemented.

### 5. Class methods, static methods, and basic design

File: [`05_class_static_methods_and_basic_oop_design.py`](05_class_static_methods_and_basic_oop_design.py)

- Instance methods receive `self`.
- Class methods receive `cls` and can change class state or create instances.
- Static methods receive neither `self` nor `cls`; they group related
  utility behavior without object state.

```python
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32
```

Use inheritance for is-a relationships and composition for has-a
relationships. Keep classes focused and expose only the behavior callers need.

## Good practices

- Treat `_name` and `__name` as conventions; do not use privacy as security.
- Validate state changes in methods or property setters.
- Prefer `super()` over directly calling a parent class by name.
- Keep inheritance hierarchies small and coherent.
- Depend on clear interfaces rather than implementation details.
- Use class methods for alternative constructors and class state.
- Use static methods for stateless utilities related to the class.
- Use composition when one object contains or uses another object.

## Practice ideas

1. Add validation to a protected bank-balance property.
2. Create a `Person` parent and `Teacher` and `Student` child classes.
3. Override `describe()` in several child classes.
4. Create an abstract `Exporter` class with a `export()` method.
5. Implement CSV and JSON exporter subclasses.
6. Add a `from_string()` class method to a date or record class.
7. Design a `Library` using composition with `Book` objects.

## Running the examples

Run each lesson file with Python 3 from this directory:

```bash
python 01_encapsulation_public_private_and_data_protection.py
python 02_inheritance_reuse_and_super.py
python 03_polymorphism_and_method_overriding.py
python 04_abstraction_abstract_classes_and_methods.py
python 05_class_static_methods_and_basic_oop_design.py
```
