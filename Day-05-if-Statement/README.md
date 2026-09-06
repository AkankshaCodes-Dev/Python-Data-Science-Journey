# Day 5 - if Statement 🐍

## 📚 Topics Learned

- `if` statement
- Conditions
- Condition checking
- Indentation
- Comparison operators with `if`
- Using `if` with user input

## 🤔 What is an `if` Statement?

An `if` statement allows a Python program to execute some code only when a condition is true.

Basic syntax:

```python
if condition:
    statement
```

The code inside the `if` block must be indented.

## 💻 Example

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

Since `20 >= 18` is true, the message is printed.

## 🔍 Condition Checking

We can use comparison operators inside an `if` statement.

```python
number = 10

if number > 0:
    print("The number is positive.")
```

## ⌨️ Using `if` with User Input

```python
marks = int(input("Enter your marks: "))

if marks >= 40:
    print("You passed.")
```

## ⚠️ Important: Indentation

Python uses indentation to identify the code that belongs to the `if` statement.

Correct:

```python
if age >= 18:
    print("You are an adult.")
```

The `print()` statement is indented because it belongs to the `if` block.

## 📝 Practice Tasks

Today I practiced:

- Checking whether a number is positive
- Checking voting eligibility
- Comparing numbers
- Checking passing marks
- Using `if` with user input
- Checking whether a number is even

The solutions are available in [`tasks.py`](tasks.py).

## 📊 Data Science Connection

Conditional statements are important in Data Science because they allow programs to make decisions based on data.

For example, conditions can be used to:

- Check values
- Categorize data
- Identify specific records
- Apply rules to data
- Filter information

Learning `if` statements is an important step toward working with data using Python.

## 🎯 Progress

**Day 5 completed!** ✅

Today I learned how to use `if` statements to make Python programs check conditions and make decisions.

Continuing to build my Python foundation for Data Science. 🚀
