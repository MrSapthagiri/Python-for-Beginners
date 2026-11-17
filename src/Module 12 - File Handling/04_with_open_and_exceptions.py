"""Demonstrate automatic file closing and common file exceptions."""

from pathlib import Path
from tempfile import TemporaryDirectory

# Module 12: File Handling
# Topic 4: with open() and file exception handling
#
# The with statement closes its file even if work inside the block fails.
# Catch a specific exception only when the program can respond usefully.


with TemporaryDirectory() as temporary_directory:
    file_path = Path(temporary_directory) / "message.txt"
    file_path.write_text("File handling is useful.\n", encoding="utf-8")

    # Example 1: Read and automatically close the file.
    with open(file_path, "r", encoding="utf-8") as file:
        message = file.read().strip()
        file_was_open = not file.closed
    print("Example 1 - Message:", message)
    print("Example 1 - Open inside block:", file_was_open)
    print("Example 1 - Closed after block:", file.closed)
    # Output: Example 1 - Message: File handling is useful.
    # Output: Example 1 - Open inside block: True
    # Output: Example 1 - Closed after block: True

    # Example 2: A missing input file raises FileNotFoundError.
    missing_path = Path(temporary_directory) / "missing.txt"
    try:
        with open(missing_path, "r", encoding="utf-8") as file:
            file.read()
    except FileNotFoundError:
        print("Example 2 - Could not find the requested file.")
    # Output: Example 2 - Could not find the requested file.

    # Example 3: Exclusive creation raises FileExistsError for an existing file.
    try:
        with open(file_path, "x", encoding="utf-8") as file:
            file.write("This will not replace the message.\n")
    except FileExistsError:
        print("Example 3 - The file already exists; existing text is safe.")
    # Output: Example 3 - The file already exists; existing text is safe.

    # Example 4: Operating systems may report a directory path differently.
    try:
        with open(temporary_directory, "r", encoding="utf-8") as file:
            file.read()
    except (IsADirectoryError, PermissionError):
        print("Example 4 - A directory path is not a text file.")
    # Output: Example 4 - A directory path is not a text file.


# Quick review:
# - The file is closed when the with block ends, even if an exception occurs.
# - Handle expected errors specifically; do not silently discard exceptions.
