# Module 9: Tuples
# ===============
#
# DEFINITION
# A tuple is an ordered collection. Like a list, it can hold multiple values
# and supports indexing and slicing. Unlike a list, a tuple is immutable:
# its items cannot be reassigned after creation.
#
# SYNTAX
#     colors = ("red", "green", "blue")
#
# A one-item tuple needs a trailing comma: one_item = ("red",)
#
# COMMON OPERATIONS
# - Indexing and slicing read items and return values or a new tuple.
# - count(value) returns how many times a value appears.
# - index(value) returns the first matching index.
#
# TUPLE VS. LIST
# - Tuple: immutable; usually written with parentheses.
# - List: mutable; usually written with square brackets.
# - Both are ordered and can contain repeated values.


# Example 1: Create a tuple
# Explanation: Parentheses and commas group the values into a tuple.
colors = ("red", "green", "blue")
print("Example 1 - Tuple:", colors)
# Output: Example 1 - Tuple: ('red', 'green', 'blue')


# Example 2: Create a one-item tuple
# Explanation: The comma makes this a tuple rather than a string in parentheses.
one_color = ("red",)
print("\nExample 2 - One-item tuple:", one_color)
# Output: Example 2 - One-item tuple: ('red',)


# Example 3: Access items by index
# Explanation: Index 0 is the first item; index -1 is the last.
dimensions = (1920, 1080)
print("\nExample 3 - Width:", dimensions[0])
print("Example 3 - Height:", dimensions[-1])
# Output:
# Example 3 - Width: 1920
# Example 3 - Height: 1080


# Example 4: Slice a tuple
# Explanation: The start is included and the stop index is excluded.
numbers = (10, 20, 30, 40, 50)
print("\nExample 4 - Slice:", numbers[1:4])
# Output: Example 4 - Slice: (20, 30, 40)


# Example 5: Count repeated values
# Explanation: count() returns the number of matching items.
scores = (10, 20, 10, 30, 10)
print("\nExample 5 - Count of 10:", scores.count(10))
# Output: Example 5 - Count of 10: 3


# Example 6: Find a value's index
# Explanation: index() returns the position of the first matching item.
animals = ("cat", "dog", "bird")
print("\nExample 6 - Index of dog:", animals.index("dog"))
# Output: Example 6 - Index of dog: 1


# Example 7: Compare a tuple with a list
# Explanation: The list can be updated; the tuple cannot be changed in place.
tuple_values = (1, 2, 3)
list_values = [1, 2, 3]
list_values[0] = 99
print("\nExample 7 - Tuple stays unchanged:", tuple_values)
print("Example 7 - List after update:", list_values)
# Output:
# Example 7 - Tuple stays unchanged: (1, 2, 3)
# Example 7 - List after update: [99, 2, 3]


# QUICK REVISION
# - Tuples are ordered and immutable.
# - Use a trailing comma to create a one-item tuple.
# - Index and slice tuples like lists.
# - count() counts matches; index() finds the first matching position.
