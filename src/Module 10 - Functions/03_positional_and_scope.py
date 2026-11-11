# Module 10: Functions
# Topic 3: Positional arguments and local/global variables
#
# Positional arguments are matched to parameters from left to right. A local
# variable is created inside a function. A global variable is created outside
# functions and can be read throughout this file.


# Example 1: Positional arguments match from left to right
def show_two_values(first, second):
    print("First:", first)
    print("Second:", second)


show_two_values("red", "blue")
# Output:
# First: red
# Second: blue


# Example 2: Changing argument order changes parameter values
def introduce(name, city):
    print(f"{name} lives in {city}.")


introduce("Asha", "Pune")
introduce("Pune", "Asha")
# Output:
# Asha lives in Pune.
# Pune lives in Asha.


# Example 3: A local variable belongs to the function call
def show_local_message():
    message = "I was created inside the function."
    print(message)


show_local_message()
# Output: I was created inside the function.
# message is local to show_local_message().


# Example 4: A local variable can have the same name as a global variable
color = "blue"


def show_another_color():
    color = "green"
    print("Inside:", color)


show_another_color()
print("Outside:", color)
# Output:
# Inside: green
# Outside: blue


# Example 5: A function can read a global variable
greeting = "Good morning"


def greet_user():
    print(greeting, "Asha")


greet_user()
# Output: Good morning Asha


# Example 6: Pass a value instead of relying on a global variable
def greet_with_message(message, name):
    print(message, name)


greet_with_message("Welcome,", "Ravi")
# Output: Welcome, Ravi
# Parameters make it clear which information the function needs.


# Example 7: Keep a calculation variable local
def rectangle_area(width, height):
    area = width * height
    return area


print("Example 7 - Area:", rectangle_area(4, 3))
# Output: Example 7 - Area: 12
# area is local; the returned value can be used by the caller.


# Example 8: Read and update a global variable explicitly
visit_count = 0


def record_visit():
    global visit_count
    visit_count += 1


record_visit()
record_visit()
print("Example 8 - Visits:", visit_count)
# Output: Example 8 - Visits: 2
# global allows assignment to the variable defined outside this function.


# Example 9: Each function call gets its own local parameter value
def show_double(number):
    doubled = number * 2
    print(f"{number} doubled is {doubled}.")


show_double(3)
show_double(7)
# Output:
# 3 doubled is 6.
# 7 doubled is 14.


# Example 10: Return a local result so other code can use it
def make_label(item):
    label = f"Item: {item}"
    return label


saved_label = make_label("notebook")
print("Example 10 -", saved_label)
# Output: Example 10 - Item: notebook
# The local name label is not needed outside; its value is returned.


# Quick review:
# - Positional arguments are matched left to right.
# - Local variables are created inside a function.
# - Functions can read global names, but global assignment needs global.
# - Prefer parameters and return values over changing global variables.
