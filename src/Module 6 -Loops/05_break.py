"""
================================================================================
Topic: The 'break' Statement
================================================================================

1. DEFINITION:
The `break` statement instantly terminates the current loop it is inside. 
It doesn't matter if the loop was supposed to run 1000 more times; when 
Python hits `break`, it completely exits the loop immediately.

2. FLOWCHART (Mental Model):
      [Start Loop]
         |
         v
   [Is Condition True?] --(Yes)--> [Run code block]
                                         |
                                  [Hit 'break'?] --(Yes)--> [EXIT LOOP INSTANTLY]
                                         |
                                       (No)
                                         |
                                   [Next Loop]

================================================================================
"""

print("\n--- Low Level (Basic) ---")

# ==========================================
# Example 1: Breaking a 'for' loop
# ==========================================
for i in range(5):      3 4 
    if i == 3:
        print("Ex 1: Hit 3, breaking out!")
        break
    print(f"Ex 1: {i}")
# Explanation: It prints 0, 1, 2. When i becomes 3, it breaks, so 3 and 4 are never printed.

# ==========================================
# Example 2: Breaking a 'while' loop
# ==========================================
count = 0
while count < 10:  
    if count == 2:
        break
    print(f"Ex 2: Count is {count}")
    count += 1
# Explanation: It only reaches 0 and 1 before hitting the break.

# ==========================================
# Example 3: Searching for an item
# ==========================================
animals = ["dog", "cat", "bird", "fish"]
target = "bird"
for pet in animals:
    print(f"Ex 3: Checking {pet}")
    if pet == target:
        print("Ex 3: Found it! Stopping search.")
        break
# Explanation: Once we find the bird, there's no need to check the fish. We break to save time.

print("\n--- Medium Level (Intermediate) ---")

# ==========================================
# Example 4: User Input Loop (Simulation)
# ==========================================
# Simulating a user typing 'quit' to exit a program
commands = ["run", "jump", "quit", "attack"]
for cmd in commands:
    if cmd == "quit":
        print("Ex 4: Exiting program.")
        break
    print(f"Ex 4: Executing {cmd}")
# Explanation: Common pattern in games or command-line apps.

# ==========================================
# Example 5: Breaking nested loops (Watch out!)
# ==========================================
for x in range(2):
    for y in range(3):
        if y == 1:
            break
        print(f"Ex 5: x={x}, y={y}")
# Explanation: The break ONLY exits the INNER 'y' loop. The outer 'x' loop continues!

# ==========================================
# Example 6: First match in a dictionary
# ==========================================
users = {"u1": "offline", "u2": "online", "u3": "online"}
for uid, status in users.items():
    if status == "online":
        print(f"Ex 6: First online user found: {uid}")
        break
# Explanation: Efficiently finds the first person online without scanning the whole database.

# ==========================================
# Example 7: Limiting a while loop intentionally
# ==========================================
capacity = 100
current = 0
while True: # Infinite loop!
    current += 20
    if current >= capacity:
        print("Ex 7: Tank is full! Stopping pump.")
        break
# Explanation: The 'while True' + 'break' combination is a staple in Python.

print("\n--- High Level (Advanced/Senior) ---")

# ==========================================
# Example 8: Breaking with a 'for...else' clause
# ==========================================
primes = [2, 3, 5, 7]
search = 4
for p in primes:
    if p == search:
        print("Ex 8: Found prime!")
        break
else:
    # Runs ONLY because the break was NEVER hit.
    print("Ex 8: Not a prime number.")
# Explanation: If a loop finishes completely, it means we didn't find what we were looking for.

# ==========================================
# Example 9: Processing chunks of data
# ==========================================
data_stream = [1, 1, 1, 0, 0, 1]
# We want to process 1s, but stop completely if we see a 0 (error code)
for packet in data_stream:
    if packet == 0:
        print("Ex 9: Corrupt packet detected. Halting data stream.")
        break
    # pretend to process packet
print("Ex 9: Stream processing finished.")
# Explanation: Failsafe mechanism for data pipelines.

# ==========================================
# Example 10: Breaking out of multiple loops (The Flag method)
# ==========================================
# Because 'break' only exits one loop, we use a flag to break outer loops.
found_target = False
for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            print("Ex 10: Found target deep in matrix!")
            found_target = True
            break # Breaks inner loop
    if found_target:
        break # Breaks outer loop
# Explanation: Seniors use boolean flags or extract this logic to a function with 'return' to avoid this messy flag code!
