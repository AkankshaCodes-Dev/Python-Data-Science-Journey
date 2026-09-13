# Day 12 - Strings 🐍

## 📚 Topics Learned

- Strings
- Creating strings
- Single quotes and double quotes
- String indexing
- Positive indexing
- Negative indexing
- String slicing
- String length using `len()`
- Accessing individual characters
- Traversing strings using loops
- Strings are immutable
- String concatenation
- String repetition
- `in` operator
- `not in` operator
- Basic string operations

---

## 🤔 What is a String?

A **string** is a sequence of characters enclosed inside quotes.

Strings are used to store text such as:

- Names
- Cities
- Messages
- Email addresses
- Product names
- Descriptions

Example:

```python
name = "Akanksha"
city = "Ballari"

print(name)
print(city)
```

Output:

```text
Akanksha
Ballari
```

---

## ✍️ Creating Strings

Strings can be created using single quotes or double quotes.

### Single Quotes

```python
name = 'Akanksha'
print(name)
```

Output:

```text
Akanksha
```

### Double Quotes

```python
name = "Akanksha"
print(name)
```

Output:

```text
Akanksha
```

Both create a string.

---

## 🔢 String Indexing

Each character in a string has a position called an **index**.

Python starts indexing from `0`.

Example:

```python
name = "Python"

print(name[0])
print(name[1])
print(name[2])
```

Output:

```text
P
y
t
```

The indexes are:

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
```

So:

- `name[0]` → `P`
- `name[1]` → `y`
- `name[2]` → `t`

---

## 🔙 Negative Indexing

Python also supports negative indexing.

Negative indexing starts from the end of the string.

Example:

```python
name = "Python"

print(name[-1])
print(name[-2])
print(name[-3])
```

Output:

```text
n
o
h
```

The indexes are:

```text
 P   y   t   h   o   n
-6  -5  -4  -3  -2  -1
```

So:

- `name[-1]` → `n`
- `name[-2]` → `o`
- `name[-3]` → `h`

---

## ✂️ String Slicing

Slicing is used to extract a portion of a string.

### Syntax

```python
string[start:end]
```

The `start` index is included, but the `end` index is excluded.

Example:

```python
name = "Python"

print(name[0:3])
```

Output:

```text
Pyt
```

Indexes `0`, `1`, and `2` are included.

---

## 🔹 More Slicing Examples

```python
text = "Python Programming"

print(text[0:6])
print(text[7:18])
```

Output:

```text
Python
Programming
```

---

## 🔄 Slicing with Step

We can also provide a step value.

### Syntax

```python
string[start:end:step]
```

Example:

```python
text = "Python"

print(text[0:6:2])
```

Output:

```text
Pto
```

The program takes every second character.

---

## 📏 Finding String Length

The `len()` function is used to find the number of characters in a string.

Example:

```python
name = "Python"

print(len(name))
```

Output:

```text
6
```

Spaces are also counted as characters.

Example:

```python
text = "Hello World"

print(len(text))
```

Output:

```text
11
```

---

## 🔁 Traversing a String Using a `for` Loop

We can use a `for` loop to access every character in a string.

Example:

```python
name = "Python"

for char in name:
    print(char)
```

Output:

```text
P
y
t
h
o
n
```

This is called **traversing a string**.

---

## 🔒 Strings are Immutable

Strings in Python are **immutable**.

Immutable means that after creating a string, we cannot directly change an individual character.

Example:

```python
name = "Python"

name[0] = "J"
```

This produces an error because strings cannot be changed directly using indexing.

Instead, we can create a new string.

```python
name = "Python"

name = "J" + name[1:]

print(name)
```

Output:

```text
Jython
```

---

## ➕ String Concatenation

Concatenation means joining strings together.

We use the `+` operator.

Example:

```python
first_name = "Akanksha"
last_name = "Bodimi"

full_name = first_name + " " + last_name

print(full_name)
```

Output:

```text
Akanksha Bodimi
```

---

## 🔁 String Repetition

The `*` operator can be used to repeat a string.

Example:

```python
text = "Hi "

print(text * 3)
```

Output:

```text
Hi Hi Hi
```

---

## 🔍 `in` Operator

The `in` operator checks whether a character or sequence exists inside a string.

Example:

```python
name = "Python"

print("P" in name)
print("z" in name)
```

Output:

```text
True
False
```

---

## 🚫 `not in` Operator

The `not in` operator checks whether something does not exist inside a string.

Example:

```python
name = "Python"

print("z" not in name)
print("P" not in name)
```

Output:

```text
True
False
```

---

## 🧠 Important Points

- A string stores text.
- Strings are written inside quotes.
- Python supports single quotes and double quotes.
- String indexing starts from `0`.
- Negative indexing starts from `-1`.
- Slicing is used to extract part of a string.
- The `start` index is included in slicing.
- The `end` index is excluded in slicing.
- `len()` returns the number of characters.
- Spaces are also counted by `len()`.
- Strings can be traversed using loops.
- Strings are immutable.
- `+` is used for string concatenation.
- `*` is used for string repetition.
- `in` checks whether something exists in a string.
- `not in` checks whether something does not exist in a string.

---

## 🌍 Real-World / Data Science Connection

Strings are extremely important in **Data Science**.

Real-world datasets contain a lot of text data.

For example:

```python
customer_name = "Akanksha"
city = "Ballari"
product = "Laptop"
```

In Data Science, strings are commonly used for:

- Customer names
- City names
- Product names
- Categories
- Email addresses
- Reviews
- Comments
- Text data
- CSV column values

Later, when working with **Pandas**, we will clean and analyze large amounts of string data.

For example, a dataset may contain:

```text
"  Akanksha  "
"akanksha"
"AKANKSHA"
```

We will learn how to clean and transform this type of data.

So understanding strings properly is an important foundation for Data Science.



---

## 🐍 Python → Data Science Journey

Day 12 completed! 🎉

I am building my Python fundamentals step by step before moving deeper into Data Science.

