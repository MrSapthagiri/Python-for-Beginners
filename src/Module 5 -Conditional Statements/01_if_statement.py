"""
================================================================================
Topic: The 'if' Statement
================================================================================

1. DEFINITION:
The 'if' statement is the simplest decision-making tool in Python. 
It checks a condition. If the condition is True, Python runs the indented code. 
If the condition is False, Python completely ignores the indented code.

2. FLOWCHART:
      [Start]
         |
         v
   [Is Condition True?] ----->(No/False)-----> [Skip the code block]
         |                                           |
     (Yes/True)                                      |
         |                                           |
         v                                           |
 [Run the indented code]                             |
         |                                           |
         +-------------------------------------------+
         |
         v
    [Continue with the rest of the program]

================================================================================
"""

# ==========================================
# Example 1: Basic Number Check
# ==========================================
age = 20
if age >= 18:
    print("Ex 1: You are an adult.")
# Explanation 1: We check if `age` is 18 or higher. 20 is >= 18, so it prints.

# ==========================================
# Example 2: String Matching
# ==========================================
password = "secret_pass"
if password == "secret_pass":
    print("Ex 2: Access Granted!")
# Explanation 2: We use `==` to check if the string exactly matches. It does.

# ==========================================
# Example 3: Boolean Flag Check
# ==========================================
is_raining = True
if is_raining:
    print("Ex 3: Remember to take an umbrella.")
# Explanation 3: `is_raining` is already True, so we don't need to write `== True`.

# ==========================================
# Example 4: List Membership
# ==========================================
fruits = ["apple", "banana", "mango"]
if "apple" in fruits:
    print("Ex 4: We have apples in stock.")
# Explanation 4: The `in` keyword checks if an item exists inside a list.

# ==========================================
# Example 5: Substring Check
# ==========================================
email = "user@gmail.com"
if "@" in email:
    print("Ex 5: Valid email format detected.")
# Explanation 5: The `in` keyword also works for checking if a character is in a string.

# ==========================================
# Example 6: Multiple Conditions (AND)
# ==========================================
user_age = 25
has_license = True
if user_age >= 18 and has_license:
    print("Ex 6: You are legally allowed to drive.")
# Explanation 6: `and` requires BOTH conditions to be True for the code to run.

# ==========================================
# Example 7: Multiple Conditions (OR)
# ==========================================
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("Ex 7: It's the weekend! Time to relax.")
# Explanation 7: `or` requires at least ONE condition to be True.

# ==========================================
# Example 8: Mathematical Check (Modulo)
# ==========================================
number = 10
if number % 2 == 0:
    print("Ex 8: The number is Even.")
# Explanation 8: `% 2 == 0` checks if a number divides perfectly by 2 (meaning it's even).

# ==========================================
# Example 9: Checking if a list has items
# ==========================================
shopping_cart = ["shoes", "shirt"]
if shopping_cart:
    print("Ex 9: You have items in your cart.")
# Explanation 9: In Python, a list with items is automatically evaluated as True. An empty list `[]` is False.

# ==========================================
# Example 10: Using the 'not' operator
# ==========================================
is_banned = False
if not is_banned:
    print("Ex 10: You can enter the server.")
# Explanation 10: `not` flips the boolean. `not False` becomes `True`.
