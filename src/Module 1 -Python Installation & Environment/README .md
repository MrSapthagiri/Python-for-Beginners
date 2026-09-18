# 🐍 Python Module 1 -- Installation & Environment

## Overview

This module covers the basic Python environment needed before starting
programming:

1.  Python introduction, features, use cases, and versions
2.  Python installation and environment setup
3.  VS Code setup, Python extension, and `.py` files
4.  Python interpreter, running programs, and `pip`
5.  Virtual environments and the first Python program

------------------------------------------------------------------------

# 1. Python Introduction

## What is Python?

Python is a high-level, general-purpose programming language known for
readable syntax and a large ecosystem.

### Key characteristics

-   High-level
-   Interpreted/runtime-executed
-   Dynamically typed
-   Object-oriented
-   Cross-platform
-   Open source
-   Large standard library
-   Large third-party package ecosystem

### Simple example

``` python
name = "Giri"
age = 30

print(name) 
print(age)
```

Python determines the type of the values automatically.

------------------------------------------------------------------------

# 2. Python Features

## 2.1 Simple Syntax

Python code is designed to be easy to read.

``` python
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

## 2.2 Readability

Python uses indentation to define code blocks.

``` python
for i in range(5):
    print(i)
```

## 2.3 Dynamic Typing

You do not normally declare a variable's type explicitly.

``` python
value = 100
value = "Python"
```

The name can refer to objects of different types at different times.

## 2.4 Cross-Platform

Python can run on Windows, Linux, and macOS when the required Python
version and dependencies are available.

## 2.5 Object-Oriented

Python supports:

-   Classes
-   Objects
-   Encapsulation
-   Inheritance
-   Polymorphism
-   Abstraction

## 2.6 Large Library Ecosystem

Examples:

-   `requests`
-   `pytest`
-   `selenium`
-   `playwright`
-   `pandas`
-   `numpy`

------------------------------------------------------------------------

# 3. Python Use Cases

Python is used in many areas.

## Testing and Automation

Common tools include:

-   Selenium
-   Playwright
-   PyTest
-   Requests

Example:

``` python
print("Automation test started")
```

## Web Development

Popular Python frameworks include:

-   Django
-   Flask
-   FastAPI

## Data Science

Common libraries include:

-   NumPy
-   Pandas
-   Matplotlib

## AI / Machine Learning

Python is widely used for:

-   Machine Learning
-   Deep Learning
-   NLP
-   Computer Vision
-   Generative AI

## Automation and Scripting

Python can automate repetitive tasks such as:

-   File processing
-   Data processing
-   Report generation
-   API calls

## DevOps

Python can be used for:

-   Automation scripts
-   CI/CD utilities
-   API automation
-   Cloud automation

------------------------------------------------------------------------

# 4. Python Versions

The major distinction to know is:

-   Python 2.x -- older generation
-   Python 3.x -- modern Python family

For new learning and development, use Python 3.

## Check the installed version

``` bash
python --version
```

On some systems:

``` bash
python3 --version
```

On Windows, you can also use:

``` bash
py --version
```

------------------------------------------------------------------------

# 5. Python Installation

## Installation Flow

``` text
Download Python
      ↓
Run Installer
      ↓
Configure PATH
      ↓
Install Python
      ↓
Open Terminal
      ↓
Verify Installation
```

Download Python from:

https://www.python.org/

## Windows

1.  Download the Python 3 installer.
2.  Run the installer.
3.  Add Python to PATH when appropriate.
4.  Complete the installation.
5.  Open Command Prompt or PowerShell.
6.  Verify:

``` bash
python --version
```

If `python` is not recognized, try:

``` bash
py --version
```

------------------------------------------------------------------------

# 6. What is PATH?

`PATH` is an operating-system environment variable containing
directories where executable programs can be found.

When you type:

``` bash
python
```

the operating system searches configured PATH locations for the Python
executable.

A PATH problem may produce an error such as:

``` text
'python' is not recognized...
```

------------------------------------------------------------------------

# 7. Python Interpreter

The Python interpreter/runtime executes Python programs.

Basic execution flow:

``` text
Python Source Code
       ↓
Python Runtime
       ↓
Program Execution
       ↓
Output
```

A `.py` file can be executed from the terminal:

``` bash
python hello.py
```

> Note: CPython normally compiles source into bytecode before executing
> it in its virtual machine. Python is commonly described as an
> interpreted language because the Python runtime executes the program
> rather than producing a traditional standalone native executable in
> the usual C/C++ workflow.

------------------------------------------------------------------------

# 8. Interactive Python Mode

Start Python:

``` bash
python
```

You may see:

``` text
>>>
```

The `>>>` prompt means Python is ready for commands.

Example:

``` python
>>> 10 + 20
30

>>> print("Hello Python")
Hello Python
```

Exit:

``` python
exit()
```

## Interactive Mode vs Script Mode

  Interactive Mode                 Script Mode
  -------------------------------- -------------------------------
  Commands entered one at a time   Code stored in a `.py` file
  Immediate output                 Program can be run repeatedly
  Good for experiments             Good for projects
  Uses `>>>` prompt                Uses source file

------------------------------------------------------------------------

# 9. VS Code Setup

## What is VS Code?

Visual Studio Code is a source-code editor that can be used to write,
run, and debug Python programs.

Download:

https://code.visualstudio.com/

## Install Python Extension

In VS Code:

``` text
Extensions
   ↓
Search: Python
   ↓
