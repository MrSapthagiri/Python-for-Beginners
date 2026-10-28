# Module 6: Python Strings — Formatting Methods

> **Study guide:** 

            `split()`, 
            `join()`, 
            `replace()`, and 
            `find()`  

> Includes definitions, syntax, parameter explanations, practical examples, expected outputs, common mistakes, interview questions, and exercises.

---

## Learning objectives

By the end of this module, you should be able to:

- Split text into meaningful parts using delimiters.
- Combine strings using a chosen separator.
- Replace, remove, or standardize text.
- Search for a substring and safely handle missing results.
- Chain string methods to clean and format data.
- Explain the differences between these methods in interviews.

## 1. Important concepts

A **string** is a sequence of characters enclosed in quotes.

```python
message = "Learn Python"
```

Python strings are **immutable**. String methods return a result; they do not change the original string in place. Assign the result if you want to keep the change:

```python
text = "I like Java"
text = text.replace("Java", "Python")
print(text)
```

Output:

```text
I like Python
```

String positions start at index `0`. Searching methods such as `find()` return zero-based positions.

---

## 2. `split()` — divide a string

### Definition

`split()` divides a string into a **list of strings**, using a separator (delimiter). If no separator is provided, Python splits on runs of whitespace and ignores leading/trailing whitespace.

### Syntax

```python
string.split(sep=None, maxsplit=-1)
```

| Parameter | Meaning |
|---|---|
| `sep` | Optional separator, such as `","`, `"-"`, or `" "` |
| `maxsplit` | Maximum number of splits; default `-1` means split as many times as possible |

### Example 1: Split a sentence into words

```python
text = "Python is easy to learn"
words = text.split()

print(words)
```

Output:

```text
['Python', 'is', 'easy', 'to', 'learn']
```

### Example 2: Split comma-separated values

```python
text = "apple,banana,mango"
fruits = text.split(",")

print(fruits)
```

Output:

```text
['apple', 'banana', 'mango']
```

### Example 3: Limit the number of splits

```python
text = "one-two-three-four"
parts = text.split("-", 2)

print(parts)
```

Output:

```text
['one', 'two', 'three-four']
```

### Example 4: Split while preserving awareness of whitespace

```python
text = "QA, Automation, Python"
items = text.split(",")

print(items)
print([item.strip() for item in items])
```

Output:

```text
['QA', ' Automation', ' Python']
['QA', 'Automation', 'Python']
```

**Key point:** `split(",")` does not automatically remove spaces around each item. Use `strip()` when needed.

**Practical use cases:** parsing simple comma-separated input, separating words, processing labels, and extracting fields from consistently formatted text. For complex CSV files with quoted commas or escaped values, use Python's `csv` module instead of plain `split()`.

---

## 3. `join()` — combine strings

### Definition

`join()` combines an iterable of strings into one string. The separator is inserted **between** items.

### Syntax

```python
separator.join(iterable)
```

### Example 5: Join words with spaces

```python
words = ["Learn", "Python",",", "Today"]
result = " ".join(words)

print(result)
```

Output:

```text
Learn Python , Today
```

### Example 6: Join with a pipe separator

```python
tools = ["Playwright", "Selenium", "Pytest"]
result = " | ".join(tools)

print(result)
```

Output:

```text
Playwright | Selenium | Pytest
```

### Example 7: Join characters without a separator

```python
letters = ["P", "y", "t", "h", "o", "n"]
print("".join(letters))
```

Output:

```text
Python
```

### Example 8: Convert a list of numbers safely

```python
numbers = [2026, 10, 14]
date_text = "-".join(str(number) for number in numbers)

print(date_text)
```

Output:

```text
2026-10-14
```

**Key point:** Every item passed to `join()` must be a string. Convert non-string values with `str()` first.

**Practical use cases:** formatting lists, creating readable messages, building simple delimited records, and generating text identifiers.

---

## 4. `replace()` — substitute text

### Definition

`replace()` returns a new string where matching occurrences of one substring are replaced by another.

### Syntax

```python
string.replace(old, new, count=-1)
```

| Parameter | Meaning |
|---|---|
| `old` | Substring to find |
| `new` | Replacement substring |
| `count` | Optional maximum number of replacements; default `-1` replaces all occurrences |

