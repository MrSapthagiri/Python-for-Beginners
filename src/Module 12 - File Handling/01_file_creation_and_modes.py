"""Demonstrate file creation, closing, and common text file modes."""

from pathlib import Path
from tempfile import TemporaryDirectory

# Module 12: File Handling
# Topic 1: File creation, opening, closing, and modes
#
# "x" creates a new file and refuses to overwrite an existing one.
# "w" creates or replaces a file, and "a" creates or appends to a file.
# A file opened with open() should be closed when it is no longer needed.


with TemporaryDirectory() as temporary_directory:
    file_path = Path(temporary_directory) / "notes.txt"

    # Create a new file exclusively and close it explicitly.
    file = open(file_path, "x", encoding="utf-8")
    file.write("First note\n")
    file.close()
    print("Example 1 - Closed:", file.closed)
    # Output: Example 1 - Closed: True

    # Exclusive creation protects existing contents.
    try:
        open(file_path, "x", encoding="utf-8")
    except FileExistsError:
        print("Example 2 - The file already exists; it was not overwritten.")
    # Output: Example 2 - The file already exists; it was not overwritten.

    # Append mode preserves the first line and adds another.
    file = open(file_path, "a", encoding="utf-8")
    file.write("Second note\n")
    file.close()

    file = open(file_path, "r", encoding="utf-8")
    contents = file.read()
    file.close()
    print("Example 3 - Contents:", repr(contents))
    # Output: Example 3 - Contents: 'First note\nSecond note\n'

    # Write mode replaces the old contents.
    file = open(file_path, "w", encoding="utf-8")
    file.write("Replacement note\n")
    file.close()

    file = open(file_path, "r", encoding="utf-8")
    print("Example 4 - After write mode:", repr(file.read()))
    file.close()
    # Output: Example 4 - After write mode: 'Replacement note\n'


# Quick review:
# - "r" reads, "w" writes from scratch, "a" appends, and "x" creates safely.
# - Closing a file releases its resources. The next lesson introduces "with".
