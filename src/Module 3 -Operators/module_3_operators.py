"""Module 3: Arithmetic, comparison, logical, and membership operators."""

first_number = 10
second_number = 3

print("Arithmetic operators:")
print(f"Addition: {first_number + second_number}")
print(f"Subtraction: {first_number - second_number}")
print(f"Multiplication: {first_number * second_number}")
print(f"Division: {first_number / second_number}")
print(f"Remainder: {first_number % second_number}")
print(f"Power: {first_number ** second_number}")
print(f"Floor division: {first_number // second_number}")

has_enough_points = 85 >= 70
has_good_attendance = 90 >= 75
passed = has_enough_points and has_good_attendance

print("\\nConditions:")
print(f"Passed: {passed}")
print(f"Needs improvement: {not passed}")

languages = ["Python", "Java", "C++"]
print(f"\\nPython is included: {'Python' in languages}")
