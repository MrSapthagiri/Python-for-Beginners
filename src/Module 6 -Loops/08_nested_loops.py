"""
================================================================================
Topic: Nested Loops
================================================================================

1. DEFINITION:
A nested loop is a loop inside the body of another loop. 
The "inner loop" will complete ALL of its iterations for EVERY single 
iteration of the "outer loop".
Example: If the outer loop runs 3 times, and the inner loop runs 3 times, 
the inner code executes 9 times (3 * 3).

2. FLOWCHART (Mental Model):
   [Outer Loop Iteration 1]
       -> [Inner Loop 1, Inner Loop 2, Inner Loop 3]
   [Outer Loop Iteration 2]
       -> [Inner Loop 1, Inner Loop 2, Inner Loop 3]
   [Outer Loop Iteration 3]
       -> [Inner Loop 1, Inner Loop 2, Inner Loop 3]

================================================================================
"""

print("\n--- Low Level (Basic) ---")

# ==========================================
# Example 1: Basic nested for loops
# ==========================================
print("Ex 1:")
for outer in range(2): # Runs 0, 1
    for inner in range(3): # Runs 0, 1, 2
        print(f"  Outer: {outer}, Inner: {inner}")
# Explanation: The inner loop spins fully 3 times before the outer loop moves forward once.

# ==========================================
# Example 2: Generating coordinates (Grid)
# ==========================================
print("Ex 2: 2x2 Grid")
for x in range(2):
    for y in range(2):
        print(f"({x}, {y})", end=" ")
    print() # New line after the inner loop finishes
# Explanation: Common way to generate (X,Y) coordinates for a 2D map.

# ==========================================
# Example 3: Nested while loops
# ==========================================
print("Ex 3:")
i = 1
while i <= 2:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
# Explanation: Same logic as 'for', but using 'while'. Note how 'j' is reset inside the outer loop.

print("\n--- Medium Level (Intermediate) ---")

# ==========================================
# Example 4: Creating a multiplication table
# ==========================================
print("Ex 4: Times Table")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end=" | ")
    print()
# Explanation: Creates a 3x3 multiplication grid.

# ==========================================
# Example 5: Iterating over a list of lists (2D Array)
# ==========================================
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Ex 5: Reading a Matrix")
for row in matrix: # First loop gets the rows (lists)
    for num in row: # Second loop gets the numbers inside those lists
        print(num, end=" ")
    print()
# Explanation: The standard way to read spreadsheets, matrices, or image pixels.

# ==========================================
# Example 6: Combining items from two lists
# ==========================================
colors = ["Red", "Blue"]
cars = ["Ford", "BMW"]
print("Ex 6: Combinations")
for color in colors:
    for car in cars:
        print(f"{color} {car}")
# Explanation: Creates every possible combination (Cartesian product) of the two lists.

print("\n--- High Level (Advanced/Senior) ---")

# ==========================================
# Example 7: Flattening a 2D list with Nested Comprehensions
# ==========================================
# Seniors often turn nested loops into a one-liner
nested_list = [[1, 2], [3, 4], [5, 6]]
# Read as: give me 'item' for every 'sublist' in 'nested_list', for every 'item' in that 'sublist'
flat_list = [item for sublist in nested_list for item in sublist]
print(f"Ex 7: Flattened -> {flat_list}")
# Explanation: Extremely fast and compact way to flatten arrays.

# ==========================================
# Example 8: Breaking out of Nested Loops (Watch out!)
# ==========================================
print("Ex 8: Break behavior")
for i in range(3):
    for j in range(3):
        if j == 1:
            break # This ONLY breaks the 'j' loop! The 'i' loop keeps going.
        print(f"  {i},{j}")
# Explanation: Remember, 'break' only escapes the immediate loop it sits inside.

# ==========================================
# Example 9: Avoiding deep nesting for performance (O(N^2) warning)
# ==========================================
# Nested loops are SLOW if datasets are large.
list1 = [1, 2, 3]
list2 = [3, 4, 5]
# Bad way: nested loops (9 operations)
# Good way (Senior): Using sets
common = set(list1).intersection(list2)
print(f"Ex 9: Avoiding nested loops for intersection -> {common}")
# Explanation: Seniors try to avoid nested loops because they scale poorly (exponentially).

# ==========================================
# Example 10: Building a dictionary from nested lists
# ==========================================
pairs = [["Alice", 25], ["Bob", 30]]
# Using a loop to unpack
user_db = {}
for name, age in pairs: # Unpacking directly avoids needing an inner loop!
    user_db[name] = age
print(f"Ex 10: DB -> {user_db}")
# Explanation: Sometimes you can avoid an inner loop entirely by using tuple unpacking.
