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
profile = {"name": "Asha", "city": "Pune"}
profile.update({"city": "Mumbai", "active": True})
print("\nExample 6 - Updated profile:", profile)
# Output: Example 6 - Updated profile: {'name': 'Asha', 'city': 'Mumbai', 'active': True}


# QUICK REVISION
# - Dictionaries store key-value pairs.
# - Access: dictionary[key]
# - Add or update: dictionary[key] = value
# - Delete: del dictionary[key]
# - Missing keys accessed with [] raise KeyError.
