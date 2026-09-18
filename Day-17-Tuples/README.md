# Day 17 - Tuples 🐍

## 📚 Topics Learned

Today I learned about Python Tuples and how they are different from Lists.

- What is a Tuple?
- Creating a Tuple
- Tuple indexing
- Negative indexing
- Tuple slicing
- Tuple immutability
- Difference between List and Tuple
- Single-element Tuple
- `len()` with Tuples
- Accessing Tuple elements

---

## 🤔 What is a Tuple?

A Tuple is a collection of multiple values stored in a single variable.

Tuples are written using parentheses `()`.

Example:

```python
marks = (85, 90, 78, 92, 88)

print(marks)
```

Output:

```text
(85, 90, 78, 92, 88)
```

A Tuple can store multiple values together.

---

## 📝 Creating a Tuple

A Tuple is created by placing values inside parentheses.

Example:

```python
student = ("Akanksha", 20, "BCA")

print(student)
```

Output:

```text
('Akanksha', 20, 'BCA')
```

---

## 🔢 Tuple Indexing

Indexing is used to access individual elements from a Tuple.

Python uses zero-based indexing.

That means the first element has index `0`.

Example:

```python
marks = (85, 90, 78, 92, 88)

print(marks[0])
print(marks[1])
print(marks[2])
```

Output:

```text
85
90
78
```

The index positions are:

```text
85   90   78   92   88
 ↑    ↑    ↑    ↑    ↑
 0    1    2    3    4
```

---

## 🔄 Negative Indexing

Negative indexing allows us to access elements from the end of a Tuple.

Example:

```python
marks = (85, 90, 78, 92, 88)

print(marks[-1])
print(marks[-2])
```

Output:

```text
88
92
```

The last element has index `-1`.

```text
85   90   78   92   88
 ↑    ↑    ↑    ↑    ↑
-5   -4   -3   -2   -1
```

---

## ✂️ Tuple Slicing

Slicing is used to get a part of a Tuple.

The basic syntax is:

```python
tuple[start:end]
```

The starting index is included, but the ending index is not included.

Example:

```python
marks = (85, 90, 78, 92, 88)

print(marks[0:3])
```

Output:

```text
(85, 90, 78)
```

---

## 🔒 Tuple Immutability

Tuples are **immutable**.

Immutable means that the elements of a Tuple cannot be changed after the Tuple is created.

Example:

```python
student = ("Akanksha", 20, "BCA")

print(student)
```

We cannot do this:

```python
student[1] = 21
```

Python will produce a `TypeError` because Tuples cannot be modified.

This is one of the main differences between Lists and Tuples.

---

## 🔍 List vs Tuple

### List

Lists use square brackets:

```python
marks = [85, 90, 78]
```

Lists are **mutable**, so their elements can be changed.

Example:

```python
marks[0] = 100
```

This is allowed.

### Tuple

Tuples use parentheses:

```python
marks = (85, 90, 78)
```

Tuples are **immutable**, so their elements cannot be changed.

Example:

```python
marks[0] = 100
```

This produces an error.

### Simple difference:

```text
List  → Mutable
Tuple → Immutable
```

---

## 📊 List and Tuple Comparison

| Feature | List | Tuple |
|---|---|---|
| Brackets | `[]` | `()` |
| Mutable | Yes | No |
| Can change elements | Yes | No |
| Can store multiple values | Yes | Yes |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |

---

## 1️⃣ Single-Element Tuple

When creating a Tuple with only one element, we need to add a comma.

Example:

```python
number = (10,)

print(number)
```

Output:

```text
(10,)
```

Without the comma:

```python
number = (10)

print(type(number))
```

This is an integer, not a Tuple.

The comma is important:

```python
number = (10,)
```

---

## 🧩 Mixed Data Types

A Tuple can contain different data types.

Example:

```python
student = ("Akanksha", 20, 85.5, True)

print(student)
```

Output:

```text
('Akanksha', 20, 85.5, True)
```

This Tuple contains:

- String → `"Akanksha"`
- Integer → `20`
- Float → `85.5`
- Boolean → `True`

---

## 📏 Finding the Length of a Tuple

The `len()` function returns the number of elements in a Tuple.

Example:

```python
marks = (85, 90, 78, 92, 88)

print(len(marks))
```

Output:

```text
5
```

There are five elements in the Tuple.

---

## 🔁 Accessing Tuple Elements Using a `for` Loop

A `for` loop can be used to access each element of a Tuple.

Example:

```python
marks = (85, 90, 78, 92, 88)

for mark in marks:
    print(mark)
```

Output:

```text
85
90
78
92
88
```

The loop accesses each element one by one.

---

## 📝 Practice Tasks

Today I practiced:

- Creating a student details Tuple
- Printing the first item
- Printing the last item
- Using negative indexing
- Slicing a Tuple
- Finding the length of a Tuple
- Creating a single-element Tuple
- Printing Tuple elements one by one
- Understanding Tuple immutability

The solutions are available in [`tasks.py`](tasks.py).

---

## 💻 Practice Example

```python
marks = (85, 90, 78, 92, 88)

print(marks[0])
print(marks[-1])

for mark in marks:
    print(mark)

print(len(marks))
```

Output:

```text
85
88
85
90
78
92
88
5
```

This practice helped me understand how Tuple elements can be accessed and processed.

---

## 📊 Data Science Connection

Tuples are another important Python data structure.

They can be useful when we have a collection of values that should not be changed.

For example:

```python
student = ("Akanksha", 20, "BCA")
```

This stores related information together.

Tuples can also be useful for representing fixed collections of data.

Later, when working with Data Science, I will work with data structures such as:

- Lists
- Tuples
- NumPy arrays
- Pandas Series
- Pandas DataFrames

Understanding the differences between these structures will help me choose the appropriate structure for different situations.

---

## 🧠 Key Takeaways

After completing Day 17, I can:

- Create a Tuple.
- Access Tuple elements using indexing.
- Use negative indexing.
- Slice a Tuple.
- Find the length using `len()`.
- Understand that Tuples are immutable.
- Understand the difference between Lists and Tuples.
- Create a single-element Tuple.
- Store mixed data types in a Tuple.
- Access Tuple elements using a `for` loop.

---

## 🚀 Progress

**Day 17 completed!** ✅

Today I learned about Python Tuples and understood how they differ from Lists.

I practiced indexing, negative indexing, slicing, immutability, and working with Tuple elements.

This is another step toward building a strong Python foundation for Data Science.

Continuing my Python journey step by step toward my goal of becoming a **Data Scientist**. 🐍📊🚀
