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


# QUICK REVISION
# - keys() returns the keys view.
# - values() returns the values view.
# - items() returns (key, value) pairs.
# - get(key, default) safely reads a value and supplies a missing-key default.
