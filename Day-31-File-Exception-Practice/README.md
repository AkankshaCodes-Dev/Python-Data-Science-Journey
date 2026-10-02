# Day 31 - File Handling Practice + Exception Handling Practice 🐍📁🛡️

## 📚 Topics Practiced

### File Handling
- `open()`
- `"r"`
- `"w"`
- `"a"`
- `read()`
- `readline()`
- `readlines()`
- `write()`
- `with open()`
- Reading and writing lists
- Reading and writing numbers

### Exception Handling
- `try`
- `except`
- `ValueError`
- `ZeroDivisionError`
- `FileNotFoundError`
- Handling multiple exceptions

### Combined Practice
- Files + exceptions
- Functions + files
- Functions + exceptions
- Reading and processing numbers
- Handling invalid data

---

## 📁 File Handling Revision

File handling allows Python to work with information stored in files.

### Write

```python
with open("data.txt", "w") as file:
    file.write("Hello Python")
```

### Read

```python
with open("data.txt", "r") as file:
    data = file.read()

print(data)
```

### Append

```python
with open("data.txt", "a") as file:
    file.write("\nNew data")
```

---

## 🛡️ Exception Handling Revision

Exception handling allows us to handle unexpected problems while a program is running.

Example:

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")
```

---

## 🔗 Combining Both

File handling and exception handling can be used together.

```python
try:
    with open("data.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("File not found.")
```

This prevents the program from crashing when the file does not exist.

---

## 🔢 Processing Data

We can read numbers from a file and process them.

```python
with open("numbers.txt", "r") as file:
    values = file.readlines()

numbers = [int(value.strip()) for value in values]

total = sum(numbers)
average = total / len(numbers)

print("Total:", total)
print("Average:", average)
```

---

## ⚠️ Handling Invalid Data

Real-world data may contain invalid values.

```python
values = ["10", "20", "abc", "30"]

numbers = []

for value in values:
    try:
        numbers.append(int(value))

    except ValueError:
        print("Skipping:", value)

print(numbers)
```

Output:

```text
Skipping: abc
[10, 20, 30]
```

---

## 📊 Data Science Connection

This practice is especially useful for Data Science because real-world data may not always be clean.

For example:

```text
10
20
abc
30
```

A data-processing program needs to handle invalid values instead of crashing.

File handling helps us access stored data, while exception handling helps us deal with unexpected problems.

Later, tools such as Pandas will provide more advanced ways to handle datasets and missing or invalid values.

---

## 📝 Practice Completed

I practiced:

- Creating files
- Writing data
- Reading data
- Appending data
- Reading lists
- Reading numbers
- Calculating total and average
- Handling missing files
- Handling invalid numbers
- Handling division by zero
- Combining files and exceptions
- Creating functions for file processing
- Processing data safely

---

## 🎯 Day 31 Goal

By the end of Day 31, I should be comfortable combining:

```text
Files
  ↓
Read data
  ↓
Process data
  ↓
Handle exceptions
  ↓
Produce results
```

This gives me a stronger foundation before moving to the next Python concepts.

---

## 🚀 Python → Data Science Journey

Day 31 completed — File Handling Practice + Exception Handling Practice! 🐍📁🛡️
