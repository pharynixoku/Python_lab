# PYTHON PROJECT SETUP, GIT, AND GITHUB WORKFLOW

**Name:** Simon Ohure
**Project:** Python Lab
**GitHub Repository:** `python-lab`

---

# Part A – Project Setup Using the CLI

## A1. Create the Python Lab Directory

First, I created a new directory called `python_lab` in my home directory and moved into it.

### Command

```bash
mkdir ~/python_lab
cd ~/python_lab
```

### Explanation

The `mkdir` command creates a new directory. The `~` represents my home directory. The `cd` command changes the current working directory, allowing me to work inside the newly created `python_lab` directory.

---

## A2. Create the Project Subdirectories

Inside `python_lab`, I created three subdirectories: `src`, `tests`, and `docs`.

### Command

```bash
mkdir src tests docs
```

### Explanation

The `mkdir` command creates directories. In this command, three directories are created at the same time: `src` for source code, `tests` for testing files, and `docs` for project documentation.

---

## A3. Create the Python Files

Inside the `src` directory, I created three empty Python files: `main.py`, `utils.py`, and `config.py`.

### Command

```bash
touch src/main.py src/utils.py src/config.py
```

### Explanation

The `touch` command creates empty files. The three Python files are placed inside the `src` directory.

---

## A4. Create the README File

Inside the `docs` directory, I created `README.md` and wrote the required text using output redirection.

### Command

```bash
echo "My Python Lab Project" > docs/README.md
```

### Explanation

The `echo` command displays text, while `>` redirects the text into a file. This command creates `README.md` inside the `docs` directory and writes `My Python Lab Project` as its content. It does not require opening a text editor.

---

## A5. Display the Directory Tree

To display all folders and files recursively, I used:

```bash
find . -print
```

### Expected Output

The output should look similar to:

```text
.
./src
./src/main.py
./src/utils.py
./src/config.py
./tests
./docs
./docs/README.md
```

### Screenshot Required

**Screenshot 1 – Recursive Directory Listing**

Take a screenshot showing the terminal with the `find . -print` command and its output.

The screenshot should clearly show:

```text
python_lab
├── src
│   ├── main.py
│   ├── utils.py
│   └── config.py
├── tests
└── docs
    └── README.md
```

---

## A6. Why the Project Structure Is Good Practice

The commands used in this section create the project structure and files needed for the Python project. `mkdir` creates directories, `cd` moves into a directory, `touch` creates empty files, `echo` writes text, `>` redirects output to a file, and `find` displays the directory structure recursively.

Separating the project into `src`, `tests`, and `docs` is good practice because it keeps different types of project files organized. The `src` directory contains the application code, `tests` is reserved for testing the code, and `docs` contains documentation. Even for a small project, this structure makes the project easier to understand, maintain, test, and expand in the future.

---

# Part B – Git Initialization and First Commit

## B1. Initialize the Git Repository

While inside the `python_lab` directory, I initialized a new Git repository.

### Command

```bash
git init
```

### Expected Output

The output should be similar to:

```text
Initialized empty Git repository in .../python_lab/.git/
```

### Explanation

The `git init` command creates a new Git repository in the current project directory. Git can now track changes made to the project files.

---

## B2. Create the `.gitignore` File

I created a `.gitignore` file in the project root and added three entries.

### Command

```bash
printf "__pycache__/\n*.pyc\n.env\n" > .gitignore
```

### Explanation

The `printf` command writes the specified lines into `.gitignore`.

The file contains:

```text
__pycache__/
*.pyc
.env
```

### Explanation of the Entries

`__pycache__/` tells Git to ignore Python cache directories.

`*.pyc` tells Git to ignore compiled Python files ending in `.pyc`.

`.env` tells Git to ignore environment files, which may contain configuration information or sensitive values such as passwords, API keys, or other secrets.

---

## B3. Check the `.gitignore` File

### Command

```bash
cat .gitignore
```

### Expected Output

```text
__pycache__/
*.pyc
.env
```

---

## B4. Stage All Project Files

### Command

```bash
git add .
```

### Explanation

The `git add .` command stages all files in the current project that are not excluded by `.gitignore`. Staging prepares the files to be included in the next commit.

---

## B5. Check the Staging Area

### Command

```bash
git status
```

### Expected Output

The output should show the files that are ready to be committed.

It should look similar to:

```text
On branch master

Changes to be committed:
  new file:   .gitignore
  new file:   docs/README.md
  new file:   src/config.py
  new file:   src/main.py
  new file:   src/utils.py
```

The exact output may differ depending on the Git version and branch name.

---

