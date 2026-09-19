# Day 18 - Tuple Methods + Tuple Unpacking 🐍

## 📚 Topics Learned

Today I continued learning about Python Tuples.

- `count()`
- `index()`
- Difference between List methods and Tuple methods
- Why Tuples have fewer methods
- Tuple unpacking
- Assigning Tuple values to variables
- Accessing unpacked values

---

## 🔢 `count()`

The `count()` method tells us how many times a particular value appears in a Tuple.

Example:

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))
```

Output:

```text
3
```

The number `10` appears three times.

### Simple meaning:

```text
count() → Count how many times a value appears
```

---

## 🔎 `index()`

The `index()` method returns the position of the first occurrence of a value in a Tuple.

Example:

```python
fruits = ("Apple", "Banana", "Mango")

print(fruits.index("Banana"))
```

Output:

```text
1
```

`"Banana"` is at index `1`.

### Simple meaning:

```text
index() → Find the position of a value
```

---

## 📋 Tuple Methods

Tuples have only a small number of built-in methods.

The two commonly used Tuple methods are:

```text
count()
index()
```

This is because Tuples are **immutable**.

We cannot directly add, remove, or change elements inside a Tuple.

---

## 🔍 List Methods vs Tuple Methods

Lists have many methods because Lists are mutable.

For example, Lists support:

```text
append()
insert()
remove()
pop()
sort()
reverse()
clear()
index()
count()
```

Tuples mainly provide:

```text
count()
index()
```

### Why?

A List can be changed:

```python
numbers = [10, 20, 30]

numbers.append(40)
```

A Tuple cannot be changed:

```python
numbers = (10, 20, 30)

# numbers.append(40)   # Error
```

So Tuples have fewer methods because their elements cannot be modified.

---

## 📦 What is Tuple Unpacking?

Tuple unpacking means assigning the values inside a Tuple to separate variables.

Example:

```python
student = ("Akanksha", 20, "BCA")

name, age, course = student

print(name)
print(age)
print(course)
```

Output:

```text
Akanksha
20
BCA
```

Here:

```text
name   → "Akanksha"
age    → 20
course → "BCA"
```

The values from the Tuple are assigned to the variables in the same order.

---

## 🧩 Another Example of Tuple Unpacking

```python
marks = (85, 90, 78)

maths, science, english = marks

print("Maths:", maths)
print("Science:", science)
print("English:", english)
```

Output:

```text
Maths: 85
Science: 90
English: 78
```

The first value goes to the first variable, the second value goes to the second variable, and so on.

---

## ⚠️ Important Rule of Tuple Unpacking

The number of variables should normally match the number of values.

For example:

```python
student = ("Akanksha", 20, "BCA")

name, age, course = student
```

There are:

```text
3 values
3 variables
```

So the unpacking works correctly.

If the number does not match, Python will produce an error.

---

## 🔗 Tuple Unpacking with Different Data Types

A Tuple can contain different data types.

Example:

```python
data = ("Akanksha", 85.5, True)

name, score, passed = data

print(name)
print(score)
print(passed)
```

Output:

```text
Akanksha
85.5
True
```

Tuple unpacking works regardless of the data types.

---

## 📝 Practice Tasks

Today I practiced:

- Counting repeated values using `count()`
- Finding the position of a value using `index()`
- Creating a student Tuple
- Unpacking a student Tuple
- Creating a marks Tuple
- Unpacking marks into separate variables
- Working with repeated Tuple values
- Finding the position of a value

The solutions are available in [`tasks.py`](tasks.py).

---

## 💻 Practice Example

```python
student = ("Akanksha", 20, "BCA")

name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)
```

Output:

```text
Name: Akanksha
Age: 20
Course: BCA
```

This helped me understand how Tuple values can be assigned directly to separate variables.

---

## 📊 Data Science Connection

Understanding Tuples and Tuple unpacking helps build a strong Python foundation for Data Science.

When working with data, we often deal with groups of related values.

For example:

```python
student = ("Akanksha", 20, "BCA")
```

These values can represent related information about one student.

Tuple unpacking can then make the individual values easier to work with:

```python
name, age, course = student
```

Later, when working with datasets, I will encounter many situations where values need to be separated, accessed, and processed.

---

## 🧠 Key Takeaways

After completing Day 18, I can:

- Use `count()` with Tuples.
- Use `index()` with Tuples.
- Understand why Tuples have fewer methods than Lists.
- Understand the relationship between immutability and Tuple methods.
- Understand Tuple unpacking.
- Assign Tuple values to separate variables.
- Use Tuple unpacking with different data types.
- Understand that the number of variables should match the number of Tuple values.

---

## 🚀 Progress

**Day 18 completed!** ✅

Today I learned about Tuple methods and Tuple unpacking.

I practiced counting values, finding positions, and assigning Tuple values to separate variables.

This is helping me strengthen my Python data-structure foundation before moving toward more Data Science-focused tools.

Continuing my Python journey step by step toward my goal of becoming a **Data Scientist**. 🐍📊🚀
