# Module 6: Strings — Indexing.py
# =================================
#
# 1. INTRODUCTION TO STRING INDEXING
# String indexing is used to access individual characters in a string by position.

# Python supports:
#   - Positive indexing: starts at 0 (left to right)
#   - Negative indexing: starts at -1 (right to left)
#
# Example: text = "PYTHON"
#
# Positive index:  0   1   2   3   4   5
# Character:       P   Y   T   H   O   N
# Negative index: -6  -5  -4  -3  -2  -1
#
# 2. SYNTAX
# string[index]
#
# - string: variable containing text
# - index: position of the character to access
# - The result is a one-character string.
#
# 3. IMPORTANT RULES
# - Positive indexing starts at 0.
# - Negative indexing starts at -1.
# - Spaces and punctuation also have index positions.
# - Python strings are case-sensitive.
# - The last positive index is len(string) - 1.
# - The first negative index is -len(string).
# - An invalid index raises IndexError.
# - Strings are immutable: individual characters cannot be reassigned.
#
# 4. TEN EXAMPLE PROGRAMS
# Uncomment one example at a time if you want to run it separately.


# Program 1: Access the first character
# Explanation: Index 0 accesses the first character.
text = "Python"
print("Program 1 - First character:", text[0])  # P


# Program 2: Access the last character
# Explanation: Index -1 accesses the last character.
text = "Python"
print("Program 2 - Last character:", text[-1])  # n


# Program 3: Access characters using positive indexing
# Explanation: Positive indices start at zero.
text = "Python"
print("\\nProgram 3 - Positive indexing:")
print(text[0])  # P
print(text[2])  # t
print(text[3])  # h
print(text[5])  # n


# Program 4: Access characters using negative indexing
# Explanation: Negative indices count backward from the end.
text = "Python"
print("\\nProgram 4 - Negative indexing:")
print(text[-1])  # n
print(text[-2])  # o
print(text[-3])  # h
print(text[-6])  # P


# Program 5: Access the middle character
# Explanation: For an odd-length string, len(text) // 2 gives the middle index.
# For an even-length string, this expression returns the character just right of center.
text = "Python"
print("\\nProgram 5 - Middle character:", text[len(text) // 2])  # h


# Program 6: Indexing a string containing spaces
# Explanation: A space is also a character and has an index.
text = "Hello World"
print("\\nProgram 6 - String with spaces:")
print(repr(text[0]))   # 'H'
print(repr(text[5]))   # ' '
print(repr(text[6]))   # 'W'
print(repr(text[10]))  # 'd'


# Program 7: Use len() to access the last characters
# Explanation: The last positive index is len(text) - 1.
text = "Automation"
print("\\nProgram 7 - Using len():")
print("Length:", len(text))               # 10
print("Last character:", text[len(text) - 1])  # n
print("Second-last character:", text[len(text) - 2])  # o


# Program 8: Indexing user input
# Explanation: input() reads a string; indexing accesses its first and last characters.
# This example expects non-empty input.
# Uncomment these lines to try it:
# text = input("Enter a word: ")
# if text:
#     print("First character:", text[0])
#     print("Last character:", text[-1])
# else:
#     print("Please enter a non-empty word.")


# Program 9: Handle an invalid index
# Explanation: Accessing an index outside the valid range raises IndexError.
text = "Python"
print("\\nProgram 9 - Invalid index handling:")
try:
    print(text[10])
except IndexError:
    print("Invalid index")


# Program 10: Print each character with its index
# Explanation: range(len(text)) generates all valid positive indices.
text = "Python"
print("\\nProgram 10 - Character and index:")
for i in range(len(text)):
    print(i, text[i])


# 5. POSITIVE VS NEGATIVE INDEXING
# Positive indexing: left to right; starts at 0.
# Negative indexing: right to left; starts at -1.
# For text = "Python":
#   text[0]  -> 'P'
#   text[2]  -> 't'
#   text[-1] -> 'n'
#   text[-2] -> 'o'
#   text[len(text) - 1] -> 'n'


# 6. COMMON ERRORS
# Error 1: Index out of range
# text = "Python"
# print(text[6])  # IndexError: valid positive indices are 0 through 5
#
# Error 2: Trying to modify a character (strings are immutable)
# text = "Python"
# text[0] = "J"  # TypeError
#
# Correct approach: create a new string
text = "Python"
new_text = "J" + text[1:]
print("\\nCorrect way to create a modified string:", new_text)  # Jython


# 7. QUICK REVISION
# - Indexing accesses one character.
# - Positive indexing starts at 0.
# - Negative indexing starts at -1.
# - len() returns the number of characters.
# - Invalid indices raise IndexError.
# - Strings are immutable.
# - Spaces and punctuation count as characters.
#
# Interview question:
# What is the difference between text[0], text[-1], and text[len(text) - 1]?
# Answer:
# - text[0] returns the first character.
# - text[-1] returns the last character.
# - text[len(text) - 1] also returns the last character, using the string length.
