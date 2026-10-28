"""
================================================================================
Topic: The 'if...else' Statement
================================================================================

1. DEFINITION:
The 'if...else' statement provides an alternative path. If the 'if' condition 
is True, the first block of code runs. Otherwise (if it's False), the 'else' 
block of code runs. It's a classic "Plan A vs Plan B" scenario.

2. FLOWCHART:
      [Start]
         |
         v
   [Is Condition True?] ----->(No/False)-----> [Run 'else' block (Plan B)]
         |                                           |
     (Yes/True)                                      |
         |                                           |
         v                                           |
 [Run 'if' block (Plan A)]                           |
         |                                           |
         +-------------------------------------------+
         |
         v
    [Continue with the rest of the program]

================================================================================
"""

# ==========================================
# Example 1: Pass or Fail Exam
# ==========================================
score = 45
if score >= 50:
    print("Ex 1: You Passed!")
else:
    print("Ex 1: You Failed. Try again.")
# Explanation: Score is 45. The 'if' condition is False, so the 'else' block runs.

# ==========================================
# Example 2: Even or Odd Number
# ==========================================
num = 7
if num % 2 == 0:
    print("Ex 2: The number is Even.")
else:
    print("Ex 2: The number is Odd.")
# Explanation: 7 divided by 2 has a remainder of 1. So it's False, meaning it's Odd.

# ==========================================
# Example 3: Login Check
# ==========================================
saved_pin = "1234"
entered_pin = "9999"
if entered_pin == saved_pin:
    print("Ex 3: Phone Unlocked.")
else:
    print("Ex 3: Incorrect PIN.")
# Explanation: The pins don't match, so the 'else' block triggers.

# ==========================================
# Example 4: Checking Dictionary Keys
# ==========================================
student = {"name": "John", "age": 20}
if "grade" in student:
    print("Ex 4: Student has a grade recorded.")
else:
    print("Ex 4: No grade found for student.")
# Explanation: The key "grade" doesn't exist in the dictionary, so 'else' runs.

# ==========================================
# Example 5: Palindrome Word Check
# ==========================================
word = "radar"
if word == word[::-1]:  # word[::-1] reverses the string
    print(f"Ex 5: '{word}' is a palindrome.")
else:
    print(f"Ex 5: '{word}' is not a palindrome.")
# Explanation: 'radar' spelled backwards is still 'radar'. 'if' block runs.

# ==========================================
# Example 6: Positive or Negative
# ==========================================
balance = -50
if balance >= 0:
    print("Ex 6: Your account is in good standing.")
else:
    print("Ex 6: Warning! Your account is overdrawn.")
# Explanation: Balance is less than 0, triggering the 'else' warning.

# ==========================================
# Example 7: Checking string case
# ==========================================
username = "ADMIN"
if username.islower():
    print("Ex 7: Username is lowercase.")
else:
    print("Ex 7: Username contains uppercase letters.")
# Explanation: `islower()` is False because it's uppercase. 'else' block runs.

# ==========================================
# Example 8: Checking if a list is empty
# ==========================================
tasks = []
if tasks:
    print("Ex 8: You have pending tasks.")
else:
    print("Ex 8: All caught up! No tasks left.")
# Explanation: Empty lists evaluate to False in Python, triggering the 'else'.

# ==========================================
# Example 9: The 'not in' operator
# ==========================================
banned_users = ["troll123", "spammer99"]
new_user = "cool_guy"
if new_user not in banned_users:
    print("Ex 9: Welcome to the forum!")
else:
    print("Ex 9: You are banned.")
# Explanation: Checks if 'cool_guy' is missing from the list. It is missing (True).

# ==========================================
# Example 10: Age verification for a website
# ==========================================
birth_year = 2010
current_year = 2024
if (current_year - birth_year) >= 18:
    print("Ex 10: Access granted to mature content.")
else:
    print("Ex 10: You are too young to view this site.")
# Explanation: 2024 - 2010 = 14. 14 is not >= 18, so access is denied via 'else'.
