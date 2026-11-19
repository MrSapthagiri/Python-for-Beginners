# Module 14: OOP Fundamentals
# Topic 4: Instance variables and instance methods


class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed = max(0, self.speed - amount)

    def display(self):
        return f"{self.brand} is moving at {self.speed} km/h"


# Example 1: Instance variables belong to each object.
first_car = Car("Toyota", 20)
second_car = Car("Honda")
print("Example 1 - Instances:",
      first_car.brand, second_car.brand)


# Example 2: Instance methods read instance variables.
print("Example 2 -", first_car.display())


# Example 3: An instance method updates instance state.
first_car.accelerate(30)
print("Example 3 -", first_car.display())


# Example 4: The second object is unaffected.
print("Example 4 -", second_car.display())


# Example 5: Brake a car safely with max().
first_car.brake(70)
print("Example 5 -", first_car.display())


# Example 6: Objects can expose useful instance methods.
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        return self.score >= 40


student = Student("Asha", 55)
print("Example 6 - Passed:", student.is_passed())


# Example 7: Instance variables can be added after construction.
student.grade = "A"
print("Example 7 - Grade:", student.grade)


# Example 8: Methods can produce values from multiple instance variables.
class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


box = Box(4, 3, 2)
print("Example 8 - Volume:", box.volume())


# Example 9: Instance variables are stored in each object's __dict__.
print("Example 9 - Student data:", student.__dict__)


# Example 10: Each instance can have a different value.
another_student = Student("Ravi", 35)
print("Example 10 - Scores:",
      student.score, another_student.score)


# Quick review:
# - Instance variables are typically created with self in __init__.
# - Each object has its own copy of instance variable values.
# - Instance methods receive self as their first parameter.
