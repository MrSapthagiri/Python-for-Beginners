"""Demonstrate basic object-oriented programming concepts."""

# pylint: disable=invalid-name,too-few-public-methods

# Module 14: OOP Fundamentals
# Topic 1: OOP concepts, classes, and objects


# OOP organizes related data and behavior into objects.
class Student:
    """Represent a student created for a basic OOP example."""

    name: str
    grade: int


# A class is a blueprint. An object is a usable instance created from it.
student = Student()
print("Example 1 - Object type:", type(student).__name__)


# Example 2: Two objects can have the same class and different identities.
first_student = Student()
second_student = Student()
print("Example 2 - Both students:", isinstance(first_student, Student),
      isinstance(second_student, Student))


# Example 3: Objects are separate even when they have no instance data.
print("Example 3 - Same object?:", first_student is second_student)


# Example 4: Attributes store data belonging to an object.
student.name = "Asha"
student.grade = 10
print("Example 4 - Attributes:", student.name, student.grade)


# Example 5: Attributes can be read and changed.
student.grade = 11
print("Example 5 - Updated grade:", student.grade)


# Example 6: An object can contain data after a class has been created.
class Book:
    """Represent a book with a title."""

    def __init__(self, title: str) -> None:
        self.title = title


book = Book("Python Basics")
print("Example 6 - Book title:", book.title)


# Example 7: getattr can read an attribute when a default is useful.
print("Example 7 - Default:", getattr(book, "pages", "Not set"))


# Example 8: hasattr checks whether an attribute exists.
print("Example 8 - Has title:", hasattr(book, "title"))


# Example 9: del removes an attribute.
del book.title
print("Example 9 - Title removed:", hasattr(book, "title"))


# Example 10: Objects created from a class belong to that class.
print("Example 10 - Type check:", isinstance(book, Book))


# Quick review:
# - A class is a blueprint for objects.
# - An object is an instance of a class.
# - Attributes store object data.
