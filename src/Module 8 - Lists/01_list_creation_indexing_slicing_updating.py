# Module 8: Lists — Creation, Indexing, Slicing, and Updating
# ===========================================================
#
# DEFINITION
# A list is an ordered, mutable collection that can store multiple values.
# "Ordered" means items keep their positions. "Mutable" means items can be
# changed after the list is created.
#
# SYNTAX
#     list_name = [item1, item2, item3]
#
# Indexes start at 0. Negative indexes count backward from the end, beginning
# at -1. A slice uses list_name[start:stop], including start but excluding stop.
#
# IMPORTANT NOTES
# - Lists can contain values of the same or different types.
# - An invalid index raises IndexError.
# - Updating an item changes the existing list.
# - Slicing returns a new list and does not change the original list.


# Example 1: Create a list
# Explanation: Square brackets enclose the list's items.
fruits = ["apple", "banana", "cherry"]
print("Example 1 - Created list:", fruits)
# Output: Example 1 - Created list: ['apple', 'banana', 'cherry']


# Example 2: Create lists with different kinds of values
# Explanation: A list may contain different data types.
details = ["Asha", 18, True]
print("\nExample 2 - Mixed values:", details)
# Output: Example 2 - Mixed values: ['Asha', 18, True]


# Example 3: Access items with positive and negative indexes
# Explanation: Index 0 is the first item; index -1 is the last item.
colors = ["red", "green", "blue"]
print("\nExample 3 - First color:", colors[0])
print("Example 3 - Last color:", colors[-1])
# Output:
# Example 3 - First color: red
# Example 3 - Last color: blue


# Example 4: Get a slice
# Explanation: The slice starts at index 1 and stops before index 3.
numbers = [10, 20, 30, 40, 50]
print("\nExample 4 - Slice:", numbers[1:3])
# Output: Example 4 - Slice: [20, 30]


# Example 5: Use omitted slice boundaries
# Explanation: [:2] selects from the beginning; [2:] selects through the end.
print("\nExample 5 - First two:", numbers[:2])
print("Example 5 - From index two:", numbers[2:])
# Output:
# Example 5 - First two: [10, 20]
# Example 5 - From index two: [30, 40, 50]


# Example 6: Update an item
# Explanation: Assign a new value to the item's index to replace it.
fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print("\nExample 6 - Updated list:", fruits)
# Output: Example 6 - Updated list: ['apple', 'mango', 'cherry']


# Example 7: Update a range with slice assignment
# Explanation: Slice assignment replaces the selected range with new items.
numbers = [1, 2, 3, 4]
numbers[1:3] = [20, 30]
print("\nExample 7 - Updated range:", numbers)
# Output: Example 7 - Updated range: [1, 20, 30, 4]


# QUICK REVISION
# - Create: items = ["a", "b", "c"]
# - First item: items[0]
# - Last item: items[-1]
# - Slice: items[start:stop], where stop is excluded
# - Update: items[index] = new_value
