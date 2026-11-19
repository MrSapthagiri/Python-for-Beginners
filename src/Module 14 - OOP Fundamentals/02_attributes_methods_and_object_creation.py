# Module 14: OOP Fundamentals
# Topic 2: Attributes, methods, and object creation


class Rectangle:
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Example 1: Call the class constructor to create an object.
rectangle = Rectangle()
print("Example 1 - Object:", rectangle)


# Example 2: Set attributes through a method.
rectangle.set_dimensions(5, 3)
print("Example 2 - Dimensions:", rectangle.width, rectangle.height)


# Example 3: Call a method that uses the object's attributes.
print("Example 3 - Area:", rectangle.area())


# Example 4: Create and configure a second object independently.
small_rectangle = Rectangle()
small_rectangle.set_dimensions(2, 4)
print("Example 4 - Small area:", small_rectangle.area())


# Example 5: The original object keeps its own dimensions.
print("Example 5 - First area:", rectangle.area())


# Example 6: Read and update an attribute directly.
rectangle.width = 7
print("Example 6 - Updated area:", rectangle.area())


# Example 7: Methods can return calculated values.
class Temperature:
    def set_celsius(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9 / 5) + 32


temperature = Temperature()
temperature.set_celsius(25)
print("Example 7 - Fahrenheit:", temperature.to_fahrenheit())


# Example 8: Methods can format and return text.
class Counter:
    def set_value(self, value):
        self.value = value

    def description(self):
        return f"Counter value: {self.value}"


counter = Counter()
counter.set_value(12)
print("Example 8 -", counter.description())


# Example 9: A method can update one of the object's attributes.
class Score:
    def set_points(self, points):
        self.points = points

    def add_points(self, points):
        self.points += points


score = Score()
score.set_points(10)
score.add_points(5)
print("Example 9 - Score:", score.points)


# Example 10: Attribute access is object-specific.
another_score = Score()
another_score.set_points(30)
print("Example 10 - Scores:", score.points, another_score.points)


# Quick review:
# - Attributes represent data stored on an object.
# - Methods represent actions performed by an object.
# - Calling a method is written as object.method(arguments).
