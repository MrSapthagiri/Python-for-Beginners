# Module 13: Modules & Packages

## Module overview

As a Python program grows, keeping every instruction in one file becomes
difficult to understand and maintain. **Modules** and **packages** let you
organize code into reusable files and directories. Python also includes
standard-library modules for common tasks, while `pip` and virtual
environments help manage third-party packages separately for each project.

## Learning outcomes

After completing this module, you should be able to:

- Explain what a module is and use `import` and `from ... import`.
- Import selected names, use aliases, and avoid wildcard imports.
- Use `math`, `random`, and `datetime` for common tasks.
- Create a custom module and import its functions from another file.
- Recognize a package structure and import from a package.
- Create and activate a virtual environment.
- Install a third-party package with `pip` and record dependencies in
  `requirements.txt`.

## Important definitions

### Module

A **module** is a Python file, usually ending in `.py`, that contains code
such as functions, variables, and classes. For example, `math` is a
standard-library module, and a file named `calculator_tools.py` can be a
custom module.

### Package

A **package** organizes related modules in a directory. A regular package
normally contains an `__init__.py` file. Packages make imports easier to
organize when a project contains several related files.

### Standard library and third-party package

The **Python standard library** is included with Python; modules such as
`math`, `random`, and `datetime` do not need to be installed separately. A
**third-party package** is maintained outside the standard library and is
typically installed into the project's environment with `pip`.

## Topics and files

### 1. Modules, `import`, and `from ... import`

File: [`01_import_syntax.py`](01_import_syntax.py)

Use `import module_name` to access names through the module, or
`from module_name import name` to import selected names directly. An alias
can make a long name shorter or avoid a naming conflict:

```python
import math as mathematics
from math import sqrt as square_root

print(mathematics.pi)
print(square_root(81))
```

Prefer explicit imports. Avoid `from module_name import *` because it makes
it unclear where names came from and can overwrite other names.

Python searches for modules in locations such as the running script's
directory, the active environment's installed packages, and the standard
library. If an import fails, check the module name, project structure, and
which Python interpreter is running.

### 2. Built-in modules: `math`, `random`, and `datetime`

File: [`02_builtin_modules.py`](02_builtin_modules.py)

- `math` provides mathematical constants and functions such as `pi`,
  `sqrt()`, and `ceil()`.
- `random` provides pseudo-random choices and numbers, useful for games,
  simulations, and examples. It is **not** suitable for passwords, tokens,
  or other security-sensitive values; use the `secrets` module for those.
- `datetime` provides date and time types, parsing, and formatting. A
  formatted date is still text; use date/time objects when comparing dates.

All three modules are part of Python's standard library.

### 3. Creating and using custom modules

Files: [`03_custom_modules.py`](03_custom_modules.py) and
[`calculator_tools.py`](calculator_tools.py)

Place related reusable functions in a `.py` file, then import those
functions from another file in the same project. Keep the module name
lowercase and avoid names that collide with Python's standard library or
installed packages.

```python
from calculator_tools import add

print(add(8, 5))
```

Use the `if __name__ == "__main__":` guard for code that should run only when
a file is executed directly, not when it is imported. Importing a module
executes its top-level statements, so keep those statements limited to
definitions and safe initialization.

### 4. Packages and basic project structure

Files: [`04_packages_and_structure.py`](04_packages_and_structure.py),
[`course_utils/__init__.py`](course_utils/__init__.py), and
[`course_utils/text_tools.py`](course_utils/text_tools.py)

A simple project can keep its entry point, reusable module, and package
separate:

```text
student_project/
├── main.py
├── calculator_tools.py
├── course_utils/
│   ├── __init__.py
│   └── text_tools.py
├── requirements.txt
└── .venv/
```

The `.venv/` folder is generated locally and should not be committed to
version control. `__init__.py` marks a regular package and may expose selected
names as its public interface. For small projects, keep the structure
straightforward; add packages when they make related code easier to find.

### 5. `pip`, package installation, virtual environments, and
`requirements.txt`

File: [`05_virtual_environments_and_pip.py`](05_virtual_environments_and_pip.py)

A **virtual environment** is an isolated Python environment for one project.
It helps keep that project's installed packages separate from other
projects. Run `pip` through the intended interpreter with `python -m pip` so
the package is installed in the environment associated with that Python.

#### Create and activate a virtual environment

From the project directory on Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, `python` and `python -m pip` refer to the environment.
Confirm the selected interpreter if needed with `python --version` and
`python -c "import sys; print(sys.executable)"`. Leave the environment with
`deactivate`.

#### Install and record dependencies

Install a third-party package inside the activated environment:

```bash
python -m pip install package-name
```

For a small project, record its installed package versions in
`requirements.txt`:

```bash
python -m pip freeze > requirements.txt
```

Another computer can create its own environment and install those recorded
packages with:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

`pip freeze` records all installed distributions, including transitive
dependencies. For larger projects, use a dedicated dependency manager and
lockfile where appropriate. Do not copy a sample dependency list blindly;
record the packages the project actually uses.

#### Keep the environment out of source control

Add `.venv/` to `.gitignore`. Do not commit the environment's interpreter,
installed package files, or machine-specific paths. Share dependency
information, such as `requirements.txt`, instead.

## Good practices

- Prefer explicit imports and use aliases sparingly.
- Keep reusable functions in modules; avoid doing substantial work at import
  time.
- Use `if __name__ == "__main__":` to separate a module's runnable example
  from its reusable definitions.
- Prefer standard-library modules when they satisfy the need; no installation
  is required for them.
- Install third-party packages in the project's virtual environment, not
  globally.
- Use `python -m pip` with the Python interpreter you intend to run.
- Keep `.venv/` out of version control and share dependency declarations
  instead.

## Practice ideas

1. Import `sqrt` directly, then import `math` and call `math.sqrt()`.
2. Use `math.ceil()` and `math.floor()` on a decimal number.
3. Use `random.choice()` to select a game option; then identify why it should
   not generate a password.
4. Parse a date string with `datetime.strptime()` and display it with
   `strftime()`.
5. Add a function to `calculator_tools.py` and import it into another file.
6. Add a new function to the `course_utils` package and import it by its
   module path.
7. Create a virtual environment for a practice project and write down the
   commands to install and restore its dependencies.

## Running the examples

Run each lesson file with Python 3 from this directory. For example:

```bash
python 02_builtin_modules.py
```

The examples use only Python's standard library. The custom-module and
package lessons import the neighboring example files in this directory.
