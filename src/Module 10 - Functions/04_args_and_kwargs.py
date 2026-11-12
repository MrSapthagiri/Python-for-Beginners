# Module 10: Functions
# Topic 4: *args and **kwargs
#
# *args gathers extra positional arguments into a tuple. ()
# **kwargs gathers extra keyword arguments into a dictionary. key and values {}
# The names args and kwargs are conventions; the * and ** symbols do the work.


# Example 1: Gather extra positional arguments
def show_fruits(*fruits):
    print(fruits)


show_fruits("apple", "banana", "orange")
# Output: ('apple', 'banana', 'orange')


# Example 2: Loop over values gathered by *args
def list_tasks(*tasks):
    for task in tasks:
        print("new", task)


list_tasks("read", "practice", "review")
# Output:
# - read
# - practice
# - review


# Example 3: *args can contain no extra arguments
def count_items(*items):
    print("Number of items:", len(items))


count_items()
# Output: Number of items: 0


# Example 4: Use *args to calculate a total
def adlld_a(*numbers):
    return sum(numbers)


print("Example 4 - Total:", adlld_a(2, 4, 6))
# Output: Example 4 - Total: 12


# Example 5: Combine a regular parameter and *args
def greet_group(greeting, *names):
    for name in names:
        print(greeting, name)


greet_group("Hello,", "Asha", "Ravi")
# Output:
# Hello, Asha
# Hello, Ravi


# Example 6: Gather extra keyword arguments
def show_profile(**details):
    print(details)


show_profile(name="Mina", age=19)
# Output: {'name': 'Mina', 'age': 19}


# Example 7: Read values from the **kwargs dictionary
def print_settings(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")


print_settings(theme="light", language="English")
# Output:
# theme: light
# language: English


# Example 8: Use a regular parameter with **kwargs
def create_message(title, **details):
    print(title)
    for key, value in details.items():
        print(f"{key}: {value}")


create_message("Profile", city="Delhi", member=True)
# Output:
# Profile
# city: Delhi
# member: True


# Example 9: Unpack a list into positional arguments with *
def multiply(first, second):
    return first * second


values = [3, 5]
print("Example 9 - Product:", multiply(*values))
# Output: Example 9 - Product: 15


# Example 10: Unpack a dictionary into keyword arguments with **
def introduce(name, city):
    print(f"{name} lives in {city}.")


person = {"name": "Asha", "city": "Pune"}
introduce(**person)
# Output: Asha lives in Pune.


# Quick review:
# - *args is a tuple of extra positional arguments.
# - **kwargs is a dictionary of extra keyword arguments.
# - *list and **dictionary unpack values into a function call.
