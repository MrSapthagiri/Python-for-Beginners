"""Module 2: Variables and basic Python data types."""

student_name = "Asha"
age = 18
average_score = 91.5
is_enrolled = True
missing_value = None

print(f"Name: {student_name}")
print(f"Age: {age}")
print(f"Average score: {average_score}")
print(f"Enrolled: {is_enrolled}")
print(f"Missing value: {missing_value}")

print("\\nData types:")
print(type(student_name).__name__)
print(type(age).__name__)
print(type(average_score).__name__)
print(type(is_enrolled).__name__)
print(type(missing_value).__name__)

# Python variables can refer to values of different types.
value = 10
print(f"\\nOriginal value: {value}")
value = "ten"
print(f"Updated value: {value}")
