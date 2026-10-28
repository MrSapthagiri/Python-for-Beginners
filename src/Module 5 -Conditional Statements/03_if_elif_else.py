"""
================================================================================
Topic: The 'if...elif...else' Statement
================================================================================

1. DEFINITION:
Allows checking multiple conditions in order. 'elif' stands for 'else if'. 
Python checks them from top to bottom. As soon as one condition evaluates to True, 
its block executes and Python skips the rest of the chain. If nothing matches, 
the final 'else' block runs.

2. FLOWCHART:
      [Start]
         |
         v
   [Condition 1?] ----->(True)-----> [Run Block 1] ---+
         |                                            |
      (False)                                         |
         |                                            |
         v                                            |
   [Condition 2?] ----->(True)-----> [Run Block 2] ---+
         |                                            |
      (False)                                         |
         |                                            |
         v                                            |
   [Final 'else'] -----------------> [Run 'else' Block]-+
         |                                            |
         v                                            <
    [Continue with the rest of the program]

================================================================================
"""

# ==========================================
# Example 1: Grading System
# ==========================================
score = 85
if score >= 90:
    print("Ex 1: Grade A")
elif score >= 80:
    print("Ex 1: Grade B")
elif score >= 70:
    print("Ex 1: Grade C")
else:
    print("Ex 1: Grade F")
# Explanation: Checks top to bottom. 85 is not >= 90. But 85 IS >= 80. 'Grade B' prints.

# ==========================================
# Example 2: Traffic Light
# ==========================================
light_color = "Yellow"
if light_color == "Green":
    print("Ex 2: Go!")
elif light_color == "Yellow":
    print("Ex 2: Slow down!")
elif light_color == "Red":
    print("Ex 2: Stop!")
else:
    print("Ex 2: Broken traffic light, proceed with caution.")
# Explanation: Matches the 'Yellow' elif branch.

# ==========================================
# Example 3: Number Comparison (Pos/Neg/Zero)
# ==========================================
num = 0
if num > 0:
    print("Ex 3: Positive")
elif num < 0:
    print("Ex 3: Negative")
else:
    print("Ex 3: Zero")
# Explanation: Fails the first two checks, defaults to the 'else' block.

# ==========================================
# Example 4: Movie Ticket Pricing
# ==========================================
age = 65
if age <= 12:
    print("Ex 4: Child Ticket - $5")
elif age >= 60:
    print("Ex 4: Senior Ticket - $7")
else:
    print("Ex 4: Adult Ticket - $12")
# Explanation: Matches the second condition (>= 60).

# ==========================================
# Example 5: Temperature Status
# ==========================================
temp = 35 # Celsius
if temp >= 30:
    print("Ex 5: It's Hot outside.")
elif temp >= 20:
    print("Ex 5: It's Warm.")
elif temp >= 10:
    print("Ex 5: It's Cool.")
else:
    print("Ex 5: It's Freezing cold.")
# Explanation: Matches the very first condition, so it never checks the others.

# ==========================================
# Example 6: Menu Selection
# ==========================================
choice = 2
if choice == 1:
    print("Ex 6: Starting New Game...")
elif choice == 2:
    print("Ex 6: Opening Options Menu...")
elif choice == 3:
    print("Ex 6: Exiting Game.")
else:
    print("Ex 6: Invalid Selection.")
# Explanation: A simple menu router. Matches option 2.

# ==========================================
# Example 7: Time of Day Greeting
# ==========================================
hour = 14 # 2 PM
if hour < 12:
    print("Ex 7: Good Morning!")
elif hour < 18:
    print("Ex 7: Good Afternoon!")
else:
    print("Ex 7: Good Evening!")
# Explanation: 14 is not < 12, but it is < 18. Prints Good Afternoon.

# ==========================================
# Example 8: File Size Formatter
# ==========================================
bytes_size = 1500000
if bytes_size < 1000:
    print(f"Ex 8: Size is {bytes_size} Bytes")
elif bytes_size < 1000000:
    print(f"Ex 8: Size is {bytes_size/1000} KB")
else:
    print(f"Ex 8: Size is {bytes_size/1000000} MB")
# Explanation: Falls into the 'else' block because it's over 1 million bytes.

# ==========================================
# Example 9: HTTP Status Codes
# ==========================================
status = 404
if status == 200:
    print("Ex 9: OK - Request successful.")
elif status == 404:
    print("Ex 9: Not Found - Page doesn't exist.")
elif status == 500:
    print("Ex 9: Internal Server Error.")
else:
    print("Ex 9: Unknown Status.")
# Explanation: Simulates handling website errors. Matches 404.

# ==========================================
# Example 10: Coordinate Quadrants (X, Y)
# ==========================================
x = -5
y = 10
if x > 0 and y > 0:
    print("Ex 10: Top-Right Quadrant")
elif x < 0 and y > 0:
    print("Ex 10: Top-Left Quadrant")
elif x < 0 and y < 0:
    print("Ex 10: Bottom-Left Quadrant")
elif x > 0 and y < 0:
    print("Ex 10: Bottom-Right Quadrant")
else:
    print("Ex 10: Origin or on an Axis")
# Explanation: Combines 'and' logic in elif chains to find where a point is on a map.