## B6. Make the First Commit

### Command

```bash
git commit -m "Set up initial Python lab project structure"
```

### Explanation

The `git commit` command permanently records the staged changes in Git's project history.

The message:

```text
Set up initial Python lab project structure
```

clearly describes what was added.

---

## B7. Display the Commit History

### Command

```bash
git log --oneline
```

### Expected Output

The output should look similar to:

```text
a1b2c3d Set up initial Python lab project structure
```

The first part is the commit ID, while the text after it is the commit message.

### Screenshot Required

**Screenshot 2 – First Commit History**

Take a screenshot showing:

```bash
git log --oneline
```

and the first commit with the message:

```text
Set up initial Python lab project structure
```

---

## B8. What `.gitignore` Does

The `.gitignore` file tells Git which files and directories should not be tracked or committed to the repository. In this project, `__pycache__/` and `*.pyc` are ignored because they are generated Python cache files and do not need to be stored in the source code repository. The `.env` file is also ignored because it may contain private configuration information such as passwords, tokens, or API keys.

---

## B9. What the Commit History Shows

The Git commit history shows how a project changes over time. Each commit contains information such as the commit ID, author, date, and commit message. By reviewing the history, developers can understand what changes were made, when they were made, and why they were made. This also makes it possible to return to an earlier version of the project when necessary.

---

# Part C – Writing and Committing Python Code

## C1. Create the `square()` Function

The first function calculates the square of a number.

### Function

```python
def square(n):
    return n ** 2
```

For example:

```text
square(5) = 25
```

---

## C2. Create the `is_even()` Function

The second function checks whether a number is even.

### Function

```python
def is_even(n):
    return n % 2 == 0
```

The `%` operator calculates the remainder after division.

For example:

```text
10 % 2 = 0
```

Therefore, 10 is even.

---

## C3. Create the `celsius_to_fahrenheit()` Function

The third function converts Celsius to Fahrenheit.

The required formula is:

```text
F = (C × 9/5) + 32
```

### Function

```python
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
```

---

# C4. Complete `utils.py`

Open:

```text
src/utils.py
```

and add the following code:

```python
def square(n):
    """Return the square of a number."""
    return n ** 2


def is_even(n):
    """Return True if the number is even, otherwise False."""
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32
```

---

# C5. Complete `main.py`

Open:

```text
src/main.py
```

and add:

```python
from utils import square, is_even, celsius_to_fahrenheit


def main():
    number = float(input("Enter a number: "))

    print("Square:", square(number))

    if is_even(number):
        print("The number is even.")
    else:
        print("The number is odd.")

    print("Fahrenheit equivalent:", celsius_to_fahrenheit(number))


if __name__ == "__main__":
    main()
```

---

# C6. How `main.py` Connects to `utils.py`

The connection between the two files is made using Python's import system.

At the top of `main.py`, the following line is used:

```python
from utils import square, is_even, celsius_to_fahrenheit
```

This tells Python to import the three functions from the `utils.py` module.

The functions are defined in `utils.py`, while `main.py` uses those functions to interact with the user.

The structure is:

```text
src/
├── main.py
├── utils.py
└── config.py
```

The relationship can be represented as:

```text
utils.py
   │
   ├── square()
   ├── is_even()
   └── celsius_to_fahrenheit()
   │
   ↓
main.py
   │
   └── imports and uses the functions
```

This separation makes the program easier to organize because the reusable functions are kept in one module while the main program handles user interaction.

---

# C7. Run the Python Program

Make sure you are inside the project root:

```bash
cd ~/python_lab
```

Then run:

```bash
python src/main.py
```

---

# C8. Test 1

Enter:

```text
5
```

### Sample Output

```text
Enter a number: 5
Square: 25.0
The number is odd.
Fahrenheit equivalent: 41.0
```

---

# C9. Test 2

Run the program again:

```bash
python src/main.py
```

Enter:

```text
10
```

### Sample Output

```text
Enter a number: 10
Square: 100.0
The number is even.
Fahrenheit equivalent: 50.0
```

---

# C10. Test 3

Run the program again:

```bash
python src/main.py
```

Enter:

```text
20
```

### Sample Output

```text
Enter a number: 20
Square: 400.0
The number is even.
Fahrenheit equivalent: 68.0
```

---

## C11. Test Summary

I tested the program using three different input values: `5`, `10`, and `20`.

| Input | Square | Result | Fahrenheit |
| ----: | -----: | ------ | ---------: |
|     5 |     25 | Odd    |       41°F |
|    10 |    100 | Even   |       50°F |
|    20 |    400 | Even   |       68°F |

