# Module 10: Functions
# Topic 2: Return values, multiple parameters, default and keyword arguments
#
# return sends a result back to the code that called the function. print()
# displays a value, but it does not send that value back for later use.


# Example 1: Return a result
def add_numbers(first, second):
    return first + second


total = add_numbers(3, 4)
print("Example 1 - Total:", total)
# Output: Example 1 - Total: 7




# Example 2: Use a returned value in another calculation
def get_square(number):
    return number * number


answer = get_square(5) + 2
print("\nExample 2 - Answer:", answer)
# Output: Example 2 - Answer: 27


# Example 3: Return a string
def make_greeting(name):
    return f"Hello, {name}!"


message = make_greeting("Ravi")
print("\nExample 3 - Message:", message)
# Output: Example 3 - Message: Hello, Ravi!


# Example 4: Return a value based on a condition
def is_adult(age):
    return age >= 18


print("\nExample 4 - Is age 20 adult?", is_adult(20))
# Output: Example 4 - Is age 20 adult? True


# Example 5: Give a parameter a default value
def greet(name="friend"):
    return f"Hello, {name}!"


print("\nExample 5 - Default:", greet())
print("Example 5 - Named person:", greet("Mina"))
# Output:
# Example 5 - Default: Hello, friend!
# Example 5 - Named person: Hello, Mina!


# Example 6: Use several parameters
def make_full_name(first_name, last_name):
    return f"{first_name} {last_name}"


print("\nExample 6 - Full name:", make_full_name("Asha", "Patel"))
# Output: Example 6 - Full name: Asha Patel


# Example 7: Pass keyword arguments by parameter name
def describe_book(title, author):
    return f"{title} was written by {author}."


description = describe_book(author="A. Writer", title="Python Basics")
print("\nExample 7 - Book:", description)
# Output: Example 7 - Book: Python Basics was written by A. Writer.


# Example 8: Combine a default parameter with a keyword argument
def calculate_price(price, tax_rate=0.1):
    return price + price * tax_rate


print("\nExample 8 - Default tax:", calculate_price(100))
print("Example 8 - Chosen tax:", calculate_price(100, tax_rate=0.2))
# Output:
# Example 8 - Default tax: 110.0
# Example 8 - Chosen tax: 120.0


# Example 9: A function can return more than one value
def get_minimum_and_maximum(numbers):
    return min(numbers), max(numbers)


lowest, highest = get_minimum_and_maximum([8, 3, 10, 5])
print("\nExample 9 - Lowest:", lowest)
print("Example 9 - Highest:", highest)
# Output:
# Example 9 - Lowest: 3
# Example 9 - Highest: 10


# Example 10: A function without return gives back None
def print_notice():
    print("Remember to save your work.")


result = print_notice()
print("\nExample 10 - Returned value:", result)
# Output:
# Remember to save your work.
# Example 10 - Returned value: None


# Quick review:
# - return gives a result back; print only displays something.
# - Keyword arguments name the parameter, so their order can change.
# - Default values are used when an argument is not supplied.