### Example 9: Replace all occurrences

```python
text = "Java is popular. Java is powerful."
result = text.replace("Java", "Python")

print(result)
```

Output:

```text
Python is popular. Python is powerful.
```

### Example 10: Replace only the first occurrence

```python
text = "test test test"
print(text.replace("test", "pass", 1))
```

Output:

```text
pass test test
```

### Example 11: Remove a character

Replacing text with an empty string removes that substring.

```python
phone = "123-456-7890"
print(phone.replace("-", ""))
```

Output:

```text
1234567890
```

### Example 12: Standardize text

```python
status = "Build: FAILED"
status = status.replace("FAILED", "PASSED")

print(status)
```

Output:

```text
Build: PASSED
```

**Key points:**

- `replace()` is case-sensitive.
- It does not modify the original string.
- The optional `count` limits replacements, not the length of the result.
- Use it for straightforward text substitutions; it is not a full regular-expression engine.

**Practical use cases:** normalizing labels, removing unwanted separators, updating text, and formatting test data.

---

## 5. `find()` — search for a substring

### Definition

`find()` returns the index of the **first occurrence** of a substring. If it is not found, it returns `-1`.

### Syntax

```python
string.find(sub, start=0, end=len(string))
```

| Parameter | Meaning |
|---|---|
| `sub` | Substring to search for |
| `start` | Optional index at which to begin searching |
| `end` | Optional ending boundary; this index is excluded |

### Example 13: Find a word

```python
text = "Learn Python programming"
position = text.find("Python")

print(position)
```

Output:

```text
6
```

### Example 14: Handle text that is not found

```python
text = "Learn Python"

position = text.find("Java")
print(position)
```

Output:

```text
-1
```

### Example 15: Search from a specific position

```python
text = "banana"
print(text.find("a", 2))
```

Output:

```text
3
```

The search starts at index `2`, so the first matching `"a"` is at index `3`.

### Example 16: Use `find()` in a condition

```python
message = "Status: PENDING"

if message.find("PENDING") != -1:
    print("Pending status found")
else:
    print("Pending status not found")
```

Output:

```text
Pending status found
```

**Key points:**

- `find()` returns an integer, not `True` or `False`.
- It returns `-1` when the substring is absent.
- It is case-sensitive.
- If you only need to check whether text exists, `"Python" in text` is usually clearer.
- `find()` searches for literal substrings, not regular expressions.

---

## 6. Combining methods in practical workflows

### Example 17: Clean and format a comma-separated list

```python
raw_items = " apple, banana , mango "
items = [item.strip() for item in raw_items.split(",")]
result = " | ".join(items)

print(result)
```

Output:

```text
apple | banana | mango
```

**What happens?**

1. `split(",")` separates the items.
2. `strip()` removes surrounding whitespace from each item.
3. `join()` combines the cleaned items with a readable separator.

### Example 18: Find a keyword and replace it

```python
message = "Status: PENDING"

if message.find("PENDING") != -1:
    message = message.replace("PENDING", "APPROVED")

print(message)
```

Output:

```text
Status: APPROVED
```

### Example 19: Create a simple text slug

```python
title = "learn python strings"
slug = "_".join(title.split())

print(slug)
```

Output:

```text
learn_python_strings
```

### Example 20: Parse a simple key-value record

```python
record = "STATUS:ACTIVE|ID:1042"
fields = record.split("|")

for field in fields:
    key, value = field.split(":", 1)
    print(key, "=", value)
```

Output:

```text
STATUS = ACTIVE
ID = 1042
```

This example assumes the record consistently uses `|` between fields and `:` between each key and value.

---

## 7. Comparison table

| Method | Main purpose | Returns | When text is missing |
|---|---|---|---|
| `split()` | Divide a string | List | Not applicable |
| `join()` | Combine strings | String | Not applicable |
| `replace()` | Substitute text | String | Original string is returned unchanged if no match exists |
| `find()` | Locate a substring | Integer | Returns `-1` |

### `find()` vs `index()`

```python
text = "Hello Python"

print(text.find("Java"))  # -1
# print(text.index("Java"))  # Raises ValueError
```

