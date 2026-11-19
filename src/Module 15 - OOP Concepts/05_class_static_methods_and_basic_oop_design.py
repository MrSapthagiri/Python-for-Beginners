# Module 15: OOP Concepts
# Topic 5: Class methods, static methods, and basic OOP design


# Example 1: A class method receives the class as cls.
class Student:
    school = "Greenwood School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, school):
        cls.school = school

    @classmethod
    def create(cls, name):
        return cls(name)


Student.change_school("Central Academy")
student = Student.create("Asha")
print("Example 1 -", student.name, Student.school)


# Example 2: A static method does not receive self or cls.
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32


print("Example 2 - Fahrenheit:",
      Temperature.celsius_to_fahrenheit(25))


# Example 3: Static methods are useful for related utility calculations.
class Geometry:
    @staticmethod
    def rectangle_area(width, height):
        if width < 0 or height < 0:
            raise ValueError("dimensions must not be negative")
        return width * height


print("Example 3 - Area:",
      Geometry.rectangle_area(5, 3))


# Example 4: Class methods can serve as alternative constructors.
class DateRecord:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, text):
        year, month, day = map(int, text.split("-"))
        return cls(year, month, day)


record = DateRecord.from_string("2026-11-19")
print("Example 4 - Date:",
      record.year, record.month, record.day)


# Example 5: Instance methods use object state.
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value


counter = Counter()
print("Example 5 - Counter:", counter.increment())


# Example 6: Composition combines objects rather than creating is-a inheritance.
class Engine:
    def start(self):
        return "Engine started"


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        return self.engine.start()


print("Example 6 -", Car().start())


# Example 7: A small responsibility should have a focused class.
class PasswordValidator:
    @staticmethod
    def is_valid(password):
        return len(password) >= 8


print("Example 7 - Valid password:",
      PasswordValidator.is_valid("python123"))


# Example 8: Encapsulation keeps data changes behind public methods.
class Wallet:
    def __init__(self, balance=0):
        self.__balance = balance

    def add_money(self, amount):
        if amount > 0:
            self.__balance += amount

    def balance(self):
        return self.__balance


wallet = Wallet(100)
wallet.add_money(25)
print("Example 8 - Balance:", wallet.balance())


# Example 9: Injected dependencies make behavior easier to replace.
class Greeter:
    def __init__(self, notifier):
        self.notifier = notifier

    def greet(self, name):
        return self.notifier(name)


greeter = Greeter(lambda name: f"Hello, {name}")
print("Example 9 -", greeter.greet("Asha"))


# Example 10: Keep public interfaces small and describeable.
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("discount must be from 0 to 100")
        self.price *= (100 - percent) / 100


product = Product("Notebook", 100)
product.apply_discount(10)
print("Example 10 - Price:", product.price)


# Quick review:
# - Instance methods operate on self and object state.
# - Class methods receive cls and can be alternative constructors.
# - Static methods receive neither cls nor self.
# - Prefer composition when objects have a has-a relationship.
