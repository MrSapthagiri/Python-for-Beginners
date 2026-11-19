# Module 15: OOP Concepts
# Topic 2: Inheritance, parent/child classes, reuse, and super()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


# Example 1: A child class inherits attributes and methods.
class Dog(Animal):
    def speak(self):
        return "Woof"


dog = Dog("Milo")
print("Example 1 -", dog.name, dog.speak())


# Example 2: super() calls a method from the parent class.
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return f"{self.brand} started"


class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def start(self):
        parent_message = super().start()
        return f"{parent_message} with {self.doors} doors"


car = Car("Toyota", 4)
print("Example 2 -", car.start())


# Example 3: isinstance recognizes inheritance relationships.
print("Example 3 - Is car a Vehicle:",
      isinstance(car, Vehicle), isinstance(car, Car))


# Example 4: issubclass checks the relationship between classes.
print("Example 4 - Car subclass:",
      issubclass(Car, Vehicle))


# Example 5: An unoverridden method is reused from the parent.
class Employee:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Hello, I am {self.name}"


class Manager(Employee):
    pass


manager = Manager("Ravi")
print("Example 5 -", manager.greeting())


# Example 6: A child can extend parent initialization.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course


student = Student("Asha", 20, "Python")
print("Example 6 -",
      student.name, student.age, student.course)


# Example 7: Multiple inheritance can combine cooperative parent behavior.
class FlyMixin:
    def fly(self):
        return f"{self.name} is flying"


class Bird(Animal, FlyMixin):
    pass


bird = Bird("Parrot")
print("Example 7 -", bird.fly())


# Example 8: A child can override a parent method.
class Cat(Animal):
    def speak(self):
        return "Meow"


cat = Cat("Kitty")
print("Example 8 -", cat.speak())


# Example 9: Reuse shared code while specializing behavior.
class Shape:
    def describe(self):
        return f"This is a {type(self).__name__}"


class Circle(Shape):
    pass


print("Example 9 -", Circle().describe())


# Example 10: Prefer inheritance only for a genuine is-a relationship.
class ElectricCar(Car):
    def __init__(self, brand, doors, range_km):
        super().__init__(brand, doors)
        self.range_km = range_km


electric_car = ElectricCar("EV Motor", 5, 400)
print("Example 10 -",
      electric_car.brand, electric_car.range_km)


# Quick review:
# - A child class inherits from a parent class.
# - super() delegates to the parent implementation.
# - Overrides replace or specialize parent behavior.
