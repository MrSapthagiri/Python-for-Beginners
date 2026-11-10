# Module 8: Lists

## Module overview

A **list** is a built-in Python collection for storing several items under one
variable name. Lists keep their items in order, allow duplicate values, and
can be changed after they are created. Because lists are mutable, a program can
add, remove, replace, sort, and process their items as it runs.

Lists are useful for representing collections such as shopping items, scores,
names, temperatures, and rows of data. This module explains how to create and
work with lists, and then use them to solve small problems.

## Learning outcomes

After completing this module, you should be able to:

- Create lists containing strings, numbers, or mixed types.
- Read list items using positive and negative indexes.
- Select a range of items using slices.
- Update individual items and ranges of items.
- Add and remove items using `append()`, `insert()`, `remove()`, and `pop()`.
- Sort, reverse, search, and count list values.
- Read and process nested lists with loops.
- Create transformed or filtered lists with list comprehensions.
- Solve simple list problems such as finding a total, largest value, or count.

## Topics and files

### 1. List creation, indexing, slicing, and updating

File: [`01_list_creation_indexing_slicing_updating.py`](01_list_creation_indexing_slicing_updating.py)

#### Creating lists

Write list items inside square brackets, separating items with commas:

```python
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30]
empty_list = []
```

Lists can contain repeated values and values of different types. Usually,
keeping items of a similar kind in one list makes the program easier to
understand.

#### Indexing: reading one item

Each item has a position called an **index**. Positive indexes begin at `0`;
negative indexes count backward from `-1`.

```python
colors = ["red", "green", "blue"]
print(colors[0])
print(colors[-1])
```

Output:

```text
red
blue
```

Use an index within the list's valid range. Accessing a missing position, such
as `colors[3]` above, raises `IndexError`.

#### Slicing: reading a range

The general slice form is `list[start:stop:step]`. The start position is
included, and the stop position is excluded. The step is optional and defaults
to `1`.

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
print(numbers[:2])
print(numbers[2:])
print(numbers[::2])
```

Output:

```text
[20, 30, 40]
[10, 20]
[30, 40, 50]
[10, 30, 50]
```

When start or stop is omitted, the slice uses the beginning or end of the list.
A slice creates a new list; it does not replace the original list.

#### Updating items

Lists are **mutable**, which means an item can be replaced after the list is
created. Slice assignment can replace a range:

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)

numbers = [1, 2, 3, 4]
numbers[1:3] = [20, 30]
print(numbers)
```

Output:

```text
['apple', 'mango', 'cherry']
[1, 20, 30, 4]
```

### 2. Adding and removing elements

File: [`02_adding_removing_elements.py`](02_adding_removing_elements.py)

These methods modify the existing list:

| Method | What it does | Important detail |
|---|---|---|
| `append(value)` | Adds one value at the end | The value is added as a single item. |
| `insert(index, value)` | Adds a value at a position | Items at and after that position move to make room. |
| `remove(value)` | Removes a matching value | Removes the first match; raises `ValueError` if absent. |
| `pop(index)` | Removes and returns an item | With no index, removes and returns the last item. |

```python
tasks = ["read", "practice"]
tasks.append("review")
tasks.insert(1, "plan")
print(tasks)

removed_task = tasks.pop()
tasks.remove("read")
print(removed_task)
print(tasks)
```

Output:

```text
['read', 'plan', 'practice', 'review']
review
['plan', 'practice']
```

Choose `remove()` when you know the value to remove. Choose `pop()` when you
want to remove an item by position and possibly use the returned value. Check
that a value exists before calling `remove()` if it may be absent.

### 3. List methods: `sort()`, `reverse()`, `index()`, and `count()`

File: [`03_list_methods.py`](03_list_methods.py)

| Method | What it does | Changes the original list? |
|---|---|---|
| `sort()` | Sorts items in ascending order by default | Yes |
| `reverse()` | Reverses the current item order | Yes |
| `index(value)` | Finds the index of the first matching value | No |
| `count(value)` | Counts matching values | No |

```python
scores = [72, 95, 88, 81]
scores.sort()
print(scores)

scores.reverse()
print(scores)
print(scores.index(95))
print(scores.count(88))
```

Output:

```text
[72, 81, 88, 95]
[95, 88, 81, 72]
0
1
```

`reverse()` does not sort; it only flips the current order. `sort()` changes the
list in place and returns `None`. Use `sorted(items)` when you want a separate
sorted list while preserving the original:

```python
numbers = [3, 1, 2]
new_sorted_list = sorted(numbers)
print(numbers)
print(new_sorted_list)
```

