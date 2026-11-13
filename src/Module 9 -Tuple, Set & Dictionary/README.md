# Module 9: Tuple, Set & Dictionary

## Module overview

Python provides several built-in collection types. This module introduces:

- **Tuples** for ordered groups of values that should not be reassigned.
- **Sets** for collections of unique values and set operations.
- **Dictionaries** for associating keys with values.

Choosing a suitable collection makes code clearer and helps prevent mistakes.
For example, use a tuple for a fixed coordinate, a set to remove duplicate
tags, and a dictionary to look up a student's grade by name.

## Learning outcomes

After completing this module, you should be able to:

- Create tuples, including one-item tuples, and read their items.
- Use tuple indexing, slicing, `count()`, and `index()`.
- Explain the difference between a tuple and a list.
- Create sets and understand uniqueness and unordered behavior.
- Add and remove set items, and calculate union, intersection, and difference.
- Create dictionaries that map keys to values.
- Read, add, update, and delete dictionary entries.
- Use `keys()`, `values()`, `items()`, and `get()`.
- Select a collection type that fits a simple programming problem.

## Quick comparison

| Collection | Ordered? | Mutable? | Allows duplicates? | Access |
|---|---:|---:|---:|---|
| Tuple | Yes | No (items cannot be reassigned) | Yes | Position/index |
| Set | No guaranteed order | Yes | No | Membership, not index |
| Dictionary | Yes (insertion order) | Yes | Keys are unique | Key |

Set items and dictionary keys must be hashable. Common immutable values such
as strings, integers, and tuples of hashable values can be used. Lists and
dictionaries cannot be set items or dictionary keys.

## Topics and files

### 1. Tuples: creation, indexing, slicing, methods, and tuple vs. list

File: [`01_tuples.py`](01_tuples.py)

A **tuple** is an ordered sequence. Its positions stay in order, and duplicate
values are allowed. A tuple is **immutable**: you cannot assign a different
value to one of its positions after it is created.

```python
colors = ("red", "green", "blue")
print(colors[0])
print(colors[-1])
print(colors[1:3])
```

Output:

```text
red
blue
('green', 'blue')
```

Parentheses are common for tuples, but the commas are what make the tuple. A
one-item tuple must include a trailing comma:

```python
one_item = ("Python",)
not_a_tuple = ("Python")
print(type(one_item).__name__)
print(type(not_a_tuple).__name__)
```

Output:

```text
tuple
str
```

Tuples have two commonly taught methods:

- `count(value)` counts matching values.
- `index(value)` returns the first matching position and raises `ValueError`
  if the value is absent.

Tuple and list comparison:

| Feature | Tuple | List |
|---|---|---|
| Typical syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Can reassign an item? | No | Yes |
| Common use | Fixed group of values | Collection that changes |
| Indexing and slicing | Yes | Yes |

An immutable tuple can still contain a mutable object, such as a list. The
tuple's item reference cannot be replaced, but that inner list can be changed;
immutability is not automatically recursive.

### 2. Sets: creation, uniqueness, adding/removing, and operations

File: [`02_sets.py`](02_sets.py)

A **set** is a mutable collection of unique, hashable values. Adding a value
that is already present does not create another copy. Sets have no guaranteed
display order, so sort values in examples when predictable output is useful.

```python
numbers = {1, 2, 2, 3, 3}
print(sorted(numbers))
```

Output:

```text
[1, 2, 3]
```

Use `set()` to make an empty set. `{}` creates an empty dictionary instead.
Sets do not support position-based indexing because they do not have a
guaranteed item order.

| Operation | Meaning |
|---|---|
| `values.add(item)` | Add one item |
| `values.remove(item)` | Remove item; raises `KeyError` if absent |
| `values.discard(item)` | Remove item if present; otherwise do nothing |
| `first.union(second)` or `first \| second` | Values in either set |
| `first.intersection(second)` or `first & second` | Values in both sets |
| `first.difference(second)` or `first - second` | Values in first, not second |

Example:

```python
morning = {"tea", "toast", "fruit"}
afternoon = {"fruit", "sandwich"}

print(sorted(morning | afternoon))
print(sorted(morning & afternoon))
print(sorted(morning - afternoon))
```

Output:

```text
['fruit', 'sandwich', 'tea', 'toast']
['fruit']
['tea', 'toast']
```

