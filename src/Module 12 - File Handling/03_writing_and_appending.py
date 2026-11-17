from pathlib import Path
from tempfile import TemporaryDirectory

# Module 12: File Handling
# Topic 3: Writing and appending
#
# write() writes one string. writelines() writes each string in an iterable
# exactly as given; neither method adds a newline automatically.


with TemporaryDirectory() as temporary_directory:
    file_path = Path(temporary_directory) / "journal.txt"

    # Example 1: Write a string; write() returns the number of characters.
    with open(file_path, "w", encoding="utf-8") as file:
        character_count = file.write("Day 1: Started learning.\n")
    print("Example 1 - Characters written:", character_count)
    # Output: Example 1 - Characters written: 25

    # Example 2: Append without replacing the first entry.
    with open(file_path, "a", encoding="utf-8") as file:
        file.write("Day 2: Practised files.\n")
    print("Example 2 - Appended text:", repr(file_path.read_text(encoding="utf-8")))
    # Output: Example 2 - Appended text: 'Day 1: Started learning.\nDay 2: Practised files.\n'

    # Example 3: writelines() does not insert separators or newlines.
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(["red", "green", "blue"])
    print("Example 3 - Without newlines:", repr(file_path.read_text(encoding="utf-8")))
    # Output: Example 3 - Without newlines: 'redgreenblue'

    # Example 4: Include newline characters to write separate lines.
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(["red\n", "green\n", "blue\n"])
    print("Example 4 - With newlines:", repr(file_path.read_text(encoding="utf-8")))
    # Output: Example 4 - With newlines: 'red\ngreen\nblue\n'


# Quick review:
# - "w" replaces the existing contents; "a" preserves them and adds at end.
# - Add line separators yourself when using write() or writelines().
