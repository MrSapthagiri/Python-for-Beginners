# Module 8: Lists — Adding and Removing Elements
# ================================================
#
# DEFINITION
# Lists are mutable, so you can add or remove items after creating a list.
# These methods change the list itself.
#
# METHODS
# - append(item): adds one item to the end of the list.
# - insert(index, item): adds one item before the specified index.
# - remove(item): removes the first matching value; raises ValueError if absent.
# - pop(index): removes and returns the item at index. With no index, removes
#   and returns the last item.
#
# IMPORTANT NOTES
# - append() adds its argument as one item. To add several items individually,
#   use extend(), which is not covered in this lesson.
# - insert() places an item at an index; existing items at and after it move.
# - remove() searches by value, while pop() removes by position.
# - pop() on an empty list raises IndexError.


# Example 1: append()
# Explanation: "orange" is added to the end of the list.
fruits = ["apple", "banana"]
fruits.append("orange")
print("Example 1 - After append:", fruits)
# Output: Example 1 - After append: ['apple', 'banana', 'orange']


# Example 2: insert()
# Explanation: Index 1 is the position before "banana".
fruits = ["apple", "banana"]
fruits.insert(1, "mango")
print("\nExample 2 - After insert:", fruits)
# Output: Example 2 - After insert: ['apple', 'mango', 'banana']


# Example 3: remove()
# Explanation: remove() deletes the first matching "banana".
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print("\nExample 3 - After remove:", fruits)
# Output: Example 3 - After remove: ['apple', 'cherry', 'banana']


# Example 4: pop() without an index
# Explanation: With no index, pop() removes and returns the last item.
fruits = ["apple", "banana", "cherry"]
removed_fruit = fruits.pop()
print("\nExample 4 - Removed item:", removed_fruit)
print("Example 4 - Remaining list:", fruits)
# Output:
# Example 4 - Removed item: cherry
# Example 4 - Remaining list: ['apple', 'banana']


# Example 5: pop() with an index
# Explanation: pop(1) removes and returns the item at index 1.
colors = ["red", "green", "blue"]
removed_color = colors.pop(1)
print("\nExample 5 - Removed color:", removed_color)
print("Example 5 - Remaining colors:", colors)
# Output:
# Example 5 - Removed color: green
# Example 5 - Remaining colors: ['red', 'blue']


# Example 6: Remove an item only when it is present
# Explanation: The membership check avoids calling remove() for a missing value.
tasks = ["read", "practice"]
task_to_remove = "practice"
if task_to_remove in tasks:
    tasks.remove(task_to_remove)
print("\nExample 6 - Remaining tasks:", tasks)
# Output: Example 6 - Remaining tasks: ['read']


# QUICK REVISION
# - Add at the end: items.append(value)
# - Add at a position: items.insert(index, value)
# - Remove first matching value: items.remove(value)
# - Remove and return an item: items.pop(index)
