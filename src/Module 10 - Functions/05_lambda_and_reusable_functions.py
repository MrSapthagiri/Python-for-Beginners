# Module 10: Functions
# Topic 5: Lambda functions and reusable function design
#
# A lambda is a small anonymous function written as:
#     lambda parameters: expression
# Use def for functions with multiple steps or a useful descriptive name.
# Reusable functions do one clear job, accept needed inputs, and return results.


# Example 1: Define a small reusable function that doubles a number
def double(number):
    """Return the given number multiplied by two."""
    return number * 2


print("Example 1 - Double:", double(4))
# Output: Example 1 - Double: 8


# Example 2: Define a reusable function with two parameters
def add(first, second):
    """Return the sum of two numbers."""
    return first + second


print("\nExample 2 - Sum:", add(3, 5))
# Output: Example 2 - Sum: 8


# Example 3: Sort words by their length
words = ["pear", "fig", "banana"]
words_by_length = sorted(words, key=len)
print("\nExample 3 - By length:", words_by_length)
# Output: Example 3 - By length: ['fig', 'pear', 'banana']


# Example 4: Sort pairs by their second value
students = [("Asha", 88), ("Ravi", 95), ("Mina", 91)]
by_score = sorted(students, key=lambda student: student[1])
print("\nExample 4 - By score:", by_score)
# Output: Example 4 - By score: [('Asha', 88), ('Mina', 91), ('Ravi', 95)]


# Example 5: Keep a lambda simple; use def for a named reusable job
def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


print("\nExample 5 - 20 C in F:", celsius_to_fahrenheit(20))
# Output: Example 5 - 20 C in F: 68.0


# Example 6: Reuse one function with different inputs
def rectangle_area(width, height):
    return width * height


print("\nExample 6 - Small area:", rectangle_area(3, 4))
print("Example 6 - Large area:", rectangle_area(10, 6))
# Output:
# Example 6 - Small area: 12
# Example 6 - Large area: 60


# Example 7: Give a function a descriptive name and one clear job
def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"


print("\nExample 7 - Name:", get_full_name("Asha", "Patel"))
# Output: Example 7 - Name: Asha Patel


# Example 8: Use parameters instead of fixed values inside the function
def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    return price - discount


final_price = calculate_discount(80, 25)
print("\nExample 8 - Final price:", final_price)
# Output: Example 8 - Final price: 60.0


# Example 9: Make a function that returns a value without changing its input
def make_uppercase(text):
    return text.upper()


original_text = "hello"
uppercase_text = make_uppercase(original_text)
print("\nExample 9 - Original:", original_text)
print("Example 9 - New value:", uppercase_text)
# Output:
# Example 9 - Original: hello
# Example 9 - New value: HELLO


# Example 10: Combine small reusable functions
def add_tax(price, tax_rate):
    return price + price * tax_rate


def format_price(price):
    return f"${price:.2f}"


price_with_tax = add_tax(20, 0.1)
print("\nExample 10 - Price with tax:", format_price(price_with_tax))
# Output: Example 10 - Price with tax: $22.00


# Quick review:
# - Lambdas work well for short, one-expression functions.
# - Use def for named functions that need multiple steps or are reused.
# - Good reusable functions have clear names, inputs, and return values.
