# 🚦 Module 4: Conditional Statements

Welcome to **Module 4**! Up until now, our Python programs have run in a straight line from top to bottom. But what if we want our program to make decisions? What if we want it to do one thing if a user is logged in, and a totally different thing if they aren't? 

That's where **Conditional Statements** come in. They are the "brains" of your program, allowing it to evaluate conditions (`True` or `False`) and branch out into different paths of execution.

---

## 📁 What's Inside This Module?

We have broken down conditional logic into 6 distinct files. Each file contains clear definitions, a mental-model flowchart, and **10 practical examples** (ranging from basic to advanced) with explanations.

### 1. The `if` Statement (`01_if_statement.py`)
The foundation of decision-making. 
* **Definition:** Executes a block of code *only* if a specific condition is evaluated as `True`. If it's `False`, the code is completely ignored.
* **Analogy:** "If it is raining, take an umbrella." (If it's not raining, you do nothing special).

### 2. The `if...else` Statement (`02_if_else.py`)
Adding a "Plan B" to your code.
* **Definition:** Provides two paths. If the condition is `True`, run the `if` block. If it's `False`, run the `else` block instead.
* **Analogy:** "If you know the password, unlock the door. Else, trigger the alarm."

### 3. The `if...elif...else` Statement (`03_if_elif_else.py`)
Handling multiple possibilities in order.
* **Definition:** Allows checking a chain of conditions one by one using `elif` (else if). As soon as Python finds a `True` condition, it runs that block and skips the rest.
* **Analogy:** "If the light is green, go. Else if (elif) the light is yellow, slow down. Else (red), stop."

### 4. Nested `if` Statements (`04_nested_if.py`)
Decisions inside of decisions.
* **Definition:** Placing an `if` statement *inside* another `if` block. This is used when a secondary condition only matters if the primary condition was met first.
* **Analogy:** "If you have a ticket, you can enter the airport. *And if* you have a passport, you can board the international flight."

### 5. Match Case (`05_match_case.py`)
The modern, powerful way to route logic (Introduced in Python 3.10).
* **Definition:** Compares a variable against a series of structured patterns (cases). It is much cleaner than writing a giant wall of `elif` statements when checking specific values or data structures.
* **Analogy:** A post office sorting machine looking at the zip code and instantly dropping the letter into the right bin.

### 6. The Ternary Operator (`06_ternary_operator.py`)
One-line decision making.
* **Definition:** A super concise way to assign a value based on a condition, all in a single line of code. 
* **Syntax:** `result = Plan_A if Condition else Plan_B`
* **Analogy:** A quick coin flip to decide what shirt to wear without having to write down a whole pros/cons list.

---

## 🚀 How to Use This Module
1. Open the `.py` files one by one.
2. Read the definitions and flowcharts at the top of the file.
3. Run the files in your terminal (e.g., `python 01_if_statement.py`) to see the 10 examples output in real-time.
4. Read the explanations under each example to understand exactly *why* it did what it did.
