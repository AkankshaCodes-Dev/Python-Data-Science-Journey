# Day 15 - Lists Basics 🐍

## 📚 Topics Learned

- What is a List?
- Creating a List
- List indexing
- Negative indexing
- List slicing
- Mutable concept
- Mixed data types in a List
- Accessing list elements
- Finding the length of a List

---

## 🤔 What is a List?

A List is a collection of multiple values stored in a single variable.

Lists are written using square brackets `[]`.

Example:

```python
marks = [85, 90, 78, 92, 88]

print(marks)
```

Output:

```text
[85, 90, 78, 92, 88]
```

A list can store multiple values together.

---

## 📝 Creating a List

A list is created by placing values inside square brackets.

Example:

```python
marks = [85, 90, 78, 92, 88]

print(marks)
```

Here, the variable `marks` contains five values.

---

## 🔢 List Indexing

Indexing is used to access individual elements from a list.

Python uses zero-based indexing.

That means the first element has index `0`.

Example:

```python
marks = [85, 90, 78, 92, 88]

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

Negative indexing allows us to access elements from the end of the list.

Example:

```python
marks = [85, 90, 78, 92, 88]

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

## ✂️ List Slicing

Slicing is used to get a part of a list.

The basic syntax is:

```python
list[start:end]
```

The starting index is included, but the ending index is not included.

Example:

```python
marks = [85, 90, 78, 92, 88]

print(marks[0:3])
```

Output:

```text
[85, 90, 78]
```

Here, indexes `0`, `1`, and `2` are included.

---

## 🔄 Mutable Concept

Lists are **mutable**.

Mutable means that the elements of a list can be changed after the list is created.

Example:

```python
marks = [85, 90, 78, 92, 88]

marks[2] = 80

print(marks)
```

Output:

```text
[85, 90, 80, 92, 88]
```

The value `78` was changed to `80`.

This is called modifying a list.

---

## 🧩 Mixed Data Types in a List

A Python list can contain different data types.

Example:

```python
student = ["Akanksha", 20, 85.5, True]

print(student)
```

Output:

```text
['Akanksha', 20, 85.5, True]
```

This list contains:

- String → `"Akanksha"`
- Integer → `20`
- Float → `85.5`
- Boolean → `True`

---

## 🔁 Printing List Elements One by One

A `for` loop can be used to access each element of a list.

Example:

```python
marks = [85, 90, 78, 92, 88]

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

The loop takes each element from the list one by one.

---

## 📏 Finding the Length of a List

The `len()` function returns the number of elements in a list.

Example:

```python
marks = [85, 90, 78, 92, 88]

print(len(marks))
```

Output:

```text
5
```

There are five elements in the list.

---

## 📝 Practice Tasks

Today I practiced:

- Creating a student marks list
- Printing the first item
- Printing the last item
- Changing one element
- Printing all elements one by one
- Finding the length of a list

The solutions are available in [`tasks.py`](tasks.py).

---

## 💻 Practice Example

```python
marks = [85, 90, 78, 92, 88]

marks[2] = 80

for mark in marks:
    print(mark)

print(len(marks))
```

Output:

```text
85
90
80
92
88
5
```

This practice helped me understand how lists can store multiple values and how individual elements can be accessed and modified.

---

## 📊 Data Science Connection

Lists are an important Python foundation for Data Science.

Lists can be used to store collections of values such as:

```text
Student marks
Prices
Age values
Product names
Numbers
Categories
```

For example:

```python
marks = [85, 90, 78, 92, 88]
```

A list can represent a collection of student marks.

Later, when I learn tools such as NumPy and Pandas, I will work with much larger collections of data.

Understanding Python lists first will help me understand those data structures more easily.

---

## 🧠 Key Takeaways

After completing Day 15, I can:

- Create a Python list.
- Store multiple values in a list.
- Access elements using indexing.
- Use negative indexing.
- Extract elements using slicing.
- Understand that lists are mutable.
- Change elements inside a list.
- Store mixed data types in a list.
- Use a `for` loop to access list elements.
- Find the length of a list using `len()`.

---

## 🚀 Progress

**Day 15 completed!** ✅

Today I learned the basics of Python Lists, including indexing, slicing, mutability, and mixed data types.

I also practiced accessing, modifying, and processing list elements.

This is another important step in building my Python foundation for Data Science.

Continuing my Python journey step by step toward my goal of becoming a **Data Scientist**. 🐍📊🚀