Use `find()` when a missing substring is an expected possibility and you want `-1` rather than an exception.

---

## 8. Common mistakes to avoid

1. **Expecting `split()` to return a string:** it returns a list.
2. **Forgetting whitespace:** `split(",")` can leave spaces in individual items.
3. **Passing integers to `join()`:** convert them to strings first.
4. **Expecting `replace()` to update a variable automatically:** assign the returned value.
5. **Assuming `find()` raises an error when a match is missing:** it returns `-1`.
6. **Confusing `find()` with `index()`:** `index()` raises `ValueError` if no match exists.
7. **Ignoring case sensitivity:** `"Python"` and `"python"` are different strings for these searches and replacements.
8. **Using plain `split()` for complicated CSV data:** quoted separators require a CSV-aware parser.

---

## 9. Interview questions and answers

### Q1. What is the difference between `split()` and `join()`?

**Answer:** `split()` breaks a string into a list. `join()` combines an iterable of strings into one string using a separator.

### Q2. What does `find()` return if a substring is absent?

**Answer:** It returns `-1`. By comparison, `index()` raises `ValueError`.

### Q3. How do you replace only the first occurrence of a substring?

**Answer:** Pass `1` as the third argument: `text.replace("old", "new", 1)`.

### Q4. How can you remove hyphens from a string?

**Answer:** Use `text.replace("-", "")`.

### Q5. How can you combine list items with commas and spaces?

**Answer:** Use `", ".join(items)`, provided all items are strings.

### Q6. How do you split text using a comma?

**Answer:** Use `text.split(",")`.

### Q7. Do these methods change the original string?

**Answer:** No. Strings are immutable, so the methods return results without changing the original string in place.

### Q8. What is the difference between `find()` and the `in` operator?

**Answer:** `find()` returns the position or `-1`. The `in` operator returns a Boolean value indicating whether the substring exists.

### Q9. What does `maxsplit` do?

**Answer:** It limits how many splits `split()` performs. Any remaining text stays together in the final list item.

### Q10. Why might `join()` raise a `TypeError`?

**Answer:** Because one or more elements are not strings. Convert values with `str()` before joining.

---

## 10. Practice exercises

Try writing the code before checking the solutions.

1. Split `"red-green-blue"` using `"-"`.
2. Join `["QA", "Automation", "Engineer"]` with spaces.
3. Replace `"old"` with `"new"` in `"old code"`.
4. Find the position of `"test"` in `"automation test"`.
5. Convert `"one, two, three"` into `"one | two | three"`, removing extra spaces.
6. Replace only the first `"fail"` in `"fail fail fail"` with `"pass"`.
7. Check whether `"Python"` exists in `"Learn Python today"` using `find()`.
8. Convert `"2026/10/14"` into `"2026-10-14"` using `replace()`.
9. Split `"name: Giri: QA"` at the first colon only.
10. Create `"playwright_automation_testing"` from `"playwright automation testing"`.

<details>
<summary><strong>Suggested solutions</strong></summary>

```python
# 1
print("red-green-blue".split("-"))

# 2
print(" ".join(["QA", "Automation", "Engineer"]))

# 3
print("old code".replace("old", "new"))

# 4
print("automation test".find("test"))

# 5
text = "one, two, three"
print(" | ".join(item.strip() for item in text.split(",")))

# 6
print("fail fail fail".replace("fail", "pass", 1))

# 7
text = "Learn Python today"
print(text.find("Python") != -1)

# 8
print("2026/10/14".replace("/", "-"))

# 9
print("name: Giri: QA".split(":", 1))

# 10
print("_".join("playwright automation testing".split()))
```

</details>

---

## Final revision checklist

- [ ] I can explain the syntax and return type of all four methods.
- [ ] I can split text with a custom delimiter and `maxsplit`.
- [ ] I can join strings with spaces, commas, or custom separators.
- [ ] I can replace all or only a limited number of occurrences.
- [ ] I know that `find()` returns `-1` when text is absent.
- [ ] I can combine `split()`, `strip()`, and `join()` to clean text.
- [ ] I can explain string immutability and the difference between `find()` and `index()`.

