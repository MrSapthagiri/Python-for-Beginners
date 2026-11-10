# Module 9: Dictionary Methods
# ============================
#
# DEFINITION
# Dictionary methods provide ways to inspect or safely access the key-value
# pairs stored in a dictionary.
#
# METHODS
# - keys(): returns a view of all keys.
# - values(): returns a view of all values.
# - items(): returns a view of (key, value) pairs.
# - get(key): returns a key's value, or None if the key is missing.
# - get(key, default): returns default if the key is missing.
#
# The views returned by keys(), values(), and items() reflect changes to the
# dictionary. Convert them to lists when you want to display them as lists.
# A view is iterable, so a loop can use it without first converting it to a
# list. In a dictionary loop, writing "for key in dictionary" iterates keys.
#
# WHEN TO USE EACH METHOD
# - Use keys() to process or display keys.
# - Use values() to process or display values without their keys.
# - Use items() when each operation needs both the key and its value.
# - Use get() when the key might not exist and a default is useful.
#
# GET() AND MISSING VALUES
# dictionary.get("missing") returns None if the key is absent. If the key is
# present and stores None, the result is also None. Use "key in dictionary"
# when you need to tell those two cases apart.


# Example 1: Get all keys
# Explanation: list() converts the keys view into a list for display.
student = {"name": "Asha", "age": 18, "grade": "A"}
print("Example 1 - Keys:", list(student.keys()))
# Output: Example 1 - Keys: ['name', 'age', 'grade']


# Example 2: Get all values
# Explanation: values() provides the values in dictionary insertion order.
student = {"name": "Asha", "age": 18, "grade": "A"}
print("\nExample 2 - Values:", list(student.values()))
# Output: Example 2 - Values: ['Asha', 18, 'A']


# Example 3: Get key-value pairs
# Explanation: items() returns pairs that can be unpacked in a loop.
student = {"name": "Asha", "age": 18}
print("\nExample 3 - Items:", list(student.items()))
# Output: Example 3 - Items: [('name', 'Asha'), ('age', 18)]


# Example 4: Iterate over items
# Explanation: Each pair is unpacked into its key and value.
student = {"name": "Asha", "age": 18}
print("\nExample 4 - Student details:")
for key, value in student.items():
    print(key, "=", value)
# Output:
# Example 4 - Student details:
# name = Asha
# age = 18


# Example 5: Use get() for an existing key
# Explanation: get() returns the value associated with the requested key.
student = {"name": "Asha", "age": 18}
print("\nExample 5 - Name:", student.get("name"))
# Output: Example 5 - Name: Asha


# Example 6: Use get() with a default for a missing key
# Explanation: The default is returned instead of raising KeyError.
student = {"name": "Asha", "age": 18}
print("\nExample 6 - City:", student.get("city", "Not provided"))
# Output: Example 6 - City: Not provided


# Example 7: Iterate over keys directly
# Explanation: A for loop over a dictionary visits its keys in insertion order.
student = {"name": "Asha", "age": 18}
print("\nExample 7 - Keys using a loop:")
for key in student:
    print(key)
# Output:
# Example 7 - Keys using a loop:
# name
# age


# Example 8: Views reflect dictionary updates
# Explanation: dict_keys is a view linked to the dictionary, not a frozen copy.
student_with_view: dict[str, str | int] = {"name": "Asha"}
key_view = student_with_view.keys()
student_with_view["age"] = 18
print("\nExample 8 - Keys after update:", list(key_view))
# Output: Example 8 - Keys after update: ['name', 'age']


# Example 9: Distinguish an absent key from a key storing None
# Explanation: get() returns None for both by default, so membership checks
# determine whether the key actually exists.
profile = {"nickname": None}
print("\nExample 9 - Missing nickname:", profile.get("missing"))
print("Example 9 - Stored nickname:", profile.get("nickname"))
print("Example 9 - Missing key exists:", "missing" in profile)
print("Example 9 - Stored key exists:", "nickname" in profile)
# Output:
# Example 9 - Missing nickname: None
# Example 9 - Stored nickname: None
# Example 9 - Missing key exists: False
# Example 9 - Stored key exists: True


# Example 10: Use get() for a numeric default
# Explanation: Supplying a default such as 0 allows a missing score to be used
# safely in a calculation.
scores = {"Asha": 90}
new_score = scores.get("Ravi", 0)
print("\nExample 10 - Ravi's score:", new_score)
print("Example 10 - Score after bonus:", new_score + 5)
# Output:
# Example 10 - Ravi's score: 0
# Example 10 - Score after bonus: 5


# COMMON MISTAKES
# - keys(), values(), and items() return view objects, not lists. Use list(...)
#   when a list is specifically needed.
# - get(key) returns None by default; it does not raise KeyError.
# - Do not assume values() can identify which key a value belongs to; use
#   items() when both parts of each pair are needed.
# - A view reflects later updates. Use list(view) to make a snapshot of its
#   current items.


# QUICK REVISION
# - keys() returns the keys view.
# - values() returns the values view.
# - items() returns (key, value) pairs.
# - get(key, default) safely reads a value and supplies a missing-key default.
# - Iterate directly: for key in dictionary
# - Use "key in dictionary" to check key existence.
