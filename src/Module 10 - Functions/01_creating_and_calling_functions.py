# Module 10: Functions
# Topic 1: Creating and calling functions, parameters, and arguments
#
# A function is a named group of instructions. Define it with def, then call
# its name to run its instructions. A parameter is a name in the definition;
# an argument is the actual value supplied when the function is called.


# Example 1: Define and call a simple function
def say_hello():
    print("Hello!")


say_hello()
# Output: Hello!


# Example 2: Call a function more than once
def show_reminder():
    print("Keep practicing Python.")


show_reminder()
show_reminder()
# Output:
# Keep practicing Python.
# Keep practicing Python.


# Example 3: Define a function with one parameter
def greet(name):
    print("Hello,", name)


greet("Asha")
# Output: Hello, Asha
# Here, name is a parameter and "Asha" is an argument.


# Example 4: Call the same function with different arguments
def greet_person(name):
    print(f"Welcome, {name}!")


greet_person("Ravi")
greet_person("Mina")
# Output:
# Welcome, Ravi!
# Welcome, Mina!


# Example 5: Use a parameter inside a calculation
def show_double(number):
    print(number * 2)


show_double(6)
# Output: 12


# Example 6: Use a function to print a formatted message
def show_favorite_food(food):
    print(f"My favorite food is {food}.")


show_favorite_food("noodles")
# Output: My favorite food is noodles.


# Example 7: Pass a variable as an argument
def announce_city(city):
    print(f"Today's city is {city}.")


current_city = "Delhi"
announce_city(current_city)
# Output: Today's city is Delhi.


# Example 8: Use two parameters
def describe_pet(name, animal):
    print(f"{name} is a {animal}.")


describe_pet("Milo", "cat")
# Output: Milo is a cat.


# Example 9: Pass values of different types
def show_profile(name, age):
    print(f"{name} is {age} years old.")


show_profile("Asha", 18)
# Output: Asha is 18 years old.


# Example 10: A function can call another function
def print_line():
    print("----------------")


def show_title():
    print_line()
    print("Python Practice")
    print_line()


show_title()
# Output:
# ----------------
# Python Practice
# ----------------


# Quick review:
# - def creates a function; calling its name runs it.
# - Parameters are names in the function definition.
# - Arguments are values passed to a function call.