The program produced the expected results for all three test values.

---

# C12. Stage the Python Changes

After confirming that the program works correctly, I staged the changes.

### Command

```bash
git add src/main.py src/utils.py
```

---

# C13. Check Git Status

### Command

```bash
git status
```

The output should show that `src/main.py` and `src/utils.py` are ready to be committed.

---

# C14. Commit the Python Code

### Command

```bash
git commit -m "Add reusable Python utility functions"
```

### Explanation

This commit records the new Python functions and the main program. The commit message clearly describes the change.

---

# Part D – Publishing to GitHub and Branch Workflow

## D1. Create the GitHub Repository

I created a new **public** repository on GitHub.

### Repository Name

```text
python-lab
```

### Important Settings

When creating the repository:

* Repository name: `python-lab`
* Visibility: **Public**
* Do not add a README.
* Do not add a `.gitignore`.
* Do not add a license.

The local project already contains the required files.

---

# D2. Connect the Local Repository to GitHub

After creating the GitHub repository, copy its HTTPS repository address.

It will look similar to:

```text
https://github.com/YOUR-USERNAME/python-lab.git
```

Replace `YOUR-USERNAME` with your actual GitHub username.

### Command

```bash
git remote add origin https://github.com/YOUR-USERNAME/python-lab.git
```

For example, if your GitHub username were `simonohure`:

```bash
git remote add origin https://github.com/simonohure/python-lab.git
```

**Use your actual GitHub username.**

---

# D3. Rename the Local Branch to `main`

Use:

```bash
git branch -M main
```

### Explanation

This changes the current branch name to `main`, which will be the main branch of the GitHub repository.

---

# D4. Push the Project to GitHub

### Command

```bash
git push -u origin main
```

### Explanation

The `git push` command uploads the local commits to the GitHub repository.

`origin` represents the GitHub remote repository.

`main` is the branch being pushed.

The `-u` option sets the upstream relationship so future pushes can be made more easily.

---

# D5. Verify the GitHub Repository

Open your GitHub repository in a web browser.

The repository should contain the project structure:

```text
python-lab/
│
├── .gitignore
│
├── docs/
│   └── README.md
│
├── src/
│   ├── config.py
│   ├── main.py
│   └── utils.py
│
└── tests/
```

The GitHub repository should also show the commit history.

### Screenshot Required

**Screenshot 3 – GitHub Repository**

Take a screenshot of the GitHub repository page showing:

* Repository name `python-lab`
* Public repository
* Project files
* Folders
* Commit information

---

# D6. Create a Feature Branch

Create a new branch called:

```text
feature/add-greeting
```

### Command

```bash
git checkout -b feature/add-greeting
```

### Explanation

This command creates a new branch and immediately switches to it.

The feature branch allows me to work on the greeting feature without changing the `main` branch directly.

---

# D7. Add the `greet()` Function

Open:

```text
src/utils.py
```

Add this function below the existing functions:

```python
def greet(name):
    """Return a personalized greeting."""
    return f"Hello, {name}! Welcome to the Python Lab."
```

The complete `utils.py` should now be:

```python
def square(n):
    """Return the square of a number."""
    return n ** 2


def is_even(n):
    """Return True if the number is even, otherwise False."""
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32


def greet(name):
    """Return a personalized greeting."""
    return f"Hello, {name}! Welcome to the Python Lab."
```

---

# D8. Update `main.py`

Open:

```text
src/main.py
```

Change the import line to:

```python
from utils import square, is_even, celsius_to_fahrenheit, greet
```

Then update the complete program to:

```python
from utils import square, is_even, celsius_to_fahrenheit, greet


def main():
    name = input("Enter your name: ")
    print(greet(name))

    number = float(input("Enter a number: "))

    print("Square:", square(number))

    if is_even(number):
        print("The number is even.")
    else:
        print("The number is odd.")

    print("Fahrenheit equivalent:", celsius_to_fahrenheit(number))


if __name__ == "__main__":
    main()
```

---

# D9. Test the Greeting Feature

Run:

```bash
python src/main.py
```

### Sample Output

```text
Enter your name: Simon
Hello, Simon! Welcome to the Python Lab.
Enter a number: 10
Square: 100.0
The number is even.
Fahrenheit equivalent: 50.0
```

This confirms that the new `greet()` function is imported from `utils.py` and called from `main.py`.

---

# D10. Stage the Changes

### Command

```bash
git add src/main.py src/utils.py
```

---

# D11. Commit the Greeting Feature

### Command

```bash
git commit -m "Add personalized greeting feature"
```

### Explanation

