# Module 6: Strings — String_Methods.py
# =====================================
#
# 1. WHAT ARE STRING METHODS?
# String methods are built-in operations used to work with text.
# They can convert letter case, remove whitespace, search, count,
# validate text, and more.
#
# Syntax:
#     string.method()   
#     string.method(arguments)
#
# IMPORTANT:
# - Strings are immutable. Methods that change text return a new string.
# - Unless otherwise stated, these methods are case-sensitive.
# - Methods such as isdigit() return True or False.
#
# 2. COMMON STRING METHODS
#
# upper()       -> converts all letters to uppercase
# lower()       -> converts all letters to lowercase
# capitalize()  -> capitalizes the first character and lowercases the rest
# title()       -> capitalizes the first character of each word
# swapcase()    -> changes uppercase to lowercase and vice versa
# strip()       -> removes leading and trailing whitespace
# lstrip()      -> removes leading whitespace
# rstrip()      -> removes trailing whitespace
# count(x)      -> counts occurrences of substring x
# find(x)       -> returns the first index of x, or -1 if not found
# index(x)      -> returns the first index of x; raises ValueError if not found
# replace(old, new) -> replaces occurrences of old with new
# startswith(x) -> checks whether the string begins with x
# endswith(x)   -> checks whether the string ends with x
# split(sep)    -> splits a string into a list
# join(iterable)-> combines strings using the string as a separator
# isalpha()     -> True if all characters are letters and string is non-empty
# isdigit()     -> True if all characters are digits and string is non-empty
# isalnum()     -> True if all characters are letters or digits and non-empty
# isspace()     -> True if all characters are whitespace and string is non-empty
#
# 3. TEN EXAMPLE PROGRAMS
# Run this file to see examples and output.


# Program 1: upper() and lower()
# Explanation: Convert all letters to uppercase or lowercase.
text = "Hello Python"
print("Program 1:")
print(text.upper())  # HELLO PYTHON
print(text.lower())  # hello python


# Program 2: capitalize() and title()
# Explanation: capitalize() changes the first character to uppercase and
# lowercases the remaining characters. title() capitalizes each word.
text = "hello PYTHON programming"
print("\\nProgram 2:")
print(text.capitalize())  # Hello python programming
print(text.title())       # Hello Python Programming


# Program 3: swapcase()
# Explanation: Swap uppercase and lowercase letters.
text = "PyThOn"
print("\\nProgram 3:", text.swapcase())  # pYtHoN


# Program 4: strip(), lstrip(), and rstrip()
# Explanation: Remove whitespace from both ends, left end, or right end.
text = "   Hello Python   "
print("\\nProgram 4:")
print(repr(text.strip()))   # 'Hello Python'
print(repr(text.lstrip()))  # 'Hello Python   '
print(repr(text.rstrip()))  # '   Hello Python'


# Program 5: count()
# Explanation: Count how many times a substring appears (non-overlapping).
text = "banana"
print("\\nProgram 5:", text.count("a"))  # 3
print(text.count("an"))                 # 2


# Program 6: find() and index()
# Explanation: find() returns -1 when not found; index() raises ValueError.
text = "Hello Python"
print("\\nProgram 6:")
print(text.find("Python"))  # 6
print(text.find("Java"))    # -1
print(text.index("Hello"))  # 0
# print(text.index("Java")) # Uncomment to see ValueError


# Program 7: replace()
# Explanation: Replace old text with new text. The optional third argument
# limits the number of replacements.
text = "I like Java. Java is popular."
print("\\nProgram 7:")
print(text.replace("Java", "Python"))
print("one one one".replace("one", "two", 1))  # two one one


# Program 8: startswith() and endswith()
# Explanation: Return True or False depending on the beginning or ending text.
text = "report.pdf"
print("\\nProgram 8:")
print(text.startswith("report"))  # True
print(text.endswith(".pdf"))      # True


# Program 9: split() and join()
# Explanation: split() turns a string into a list. join() combines strings.
text = "red,green,blue"
colors = text.split(",")
print("\\nProgram 9:")
print(colors)                  # ['red', 'green', 'blue']
print(" | ".join(colors))      # red | green | blue


# Program 10: String checking methods
# Explanation: These methods check whether all characters meet a condition.
print("\\nProgram 10:")
print("Python".isalpha())    # True
print("12345".isdigit())     # True
print("Python123".isalnum()) # True
print("   ".isspace())       # True
print("Python 3".isalpha())  # False (space and digit are not letters)


# 4. EXTRA EXAMPLES
print("\\nExtra examples:")
print("hello".upper())                 # HELLO
print("HELLO".lower())                 # hello
print("  data  ".strip())              # data
print("mississippi".count("s"))        # 4
print("automation".find("m"))           # 2
print("cat and cat".replace("cat", "dog"))  # dog and dog
print("one two three".split())         # ['one', 'two', 'three']
print("-".join(["2026", "10", "14"]))  # 2026-10-14


# 5. IMPORTANT NOTES
# - Most string methods are case-sensitive: "Python".find("py") returns -1.
# - strip() removes whitespace at the ends, not from the middle.
# - split() returns a list of strings.
# - join() requires an iterable containing strings; non-string items cause TypeError.
# - find() returns -1 if the substring is missing.
# - index() raises ValueError if the substring is missing.
# - isalpha(), isdigit(), isalnum(), and isspace() return booleans.
# - Empty strings return False for these checking methods.
# - String methods return new results; the original string remains unchanged.


# 6. QUICK REVISION
# upper() / lower()  -> change letter case
# strip()             -> remove whitespace at both ends
# count()             -> count substring occurrences
# find()              -> find index or return -1
# replace()           -> replace text
# split()              -> string to list
# join()               -> list/iterable of strings to string
# startswith()         -> check beginning
# endswith()           -> check ending
# isalpha()/isdigit()  -> validate character types
#
# Interview question:
# What is the difference between find() and index()?
# Answer:
# find() returns -1 when a substring is absent, while index() raises ValueError.
