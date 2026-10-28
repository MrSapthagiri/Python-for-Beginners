# 🔄 Module 5: Loops

Welcome to **Module 5**! We've learned how to make our programs make decisions (Conditionals). Now, we need to learn how to make our programs do repetitive tasks without us having to copy and paste code a hundred times.

This is where **Loops** come in. Loops allow you to execute a block of code repeatedly until a certain condition is met or until you've gone through all the items in a collection.

---

## 📁 What's Inside This Module?

We have broken down loops and iteration tools into 8 distinct files. Each file contains clear definitions, a mental-model flowchart, and **10 practical examples** (ranging from basic to advanced) with explanations.

### 1. `for` Loop (`01_for_loop.py`)
* **Definition:** Used to iterate over a sequence (like a list, string, or dictionary) and do something for every item inside it.
* **Analogy:** A factory assembly line. For every item coming down the belt, perform an action on it.

### 2. `while` Loop (`02_while_loop.py`)
* **Definition:** Executes a block of code repeatedly *as long as* a specific condition remains `True`.
* **Analogy:** "Keep bailing water out of the boat *while* there is still water in it."

### 3. `range()` Function (`03_range.py`)
* **Definition:** A built-in function that generates a sequence of numbers. Extremely useful for running a loop a specific number of times.
* **Analogy:** A ticket dispenser that gives out numbers 1 through 10.

### 4. `enumerate()` Function (`04_enumerate.py`)
* **Definition:** Adds a counter (index) to an iterable and returns it. Perfect for when you need the item *and* its position in the list.
* **Analogy:** A teacher reading a class roster: "Number 1, Alice. Number 2, Bob."

### 5. `break` Statement (`05_break.py`)
* **Definition:** Immediately completely escapes (exits) the loop it is inside, regardless of the loop's original condition.
* **Analogy:** Pulling the emergency stop brake on a train. The journey ends instantly.

### 6. `continue` Statement (`06_continue.py`)
* **Definition:** Skips the rest of the code inside the loop for the *current* iteration only, and immediately jumps to the *next* iteration.
* **Analogy:** A bouncer checking IDs. If the person is under 18, skip them (continue to the next person), but keep checking the rest of the line.

### 7. `pass` Statement (`07_pass.py`)
* **Definition:** A null operation. It literally does nothing. Used as a placeholder when a statement is required syntactically, but no code needs to be executed.
* **Analogy:** A "Under Construction" sign on a webpage.

### 8. Nested Loops (`08_nested_loops.py`)
* **Definition:** Placing a loop inside another loop. The "inner loop" finishes all of its iterations for *each* single iteration of the "outer loop".
* **Analogy:** A clock. For every 1 hour (outer loop), the minute hand (inner loop) must tick 60 times.

---

## 🚀 How to Use This Module
1. Open the `.py` files one by one.
2. Read the definitions and flowcharts at the top of the file.
3. Run the files in your terminal (e.g., `python 01_for_loop.py`) to see the 10 examples output in real-time.
4. Read the explanations under each example to understand exactly *why* it did what it did.
