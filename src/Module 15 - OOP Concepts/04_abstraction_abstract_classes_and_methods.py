# Module 15: OOP Concepts
# Topic 4: Abstraction, abstract classes, and methods


from abc import ABC, abstractmethod


# Example 1: An abstract class cannot usually be instantiated directly.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


try:
    Shape()
except TypeError as error:
    print("Example 1 -", error)


# Example 2: A subclass implements the required abstract method.
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(5, 3)
print("Example 2 - Area:", rectangle.area())


# Example 3: Concrete subclasses hide implementation details behind methods.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


circle = Circle(4)
print("Example 3 - Area:", round(circle.area(), 2))


# Example 4: An abstract class may include a concrete helper method.
class FileExporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

    def describe(self):
        return f"{type(self).__name__} exporter"


class CsvExporter(FileExporter):
    def export(self, data):
        return ",".join(str(value) for value in data)


csv_exporter = CsvExporter()
print("Example 4 -",
      csv_exporter.describe(), csv_exporter.export(["Asha", 20]))


# Example 5: Abstraction defines a required interface.
class Database(ABC):
    @abstractmethod
    def save(self, record):
        pass


class MemoryDatabase(Database):
    def __init__(self):
        self.records = []

    def save(self, record):
        self.records.append(record)


database = MemoryDatabase()
database.save({"name": "Asha"})
print("Example 5 - Records:", database.records)


# Example 6: A missing abstract method prevents instantiation.
class PartialDatabase(Database):
    pass


try:
    PartialDatabase()
except TypeError as error:
    print("Example 6 -", error)


# Example 7: Abstract properties can require a read-only interface.
class Vehicle(ABC):
    @property
    @abstractmethod
    def wheels(self):
        pass


class Bicycle(Vehicle):
    @property
    def wheels(self):
        return 2


print("Example 7 - Wheels:", Bicycle().wheels)


# Example 8: Use abstract classes when multiple implementations share a contract.
class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotifier(Notifier):
    def send(self, message):
        return f"Email sent: {message}"


print("Example 8 -", EmailNotifier().send("Hello"))


# Example 9: super() can call concrete behavior from an abstract base.
class Logger(ABC):
    def log(self, message):
        print("Log:", message)


class ConsoleLogger(Logger):
    def log(self, message):
        super().log(message)
        print("Console:", message)


ConsoleLogger().log("Started")


# Example 10: Abstraction separates what a caller needs from how it works.
def print_area(shape: Shape):
    print("Example 10 - Shape area:", shape.area())


print_area(Rectangle(4, 6))
print_area(Circle(2))


# Quick review:
# - ABC creates an abstract base class.
# - @abstractmethod requires subclasses to implement the method.
# - Abstract classes enforce a consistent interface.
