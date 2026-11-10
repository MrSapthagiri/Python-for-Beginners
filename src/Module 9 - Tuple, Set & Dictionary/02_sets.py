# Module 9: Sets
# ==============
#
# DEFINITION
# A set is a mutable collection of unique items. Sets do not keep items in a
# guaranteed display order, and they do not support indexing or slicing.
#
# SYNTAX
#     colors = {"red", "green", "blue"}
#     empty_set = set()
#
# Use set() for an empty set: {} creates an empty dictionary instead.
#
# COMMON OPERATIONS
# - add(value): add one value.
# - remove(value): remove a value; raises KeyError if it is absent.
# - discard(value): remove a value if present; does nothing if absent.
# - union(other): values in either set.
# - intersection(other): values shared by both sets.
# - difference(other): values in this set but not the other.
#
# Set order is not guaranteed. The examples sort displayed values to make the
# sample output predictable.


# Example 1: Create a set
# Explanation: Braces with comma-separated values create a set.
colors = {"red", "green", "blue"}
print("Example 1 - Set values:", sorted(colors))
# Output: Example 1 - Set values: ['blue', 'green', 'red']


# Example 2: Sets keep only unique values
# Explanation: Repeated values are reduced to one occurrence.
numbers = {1, 2, 3}
print("\nExample 2 - Unique values:", sorted(numbers))
# Output: Example 2 - Unique values: [1, 2, 3]


# Example 3: Create an empty set
# Explanation: set() creates an empty set; {} creates an empty dictionary.
empty_set: set[object] = set()
print("\nExample 3 - Empty set:", empty_set)
# Output: Example 3 - Empty set: set()


# Example 4: Add an item
# Explanation: add() inserts a value; adding an existing value has no effect.
colors = {"red", "blue"}
colors.add("green")
colors.add("red")
print("\nExample 4 - After adding:", sorted(colors))
# Output: Example 4 - After adding: ['blue', 'green', 'red']


# Example 5: Remove an item safely with discard()
# Explanation: discard() removes the value if present and does not raise an
# error if it is missing.
colors = {"red", "green", "blue"}
colors.discard("green")
colors.discard("purple")
print("\nExample 5 - After discard:", sorted(colors))
# Output: Example 5 - After discard: ['blue', 'red']


# Example 6: Union
# Explanation: Union contains every distinct value from either set.
first = {1, 2, 3}
second = {3, 4, 5}
print("\nExample 6 - Union:", sorted(first.union(second)))
# Output: Example 6 - Union: [1, 2, 3, 4, 5]


# Example 7: Intersection
# Explanation: Intersection contains only values present in both sets.
first = {1, 2, 3}
second = {3, 4, 5}
print("\nExample 7 - Intersection:", sorted(first.intersection(second)))
# Output: Example 7 - Intersection: [3]


# Example 8: Difference
# Explanation: first.difference(second) contains values in first but not second.
first = {1, 2, 3}
second = {3, 4, 5}
print("\nExample 8 - Difference:", sorted(first.difference(second)))
# Output: Example 8 - Difference: [1, 2]


# QUICK REVISION
# - Sets contain unique values and have no guaranteed order.
# - Use set() to create an empty set.
# - Use add(), remove(), or discard() to change a set.
# - Use union(), intersection(), and difference() to compare sets.
