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


# QUICK REVISION
# - Transform items: [expression for item in iterable]
# - Filter items: [item for item in iterable if condition]
# - Use a loop to calculate totals, find a largest value, or count matches.
