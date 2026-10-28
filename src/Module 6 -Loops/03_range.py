"""
================================================================================
Topic: The 'range()' Function
================================================================================

1. DEFINITION:
`range()` is a built-in function that generates a sequence of numbers. 
It is almost always used in 'for' loops to run a block of code a specific 
number of times.
Syntax: range(stop) OR range(start, stop) OR range(start, stop, step)

2. FLOWCHART (Mental Model):
      [range(3)] generates -> [0, 1, 2]
      [range(2, 5)] generates -> [2, 3, 4]
      [range(0, 10, 2)] generates -> [0, 2, 4, 6, 8] 0 1 2 3 4 5 6 7 8 9
      * Note: It ALWAYS stops BEFORE the 'stop' number.

================================================================================
"""

print("\n--- Low Level (Basic) ---")

# ==========================================
# Example 1: Basic range(stop)
# ==========================================
for i in range(3):
    print(f"Ex 1: Loop number {i}")
# Explanation: range(3) gives 0, 1, 2. It loops exactly 3 times.

# ==========================================
# Example 2: Repeating an action
# ==========================================
for i in range(2):
    print("Ex 2: Hello!")
# Explanation: We don't even use 'i', we just want it to say Hello twice.

# ==========================================
# Example 3: range(start, stop)
# ==========================================
for i in range(5, 8):
    print(f"Ex 3: {i}")
# Explanation: Starts at 5, stops BEFORE 8. Outputs 5, 6, 7.

print("\n--- Medium Level (Intermediate) ---")

# ==========================================
# Example 4: range(start, stop, step)
# ==========================================
for i in range(0, 10, 2):
    print(f"Ex 4: Even number: {i}")
# Explanation: Starts at 0, steps by +2. Outputs 0, 2, 4, 6, 8.

# ==========================================
# Example 5: Counting backwards
# ==========================================
for i in range(3, 0, -1):
    print(f"Ex 5: Countdown: {i}")
# Explanation: Negative step (-1) counts backwards. Stops before 0. Outputs 3, 2, 1.

# ==========================================
# Example 6: Converting range to a list
# ==========================================
numbers = list(range(1, 6))
print(f"Ex 6: Created list: {numbers}")
# Explanation: range() generates numbers on the fly, but list() forces it to save them.

# ==========================================
# Example 7: Looping using list length (len)
# ==========================================
colors = ["red", "blue", "green"]
for i in range(len(colors)):
    print(f"Ex 7: Index {i} has color {colors[i]}")
# Explanation: len(colors) is 3. range(3) gives 0, 1, 2, matching the list indexes.

print("\n--- High Level (Advanced/Senior) ---")

# ==========================================
# Example 8: Checking if a number is in a range (Fast!)
# ==========================================
age = 25
if age in range(18, 30):
    print("Ex 8: User is a young adult.")
# Explanation: Python optimizes this to be a fast math check rather than scanning a list.

# ==========================================
# Example 9: Memory efficiency of range()
# ==========================================
import sys
massive_range = range(1000000)
print(f"Ex 9: Memory size of 1 Million numbers: {sys.getsizeof(massive_range)} bytes")
# Explanation: range() doesn't store all the numbers in memory, it just remembers the formula (start, stop, step). So it's incredibly tiny in RAM!

# ==========================================
# Example 10: Generating alternating patterns
# ==========================================
# Use range step to process every 3rd item in a large dataset simulation
data = ["A", "B", "C", "D", "E", "F"]
for i in range(0, len(data), 3):
    print(f"Ex 10: Processing batch at index {i}: {data[i]}")
# Explanation: Powerful way to jump through data at fixed intervals.
