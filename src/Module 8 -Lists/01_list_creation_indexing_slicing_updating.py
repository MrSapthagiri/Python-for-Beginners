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
# - len(items) returns the number of items; it is not the last index.
# - The last positive index is len(items) - 1; the last item is also items[-1].
# - The membership operators "in" and "not in" check for a value.
# - Assigning another variable to a list does not make an independent copy:
#   both variable names refer to the same list. Use list.copy() for a shallow
#   copy when you need an independent outer list.
#
# INDEX MAP
# For values = ["A", "B", "C"]:
#     Positive index:   0    1    2
#     Value:           "A"  "B"  "C"
#     Negative index:  -3   -2   -1
#
# SLICE MAP
# In items[start:stop:step], start is included and stop is excluded.
# A positive step moves left to right; a negative step moves right to left.
# A step of zero is invalid and raises ValueError.


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


# Example 8: Check the length and whether a value is present
# Explanation: len() counts items; "in" checks for a matching value.
fruits = ["apple", "banana", "cherry"]
print("\nExample 8 - Number of fruits:", len(fruits))
print("Example 8 - Is banana present?", "banana" in fruits)
print("Example 8 - Is mango absent?", "mango" not in fruits)
# Output:
# Example 8 - Number of fruits: 3
# Example 8 - Is banana present? True
# Example 8 - Is mango absent? True


# Example 9: Use a slice step and reverse a list with slicing
# Explanation: [::2] selects every second item. [::-1] reads from end to start.
letters = ["A", "B", "C", "D", "E"]
print("\nExample 9 - Every second letter:", letters[::2])
print("Example 9 - Reversed copy:", letters[::-1])
print("Example 9 - Original remains:", letters)
# Output:
# Example 9 - Every second letter: ['A', 'C', 'E']
# Example 9 - Reversed copy: ['E', 'D', 'C', 'B', 'A']
# Example 9 - Original remains: ['A', 'B', 'C', 'D', 'E']


# Example 10: Copy a list before updating it
# Explanation: Assignment creates another reference to the same list. copy()
# creates a separate outer list, so changing the copy does not change the
# original list.
original = ["pen", "book"]
same_list = original
separate_list = original.copy()
same_list[0] = "pencil"
separate_list[1] = "notebook"
print("\nExample 10 - Original after shared-reference update:", original)
print("Example 10 - Separate copy:", separate_list)
# Output:
# Example 10 - Original after shared-reference update: ['pencil', 'book']
# Example 10 - Separate copy: ['pen', 'notebook']


# Example 11: Create a list from another iterable
# Explanation: list() builds a list from an iterable such as a string.
letters = list("cat")
print("\nExample 11 - List from string:", letters)
# Output: Example 11 - List from string: ['c', 'a', 't']


# COMMON ERRORS
# - items[len(items)] is out of range; the last valid positive index is
#   len(items) - 1. Prefer items[-1] to get the last item.
# - items[1:3] does not include index 3.
# - items[0] = value changes the list. This differs from strings, which cannot
#   be changed one character at a time.
# - A shallow copy separates the outer list, but nested inner lists are still
#   shared. Deep copying is beyond the scope of this lesson.


# QUICK REVISION
# - Create: items = ["a", "b", "c"]
# - First item: items[0]
# - Last item: items[-1]
# - Slice: items[start:stop], where stop is excluded
# - Update: items[index] = new_value
# - Length: len(items); membership: value in items
# - Copy outer list: items.copy()
