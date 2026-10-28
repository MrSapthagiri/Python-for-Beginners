"""
================================================================================
Topic: The 'pass' Statement
================================================================================

1. DEFINITION:
The `pass` statement does absolutely nothing. It is a "null operation". 
It is used as a placeholder when a statement is required syntactically 
(because Python relies on indentation and expects a block of code), but you 
don't want any code to execute.

2. FLOWCHART (Mental Model):
      [Code block expects content]
         |
         v
       [pass] ---> (Does nothing, moves to next line)

================================================================================
"""

print("\n--- Low Level (Basic) ---")

# ==========================================
# Example 1: Placeholder in an 'if' block
# ==========================================
x = 10
if x > 5:
    pass # I'll write this code later
print("Ex 1: Program didn't crash!")
# Explanation: If we left it empty, Python would throw an IndentationError.

# ==========================================
# Example 2: Placeholder in a 'for' loop
# ==========================================
for i in range(5):
    pass 
print("Ex 2: Loop finished silently.")
# Explanation: Loops 5 times doing nothing.

# ==========================================
# Example 3: Placeholder in a 'while' loop
# ==========================================
ready = True
while not ready:
    pass # Wait until ready
# Explanation: Note - this is a bad idea in real life (creates a CPU-hogging infinite loop), but syntactically valid.

print("\n--- Medium Level (Intermediate) ---")

# ==========================================
# Example 4: Creating empty functions (Stubs)
# ==========================================
def calculate_taxes():
    pass # TODO: Implement complex tax logic later

print("Ex 4: Empty function defined successfully.")
# Explanation: Allows you to sketch out the structure of your program without writing the logic yet.

# ==========================================
# Example 5: Creating empty classes
# ==========================================
class DatabaseConnection:
    pass

db = DatabaseConnection()
print("Ex 5: Empty class instantiated.")
# Explanation: Useful when setting up an architecture blueprint.

# ==========================================
# Example 6: Exception handling (Ignoring errors)
# ==========================================
try:
    zero = 0
    result = 10 / zero
except ZeroDivisionError:
    pass # Silently ignore the error

print("Ex 6: Division error ignored.")
# Explanation: Sometimes you expect an error and genuinely want to do nothing about it.

# ==========================================
# Example 7: Ignoring specific conditions
# ==========================================
user_type = "guest"
if user_type == "admin":
    print("Show admin dashboard")
elif user_type == "guest":
    pass # Guests see nothing special, so do nothing.
else:
    print("Show standard dashboard")
print("Ex 7: Guest logic handled via pass.")
# Explanation: Explicitly showing that we intentionally do nothing for guests.

print("\n--- High Level (Advanced/Senior) ---")

# ==========================================
# Example 8: Abstract Base Classes (OOP)
# ==========================================
# Seniors use pass in abstract methods to enforce child classes to write the code.
class Animal:
    def make_sound(self):
        pass # The base class has no sound, but forces subclasses to implement it.

class Dog(Animal):
    def make_sound(self):
        print("Bark!")
print("Ex 8: Defined abstract-like class architecture.")
# Explanation: A blueprint pattern in Object-Oriented Programming.

# ==========================================
# Example 9: Minimal Custom Exceptions
# ==========================================
class PaymentFailedError(Exception):
    pass # We just need the class name, the base Exception class handles the rest!

print("Ex 9: Custom exception created.")
# Explanation: The fastest way to create custom, descriptive error types.

# ==========================================
# Example 10: pass vs continue
# ==========================================
print("Ex 10: Pass vs Continue:")
for i in range(3):
    if i == 1:
        pass # Does nothing, the loop continues normally right below it.
        print(f"Inside the pass block: {i}")
    
    if i == 2:
        continue # Instantly jumps to the top, skipping the print below.
        print("This will NEVER print!")
# Explanation: `pass` is just a blank space. `continue` is an active command to jump.
