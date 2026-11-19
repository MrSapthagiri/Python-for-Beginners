# Module 14: OOP Fundamentals
# Topic 3: Constructor, __init__, and self


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


# __init__ runs automatically when an object is created.
# Example 1:
person = Person("Asha", 20)
print("Example 1 -", person.introduce())


# Example 2: self refers to the object that received the method call.
class Lamp:
    def __init__(self, color):
        self.color = color

    def turn_on(self):
        print(f"Example 2 - The {self.color} lamp is on.")


lamp = Lamp("blue")
lamp.turn_on()


# Example 3: Different constructor arguments create different objects.
another_person = Person("Ravi", 25)
print("Example 3 -", another_person.introduce())


# Example 4: Default constructor arguments are allowed.
class Item:
    def __init__(self, name, quantity=1):
        self.name = name
        self.quantity = quantity


pen = Item("Pen")
print("Example 4 -", pen.name, pen.quantity)


# Example 5: __init__ should initialize the object's starting state.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


account = BankAccount("Mina", 100)
account.deposit(50)
print("Example 5 - Balance:", account.balance)


# Example 6: Store constructor values for later use.
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


circle = Circle(4)
print("Example 6 - Area:", round(circle.area(), 2))


# Example 7: Validation can be performed in __init__.
class Age:
    def __init__(self, years):
        if years < 0:
            raise ValueError("age cannot be negative")
        self.years = years


valid_age = Age(18)
print("Example 7 - Age:", valid_age.years)


# Example 8: Without an explicit __init__, Python provides an empty one.
class Empty:
    pass


empty = Empty()
print("Example 8 - Empty object:", isinstance(empty, Empty))


# Example 9: Calling a method passes the object automatically to self.
class Number:
    def __init__(self, value):
        self.value = value

    def add(self, amount):
        self.value += amount


number = Number(10)
number.add(5)
print("Example 9 - Value:", number.value)


# Example 10: Constructor-created objects keep separate state.
number_two = Number(100)
print("Example 10 - Values:", number.value, number_two.value)


# Quick review:
# - __init__ initializes a newly created object.
# - self refers to the current object.
# - Constructor arguments provide initial instance data.
