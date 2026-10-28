"""
================================================================================
Topic: The 'for' Loop
================================================================================

1. DEFINITION:
A 'for' loop is used to iterate (loop) over a sequence (like a list, tuple, 
dictionary, set, or string). It runs a block of code once for each item in the sequence.

2. FLOWCHART:
      [Start Loop]
         |
         v
   [Are there more items in sequence?] --(No)--> [Exit Loop]
         |                                           |
       (Yes)                                         |
         |                                           |
         v                                           |
   [Get the next item]                               |
         |                                           |
         v                                           |
   [Run code block using that item]                  |
         |                                           |
         +-------------------------------------------+

================================================================================
"""

print("\n--- Low Level (Basic) ---")

# ==========================================
# Example 1: Looping over a list
# ==========================================
fruits = ["apple", "banana", "cherry"]
for Number_fruit in fruits:
    print(f"Ex 1: I Need a {Number_fruit}")
# Explanation: The loop grabs "apple", prints it, then grabs "banana", prints it, etc.

# ==========================================
# Example 2: Looping over a string
# ==========================================
word = "Python"
for letter in word:
    print(f"Ex 2: {letter}")
# Explanation: Strings are sequences of characters. It prints one letter per line.

# ==========================================
# Example 3: Adding numbers in a list
# ==========================================
numbers = [1, 2, 3, 4]
total = 0
for num in numbers:
    total = total + num
print(f"Ex 3: Total sum is {total}")
# Explanation: We update the 'total' variable during every loop iteration.

print("\n--- Medium Level (Intermediate) ---")

# ==========================================
# Example 4: Looping over a dictionary (Keys)
# ==========================================
person = {"name": "Alice", "age": 25, "city": "NY"}
for key in person:
    print(f"Ex 4: Key -> {key}")
# Explanation: By default, iterating a dictionary gives you the keys.

# ==========================================
# Example 5: Looping over a dictionary (Values)
# ==========================================
for value in person.values():
    print(f"Ex 5: Value -> {value}")
# Explanation: .values() gives us just the data, ignoring the keys.

# ==========================================
# Example 6: Looping over a dictionary (Keys & Values)
# ==========================================
for key, value in person.items():
    print(f"Ex 6: {key} is {value}")
# Explanation: .items() gives us both at the same time! Very useful.

# ==========================================
# Example 7: Using unpacking with tuples
# ==========================================
coordinates = [(0, 1), (10, 20), (5, 5)]
for x, y in coordinates:
    print(f"Ex 7: X: {x}, Y: {y}")
# Explanation: We can assign multiple variables at once in the 'for' statement.

print("\n--- High Level (Advanced/Senior) ---")

# ==========================================
# Example 8: Filtering data into a new list
# ==========================================
raw_data = [10, -5, 20, 0, -1]
clean_data = []
for num in raw_data:
    if num > 0:
        clean_data.append(num)
print(f"Ex 8: Only positive numbers: {clean_data}")
# Explanation: Using an if-statement inside a loop to filter out bad data.

# ==========================================
# Example 9: The 'for...else' construct
# ==========================================
targets = ["server1", "server2"]
search_for = "server3"

for target in targets:
    if target == search_for:
        print("Ex 9: Found it!")
        break
else:
    # This else belongs to the FOR loop, not an IF statement!
    print("Ex 9: Search finished. Target not found.")
# Explanation: A special Python feature. The 'else' block runs ONLY if the loop finishes naturally.

# ==========================================
# Example 10: List Comprehensions (The Senior way to do Example 8)
# ==========================================
# This does the exact same thing as Example 8, but in one line of code!
senior_clean_data = [num for num in raw_data if num > 0]
print(f"Ex 10: Comprehension output: {senior_clean_data}")
# Explanation: List comprehensions are a compact, fast way to write simple for-loops that build lists.
