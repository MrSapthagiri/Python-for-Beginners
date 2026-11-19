# Module 15: OOP Concepts
# Topic 3: Polymorphism and method overriding


class Payment:
    def pay(self, amount):
        raise NotImplementedError("subclasses must implement pay")


class CardPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount:.2f} with card"


class CashPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount:.2f} with cash"


class UpiPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount:.2f} with UPI"


# Example 1: Different objects implement the same method name.
payments = [CardPayment(), CashPayment(), UpiPayment()]
for payment in payments:
    print("Example 1 -", payment.pay(100))


# Example 2: One loop sends the same message to different types.
for payment in payments:
    print("Example 2 -", type(payment).__name__)


# Example 3: A method can return a different behavior for each subclass.
class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


animals = [Dog(), Cat()]
print("Example 3 -",
      [animal.speak() for animal in animals])


# Example 4: Polymorphism works with duck typing too.
class Robot:
    def speak(self):
        return "Beep"


for object_with_speak in animals + [Robot()]:
    print("Example 4 -", object_with_speak.speak())


# Example 5: Calling len() on different types demonstrates polymorphism.
print("Example 5 - Built-in polymorphism:",
      len("Python"), len([1, 2, 3]))


# Example 6: Override run() to specialize an activity.
class Task:
    def run(self):
        return "Running generic task"


class ReportTask(Task):
    def run(self):
        return "Generating report"


print("Example 6 -", ReportTask().run())


# Example 7: Override string representation for user-friendly output.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


print("Example 7 -", Point(3, 5))


# Example 8: Override addition to give a class custom behavior.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


print("Example 8 -", Vector(1, 2) + Vector(3, 4))


# Example 9: A function can accept any compatible payment object.
def process_payment(payment: Payment, amount):
    print("Example 9 -", payment.pay(amount))


process_payment(CashPayment(), 75)


# Example 10: Same interface, different implementation.
class SmsNotification:
    def send(self, message):
        return f"SMS: {message}"


class EmailNotification:
    def send(self, message):
        return f"Email: {message}"


notifications = [SmsNotification(), EmailNotification()]
print("Example 10 -",
      [notification.send("Hello") for notification in notifications])


# Quick review:
# - Polymorphism lets different classes respond to the same method call.
# - Overriding provides a different implementation for a subclass.
# - Duck typing uses compatible behavior rather than a required inheritance.