`difference()` is directional: `first - second` is not necessarily the same as
`second - first`. The lesson also compares `remove()` with `discard()` and
demonstrates using a set to remove duplicate values from a list.

### 3. Dictionaries: key-value pairs, creation, access, update, and delete

File: [`03_dictionaries.py`](03_dictionaries.py)

A **dictionary** stores **key-value pairs**. A key acts as a label used to look
up its value. Keys must be unique and hashable; values may be any type.
Dictionaries preserve insertion order in modern Python.

```python
student = {"name": "Asha", "age": 18}
print(student["name"])
```

Output:

```text
Asha
```

Assigning to a new key adds a pair. Assigning to an existing key updates its
value. `del dictionary[key]` removes that pair. Reading a missing key with
bracket notation raises `KeyError`.

```python
student = {"name": "Asha", "age": 18}
student["grade"] = "A"  # Add a new key
student["age"] = 19      # Update an existing key
del student["grade"]     # Delete a key and its value
print(student)
```

Output:

```text
{'name': 'Asha', 'age': 19}
```

Duplicate keys in a dictionary literal do not create multiple entries: the
later value replaces the earlier value. Use `key in dictionary` to check key
membership; this checks keys, not values.

### 4. Dictionary methods: `keys()`, `values()`, `items()`, and `get()`

File: [`04_dictionary_methods.py`](04_dictionary_methods.py)

| Method | Result |
|---|---|
| `dictionary.keys()` | A dynamic view of the keys |
| `dictionary.values()` | A dynamic view of the values |
| `dictionary.items()` | A dynamic view of `(key, value)` pairs |
| `dictionary.get(key)` | Value for key, or `None` if the key is absent |
| `dictionary.get(key, default)` | Value for key, or `default` if absent |

Views can be iterated over directly and reflect changes made to the dictionary.
Use `list(...)` when you specifically need a list for display or further list
operations.

```python
student = {"name": "Asha", "age": 18}
print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
print(student.get("city", "Not provided"))
```

Output:

```text
['name', 'age']
['Asha', 18]
[('name', 'Asha'), ('age', 18)]
Not provided
```

Use `items()` to iterate over both key and value:

```python
for key, value in student.items():
    print(key, "=", value)
```

Output:

```text
name = Asha
age = 18
```

`get()` does not raise `KeyError` for a missing key. It returns `None` unless
you provide a default. Be aware that `None` can also be a value deliberately
stored in the dictionary; use `key in dictionary` if you need to distinguish
that case from an absent key.

## Common mistakes to avoid

- **Forgetting a one-item tuple's comma:** `("x",)` is a tuple, but `("x")` is
  just a string in parentheses.
- **Trying to update a tuple item:** tuples do not support item assignment.
- **Expecting a set to retain duplicates or a stable display order:** set items
  are unique and have no guaranteed order.
- **Using `{}` for an empty set:** use `set()`; `{}` creates a dictionary.
- **Using `remove()` for a missing set item:** it raises `KeyError`; use
  `discard()` if absence is acceptable.
- **Reversing set difference:** `A - B` means in A and not B, not the reverse.
- **Using a list or dictionary as a set item or dictionary key:** these
  mutable, unhashable types cannot be used there.
- **Confusing dictionary keys with values:** `key in dictionary` checks keys.
- **Accessing a missing dictionary key with brackets:** this raises `KeyError`;
  use `get()` when a fallback is appropriate.
- **Assuming `get()` can distinguish missing from stored `None`:** check
  membership with `key in dictionary` when that distinction matters.

## Practice ideas

1. Make a tuple describing a point `(x, y)`. Print each coordinate, then try
   changing one coordinate and observe the error.
2. Make a set from a list containing repeated names. Print the sorted unique
   names.
3. Create two sets of hobbies and display the union, intersection, and
   difference in both directions.
4. Create a dictionary for a book with title, author, and year. Add a genre,
   update the year, and delete a key.
5. Use `get()` to display an optional dictionary field with a default message.
6. Iterate through a dictionary with `items()` and print each key with its
   value.

## Running the examples

Run each lesson file from its directory with Python. For example:

```bash
python 01_tuples.py
```

Each Python file includes definitions, explanations, runnable examples, and
expected output comments:

1. `01_tuples.py`
2. `02_sets.py`
3. `03_dictionaries.py`
4. `04_dictionary_methods.py`
