# Module 6: Strings — Formatting_String_Methods.py
# ==================================================
#
# TOPIC: split(), join(), replace(), find()
#
# 1. OVERVIEW
# These methods help format, transform, and search text in Python.
#
# split()   : Splits one string into a list of strings.
# join()    : Combines strings from an iterable into one string.
# replace() : Replaces occurrences of a substring with another substring.
# find()    : Finds the first occurrence of a substring and returns its index.
#
# IMPORTANT CONCEPTS
# - Strings are immutable: these methods return results without changing
#   the original string.
# - String positions are zero-based.
# - find() returns -1 when the substring is not found.
# - split() returns a list.
# - join() returns a string and requires string elements.
# - replace() can optionally limit the number of replacements.
#
# ==================================================
# 2. split()
# ==================================================
# Definition:
# Splits a string into a list of smaller strings based on a separator.
#
# Syntax:
#     string.split(separator, maxsplit)
#
# separator: Optional delimiter. If omitted or None, splits on whitespace.
# maxsplit : Optional maximum number of splits. Default is -1 (all possible).
#
# Example:
text = "Python Java Selenium"
print("Example 1 - split():", text.split())
# Output: ['Python', 'Java', 'Selenium']
#
# Example with a delimiter:
text = "apple,banana,mango"
print("Example 2 - split(','):", text.split(","))
# Output: ['apple', 'banana', 'mango']
#
# Example with maxsplit:
text = "one-two-three-four"
print("Example 3 - maxsplit:", text.split("-", 2))
# Output: ['one', 'two', 'three-four']
#
# Practical use: parse comma-separated values, split a sentence into words,
# or separate fields in simple text data.
#
# Note: split(',') uses commas as separators; whitespace is not automatically
# removed from each item. For example, "a, b".split(",") returns ['a', ' b'].


# ==================================================
# 3. join()
# ==================================================
# Definition:
# Combines strings from an iterable into a single string using a separator.
#
# Syntax:
#     separator.join(iterable)
#
# The separator is placed BETWEEN items, not at the beginning or end.
# Every item in the iterable must be a string.
#
# Example:
languages = ["Python", "Java", "TypeScript"]
print("Example 4 - join():", " | ".join(languages))
# Output: Python | Java | TypeScript
#
# Example with no separator:
letters = ["P", "y", "t", "h", "o", "n"]
print("Example 5 - empty separator:", "".join(letters))
# Output: Python
#
# Practical use: format lists as readable text, create CSV-like lines,
# construct paths or messages, and combine words.
#
# Common error:
# "-".join([2026, 10, 14]) raises TypeError because the items are integers.
# Correct approach: "-".join(["2026", "10", "14"]).


# ==================================================
# 4. replace()
# ==================================================
# Definition:
# Replaces occurrences of old text with new text and returns a new string.
#
# Syntax:
#     string.replace(old, new, count)
#
# old   : Text to find.
# new   : Replacement text.
# count : Optional maximum number of replacements; if omitted, replace all.
#
# Example:
text = "I like Java. Java is popular."
print("Example 6 - replace():", text.replace("Java", "Python"))
# Output: I like Python. Python is popular.
#
# Limit the replacements:
text = "yes yes yes"  # no yes yes
print("Example 7 - count limit:", text.replace("yes", "no", 1))
# Output: no yes yes
#
# Remove a substring by replacing it with an empty string:
phone = "123-456-7890"
print("Example 8 - remove hyphens:", phone.replace("-", ""))
# Output: 1234567890
#
# Practical use: standardize labels, clean unwanted characters, correct text,
# or mask sensitive-looking data in sample strings.
#
# Important: replace() is case-sensitive by default.
# "Python".replace("python", "Java") returns "Python".


