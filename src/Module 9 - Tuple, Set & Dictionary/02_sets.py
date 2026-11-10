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
# - pop(): removes and returns an arbitrary item; do not rely on which one.
# - clear(): removes every item.
# - "value in my_set": tests membership.
#
# Set order is not guaranteed. The examples sort displayed values to make the
# sample output predictable.
#
# SET OPERATION DIAGRAM (IN WORDS)
# A = {1, 2, 3}; B = {3, 4}
# - A union B contains all distinct values: {1, 2, 3, 4}.
# - A intersection B contains shared values: {3}.
# - A difference B contains values only in A: {1, 2}.
# - B difference A contains values only in B: {4}.
# Difference depends on which set comes first; union and intersection do not.


# Example 1: Create a set
# Explanation: Braces with comma-separated values create a set.
colors = {"red", "green", "blue"}
print("Example 1 - Set values:", sorted(colors))
# Output: Example 1 - Set values: ['blue', 'green', 'red']


# Example 2: Sets keep only unique values
# Explanation: Repeated values are reduced to one occurrence.
numbers = {1, 2, 2, 3, 3, 3}
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


# Example 9: Difference is directional
# Explanation: Reversing the operands finds values exclusive to the other set.
first = {1, 2, 3}
second = {3, 4, 5}
print("\nExample 9 - First minus second:", sorted(first - second))
print("Example 9 - Second minus first:", sorted(second - first))
# Output:
# Example 9 - First minus second: [1, 2]
# Example 9 - Second minus first: [4, 5]


# Example 10: Remove values with remove() and discard()
# Explanation: remove() works when the item exists; discard() is safe if it
# might not exist. Both change the original set.
colors = {"red", "green", "blue"}
colors.remove("green")
colors.discard("purple")
print("\nExample 10 - Remaining colors:", sorted(colors))
# Output: Example 10 - Remaining colors: ['blue', 'red']


# Example 11: Check membership and compare sets
# Explanation: Membership checks are useful when asking whether a set contains
# a value. isdisjoint() is true when two sets share no items.
allowed = {"read", "write"}
requested = {"read"}
print("\nExample 11 - Write allowed:", "write" in allowed)
print("Example 11 - Sets disjoint:", allowed.isdisjoint(requested))
# Output:
# Example 11 - Write allowed: True
# Example 11 - Sets disjoint: False


# Example 12: Remove duplicate values from a list
# Explanation: Converting a list to a set removes duplicates. Converting back
# gives a list, but its order is not guaranteed. Sorting makes this output
# predictable and orders these strings alphabetically.
names = ["Mina", "Asha", "Mina", "Ravi"]
unique_names = sorted(set(names))
print("\nExample 12 - Unique names:", unique_names)
# Output: Example 12 - Unique names: ['Asha', 'Mina', 'Ravi']


# Example 13: Create a set from a string
# Explanation: set() takes one item per distinct character in the iterable.
letters = set("banana")
print("\nExample 13 - Unique letters:", sorted(letters))
# Output: Example 13 - Unique letters: ['a', 'b', 'n']


# COMMON MISTAKES
# - {} creates an empty dictionary, not an empty set; use set().
# - Set items must be hashable. For example, a list cannot be an item in a set.
# - Do not access a set by index or expect its printed order to stay the same.
# - remove(value) raises KeyError if value is absent; discard(value) does not.
# - pop() removes an arbitrary set item, not the first or last item.
# - A set can remove duplicates but does not preserve the original list order.


# QUICK REVISION
# - Sets contain unique values and have no guaranteed order.
# - Use set() to create an empty set.
# - Use add(), remove(), or discard() to change a set.
# - Use union(), intersection(), and difference() to compare sets.
# - Membership: value in set_name
