# Module 8: Lists — Comprehensions and Basic Problems
# ====================================================
#
# DEFINITION
# A list comprehension is a concise way to create a new list from an iterable.
#
# BASIC SYNTAX
#     [expression for item in iterable]
#
# WITH A CONDITION
#     [expression for item in iterable if condition]
#
# The expression is calculated for each item. When an if condition is present,
# only items that satisfy it are included.
#
# IMPORTANT NOTES
# - A comprehension creates a new list; it does not change the source list.
# - Use a regular loop when it makes a complicated operation easier to read.
# - The examples below use basic transformations and filtering.
#
# HOW TO READ A COMPREHENSION
#     [expression for item in iterable if condition]
# Read it as: "For each item in iterable, include expression if condition is
# true." The condition is optional. The expression determines the value placed
# in the output list.
#
# LOOP EQUIVALENT
#     doubled = []
#     for number in numbers:
#         doubled.append(number * 2)
# The equivalent comprehension is:
#     doubled = [number * 2 for number in numbers]
#
# PROBLEM-SOLVING STEPS
# 1. Identify the input list and the required result.
# 2. Decide whether each input produces a transformed output value.
# 3. Decide whether some input values should be filtered out.
# 4. Use a comprehension for a simple transformation/filter, or a loop when
#    several steps or state updates are needed.


# Example 1: Create squares
# Explanation: item * item is calculated for each number from 1 through 5.
squares = [number * number for number in range(1, 6)]
print("Example 1 - Squares:", squares)
# Output: Example 1 - Squares: [1, 4, 9, 16, 25]


# Example 2: Keep only even numbers
# Explanation: The if condition includes a number only when its remainder
# after division by 2 is zero.
numbers = [1, 2, 3, 4, 5, 6]
evens = [number for number in numbers if number % 2 == 0]
print("\nExample 2 - Even numbers:", evens)
# Output: Example 2 - Even numbers: [2, 4, 6]


# Example 3: Convert words to uppercase
# Explanation: word.upper() is evaluated for every word in the source list.
words = ["python", "lists", "practice"]
uppercase_words = [word.upper() for word in words]
print("\nExample 3 - Uppercase words:", uppercase_words)
# Output: Example 3 - Uppercase words: ['PYTHON', 'LISTS', 'PRACTICE']


# Example 4: Find the total of a list
# Explanation: A loop adds each number to a running total.
prices = [5, 10, 15]
total = 0
for price in prices:
    total += price
print("\nExample 4 - Total price:", total)
# Output: Example 4 - Total price: 30


# Example 5: Find the largest value
# Explanation: Start with the first item and replace largest when a bigger
# number is found.
scores = [72, 95, 88, 81]
largest = scores[0]
for score in scores[1:]:
    if score > largest:
        largest = score
print("\nExample 5 - Largest score:", largest)
# Output: Example 5 - Largest score: 95


# Example 6: Count items that match a condition
# Explanation: Increase the count whenever a word has more than four letters.
words = ["cat", "tiger", "lion", "elephant"]
long_word_count = 0
for word in words:
    if len(word) > 4:
        long_word_count += 1
print("\nExample 6 - Words longer than four letters:", long_word_count)
# Output: Example 6 - Words longer than four letters: 2


# Example 7: Transform and filter in one comprehension
# Explanation: The expression converts each selected temperature to
# Fahrenheit. The if clause includes only Celsius values at or above 20.
celsius_values = [12, 20, 25, 30]
warm_fahrenheit = [
    celsius * 9 / 5 + 32
    for celsius in celsius_values
    if celsius >= 20
]
print("\nExample 7 - Warm temperatures in Fahrenheit:", warm_fahrenheit)
# Output: Example 7 - Warm temperatures in Fahrenheit: [68.0, 77.0, 86.0]


# Example 8: Build a list of odd numbers
# Explanation: The remainder operator identifies odd numbers: an odd number
# divided by 2 has a remainder of 1.
odd_numbers = [number for number in range(1, 16) if number % 2 == 1]
print("\nExample 8 - Odd numbers:", odd_numbers)
# Output: Example 8 - Odd numbers: [1, 3, 5, 7, 9, 11, 13, 15]


# Example 9: Keep only words that start with a chosen letter
# Explanation: The if condition filters words; the expression keeps each
# selected word unchanged.
words = ["apple", "avocado", "banana", "apricot"]
words_starting_with_a = [
    word for word in words if word.startswith("a")
]
print("\nExample 9 - Words beginning with a:", words_starting_with_a)
# Output: Example 9 - Words beginning with a: ['apple', 'avocado', 'apricot']


# Example 10: Use built-in functions for common list calculations
# Explanation: sum() adds the values; max() finds the largest value.
# max() requires at least one item, so this example uses a non-empty list.
scores = [72, 95, 88, 81]
print("\nExample 10 - Sum of scores:", sum(scores))
print("Example 10 - Highest score:", max(scores))
# Output:
# Example 10 - Sum of scores: 336
# Example 10 - Highest score: 95


# Example 11: Use a regular loop for a running total
# Explanation: A loop makes the changing total explicit and works well when
# the calculation needs multiple steps.
prices = [5, 10, 15]
total = 0
for price in prices:
    total = total + price
print("\nExample 11 - Total using a loop:", total)
# Output: Example 11 - Total using a loop: 30


# COMMON MISTAKES
# - Put the expression before "for": [number * 2 for number in numbers].
# - Use "if" after the for clause when filtering:
#   [number for number in numbers if number > 0].
# - A comprehension over an empty iterable returns an empty list.
# - Avoid deeply nested or complicated comprehensions; use regular loops for
#   clarity.
# - max() and min() raise ValueError on an empty list. Check the list first
#   when it might be empty.


# QUICK REVISION
# - Transform items: [expression for item in iterable]
# - Filter items: [item for item in iterable if condition]
# - Use a loop to calculate totals, find a largest value, or count matches.
# - Use sum(), min(), and max() for common numeric list calculations.
