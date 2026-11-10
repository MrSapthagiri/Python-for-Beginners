"""Examples of creating and using Python dictionaries."""
# pylint: disable=invalid-name

# Module 9: Dictionaries — Creation and Basic Operations
# ======================================================
#
# DEFINITION
# A dictionary stores values as key-value pairs. A key is used to look up its
# associated value. Keys must be unique and hashable; common key types include
# strings and numbers.
#
# SYNTAX
#     student = {"name": "Asha", "age": 18}
#
# COMMON OPERATIONS
# - Read: dictionary[key]
# - Add or update: dictionary[key] = value
# - Delete: del dictionary[key]
#
# IMPORTANT NOTES
# - Reading a missing key with square brackets raises KeyError.
# - Assigning to an existing key replaces its value.
# - Assigning to a new key adds a key-value pair.
# - Dictionaries preserve insertion order in modern Python.
# - Keys are unique. A repeated key in a literal keeps the later value.
# - Keys must be hashable (for example, strings, numbers, or tuples of
#   hashable values); lists and dictionaries cannot be keys.
# - Values can be any type, including lists or other dictionaries.
# - "key in dictionary" checks keys, not values.
#
# COMMON DICTIONARY CREATION FORMS
#     person = {"name": "Asha", "age": 18}
#     empty_dictionary = {}
#     from_pairs = dict([("name", "Asha"), ("age", 18)])
#
# BASIC OPERATION GUIDE
# - Read a required key: person["name"] (raises KeyError if absent).
# - Add/update: person["city"] = "Pune".
# - Delete a key: del person["city"] (raises KeyError if absent).
# - Check first: if "city" in person: ...
# - For a fallback when a key may be absent, see get() in the next lesson.


# Example 1: Create a dictionary
# Explanation: Each key is associated with a value using a colon.
student = {"name": "Asha", "age": 18, "grade": "A"}
print("Example 1 - Student:", student)
# Output: Example 1 - Student: {'name': 'Asha', 'age': 18, 'grade': 'A'}


# Example 2: Access a value by key
# Explanation: The key "name" looks up its associated value.
student = {"name": "Asha", "age": 18}
print("\nExample 2 - Name:", student["name"])
# Output: Example 2 - Name: Asha


# Example 3: Add a new key-value pair
# Explanation: Assigning a value to a new key adds it to the dictionary.
student = {"name": "Asha"}
student["age"] = 18
print("\nExample 3 - After adding age:", student)
# Output: Example 3 - After adding age: {'name': 'Asha', 'age': 18}


# Example 4: Update an existing value
# Explanation: Assigning to a key already present replaces its value.
student = {"name": "Asha", "age": 18}
student["age"] = 19
print("\nExample 4 - After updating age:", student)
# Output: Example 4 - After updating age: {'name': 'Asha', 'age': 19}


# Example 5: Delete a key-value pair
# Explanation: del removes the selected key and its associated value.
student = {"name": "Asha", "age": 18, "grade": "A"}
del student["grade"]
print("\nExample 5 - After deleting grade:", student)
# Output: Example 5 - After deleting grade: {'name': 'Asha', 'age': 18}


# Example 6: Update multiple entries with update()
# Explanation: update() adds new keys and replaces values for existing keys.
profile: dict[str, str | bool] = {"name": "Asha", "city": "Pune"}
profile.update({"city": "Mumbai", "active": True})
print("\nExample 6 - Updated profile:", profile)
# Output: Example 6 - Updated profile: {'name': 'Asha', 'city': 'Mumbai', 'active': True}


# Example 7: Create a dictionary with dict()
# Explanation: dict() accepts keyword arguments when the keys are valid
# identifiers. Keys created this way are strings.
settings = dict(theme="dark", notifications=True)
print("\nExample 7 - Settings:", settings)
# Output: Example 7 - Settings: {'theme': 'dark', 'notifications': True}


# Example 8: Test whether a key exists
# Explanation: "in" searches dictionary keys. It does not search the values.
student = {"name": "Asha", "age": 18}
print("\nExample 8 - Has age key:", "age" in student)
print("Example 8 - Has Asha value as key:", "Asha" in student)
# Output:
# Example 8 - Has age key: True
# Example 8 - Has Asha value as key: False


# Example 9: Delete and return an entry with pop()
# Explanation: pop(key) removes the key and returns its former value.
student = {"name": "Asha", "age": 18, "grade": "A"}
removed_grade = student.pop("grade")
print("\nExample 9 - Removed grade:", removed_grade)
print("Example 9 - Remaining student:", student)
# Output:
# Example 9 - Removed grade: A
# Example 9 - Remaining student: {'name': 'Asha', 'age': 18}


# Example 10: Duplicate keys keep the later value
# Explanation: A dictionary can only contain one value per key. A later
# occurrence of the same key replaces the earlier value.
example = {"level": 1, "level": 2}
print("\nExample 10 - Duplicate key result:", example)
# Output: Example 10 - Duplicate key result: {'level': 2}


# Example 11: Use a tuple as a dictionary key
# Explanation: Tuples of hashable values can be keys, which is useful for
# coordinates. A list cannot be used as a key because it is mutable.
locations = {(0, 0): "origin", (1, 2): "point"}
print("\nExample 11 - Point label:", locations[(1, 2)])
# Output: Example 11 - Point label: point


# COMMON MISTAKES
# - Using a missing key with [] raises KeyError. Use get() when a fallback is
#   appropriate, or check "if key in dictionary" first.
# - "value in dictionary" checks the keys, not the values.
# - Assigning to an existing key replaces its current value.
# - Keys must be hashable; do not use a list as a key.
# - Variable names are case-sensitive: student and Student are different names.


# QUICK REVISION
# - Dictionaries store key-value pairs.
# - Access: dictionary[key]
# - Add or update: dictionary[key] = value
# - Delete: del dictionary[key]
# - Missing keys accessed with [] raise KeyError.
# - Membership: key in dictionary
# - Use get() in the next lesson for a safe lookup with a fallback.
