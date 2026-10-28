"""
================================================================================
Topic: Ternary Operator (Conditional Expressions)
================================================================================

1. DEFINITION:
A ternary operator is a fast, one-line way to write a simple 'if...else' 
statement. It is ONLY used when you want to assign a value or return a value 
based on a condition. 
Syntax:  value_if_true if condition else value_if_false

2. FLOWCHART (Mental Model):
    [Result Variable] = (Plan A) IF [Condition] ELSE (Plan B)

================================================================================
"""

# ==========================================
# Example 1: Pass / Fail
# ==========================================
score = 60
status = "Pass" if score >= 50 else "Fail"
print(f"Ex 1: Status is {status}")
# Explanation: Translates to: Assign "Pass" if score >= 50, otherwise assign "Fail".

# ==========================================
# Example 2: Even / Odd
# ==========================================
num = 10
parity = "Even" if num % 2 == 0 else "Odd"
print(f"Ex 2: The number is {parity}")
# Explanation: Replaces a 4-line if-else block with a single line.

# ==========================================
# Example 3: Finding Maximum
# ==========================================
a = 5
b = 10
maximum = a if a > b else b
print(f"Ex 3: Max is {maximum}")
# Explanation: A manual way to recreate the built-in max() function logic.

# ==========================================
# Example 4: Finding Minimum
# ==========================================
minimum = a if a < b else b
print(f"Ex 4: Min is {minimum}")
# Explanation: Same logic, but flipped for the smaller number.

# ==========================================
# Example 5: User Greeting
# ==========================================
is_logged_in = False
greeting = "Welcome Back!" if is_logged_in else "Please log in."
print(f"Ex 5: {greeting}")
# Explanation: Extremely common in web development for setting UI text.

# ==========================================
# Example 6: Grammar Pluralization
# ==========================================
apple_count = 1
message = f"You have {apple_count} apple{'s' if apple_count != 1 else ''}."
print(f"Ex 6: {message}")
# Explanation: Adds an 's' if count is not 1. Embedded directly in an f-string!

# ==========================================
# Example 7: Applying a Discount
# ==========================================
is_vip = True
price = 100 * 0.8 if is_vip else 100
print(f"Ex 7: Price is ${price}")
# Explanation: Multiplies by 0.8 (20% off) if VIP, otherwise stays 100.

# ==========================================
# Example 8: Safe Division
# ==========================================
numerator = 10
denominator = 0
# Prevent ZeroDivisionError crash
result = numerator / denominator if denominator != 0 else "Cannot divide by zero"
print(f"Ex 8: Result = {result}")
# Explanation: Checks if denominator is 0 before attempting division.

# ==========================================
# Example 9: True/False to Yes/No converter
# ==========================================
agreed_to_terms = True
display_text = "Yes" if agreed_to_terms else "No"
print(f"Ex 9: Agreed? {display_text}")
# Explanation: Translates booleans to human-readable strings for UI.

# ==========================================
# Example 10: Inside a List Comprehension (Advanced)
# ==========================================
data = [10, -5, 20, -1]
# We want negative numbers to become 0
clean_data = [x if x >= 0 else 0 for x in data]
print(f"Ex 10: Cleaned data -> {clean_data}")
# Explanation: Uses the ternary operator inside a list loop to filter bad data.
