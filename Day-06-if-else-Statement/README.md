# Day 6 - if-else Statement 🐍

## 📚 Topics Learned

- `if-else` statement
- Decision making
- `else` statement
- Conditions
- Using `if-else` with numbers
- Using `if-else` with user input
- Indentation

## 🤔 What is `if-else`?

An `if-else` statement allows a program to choose between two possibilities.

If the condition is true, the `if` block runs.

If the condition is false, the `else` block runs.

Basic syntax:

```python
if condition:
    statement
else:
    statement
```

## 💻 Example

```python
age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

Since `20 >= 18` is true, the `if` block runs.

## 🔍 Even or Odd Example

```python
number = 7

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
```

Since the remainder is not `0`, the `else` block runs.

## ⌨️ Using `if-else` with User Input

```python
marks = int(input("Enter your marks: "))

if marks >= 40:
    print("You passed.")
else:
    print("You failed.")
```

## 🔄 Difference Between `if` and `if-else`

### `if`

The code runs only when the condition is true.

```python
if age >= 18:
    print("You can vote.")
```

### `if-else`

One of the two blocks will run.

```python
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")
```

## ⚠️ Important: Indentation

Python uses indentation to identify which statements belong to the `if` or `else` block.

```python
if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote yet.")
```

## 📝 Practice Tasks

Today I practiced:

- Checking positive and negative numbers
- Checking voting eligibility
- Checking even and odd numbers
- Checking passing marks
- Taking user input
- Making decisions using `if-else`

The solutions are available in [`tasks.py`](tasks.py).

## 📊 Data Science Connection

Decision-making is important when working with data.

`if-else` statements can be used to:

- Categorize data
- Apply conditions
- Check values
- Create rules
- Make decisions based on data

For example, a dataset could contain marks, and `if-else` logic could be used to classify students as pass or fail.

## 🎯 Progress

**Day 6 completed!** ✅

Today I learned how to use `if-else` to make Python programs choose between two possible outcomes.

Continuing to build my Python foundation for Data Science. 🚀