Install the Python extension
```

The extension provides Python development features such as:

-   Syntax support
-   IntelliSense
-   Debugging
-   Testing integration
-   Interpreter selection
-   Environment support

------------------------------------------------------------------------

# 10. Python `.py` Files

Python source files normally use the `.py` extension.

Examples:

``` text
hello.py
main.py
calculator.py
test_login.py
```

Example `hello.py`:

``` python
print("Hello Python")
```

Run:

``` bash
python hello.py
```

Output:

``` text
Hello Python
```

------------------------------------------------------------------------

# 11. Select Python Interpreter in VS Code

If multiple Python installations or virtual environments exist, VS Code
needs to use the correct interpreter.

Open the Command Palette and select:

``` text
Python: Select Interpreter
```

Then choose the required Python environment.

This matters because packages installed in one environment may not be
available in another.

------------------------------------------------------------------------

# 12. Running Python Programs

## From Terminal

``` bash
python main.py
```

If your system uses `python3`:

``` bash
python3 main.py
```

## From VS Code

Open the `.py` file and use the Python run option.

------------------------------------------------------------------------

# 13. What is pip?

`pip` is the standard Python package installer.

It is used to install and manage Python packages.

## Check pip

``` bash
pip --version
```

or:

``` bash
python -m pip --version
```

## Install a package

``` bash
python -m pip install requests
```

## Upgrade a package

``` bash
python -m pip install --upgrade requests
```

## Uninstall a package

``` bash
python -m pip uninstall requests
```

## List installed packages

``` bash
python -m pip list
```

## Show package information

``` bash
python -m pip show requests
```

------------------------------------------------------------------------

# 14. Why Use `python -m pip`?

When multiple Python installations exist, `pip` and `python` can
sometimes refer to different environments.

Using:

``` bash
python -m pip install requests
```

runs pip through the Python interpreter you invoked.

This helps make the relationship between the interpreter and package
installation explicit.

------------------------------------------------------------------------

# 15. Virtual Environment

A virtual environment is an isolated Python environment created for a
project.

Example:

``` text
Project A
   ↓
Virtual Environment A

Project B
   ↓
Virtual Environment B
```

Each project can have its own dependencies.

------------------------------------------------------------------------

# 16. Why Do We Need a Virtual Environment?

Imagine:

``` text
Project A → package version A
Project B → package version B
```

Installing everything globally can create dependency conflicts.

With virtual environments:

``` text
Project A
   └── venv
       └── Project A dependencies

Project B
   └── venv
       └── Project B dependencies
```

The environments are isolated.

------------------------------------------------------------------------

# 17. Create a Virtual Environment

Create a project folder:

``` text
PythonLearning/
```

Open the terminal in that folder.

Run:

``` bash
python -m venv .venv
```

Meaning:

-   `python` → invokes Python
-   `-m` → runs a Python module
-   `venv` → Python's virtual-environment module
-   final `venv` → name of the environment directory

You can also choose another name:

``` bash
python -m venv myenv
```

------------------------------------------------------------------------

# 18. Activate Virtual Environment

## Windows Command Prompt

``` cmd
venv\Scripts\activate
```

## Windows PowerShell

``` powershell
.\venv\Scripts\Activate.ps1
```

## Linux / macOS

``` bash
source venv/bin/activate
```

After activation, the terminal normally shows:

``` text
(venv)
```

------------------------------------------------------------------------

# 19. Deactivate Virtual Environment

Run:

``` bash
deactivate
```

The `(venv)` indicator should disappear.

------------------------------------------------------------------------

# 20. Install Packages Inside the Virtual Environment

First activate the environment.

Then:

``` bash
python -m pip install requests
```

Check:

``` bash
python -m pip list
```

------------------------------------------------------------------------

# 21. requirements.txt

`requirements.txt` is commonly used to record the packages required by a
project.

Create it from the active environment:

``` bash
python -m pip freeze > requirements.txt
```

Example:

``` text
requests==<version>
```

Install dependencies later with:

``` bash
python -m pip install -r requirements.txt
```

This helps other developers reproduce the project's dependencies.

------------------------------------------------------------------------

# 22. Recommended Basic Project Structure

``` text
PythonLearning/
│
├── venv/
│
├── module1/
│   ├── hello.py
│   ├── calculator.py
│   └── input_demo.py
│
└── requirements.txt
```

Do not place your application source code inside `venv`.

------------------------------------------------------------------------

# 23. First Python Program

Create:

``` text
hello.py
```

Add:

``` python
print("Hello Python!")
```

Run:

``` bash
python hello.py
```

Output:

``` text
Hello Python!
```

------------------------------------------------------------------------

# 24. First Practical Program

``` python
name = "Giri"
role = "Software Engineer"

print("Name:", name)
print("Role:", role)
```

Output:

``` text
Name: Giri
Role: Software Engineer
```

------------------------------------------------------------------------

# 25. Module 1 Important Commands

  Purpose                Command
  ---------------------- ---------------------------------------------
  Check Python           `python --version`
  Start Python           `python`
  Run file               `python main.py`
  Create venv            `python -m venv venv`
  Activate Windows CMD   `venv\Scripts\activate`
  Activate PowerShell    `.\venv\Scripts\Activate.ps1`
  Activate Linux/macOS   `source venv/bin/activate`
  Deactivate             `deactivate`
  Check pip              `python -m pip --version`
  Install package        `python -m pip install requests`
  Uninstall package      `python -m pip uninstall requests`
  List packages          `python -m pip list`
  Package details        `python -m pip show requests`
  Create requirements    `python -m pip freeze > requirements.txt`
  Install requirements   `python -m pip install -r requirements.txt`

------------------------------------------------------------------------
