# Module 6: Strings — Slicing.py
# ================================
#
# 1. INTRODUCTION TO STRING SLICING
# String slicing extracts a portion (substring) of a string.
# It does not change the original string because strings are immutable.
#
# 2. SYNTAX
# string[start:stop:step]
#
# start: Index where slicing begins (included). Default is the beginning.
# stop:  Index where slicing ends (excluded). Default is the end.
# step:  Number of positions to move each time. Default is 1.
#
# Example string: "Python"
# Index:            0 1 2 3 4 5
# Character:        P y t h o n
#
# text[1:4] returns "yth": starts at index 1 and stops before index 4.
#
# 3. IMPORTANT RULES
# - The start index is included; the stop index is excluded.
# - You can omit start, stop, or both.
# - A positive step moves from left to right.
# - A negative step moves from right to left.
# - text[::-1] reverses a string.
# - Out-of-range slice boundaries usually do not raise IndexError.
# - A step of 0 raises ValueError.
# - Slicing returns a new string and leaves the original unchanged.
#
# 4. TEN EXAMPLE PROGRAMS
# Run this file to see all examples and outputs.


# Program 1: Slice a section using start and stop
# Explanation: Start is included and stop is excluded.
text = "Python"
print("Program 1:", text[1:4])  # yth


# Program 2: Get the first three characters
# Explanation: If start is omitted, slicing starts at the beginning.
text = "Python"
print("Program 2:", text[:3])  # Pyt


# Program 3: Get characters from an index to the end
# Explanation: If stop is omitted, slicing continues to the end.
text = "Python"
print("Program 3:", text[2:])  # thon


# Program 4: Copy the complete string using slicing
# Explanation: Omitting start and stop selects the whole string.
text = "Python"
print("Program 4:", text[:])  # Python


# Program 5: Get the last three characters
# Explanation: Negative indices count from the right; -3 starts three characters from the end.
text = "Python"
print("Program 5:", text[-3:])  # hon


# Program 6: Get characters using a step of 2
# Explanation: The step selects every second character.
text = "Python Programming"
print("Program 6:", text[::2])  # Pto rgamn


# Program 7: Reverse a string
# Explanation: A step of -1 moves backward through the string.
text = "Python"
print("Program 7:", text[::-1])  # nohtyP


# Program 8: Slice using negative start and stop indices
# Explanation: Negative indices count backward from the end.
text = "Programming"
print("Program 8:", text[-8:-3])  # gramm


# Program 9: Use slicing with user input
# Explanation: This prints the first five characters, or fewer if the input is shorter.
# Uncomment the following lines to try it:
# text = input("Enter some text: ")
# print("First five characters:", text[:5])


# Program 10: Extract characters using start, stop, and step
# Explanation: Start at index 1, stop before index 8, and select every second character.
text = "ABCDEFGHIJ"
print("Program 10:", text[1:8:2])  # BDFH


# 5. MORE SLICING EXAMPLES
text = "Python"
print("\\nMore examples:")
print(text[0:2])    # Py
print(text[2:5])    # tho
print(text[:4])     # Pyth
print(text[3:])     # hon
print(text[-1:])    # n
print(text[:-1])    # Pytho
print(text[::2])    # Pto
print(text[::-1])   # nohtyP


# 6. COMMON MISTAKES
# Mistake 1: Expecting the stop index to be included
# text[1:4] returns indices 1, 2, and 3—not index 4.
#
# Mistake 2: Using a step of zero
# text[::0]  # ValueError: slice step cannot be zero
#
# Mistake 3: Expecting an out-of-range slice to raise IndexError
# text[0:100] safely returns the string up to its end.


# 7. QUICK REVISION
# - Syntax: string[start:stop:step]
# - Start is included; stop is excluded.
# - Default step is 1.
# - Positive step moves left to right.
# - Negative step moves right to left.
# - text[:n] gets the first n characters.
# - text[-n:] gets the last n characters.
# - text[::-1] reverses the string.
# - Slicing does not modify the original string.
#
# Interview question:
# What is the difference between indexing and slicing?
# Answer:
# - Indexing returns one character, for example text[0].
# - Slicing returns a portion of a string, for example text[0:3].
