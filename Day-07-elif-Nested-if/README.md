# Day 7 - elif, Nested if & Weekly Revision 🐍

## 📚 Topics Learned

- `elif`
- Multiple conditions
- `if-elif-else`
- Nested `if`
- Weekly revision
- Decision-making practice

## 🤔 What is `elif`?

`elif` means **else if**.

It allows us to check multiple conditions.

Basic syntax:

```python
if condition1:
    statement
elif condition2:
    statement
else:
    statement
```

Python checks the conditions from top to bottom and executes the first matching branch.

## 💻 Example

```python
marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")
```

Since `75 >= 70`, the program prints:

```text
Grade B
```

## 🔍 `if-else` vs `if-elif-else`

### `if-else`

Used when there are two possible outcomes.

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### `if-elif-else`

Used when there are multiple possible conditions.

```python
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
```

## 🪆 Nested `if`

A nested `if` means placing one `if` statement inside another `if` statement.

Example:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("You can enter.")
    else:
        print("ID is required.")
else:
    print("You are under 18.")
```

The inner `if` is checked only after the outer condition is true.

## 📝 Practice Tasks

Today I practiced:

- Creating a grade calculator
- Checking positive, negative, or zero
- Categorizing age
- Using nested `if`
- Checking even and odd numbers
- Finding the larger of two numbers
- Revising `if`
- Revising `if-else`
- Revising `elif`

The solutions are available in [`tasks.py`](tasks.py).

## 📊 Data Science Connection

Conditional logic is important when working with data.

It can be used to:

- Categorize data
- Apply rules
- Filter information
- Create labels
- Make decisions based on values

For example, numerical data can be divided into different categories using conditions.

## 🏆 WEEK 1 REVISION

During the first week, I learned:

### Day 1
- Python basics
- `print()`
- Comments

### Day 2
- Variables
- Data types
- `type()`

### Day 3
- Operators
- Arithmetic
- Comparison
- Logical operators

### Day 4
- `input()`
- Type conversion

### Day 5
- `if`

### Day 6
- `if-else`

### Day 7
- `elif`
- Nested `if`
- Weekly revision

## 🎯 Progress

**Day 7 completed!** ✅

I completed my first week of Python fundamentals.

I can now use variables, data types, operators, user input, and conditional statements to build basic decision-making programs.

One week completed in my Python journey toward Data Science. 🚀
