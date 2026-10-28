"""
================================================================================
Topic: Match Case (Structural Pattern Matching)
================================================================================

1. DEFINITION:
Introduced in Python 3.10, `match case` is like a very powerful switch statement. 
You provide a variable (match), and it checks it against several patterns (case). 
It's cleaner than writing 10 `elif` statements, especially for checking the 
structure of data like lists or dictionaries.

2. FLOWCHART:
      [Start (Match Variable)]
               |
               v
      [Does it match Case 1?] --(Yes)--> [Run Case 1 Block] --+
               | (No)                                         |
               v                                              |
      [Does it match Case 2?] --(Yes)--> [Run Case 2 Block] --+
               | (No)                                         |
               v                                              |
      [Does it match Case _ (default)?] -> [Run Default Block]+
                                                              |
                                                              v
                                                    [Continue program]

================================================================================
"""

# ==========================================
# Example 1: Simple Variable Matching
# ==========================================
day = "Monday"
match day:
    case "Monday":
        print("Ex 1: Start of the work week.")
    case "Friday":
        print("Ex 1: End of the work week.")
    case _: # Wildcard/Default
        print("Ex 1: Mid-week day.")
# Explanation: Exactly matches the string "Monday".

# ==========================================
# Example 2: Command Parsing
# ==========================================
action = "start"
match action:
    case "start":
        print("Ex 2: Engine starting...")
    case "stop":
        print("Ex 2: Engine stopping...")
# Explanation: Cleanly replaces a simple if/elif chain.

# ==========================================
# Example 3: HTTP Status Codes
# ==========================================
status = 404
match status:
    case 200:
        print("Ex 3: OK")
    case 404:
        print("Ex 3: Not Found")
    case 500:
        print("Ex 3: Server Error")
# Explanation: Perfect for exact integer matching.

# ==========================================
# Example 4: Or Patterns (|)
# ==========================================
letter = "e"
match letter:
    case "a" | "e" | "i" | "o" | "u":
        print("Ex 4: It's a vowel.")
    case _:
        print("Ex 4: It's a consonant.")
# Explanation: The `|` symbol allows multiple conditions in one case.

# ==========================================
# Example 5: Matching a List exactly
# ==========================================
point = [0, 0]
match point:
    case [0, 0]:
        print("Ex 5: Point is at the origin.")
    case [x, 0]:
        print("Ex 5: Point is on the X axis.")
# Explanation: Checks if the list has exactly two 0s.

# ==========================================
# Example 6: Capturing variables from a list
# ==========================================
command = ["move", "left"]
match command:
    case ["move", direction]:
        print(f"Ex 6: Moving character to the {direction}.")
    case _:
        print("Ex 6: Invalid command.")
# Explanation: It matches "move", and saves "left" into the variable 'direction'.

# ==========================================
# Example 7: Using Guards (if statements inside case)
# ==========================================
age = 20
match age:
    case x if x >= 18:
        print("Ex 7: Adult.")
    case _:
        print("Ex 7: Minor.")
# Explanation: We can add 'if' logic directly inside the case statement!

# ==========================================
# Example 8: Matching Type
# ==========================================
data = 100
match data:
    case int():
        print("Ex 8: Received an integer.")
    case str():
        print("Ex 8: Received a string.")
# Explanation: Checks the data type dynamically.

# ==========================================
# Example 9: Matching Dictionaries
# ==========================================
user = {"name": "Alice", "role": "admin"}
match user:
    case {"name": name, "role": "admin"}:
        print(f"Ex 9: Welcome Admin, {name}.")
    case _:
        print("Ex 9: Standard user.")
# Explanation: Checks if the dictionary has an admin role, and grabs the name.

# ==========================================
# Example 10: Complex Tuple matching
# ==========================================
player = ("Bob", 100, 5) # Name, Health, Level
match player:
    case (name, health, level) if health < 10:
        print(f"Ex 10: {name} is at critical health! Level {level}.")
    case (name, _, _):
        print(f"Ex 10: {name} is doing fine.")
# Explanation: Combines unpacking a tuple, using wildcards (_), and a guard clause.
