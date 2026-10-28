"""
================================================================================
Topic: The 'while' Loop
================================================================================

1. DEFINITION:
A 'while' loop executes a block of code as long as a specified condition is True. 
Unlike a 'for' loop (which runs a set number of times), a 'while' loop runs an 
unknown number of times until something changes to make the condition False.
WARNING: If the condition never becomes False, you create an "infinite loop".

2. FLOWCHART:
      [Start Loop]
         |
         v
   [Is Condition True?] --(No)--> [Exit Loop]
         |                               |
       (Yes)                             |
         |                               |
         v                               |
   [Run code block]                      |
         |                               |
   [Update variables!]                   |
         |                               |
         +-------------------------------+

================================================================================
"""

print("\n--- Low Level (Basic) ---")

# ==========================================
# Example 1: Basic Countdown
# ==========================================
count = 3
while count > 0:
    print(f"Ex 1: Countdown... {count}")
    count -= 1  # Crucial! We must update the variable so the loop eventually ends.
print("Ex 1: Liftoff!")
# Explanation: It prints 3, 2, 1, then stops because 0 is not > 0.

# ==========================================
# Example 2: Growing a string
# ==========================================
word = ""
while len(word) < 5:
    word += "A"
print(f"Ex 2: Word is {word}")
# Explanation: Loops 5 times, adding "A" each time until length is 5.

# ==========================================
# Example 3: Simulating a battery draining
# ==========================================
battery = 100
while battery >= 90:
    print(f"Ex 3: Battery at {battery}%")
    battery -= 5
# Explanation: Stops when battery hits 85%.

print("\n--- Medium Level (Intermediate) ---")

# ==========================================
# Example 4: Removing items from a list
# ==========================================
tasks = ["Dishes", "Laundry"]
while tasks: # Remember: A list with items is True. Empty list is False.
    current_task = tasks.pop(0) # Remove first item
    print(f"Ex 4: Completing {current_task}")
# Explanation: The loop naturally ends when the list becomes empty.

# ==========================================
# Example 5: Finding a power of 2
# ==========================================
num = 1
while num < 50:
    print(f"Ex 5: Power of 2: {num}")
    num *= 2
# Explanation: Multiplies by 2 each time: 1, 2, 4, 8, 16, 32. Stops before 64.

# ==========================================
# Example 6: Validating User Input (Simulation)
# ==========================================
password_attempts = 0
is_locked = False
while password_attempts < 3:
    # Simulating a failed password attempt
    password_attempts += 1
    print(f"Ex 6: Attempt {password_attempts} failed.")
print("Ex 6: Account locked out.")
# Explanation: Common pattern for limiting retries.

# ==========================================
# Example 7: Two variables in a condition
# ==========================================
player_hp = 10
enemy_hp = 5
while player_hp > 0 and enemy_hp > 0:
    enemy_hp -= 5
    print(f"Ex 7: Player attacks! Enemy HP: {enemy_hp}")
# Explanation: Loop runs as long as BOTH are alive.

print("\n--- High Level (Advanced/Senior) ---")

# ==========================================
# Example 8: The 'while True' pattern (Infinite loop with intentional breaks)
# ==========================================
# Seniors often use 'while True' and manually 'break' out of it when a condition is met.
counter = 0
while True:
    counter += 1
    if counter == 3:
        print("Ex 8: Hit 3, manually breaking out!")
        break
# Explanation: Instead of putting the logic in the while statement, we handle it inside.

# ==========================================
# Example 9: Processing an API queue
# ==========================================
api_queue = [101, 102, 103]
processed_ids = []
while api_queue:
    # Pop from the end (fastest way to remove from a list)
    job_id = api_queue.pop()
    print(f"Ex 9: Processing job ID {job_id}")
    processed_ids.append(job_id)
# Explanation: Efficiently processing a queue until it's empty.

# ==========================================
# Example 10: 'while...else' construct
# ==========================================
retry_count = 0
while retry_count < 2:
    print("Ex 10: Trying to connect to database...")
    retry_count += 1
else:
    # Runs when the condition (retry_count < 2) finally becomes False.
    print("Ex 10: Retries exhausted. Connection failed.")
# Explanation: Just like for-else, this else runs if the loop finishes naturally.
