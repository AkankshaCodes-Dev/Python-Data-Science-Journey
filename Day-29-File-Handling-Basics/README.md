# Day 29 - File Handling Basics 📁🐍

## 📚 Topics Learned

- What is File Handling?
- Why File Handling is useful
- `open()`
- Opening files
- Reading files
- Writing files
- Appending files
- `read()`
- `readline()`
- `readlines()`
- `write()`
- `close()`
- `with open()`
- File modes
- `"r"` - Read
- `"w"` - Write
- `"a"` - Append
- File handling with functions
- File handling with lists
- Data Science connection

---

## 🤔 What is File Handling?

File Handling means using Python to work with files.

Python can be used to:

- Create files
- Read files
- Write data
- Add new data
- Store information
- Process stored data

File handling becomes important when we need to work with information stored outside our Python program.

---

## 🔓 Opening a File

Python uses the `open()` function to open a file.

### Syntax

```python
open("filename", "mode")
```

Example:

```python
file = open("student.txt", "r")
```

Here:

- `student.txt` is the file name
- `"r"` is the file mode

---

## 📌 File Modes

Python provides different modes for working with files.

### `"r"` - Read

Used to read an existing file.

```python
file = open("student.txt", "r")
```

---

### `"w"` - Write

Used to write data to a file.

```python
file = open("student.txt", "w")
file.write("Hello Python")
file.close()
```

Important:

`"w"` can overwrite existing content.

---

### `"a"` - Append

Used to add new content to the end of a file.

```python
file = open("student.txt", "a")
file.write("\nPython Data Science")
file.close()
```

---

## 📖 Reading a File

### `read()`

Reads the complete file.

```python
with open("student.txt", "r") as file:
    content = file.read()

print(content)
```

---

## 📄 `readline()`

Reads one line from a file.

```python
with open("student.txt", "r") as file:
    line = file.readline()

print(line)
```

---

## 📑 `readlines()`

Reads all lines and returns them as a list.

```python
with open("student.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

---

## ✍️ Writing to a File

The `write()` method is used to write content.

```python
with open("student.txt", "w") as file:
    file.write("Name: Akanksha")
```

Multiple lines can be written using `\n`.

```python
with open("student.txt", "w") as file:
    file.write("Name: Akanksha\n")
    file.write("Course: BCA\n")
    file.write("Goal: Data Scientist\n")
```

---

## ➕ Appending Data

Appending adds new content without replacing the existing content.

```python
with open("student.txt", "a") as file:
    file.write("Skill: Python\n")
```

---

## 🔒 Closing a File

When using `open()` directly, we can close the file using:

```python
file.close()
```

Example:

```python
file = open("student.txt", "r")

content = file.read()

file.close()

print(content)
```

---

## ⭐ Using `with open()`

A safer and cleaner way is:

```python
with open("student.txt", "r") as file:
    content = file.read()

print(content)
```

The `with` statement automatically handles closing the file.

This is the style we will prefer in our future Python programs.

---

## 🔄 File Handling with Functions

File handling can be combined with functions.

Example:

```python
def save_name(name):
    with open("name.txt", "w") as file:
        file.write(name)

save_name("Akanksha")
```

The function receives data and saves it into a file.

---

## 📋 File Handling with Lists

We can store list elements inside a file.

```python
students = ["Akanksha", "Rahul", "Priya"]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")
```

We can later read the names:

```python
with open("students.txt", "r") as file:
    students = file.readlines()

print(students)
```

---

## 🧹 Using `strip()`

When reading lines, we may get the newline character `\n`.

We can remove it using `strip()`.

```python
with open("students.txt", "r") as file:
    students = file.readlines()

students = [student.strip() for student in students]

print(students)
```

---

## 📊 Connection to Data Science

File handling is an important foundation for Data Science.

Data can be stored in files and later processed using Python.

Examples include:

- Reading text data
- Saving analysis results
- Storing information
- Working with CSV files
- Loading datasets
- Processing data from files

Later, we will learn libraries such as **Pandas**, which will make working with datasets much easier.

---

## 📝 Practice Tasks

1. Create and write to a file.
2. Read a file using `read()`.
3. Read one line using `readline()`.
4. Read all lines using `readlines()`.
5. Append new information.
6. Save a list into a file.
7. Read file data into a list.
8. Create functions for saving and reading data.
9. Read numbers from a file.
10. Calculate the sum of numbers stored in a file.

---

## 🎯 Day 29 Goal

By the end of Day 29, I should understand how to:

- Open a file
- Read a file
- Write to a file
- Append data
- Use different file modes
- Use `read()`
- Use `readline()`
- Use `readlines()`
- Use `write()`
- Use `close()`
- Use `with open()`
- Combine file handling with functions and lists

---

## 🚀 My Data Science Journey

I am learning Python step by step as part of my journey toward Data Science.

**Day 29 completed — File Handling Basics! 🐍📁**
