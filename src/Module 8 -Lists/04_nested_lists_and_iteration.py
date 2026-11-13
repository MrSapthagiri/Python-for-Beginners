# Module 8: Lists — Nested Lists and Iteration
# =============================================
#
# DEFINITION
# A nested list is a list that contains one or more lists as its items.
# Iteration means visiting items one at a time, usually with a for loop.
#
# ACCESSING NESTED ITEMS
# If groups = [["A", "B"], ["C", "D"]]:
# - groups[0] selects the first inner list: ["A", "B"].
# - groups[0][1] selects "B" from that inner list.
#
# IMPORTANT NOTES
# - A nested list can represent rows and columns, such as a small table.
# - A loop over the outer list visits each inner list.
# - A nested loop can then visit every item in each inner list.
# - Row and column indexes start at zero.
# - Rows do not have to be the same length, but code must not assume a column
#   exists in every row unless the data is known to be rectangular.
# - Iterating over items directly is usually clearer than manually using indexes.
#
# LOOP TRACE
# For grid = [[1, 2], [3, 4]]:
# - The outer loop first assigns [1, 2] to row.
# - The inner loop prints 1, then 2.
# - The outer loop next assigns [3, 4] to row.
# - The inner loop prints 3, then 4.


# Example 1: Access an item in a nested list
# Explanation: The first index selects a row; the second selects an item.
students = [["Asha", 18], ["Ravi", 19]]
print("Example 1 - First student's name:", students[0][0])
# Output: Example 1 - First student's name: Asha


# Example 2: Iterate through a flat list
# Explanation: Each loop iteration assigns the next item to fruit.
fruits = ["apple", "banana", "cherry"]
print("\nExample 2 - Fruits:")
for fruit in fruits:
    print(fruit)
# Output:
# Example 2 - Fruits:
# apple
# banana
# cherry


# Example 3: Iterate through each row in a nested list
# Explanation: The loop variable row refers to one inner list at a time.
grid = [[1, 2], [3, 4], [5, 6]]
print("\nExample 3 - Rows:")
for row in grid:
    print(row)
# Output:
# Example 3 - Rows:
# [1, 2]
# [3, 4]
# [5, 6]


# Example 4: Visit every item with a nested loop
# Explanation: The inner loop visits all values in the current row.
grid = [[1, 2], [3, 4]]
print("\nExample 4 - Every value:")
for row in grid:
    for value in row:
        print(value)
# Output:
# Example 4 - Every value:
# 1
# 2
# 3
# 4


# Example 5: Calculate a total from nested lists
# Explanation: Add each value from each row to the running total.
weekly_sales = [[10, 20], [15, 25]]
total = 0
for week in weekly_sales:
    for sale in week:
        total += sale
print("\nExample 5 - Total sales:", total)
# Output: Example 5 - Total sales: 70


# Example 6: Iterate with indexes using enumerate()
# Explanation: enumerate() supplies both the zero-based row index and the row.
students = [["Asha", 18], ["Ravi", 19]]
print("\nExample 6 - Students with row numbers:")
for index, student in enumerate(students):
    print(index, student[0])
# Output:
# Example 6 - Students with row numbers:
# 0 Asha
# 1 Ravi


# Example 7: Process rows that have different lengths
# Explanation: Loop through the values that are actually present in each row.
# This does not assume every row has the same number of columns.
data = [[1, 2], [3], [4, 5, 6]]
row_totals = []
for row in data:
    row_total = 0
    for value in row:
        row_total += value
    row_totals.append(row_total)
print("\nExample 7 - Total for each row:", row_totals)
# Output: Example 7 - Total for each row: [3, 3, 15]


# Example 8: Find a value in a nested list
# Explanation: A flag records whether the value has been seen while visiting
# rows. The loop stops as soon as the value is found.
grid = [[1, 2], [3, 4]]
target = 3
found = False
for row in grid:
    if target in row:
        found = True
        break
print("\nExample 8 - Target found:", found)
# Output: Example 8 - Target found: True


# COMMON MISTAKES
# - grid[0][1] means row 0, column 1; reversing these indexes accesses a
#   different value.
# - A nested loop is required to visit every value in a nested list.
# - Avoid changing the list structure while directly iterating over it, because
#   adding or removing items can make the loop skip or revisit values.


# QUICK REVISION
# - Nested list example: matrix = [[1, 2], [3, 4]]
# - Access a row: matrix[0]
# - Access a value: matrix[0][1]
# - Use one loop per nesting level to visit every value.
# - Use enumerate(items) when both index and item are needed.
