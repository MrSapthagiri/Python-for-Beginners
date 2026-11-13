# Module 8: Lists — sort(), reverse(), index(), and count()
# =========================================================
#
# DEFINITION
# A list method is an operation called on a list using dot notation.
# For example: numbers.sort()
#
# METHODS
# - sort(): sorts the list in place, ascending by default.
# - reverse(): reverses the current order in place; it does not sort.
# - index(value): returns the position of the first matching value.
# - count(value): returns the number of times a value appears.
#
# IMPORTANT NOTES
# - sort() and reverse() change the original list and return None.
# - Use sorted(items) if you need a new sorted list and want to keep the
#   original unchanged.
# - index() raises ValueError if the value is not found.
# - index(value, start, stop) can limit the search to a range of indexes.
# - count() returns 0 when there are no matches.
# - Sorting mixed, incompatible types (such as strings and integers) raises
#   TypeError.
#
# SORTING DETAILS
# - sort() compares values and updates their positions in the same list.
# - reverse=True sorts in descending order; it is not the same as reverse().
# - sorted(items) returns a new list and leaves items unchanged.
# - String sorting is case-sensitive and follows character ordering, which may
#   differ from a person's expected dictionary order.
#
# SEARCHING DETAILS
# - index() returns the first matching position when duplicates exist.
# - count() reports all matching occurrences.
# - Use "value in items" when you only need a True/False presence check.


# Example 1: Sort numbers in ascending order
# Explanation: sort() changes the original list into ascending order.
numbers = [5, 2, 8, 1]
numbers.sort()
print("Example 1 - Ascending:", numbers)
# Output: Example 1 - Ascending: [1, 2, 5, 8]


# Example 2: Sort numbers in descending order
# Explanation: Setting reverse=True sorts from largest to smallest.
numbers = [5, 2, 8, 1]
numbers.sort(reverse=True)
print("\nExample 2 - Descending:", numbers)
# Output: Example 2 - Descending: [8, 5, 2, 1]


# Example 3: Sort words alphabetically
# Explanation: Strings are sorted in lexicographical order.
names = ["Zara", "Asha", "Mina"]
names.sort()
print("\nExample 3 - Sorted names:", names)
# Output: Example 3 - Sorted names: ['Asha', 'Mina', 'Zara']


# Example 4: Reverse the current order
# Explanation: reverse() flips the positions; it does not alphabetically sort.
letters = ["b", "a", "c"]
letters.reverse()
print("\nExample 4 - Reversed:", letters)
# Output: Example 4 - Reversed: ['c', 'a', 'b']


# Example 5: Find an item's index
# Explanation: index() returns the position of the first matching item.
fruits = ["apple", "banana", "cherry"]
print("\nExample 5 - Index of banana:", fruits.index("banana"))
# Output: Example 5 - Index of banana: 1


# Example 6: Count occurrences
# Explanation: count() reports how many times the value appears.
scores = [10, 20, 10, 30, 10]
print("\nExample 6 - Number of tens:", scores.count(10))
# Output: Example 6 - Number of tens: 3


# Example 7: Use sorted() to keep the original list unchanged
# Explanation: sorted() returns a new sorted list.
numbers = [3, 1, 2]
sorted_numbers = sorted(numbers)
print("\nExample 7 - Original:", numbers)
print("Example 7 - New sorted list:", sorted_numbers)
# Output:
# Example 7 - Original: [3, 1, 2]
# Example 7 - New sorted list: [1, 2, 3]


# Example 8: index() with repeated values
# Explanation: index() returns the first occurrence. Supplying a start index
# lets the search continue after an earlier occurrence.
letters = ["a", "b", "a", "c"]
print("\nExample 8 - First a:", letters.index("a"))
print("Example 8 - Next a from index 1:", letters.index("a", 1))
# Output:
# Example 8 - First a: 0
# Example 8 - Next a from index 1: 2


# Example 9: Count a value and check whether it exists
# Explanation: count() gives the number of occurrences; "in" provides a
# Boolean presence check.
colors = ["red", "blue", "red"]
print("\nExample 9 - Red count:", colors.count("red"))
print("Example 9 - Green is present:", "green" in colors)
print("Example 9 - Green count:", colors.count("green"))
# Output:
# Example 9 - Red count: 2
# Example 9 - Green is present: False
# Example 9 - Green count: 0


# Example 10: Sort text without changing its capitalization
# Explanation: str.lower is used as the sort key, so uppercase and lowercase
# words are compared by their lowercase forms.
names = ["zoe", "Asha", "mina"]
names.sort(key=str.lower)
print("\nExample 10 - Case-insensitive sort:", names)
# Output: Example 10 - Case-insensitive sort: ['Asha', 'mina', 'zoe']


# COMMON ERRORS
# - Do not write sorted_numbers = numbers.sort(). sort() returns None; use
#   numbers.sort() to change the list or sorted(numbers) to create a new list.
# - reverse() does not order values from smallest to largest.
# - index(value) fails with ValueError if the value is absent. Check membership
#   first if absence is a normal possibility.


# QUICK REVISION
# - items.sort() changes the list into ascending order.
# - items.sort(reverse=True) changes it into descending order.
# - items.reverse() reverses the current order.
# - items.index(value) finds the first matching index.
# - items.count(value) counts matching items.
# - sorted(items) returns a new sorted list.