# ==================================================
# 5. find()
# ==================================================
# Definition:
# Returns the lowest index where a substring is found. Returns -1 if absent.
#
# Syntax:
#     string.find(sub, start, end)
#
# sub   : Substring to search for.
# start : Optional starting index.
# end   : Optional ending boundary (excluded).
#
# Example:
text = "Hello Python"
print("Example 9 - find():", text.find("Python"))
# Output: 6
#
# Not found:
print("Example 10 - missing text:", text.find("Java"))
# Output: -1
#
# Search from a particular position:
text = "banana"
print("Example 11 - start position:", text.find("a", 2))
# Output: 3
#
# Practical use: check whether text exists, locate a delimiter, or find the
# position where a keyword begins.
#
# Important: find() returns an index, not True/False.
# Use: if text.find("Python") != -1:
# Alternative: use "Python" in text when you only need a membership check.
#
# Difference from index():
# - find("Java") returns -1 if not found.
# - index("Java") raises ValueError if not found.


# ==================================================
# 6. COMBINED PRACTICAL EXAMPLES
# ==================================================

# Example A: Split a comma-separated list, clean each item, and join it neatly.
raw_items = " apple, banana , mango "
items = [item.strip() for item in raw_items.split(",")]
cleaned_text = " | ".join(items)
print("Example 12 - clean and format:", cleaned_text)
# Output: apple | banana | mango

# Example B: Find a keyword before replacing it.
message = "Status: PENDING"
position = message.find("PENDING")
if position != -1:
    message = message.replace("PENDING", "APPROVED")
print("Example 13 - find then replace:", message)
# Output: Status: APPROVED

# Example C: Split a sentence into words and join with underscores.
sentence = "learn python strings"
slug = "_".join(sentence.split())
print("Example 14 - create a slug:", slug)
# Output: learn_python_strings

# Example D: Replace separators and locate a value.
record = "ID:1042|STATUS:ACTIVE"
normalized = record.replace("|", ", ")
print("Example 15 - normalized record:", normalized)
print("STATUS index:", normalized.find("STATUS"))
# Output:
# ID:1042, STATUS:ACTIVE
# STATUS index: 12


# ==================================================
# 7. COMPARISON TABLE (QUICK REVISION)
# ==================================================
# Method    | Main purpose             | Return type
# ----------|--------------------------|------------
# split()   | Divide a string          | list
# join()    | Combine strings          | str
# replace() | Replace matching text    | str
# find()    | Locate substring         | int (-1 if missing)
#
# ==================================================
# 8. COMMON MISTAKES
# ==================================================
# 1. Expecting split() to return a string: it returns a list.
# 2. Calling join() on a list of integers: join() requires strings.
# 3. Forgetting that replace() is case-sensitive.
# 4. Assuming find() raises an error when text is missing: it returns -1.
# 5. Confusing find() with index(): index() raises ValueError when absent.
# 6. Assuming replace() changes the original variable automatically:
#       text.replace("old", "new")       # result is discarded
#    Correct:
#       text = text.replace("old", "new")
# 7. Forgetting maxsplit limits the number of splits, not the list length.
#
# ==================================================
# 9. INTERVIEW QUESTIONS AND ANSWERS
# ==================================================
# Q1. What is the difference between split() and join()?
# A. split() converts a string into a list; join() combines strings into one.
#
# Q2. What happens when find() cannot locate a substring?
# A. It returns -1.
#
# Q3. What is the difference between find() and index()?
# A. find() returns -1 when absent; index() raises ValueError.
#
# Q4. How can you replace only the first occurrence?
# A. Use string.replace(old, new, 1).
#
# Q5. How do you split text using a comma?
# A. Use text.split(",").
#
# Q6. How do you combine list items with a comma and a space?
# A. Use ", ".join(items).
#
# Q7. Do these methods modify the original string?
# A. No. Strings are immutable; assign the returned result if you want to keep it.
#
# Q8. How do you check for a substring without getting its position?
# A. Use: "Python" in text.
#
# ==================================================
# 10. MINI PRACTICE TASKS
# ==================================================
# Try these yourself:
# 1. Split "red-green-blue" using "-".
# 2. Join ["QA", "Automation", "Engineer"] with spaces.
# 3. Replace "old" with "new" in "old code".
# 4. Find the position of "test" in "automation test".
# 5. Convert "one, two, three" into "one | two | three", removing extra spaces.
#
# Suggested solutions:
# 1. "red-green-blue".split("-")
# 2. " ".join(["QA", "Automation", "Engineer"])
# 3. "old code".replace("old", "new")
# 4. "automation test".find("test")
# 5. " | ".join(item.strip() for item in "one, two, three".split(","))
