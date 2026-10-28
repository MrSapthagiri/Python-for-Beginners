"""
================================================================================
Topic: Nested 'if' Statements
================================================================================

1. DEFINITION:
A nested 'if' statement is an 'if' statement placed inside another 'if' or 
'else' block. We use it when a secondary check is only needed if a primary 
check passes. Be careful: too much nesting makes code hard to read!

2. FLOWCHART:
      [Start]
         |
         v
   [Primary Condition True?] --(No)--> [Skip or do 'else']
         |
       (Yes)
         |
         v
   [Secondary Condition True?] --(No)-> [Inner 'else' or skip]
         |
       (Yes)
         |
         v
  [Run deeply nested code]
         |
         v
    [Continue program]

================================================================================
"""

# ==========================================
# Example 1: Login & Admin Check
# ==========================================
is_logged_in = True
is_admin = False
if is_logged_in:
    print("Ex 1: Welcome User.")
    if is_admin:
        print("Ex 1: Admin Panel Access Granted.")
# Explanation: First checks if logged in. Since True, it checks admin. Admin is False.

# ==========================================
# Example 2: Even Number & Divisible by 4
# ==========================================
num = 12
if num % 2 == 0:
    print("Ex 2: Number is even.")
    if num % 4 == 0:
        print("Ex 2: It is also divisible by 4.")
# Explanation: 12 is even, so we step inside and check if 12 is divisible by 4.

# ==========================================
# Example 3: Loan Approval Logic
# ==========================================
credit_score = 750
salary = 50000

if credit_score > 700:
    if salary > 40000:
        print("Ex 3: Loan Approved!")
    else:
        print("Ex 3: Salary too low for this loan.")
else:
    print("Ex 3: Credit score too low.")
# Explanation: Both conditions must pass sequentially.

# ==========================================
# Example 4: Video Game Door Check
# ==========================================
at_door = True
has_key = True
if at_door:
    if has_key:
        print("Ex 4: You opened the door!")
    else:
        print("Ex 4: The door is locked. Find the key.")
# Explanation: You can't open a door if you aren't standing at it first.

# ==========================================
# Example 5: Online Shopping Checkout
# ==========================================
item_in_stock = True
funds = 100
price = 150
if item_in_stock:
    if funds >= price:
        print("Ex 5: Purchase successful.")
    else:
        print("Ex 5: Card Declined. Insufficient funds.")
else:
    print("Ex 5: Item is out of stock.")
# Explanation: It only checks your bank balance if the item is actually available.

# ==========================================
# Example 6: Leap Year Check (Math)
# ==========================================
year = 2024
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Ex 6: Leap Year")
        else:
            print("Ex 6: Not a Leap Year")
    else:
        print("Ex 6: Leap Year")
else:
    print("Ex 6: Not a Leap Year")
# Explanation: The classic algorithm for a leap year requires deep nesting.

# ==========================================
# Example 7: Nested Dictionary Check
# ==========================================
data = {"user": {"age": 25}}
if "user" in data:
    if "age" in data["user"]:
        print(f"Ex 7: Found age: {data['user']['age']}")
# Explanation: Safely navigating a JSON-like object to prevent crashes.

# ==========================================
# Example 8: Voting Eligibility
# ==========================================
age = 20
registered = False
if age >= 18:
    if registered:
        print("Ex 8: You can vote.")
    else:
        print("Ex 8: You must register first.")
else:
    print("Ex 8: You are too young to vote.")
# Explanation: You must be old enough before registration even matters.

# ==========================================
# Example 9: Airport Security
# ==========================================
has_ticket = True
has_passport = True
if has_ticket:
    if has_passport:
        print("Ex 9: Proceed to your gate.")
    else:
        print("Ex 9: You need a passport to fly internationally.")
else:
    print("Ex 9: You need to buy a ticket first.")
# Explanation: Sequential checks for real-world scenarios.

# ==========================================
# Example 10: Password Strength
# ==========================================
password = "Password1"
if len(password) >= 8:
    if any(char.isdigit() for char in password):
        print("Ex 10: Strong password.")
    else:
        print("Ex 10: Password must contain a number.")
else:
    print("Ex 10: Password is too short.")
# Explanation: First checks length, then does a deeper check for numbers.
