# Module 12: File Handling

## Module overview

Programs often need to keep information after they stop running. **File
handling** lets a Python program create files, read saved information, and
write updated information. This module covers ordinary text files and
comma-separated values (CSV) files.

## Learning outcomes

After completing this module, you should be able to:

- Open and close a file and explain why it is important to close it.
- Choose a file mode for reading, writing, appending, or creating a file.
- Read all text, one line, or a list of lines using `read()`, `readline()`,
  and `readlines()`.
- Write text with `write()` and multiple strings with `writelines()`.
- Use `with open(...)` to close files reliably.
- Handle common file exceptions without hiding unrelated programming errors.
- Read and write basic text and CSV data with the standard library.

## Important definitions

### File path

A **file path** identifies where a file is stored. A relative path such as
`"notes.txt"` is interpreted from the program's current working directory,
which may not be the same directory as the Python script. Use an absolute
path or a path built with `pathlib.Path` when a specific location is needed.

### File object

Calling `open()` returns a **file object**. The object provides methods such
as `read()`, `write()`, and `close()`. After a file is closed, it should not
be used for reading or writing.

```python
file = open("notes.txt", "w", encoding="utf-8")
file.write("Remember to practise.\n")
file.close()
```

For normal code, prefer `with open(...)` (covered in topic 4) so the file is
closed even if an exception occurs.

### File modes

The mode passed to `open(path, mode)` controls what the program may do:

| Mode | Purpose | If the file does not exist | If the file already exists |
|---|---|---|---|
| `"r"` | Read text (default mode) | Raises `FileNotFoundError` | Reads the existing file |
| `"w"` | Write text | Creates the file | Truncates it first |
| `"a"` | Append text at the end | Creates the file | Preserves existing contents |
| `"x"` | Create a new text file | Creates the file | Raises `FileExistsError` |
| `"b"` | Add to a mode for binary data, such as `"rb"` | Depends on the other mode | Depends on the other mode |
| `"+"` | Add reading and writing to a mode, such as `"r+"` | Depends on the other mode | Depends on the other mode |

Use `"w"` carefully: it replaces the previous contents. Use `"a"` when
existing contents must be preserved. Text mode is the default; specify
`encoding="utf-8"` for predictable text decoding and encoding.

## Topics and files

### 1. File creation, opening, closing, and modes

File: [`01_file_creation_and_modes.py`](01_file_creation_and_modes.py)

Use `open()` to get a file object and `close()` to release it. `"x"` is useful
when overwriting an existing file would be a mistake; `"w"` creates or
replaces; `"a"` creates or adds to the end. The lesson uses a temporary
directory so running it does not leave sample files in the course folder.

### 2. Reading files

File: [`02_reading_files.py`](02_reading_files.py)

- `read()` returns the remaining file contents as one string. With no size
  argument it reads to the end, which may use substantial memory for a large
  file.
- `readline()` reads one line at a time. A returned line normally includes
  its newline character if it had one.
- `readlines()` returns all remaining lines as a list of strings. Like
  `read()`, it loads the remaining contents into memory.
- A file's read position advances, so calling a read method again may return
  only what remains. Reopen the file or use `seek(0)` to return to the start.

For very large files, iterate over the file object instead of loading every
line at once:

```python
with open("large_log.txt", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

### 3. Writing and appending

File: [`03_writing_and_appending.py`](03_writing_and_appending.py)

- `write(text)` writes a string and returns the number of characters written.
- `writelines(strings)` writes each string in an iterable, but does **not**
  add newline characters. Include `"\n"` in each string when separate lines
  are wanted.
- `"w"` overwrites; `"a"` appends. Open the file in the correct mode for the
  intended result.

### 4. `with open()` and file exception handling

File: [`04_with_open_and_exceptions.py`](04_with_open_and_exceptions.py)

The `with` statement manages the file object's lifetime and closes it when
the indented block ends, including when an exception is raised. Handle
specific exceptions when the program can give a useful response:

| Exception | Typical file-related cause |
|---|---|
| `FileNotFoundError` | A file opened for reading does not exist at that path. |
| `PermissionError` | The program does not have permission for the operation. |
| `FileExistsError` | Exclusive creation with `"x"` targets an existing file. |
| `IsADirectoryError` | A file operation was attempted on a directory path. |
| `UnicodeDecodeError` | The bytes do not decode using the selected text encoding. |
| `OSError` | A broader operating-system file or device failure. |

Catch only errors you know how to handle. Avoid a bare `except:` or a broad
handler that silently hides mistakes.

### 5. Basic text and CSV file handling

File: [`05_text_and_csv_files.py`](05_text_and_csv_files.py)

Text files store characters and are read or written with text methods such as
`read()` and `write()`. CSV files store tabular data as rows and columns. Use
Python's built-in `csv` module rather than splitting lines on commas: a CSV
field can itself contain a comma, a quote, or a newline.

When opening a CSV file, use `newline=""` so the `csv` module can handle
newline conventions correctly. `csv.reader` and `csv.writer` work with
sequences; `csv.DictReader` and `csv.DictWriter` work with column names.
Values read from a CSV file are strings unless the program converts them.

```python
import csv

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        print(row["name"], row["score"])
```

## Good practices

- Specify an encoding, usually `"utf-8"`, when opening text files.
- Prefer `with open(...)` over manual `open()` and `close()` in application
  code.
- Remember that `"w"` erases existing contents; choose `"a"` to add at the
  end.
- Use `pathlib.Path` to build paths rather than manually joining path
  separators.
- Use `csv` for CSV data; simple `split(",")` is not a correct general CSV
  parser.
- Catch expected exceptions specifically and report what the program could
  not do.
- For large files, process one line at a time instead of reading everything
  into memory.

## Practice ideas

1. Create a file with `"x"`, then run the creation again and observe
   `FileExistsError`.
2. Change a lesson's mode from `"w"` to `"a"` and compare the file contents.
3. Use `readline()` repeatedly and observe when it returns an empty string.
4. Write several lines with `writelines()`; then add `"\n"` to each string
   and compare the result.
5. Try opening a missing file and handle `FileNotFoundError`.
6. Write CSV rows containing a comma inside a field and read them back.
7. Convert a numeric CSV field from text to `int` before calculating with it.

## Running the examples

Run each lesson file with Python 3 from this directory. For example:

```bash
python 02_reading_files.py
```

The examples use temporary directories and clean them up automatically.
