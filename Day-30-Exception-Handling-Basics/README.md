# Day 30 - Exception Handling Basics 🛡️🐍

## 📚 Topics Learned

- What is an error?
- What is an exception?
- Why exception handling is needed
- `try`
- `except`
- `ZeroDivisionError`
- `ValueError`
- `FileNotFoundError`
- Multiple exceptions
- `else`
- `finally`
- Exception handling with functions
- Exception handling with file handling
- Data Science connection

---

## ❓ What is an Error?

An error is a problem that prevents a program from running as expected.

Example:

```python
print(10 / 0)
```

This causes a division-by-zero error.

---

## ❓ What is Exception Handling?

Exception handling is a mechanism used to handle problems that occur while a program is running.

Instead of allowing the program to crash, we can handle the exception and provide a useful message.

---

## 🧪 What does `try` do?

The `try` block contains code that may cause an exception.

```python
try:
    number = 10 / 0
```

---

## 🛠️ What does `except` do?

The `except` block handles an exception that occurs inside the `try` block.

```python
try:
    number = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## ➗ Handling ZeroDivisionError

`ZeroDivisionError` occurs when we try to divide a number by zero.

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## 🔢 Handling ValueError

`ValueError` can occur when a value has the wrong format.

Example:

```python
try:
    number = int("hello")

except ValueError:
    print("Invalid number.")
```

---

## 👤 Handling User Input

```python
try:
    age = int(input("Enter your age: "))
    print("Age:", age)

except ValueError:
    print("Please enter a valid number.")
```

This prevents the program from stopping when the user enters something that cannot be converted to an integer.

---

## 🔀 Handling Multiple Exceptions

We can use multiple `except` blocks.

```python
try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## ➕ `else`

The `else` block runs when no exception occurs.

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("You entered:", number)
```

Flow:

```text
try
 ↓
Exception?
 ├── Yes → except
 └── No  → else
```

---

## 🔚 `finally`

The `finally` block runs whether an exception occurs or not.

```python
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

finally:
    print("Program completed.")
```

---

## 📁 File Handling + Exception Handling

Exception handling can also be used when working with files.

```python
try:
    with open("student.txt", "r") as file:
        content = file.read()

except FileNotFoundError:
    print("File not found.")
```

This prevents the program from crashing if the file does not exist.

---

## 🔧 Exception Handling with Functions

```python
def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero."


print(divide(10, 2))
print(divide(10, 0))
```

---

## 📊 Data Science Connection

Exception handling is useful in Data Science because real-world data is not always clean.

Data may contain:

- Missing values
- Invalid numbers
- Incorrect data types
- Unexpected input
- Missing files
- Incorrect file paths

Exception handling helps us deal with unexpected situations without immediately stopping the entire program.

Later, when working with datasets using Pandas and other tools, handling unexpected data situations will become important.

---

## 📝 Practice

I practiced:

- Handling division by zero
- Handling invalid number input
- Handling multiple exceptions
- Using `try`
- Using `except`
- Using `else`
- Using `finally`
- Handling missing files
- Using exception handling inside functions
- Processing values while handling invalid data

---

## 🎯 Day 30 Goal

By the end of Day 30, I should understand:

- What an error is
- What an exception is
- Why exception handling is useful
- How `try` works
- How `except` works
- How to handle `ValueError`
- How to handle `ZeroDivisionError`
- How to handle `FileNotFoundError`
- How `else` works
- How `finally` works
- How to combine exception handling with functions and file handling

---

## 🚀 Python → Data Science Journey

I am learning Python step by step as part of my journey toward Data Science.

**Day 30 completed — Exception Handling Basics! 🐍🛡️**
