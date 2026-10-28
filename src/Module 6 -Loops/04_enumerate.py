"""
================================================================================
Topic: The 'enumerate()' Function
================================================================================

1. DEFINITION:
`enumerate()` takes a collection (like a list) and adds a counter/index to it. 
Instead of just giving you the item, it gives you a tuple containing 
(index, item). It is the professional alternative to using `range(len(list))`.

2. FLOWCHART (Mental Model):
      List: ["apple", "banana"]
      
      Without enumerate:
      loop gets: "apple", then "banana"
      
      With enumerate:
      loop gets: (0, "apple"), then (1, "banana")

================================================================================
"""

print("\n--- Low Level (Basic) ---")

# ==========================================
# Example 1: Basic enumerate
# ==========================================
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"Ex 1: Index {index} is {name}")
# Explanation: It neatly unpacks the index (0, 1, 2) and the value at the same time.

# ==========================================
# Example 2: Changing the starting index
# ==========================================
for count, name in enumerate(names, start=1):
    print(f"Ex 2: Student #{count}: {name}")
# Explanation: start=1 makes it count 1, 2, 3 instead of 0, 1, 2. Great for UI numbering.

# ==========================================
# Example 3: Viewing what enumerate actually outputs
# ==========================================
raw_enum = list(enumerate(["A", "B"]))
print(f"Ex 3: Enumerate looks like this: {raw_enum}")
# Explanation: Shows that it literally creates pairs (tuples) of (index, value).

print("\n--- Medium Level (Intermediate) ---")

# ==========================================
# Example 4: Modifying a list in place safely
# ==========================================
prices = [10, 20, 30]
for index, price in enumerate(prices):
    prices[index] = price * 2 # Double the price
print(f"Ex 4: Doubled prices: {prices}")
# Explanation: We need the index to actually save the new value back into the list.

# ==========================================
# Example 5: Finding the index of a specific item
# ==========================================
colors = ["red", "blue", "green", "blue"]
target = "blue"
for i, color in enumerate(colors):
    if color == target:
        print(f"Ex 5: Found {target} at position {i}")
# Explanation: Very handy when you need to know *where* something is, not just that it exists.

# ==========================================
# Example 6: Skipping every other item (Alternative to range step)
# ==========================================
items = ["Task1", "Task2", "Task3", "Task4"]
for i, item in enumerate(items):
    if i % 2 == 0:
        print(f"Ex 6: Processing even index: {item}")
# Explanation: Uses the index to do math and skip certain iterations.

print("\n--- High Level (Advanced/Senior) ---")

# ==========================================
# Example 7: Enumerate with Strings
# ==========================================
# Strings are iterables too!
for pos, char in enumerate("DNA"):
    print(f"Ex 7: Position {pos}: {char}")
# Explanation: Useful for parsing text or highlighting errors at specific character columns.

# ==========================================
# Example 8: Creating a Dictionary from a List
# ==========================================
categories = ["Electronics", "Clothing", "Home"]
# Convert it to {0: 'Electronics', 1: 'Clothing'...}
cat_dict = dict(enumerate(categories, start=100))
print(f"Ex 8: Category DB mapping: {cat_dict}")
# Explanation: A lightning-fast way to generate a database table mapping from a raw list.

# ==========================================
# Example 9: Zipping vs Enumerating
# ==========================================
# Seniors know enumerate is basically zipping with a counter
list_a = ["A", "B"]
print(f"Ex 9: Zip approach: {list(zip(range(len(list_a)), list_a))}")
# Explanation: Just showing that enumerate is a built-in shortcut for a common pattern.

# ==========================================
# Example 10: Enumerate in list comprehensions
# ==========================================
names_list = ["dog", "cat", "bird"]
formatted = [f"{i}: {name.upper()}" for i, name in enumerate(names_list)]
print(f"Ex 10: {formatted}")
# Explanation: You can use enumerate cleanly inside list comprehensions to build formatted strings.
