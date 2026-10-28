"""
================================================================================
Topic: The 'continue' Statement
================================================================================

1. DEFINITION:
The `continue` statement skips the REST of the code inside the loop for the 
*current* iteration only, and immediately jumps back to the top of the loop 
to start the *next* iteration. It does NOT exit the loop completely like `break`.

2. FLOWCHART (Mental Model):
      [Start Loop]
         |
         v
   [Get next item]
         |
   [Hit 'continue'?] --(Yes)--> [JUMP BACK TO TOP]
         |
       (No)
         |
   [Run rest of code block]
         |
         +----------------------+

================================================================================
"""

print("\n--- Low Level (Basic) ---")

# ==========================================
# Example 1: Skipping a number
# ==========================================
for i in range(5): 
    if i == 2:
        continue # Skip the number 2
    print(f"Ex 1: {i}")
# Explanation: Prints 0, 1, 3, 4. When i=2, it skips the print statement and goes to 3.

# ==========================================
# Example 2: Only printing odd numbers
# ==========================================
for i in range(6):
    if i % 2 == 0:
        continue # Skip even numbers
    print(f"Ex 2: Odd number {i}")
# Explanation: If it's divisible by 2, we jump back to the top, skipping the print.

# ==========================================
# Example 3: Skipping specific string letters
# ==========================================
word = "Python"
for char in word:
    if char == "h":
        continue
    print(f"Ex 3: {char}")
# Explanation: Prints P, y, t, o, n. Skips 'h'.

print("\n--- Medium Level (Intermediate) ---")

# ==========================================
# Example 4: Filtering out bad data
# ==========================================
sales = [100, -50, 200, 0, 300]
valid_total = 0
for sale in sales:
    if sale <= 0:
        continue # Skip refunds or zero-dollar transactions
    valid_total += sale
print(f"Ex 4: Total valid sales: ${valid_total}")
# Explanation: Only adds positive numbers.

# ==========================================
# Example 5: Skipping empty strings in a list
# ==========================================
names = ["Alice", "", "Bob", "   ", "Charlie"]
for name in names:
    if name.strip() == "":
        continue # Skip empty or whitespace-only names
    print(f"Ex 5: Hello, {name.strip()}!")
# Explanation: Cleans up the data stream by ignoring invalid entries.

# ==========================================
# Example 6: Continue in a while loop (Watch out!)
# ==========================================
count = 0
while count < 4:
    count += 1 # MUST increment BEFORE the continue, or you get an infinite loop!
    if count == 2:
        continue
    print(f"Ex 6: Count is {count}")
# Explanation: If we incremented after the continue, it would get stuck on 2 forever.

# ==========================================
# Example 7: Skipping directories in a simulated file system
# ==========================================
files = ["doc.txt", "system_folder/", "image.png"]
for file in files:
    if file.endswith("/"):
        print(f"Ex 7: Skipping directory {file}")
        continue
    print(f"Ex 7: Processing file {file}")
# Explanation: Useful for ignoring folders and only acting on files.

print("\n--- High Level (Advanced/Senior) ---")

# ==========================================
# Example 8: The "Guard Clause" Loop pattern
# ==========================================
# Seniors use 'continue' as a guard to keep code flat (avoid deep nesting)
users = [{"active": True, "id": 1}, {"active": False, "id": 2}]

for user in users:
    # Guard clause: if inactive, just skip to the next iteration
    if not user["active"]:
        continue
        
    # Now we can do complex logic without everything being indented 4 spaces
    print(f"Ex 8: Sending email to active user {user['id']}")
# Explanation: This makes code much more readable than nesting everything inside `if active:`.

# ==========================================
# Example 9: Complex multi-condition skipping
# ==========================================
# Skip weekends and holidays
days = [{"name": "Mon", "holiday": False}, {"name": "Sat", "holiday": False}, {"name": "Tue", "holiday": True}]
for day in days:
    if day["name"] in ["Sat", "Sun"] or day["holiday"]:
        continue
    print(f"Ex 9: Scheduling meeting for {day['name']}")
# Explanation: Cleans up business logic by eliminating edge cases early.

# ==========================================
# Example 10: Continue vs Break comparison
# ==========================================
print("Ex 10: Break stops the whole loop. Continue only stops the current step.")
for i in range(3):
    if i == 1:
        continue # Skips 1, moves to 2
    print(f"Continue reached {i}")