This commit records the new greeting functionality. The message clearly describes the feature that was added.

---

# D12. Push the Feature Branch to GitHub

### Command

```bash
git push -u origin feature/add-greeting
```

### Explanation

This uploads the new feature branch and its commit to GitHub.

---

# D13. Open a Pull Request

After pushing the branch:

1. Open the `python-lab` repository on GitHub.
2. GitHub may display a message about the recently pushed branch.
3. Select **Compare & pull request**.
4. Set the base branch to `main`.
5. Set the compare branch to `feature/add-greeting`.
6. Enter a title such as:

```text
Add personalized greeting feature
```

7. Add a short description explaining that the branch adds the `greet(name)` function and uses it in `main.py`.
8. Select **Create pull request**.

The pull request should show:

```text
base: main
        ←
compare: feature/add-greeting
```

### Screenshot Required

**Screenshot 4 – Pull Request**

Take a screenshot showing the open pull request.

The screenshot should clearly show:

```text
feature/add-greeting → main
```

and the pull request title.

---

# FINAL PROJECT STRUCTURE

After completing all parts, the local project should have the following structure:

```text
python_lab/
│
├── .git/
│
├── .gitignore
│
├── docs/
│   └── README.md
│
├── src/
│   ├── config.py
│   ├── main.py
│   └── utils.py
│
└── tests/
```

The GitHub repository should be named:

```text
python-lab
```

---

# FINAL `utils.py` CODE

```python
def square(n):
    """Return the square of a number."""
    return n ** 2


def is_even(n):
    """Return True if the number is even, otherwise False."""
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32


def greet(name):
    """Return a personalized greeting."""
    return f"Hello, {name}! Welcome to the Python Lab."
```

---

# FINAL `main.py` CODE

```python
from utils import square, is_even, celsius_to_fahrenheit, greet


def main():
    name = input("Enter your name: ")
    print(greet(name))

    number = float(input("Enter a number: "))

    print("Square:", square(number))

    if is_even(number):
        print("The number is even.")
    else:
        print("The number is odd.")

    print("Fahrenheit equivalent:", celsius_to_fahrenheit(number))


if __name__ == "__main__":
    main()
```

---

# `.gitignore` CONTENT

```text
__pycache__/
*.pyc
.env
```

---

# `docs/README.md` CONTENT

```text
My Python Lab Project
```

---

# GIT COMMAND SUMMARY

The main Git commands used in this project were:

```bash
git init
```

Initializes a new Git repository.

```bash
git add .
```

Stages project files for a commit.

```bash
git status
```

Shows the current Git status and staged files.

```bash
git commit -m "Set up initial Python lab project structure"
```

Creates a commit.

```bash
git log --oneline
```

Displays the commit history.

```bash
git remote add origin https://github.com/YOUR-USERNAME/python-lab.git
```

Connects the local repository to GitHub.

```bash
git branch -M main
```

Renames the current branch to `main`.

```bash
git push -u origin main
```

Pushes the main branch to GitHub.

```bash
git checkout -b feature/add-greeting
```

Creates and switches to the feature branch.

```bash
git push -u origin feature/add-greeting
```

Pushes the feature branch to GitHub.

---

# SCREENSHOT CHECKLIST

The assignment requires the following screenshots:

### Screenshot 1 – Directory Structure

Show:

```bash
find . -print
```

The screenshot must show:

```text
src/
    main.py
    utils.py
    config.py
tests/
docs/
    README.md
```

### Screenshot 2 – First Commit

Show:

```bash
git log --oneline
```

The screenshot must show:

```text
Set up initial Python lab project structure
```

### Screenshot 3 – GitHub Repository

Show the public `python-lab` repository with the project files and commit history.

### Screenshot 4 – Pull Request

Show the open pull request:

```text
feature/add-greeting → main
```

---

# CONCLUSION

In this project, I created a Python project structure using the command-line interface and organized the project into `src`, `tests`, and `docs` directories. I initialized the project as a Git repository, created a `.gitignore` file, staged the files, and made the first commit.

I then developed reusable Python functions for calculating a square, checking whether a number is even, and converting Celsius to Fahrenheit. I connected these functions to `main.py` using Python's import system and tested the program using three different input values.

Finally, I created a public GitHub repository named `python-lab`, connected the local repository to GitHub, pushed the project to the `main` branch, created a `feature/add-greeting` branch, added a personalized greeting function, committed and pushed the changes, and opened a pull request from the feature branch into `main`.

This exercise helped me practice command-line project setup, Python programming, Git version control, GitHub collaboration, branching, commits, and pull requests.
