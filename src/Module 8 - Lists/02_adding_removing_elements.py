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
#   use extend(). For example, [1, 2].append([3, 4]) produces [1, 2, [3, 4]],
#   while [1, 2].extend([3, 4]) produces [1, 2, 3, 4].
# - insert() places an item at an index; existing items at and after it move.
#   An index larger than the list length inserts at the end; a negative index
#   counts from the end.
# - remove() searches by value, while pop() removes by position.
# - pop() on an empty list raises IndexError.
# - remove() raises ValueError when no matching value exists.
# - Use "value in items" before remove() if the item may be absent.
# - These methods change the existing list. They do not return a new list.
#
# WHICH METHOD SHOULD I USE?
# - Add one item at the end: append(value)
# - Add several items from an iterable: extend(iterable)
# - Insert one item at a chosen position: insert(index, value)
# - Remove a known value: remove(value)
# - Remove an item at a known position and keep it: pop(index)
# - Remove the last item and keep it: pop()


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


# Example 7: append() adds one object; extend() adds each item
# Explanation: append() treats its argument as one item. extend() iterates over
# its argument and adds the argument's items separately.
appended = [1, 2]
appended.append([3, 4])
extended = [1, 2]
extended.extend([3, 4])
print("\nExample 7 - append a list:", appended)
print("Example 7 - extend with a list:", extended)
# Output:
# Example 7 - append a list: [1, 2, [3, 4]]
# Example 7 - extend with a list: [1, 2, 3, 4]


# Example 8: Remove repeated values one at a time
# Explanation: remove() removes only the first matching value each time it is
# called. The while loop continues while another match remains.
numbers = [2, 1, 2, 3, 2]
while 2 in numbers:
    numbers.remove(2)
print("\nExample 8 - All twos removed:", numbers)
# Output: Example 8 - All twos removed: [1, 3]


# Example 9: Use pop() to process items from the end
# Explanation: pop() returns the removed item, so it can be stored and used.
queue = ["first", "second", "third"]
last_item = queue.pop()
print("\nExample 9 - Processed item:", last_item)
print("Example 9 - Remaining queue:", queue)
# Output:
# Example 9 - Processed item: third
# Example 9 - Remaining queue: ['first', 'second']


# COMMON ERRORS
# - Calling remove(value) for a missing value raises ValueError. Check with
#   "if value in items" when absence is expected.
# - Calling pop(index) with an invalid index, or calling pop() on an empty list,
#   raises IndexError.
# - Do not assume append() combines two lists; it adds its argument as one item.


# QUICK REVISION
# - Add at the end: items.append(value)
# - Add at a position: items.insert(index, value)
# - Add every item from another iterable: items.extend(iterable)
# - Remove first matching value: items.remove(value)
# - Remove and return an item: items.pop(index)
