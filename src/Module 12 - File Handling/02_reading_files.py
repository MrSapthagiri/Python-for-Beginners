"""Demonstrate read(), readline(), and readlines()."""

from pathlib import Path
from tempfile import TemporaryDirectory

# Module 12: File Handling
# Topic 2: Reading files
#
# read() returns text, readline() returns one line, and readlines() returns
# the remaining lines as a list. The file position advances after each read.


with TemporaryDirectory() as temporary_directory:
    file_path = Path(temporary_directory) / "poem.txt"
    file_path.write_text("Small steps\nmake progress\n", encoding="utf-8")

    # Example 1: Read all remaining text.
    with open(file_path, "r", encoding="utf-8") as file:
        contents = file.read()
    print("Example 1 - read():", repr(contents))
    # Output: Example 1 - read(): 'Small steps\nmake progress\n'

    # Example 2: Read one line at a time.
    with open(file_path, "r", encoding="utf-8") as file:
        first_line = file.readline()
        second_line = file.readline()
        end_of_file = file.readline()
    print("Example 2 - readline():", repr(first_line), repr(second_line))
    print("Example 2 - End of file:", repr(end_of_file))
    # Output: Example 2 - readline(): 'Small steps\n' 'make progress\n'
    # Output: Example 2 - End of file: ''

    # Example 3: Read all remaining lines into a list.
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    print("Example 3 - readlines():", lines)
    # Output: Example 3 - readlines(): ['Small steps\n', 'make progress\n']

    # Example 4: Read methods use the current file position.
    with open(file_path, "r", encoding="utf-8") as file:
        first_part = file.read(5)
        remaining_text = file.read()
    print("Example 4 - First part:", repr(first_part))
    print("Example 4 - Remaining:", repr(remaining_text))
    # Output: Example 4 - First part: 'Small'
    # Output: Example 4 - Remaining: ' steps\nmake progress\n'

    # Example 5: Iterate for line-by-line processing.
    with open(file_path, "r", encoding="utf-8") as file:
        line_count = sum(1 for _ in file)
    print("Example 5 - Number of lines:", line_count)
    # Output: Example 5 - Number of lines: 2


# Quick review:
# - read() and readlines() load all remaining data into memory by default.
# - Iterate over the file when processing a large text file.
# - readline() returns an empty string when there is no more text to read.