Output:

```text
[3, 1, 2]
[1, 2, 3]
```

`index()` raises `ValueError` if the value is missing. `count()` returns `0`
when the value is not present.

### 4. Nested lists and iterating through lists

File: [`04_nested_lists_and_iteration.py`](04_nested_lists_and_iteration.py)

A **nested list** is a list that contains other lists. It can represent a
simple table, grid, or groups of related values:

```python
grid = [
    [1, 2],
    [3, 4],
]

print(grid[0])
print(grid[0][1])
```

Output:

```text
[1, 2]
2
```

The first index selects an inner list (a row); the second index selects an
item inside that row. A `for` loop visits items one at a time. With nested
lists, a nested loop can visit each item in each row:

```python
for row in grid:
    for value in row:
        print(value)
```

Output:

```text
1
2
3
4
```

This same pattern can accumulate a total or perform another operation on every
value in a table.

### 5. List comprehensions and basic problem solving

File: [`05_list_comprehensions_and_problems.py`](05_list_comprehensions_and_problems.py)

A **list comprehension** builds a new list by looping over values. Its basic form is:

```python
[expression for item in iterable]
```

Add a condition to include only items that meet a rule:

```python
[expression for item in iterable if condition]
```

For example, transform numbers into their squares or filter for even values:

```python
squares = [number * number for number in range(1, 6)]
numbers = [1, 2, 3, 4, 5, 6]
evens = [number for number in numbers if number % 2 == 0]

print(squares)
print(evens)
```

Output:

```text
[1, 4, 9, 16, 25]
[2, 4, 6]
```

The expression creates each output item. The optional `if` filters the input
items; it does not alter the source list.

#### Basic list problem-solving patterns

The lesson file also shows how to use loops to:

- **Calculate a total:** start a total at `0`, then add each value.
- **Find the largest value:** start with an item and replace it whenever a
  larger value is found.
- **Count matches:** start a counter at `0`, then increment it when an item
  meets a condition.

For example, count words that have more than four letters:

```python
words = ["cat", "tiger", "lion", "elephant"]
long_word_count = 0

for word in words:
    if len(word) > 4:
        long_word_count += 1

print(long_word_count)
```

Output:

```text
2
```

## Common mistakes to avoid

- **Using the wrong index:** the first item is at index `0`, not index `1`.
- **Including the slice stop:** the stop index is excluded. For example,
  `items[1:3]` selects indexes `1` and `2`.
- **Confusing `remove()` and `pop()`:** `remove()` takes a value; `pop()` takes
  an index and returns the removed item.
- **Expecting `reverse()` to sort:** it reverses the order as it currently is.
- **Saving the result of `sort()`:** `sort()` changes the list and returns
  `None`; use `sorted(items)` to get a new sorted list.
- **Removing a missing value:** `remove()` raises `ValueError` if no matching
  item exists.
- **Using a list comprehension for every task:** a regular loop is often easier
  to read for multi-step or complicated logic.

## Quick reference

| Goal | Example |
|---|---|
| Create a list | `items = ["a", "b", "c"]` |
| Read the first item | `items[0]` |
| Read the last item | `items[-1]` |
| Select a slice | `items[1:3]` |
| Replace an item | `items[0] = "new"` |
| Add to the end | `items.append("new")` |
| Insert at a position | `items.insert(1, "new")` |
| Remove a value | `items.remove("a")` |
| Remove and return an item | `items.pop()` |
| Sort in place | `items.sort()` |
| Reverse current order | `items.reverse()` |
| Find a value's index | `items.index("b")` |
| Count a value | `items.count("b")` |
| Build a transformed list | `[item * 2 for item in numbers]` |

## Practice ideas

1. Make a list of five favorite foods and print the first and last items.
2. Slice a list of numbers to display only its middle items.
3. Add a new item, insert another at a chosen position, and remove one.
4. Sort a list of scores and find how many times a chosen score occurs.
5. Make a two-row list of numbers and calculate the total using nested loops.
6. Use a list comprehension to create a list of odd numbers from `1` through
   `15`.

## Running the examples

Run each file from its directory with Python. For example:

```bash
python 01_list_creation_indexing_slicing_updating.py
```

Each Python file includes its own definitions, explanations, examples, and
expected output comments. The module files are:

1. `01_list_creation_indexing_slicing_updating.py`
2. `02_adding_removing_elements.py`
3. `03_list_methods.py`
4. `04_nested_lists_and_iteration.py`
5. `05_list_comprehensions_and_problems.py`
