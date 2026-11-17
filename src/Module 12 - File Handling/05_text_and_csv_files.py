# pylint: disable=invalid-name
"""Demonstrate basic text and CSV file handling."""

import csv
from pathlib import Path
from tempfile import TemporaryDirectory

# Module 12: File Handling
# Topic 5: Basic text and CSV file handling
#
# Text files hold characters. CSV files represent tabular rows; use the csv
# module because fields may contain commas, quotes, and newline characters.


with TemporaryDirectory() as temporary_directory:
    directory = Path(temporary_directory)

    # Example 1: Write and read ordinary text.
    text_path = directory / "reminder.txt"
    text_path.write_text("Practise a little every day.\n", encoding="utf-8")
    with open(text_path, "r", encoding="utf-8") as file:
        reminder = file.read().strip()
    print("Example 1 - Text:", reminder)
    # Output: Example 1 - Text: Practise a little every day.

    # Example 2: Write rows to CSV. newline="" is recommended by csv.
    csv_path = directory / "books.csv"
    books = [
        ["title", "author", "price"],
        ["Python Basics", "Asha, Ravi", "19.5"],
        ["Learning CSV", "Morgan", "12.0"],
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(books)
    print("Example 2 - CSV file created:", csv_path.name)
    # Output: Example 2 - CSV file created: books.csv

    # Example 3: Read CSV rows as lists of strings.
    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))
    print("Example 3 - First data row:", rows[1])
    # Output: Example 3 - First data row: ['Python Basics', 'Asha, Ravi', '19.5']

    # Example 4: Read CSV rows by column name with DictReader.
    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        books_by_column = list(csv.DictReader(file))
    print("Example 4 - Book title:", books_by_column[0]["title"])
    print("Example 4 - Price as text:", books_by_column[0]["price"])
    # Output: Example 4 - Book title: Python Basics
    # Output: Example 4 - Price as text: 19.5

    # Example 5: Write CSV rows using named columns.
    summary_path = directory / "summary.csv"
    with open(summary_path, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["item", "quantity"]
        dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerow({"item": "notebooks", "quantity": 3})
    with open(summary_path, "r", newline="", encoding="utf-8") as file:
        summary = list(csv.DictReader(file))
    quantity = int(summary[0]["quantity"])
    print("Example 5 - Quantity:", quantity)
    # Output: Example 5 - Quantity: 3


# Quick review:
# - Text-file APIs read and write strings.
# - CSV reader values are strings; convert them before numeric calculations.
# - Use csv.reader/writer or DictReader/DictWriter instead of splitting commas.
