# Day 23 - All Python Data Structures Revision 🐍

## 📚 Topics Revised

### Lists
- Creating Lists
- Indexing
- Negative indexing
- Slicing
- Mutability
- `append()`
- `insert()`
- `remove()`
- `pop()`
- `sort()`
- `reverse()`
- `clear()`
- `index()`
- `count()`

### Tuples
- Creating Tuples
- Indexing
- Negative indexing
- Slicing
- Immutability
- `count()`
- `index()`
- Tuple unpacking

### Sets
- Creating Sets
- Unique values
- `add()`
- `update()`
- `remove()`
- `discard()`
- `len()`
- `union()`
- `intersection()`
- `difference()`
- `symmetric_difference()`

### Dictionaries
- Key-value pairs
- `keys()`
- `values()`
- `items()`
- `get()`
- `update()`
- `pop()`
- `clear()`
- Dictionary loops

### Conversions and Practice
- List to Tuple
- Tuple to List
- List to Set
- Set to List
- Removing duplicates
- Set comparisons
- Dictionary loops
- Total and average
- Mixed Data Structures

---

# 🎯 Purpose of Day 23

Today I revised all the Python data structures I have learned so far.

The goal was to understand the differences between Lists, Tuples, Sets, and Dictionaries and practice using them in programming problems.

---

# 1️⃣ Lists

A List is an ordered and mutable collection.

```python
marks = [85, 90, 78, 92, 88]
```

Lists allow duplicate values and can be changed after creation.

### Indexing

```python
print(marks[0])
print(marks[-1])
```

### Slicing

```python
print(marks[0:3])
```

### Changing a value

```python
marks[2] = 80
```

### Important List Methods

```python
marks.append(95)
marks.insert(1, 87)
marks.remove(87)
marks.pop()
marks.sort()
marks.reverse()
```

Other useful methods:

```python
marks.index(90)
marks.count(90)
marks.clear()
```

---

# 2️⃣ Tuples

A Tuple is an ordered and immutable collection.

```python
student = ("Akanksha", 20, "BCA")
```

Tuples support indexing and slicing.

```python
print(student[0])
print(student[-1])
print(student[0:2])
```

### Tuple Unpacking

```python
name, age, course = student

print(name)
print(age)
print(course)
```

### Tuple Methods

Tuples have fewer methods because they are immutable.

```python
numbers = (10, 20, 10, 30)

print(numbers.count(10))
print(numbers.index(30))
```

---

# 3️⃣ Sets

A Set stores unique values.

```python
numbers = {10, 20, 10, 30, 20}
```

Duplicate values are automatically removed.

Sets do not support indexing like Lists and Tuples.

### Adding values

```python
numbers.add(40)
```

### Adding multiple values

```python
numbers.update([50, 60])
```

### Removing values

```python
numbers.remove(20)
```

`remove()` raises an error if the element does not exist.

```python
numbers.discard(100)
```

`discard()` does not raise an error when the element is missing.

---

# 4️⃣ Set Operations

Suppose:

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
```

### Union

```python
print(set1 | set2)
```

Gets all unique elements from both Sets.

### Intersection

```python
print(set1 & set2)
```

Gets elements common to both Sets.

### Difference

```python
print(set1 - set2)
```

Gets elements present in the first Set but not the second.

### Symmetric Difference

```python
print(set1 ^ set2)
```

Gets elements that are present in only one of the Sets.

---

# 5️⃣ Dictionaries

A Dictionary stores data using key-value pairs.

```python
student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}
```

We can access a value using its key.

```python
print(student["name"])
```

---

# 🔑 Dictionary Methods

### `keys()`

```python
print(student.keys())
```

Returns the dictionary keys.

### `values()`

```python
print(student.values())
```

Returns the dictionary values.

### `items()`

```python
print(student.items())
```

Returns key-value pairs.

### `get()`

```python
print(student.get("name"))
```

Can also provide a default value:

```python
print(student.get("city", "Not Available"))
```

### `update()`

```python
student.update({"age": 21})
```

Can change an existing value or add a new key.

### `pop()`

```python
student.pop("age")
```

Removes a key-value pair.

### `clear()`

```python
student.clear()
```

Removes all items from the dictionary.

---

# 🔄 Dictionary Loops

### Loop through keys

```python
for key in student:
    print(key)
```

### Loop through values

```python
for value in student.values():
    print(value)
```

### Loop through key-value pairs

```python
for key, value in student.items():
    print(key, ":", value)
```

---

# 🔄 Converting Data Structures

Python allows us to convert between different data structures.

### List → Tuple

```python
numbers = [10, 20, 30]

numbers_tuple = tuple(numbers)

print(numbers_tuple)
```

### Tuple → List

```python
numbers = (10, 20, 30)

numbers_list = list(numbers)

print(numbers_list)
```

### List → Set

```python
numbers = [10, 20, 10, 30, 20]

numbers_set = set(numbers)

print(numbers_set)
```

### Set → List

```python
numbers_list = list(numbers_set)

print(numbers_list)
```

---

# 🧹 Removing Duplicate Values

A common technique is converting a List to a Set.

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = list(set(numbers))

print(unique_numbers)
```

The Set removes duplicate values.

Then `list()` converts the result back into a List.

---

# 📊 Data Structure Comparison

| Data Structure | Ordered | Mutable | Duplicates | Main Use |
|---|---|---|---|---|
| List | Yes | Yes | Yes | Changeable collection |
| Tuple | Yes | No | Yes | Fixed collection |
| Set | No indexing/order reliance | Yes | No | Unique values |
| Dictionary | Insertion ordered | Yes | Keys unique | Key-value data |

---

# 🧩 Mixed Data Structures

Different data structures can be combined.

Example:

```python
student_data = {
    "name": "Akanksha",
    "marks": [85, 90, 88],
    "subjects": {"Python", "Maths", "OS"},
    "details": ("BCA", 20)
}
```

Here:

- Dictionary stores the complete student information.
- List stores marks.
- Set stores unique subjects.
- Tuple stores fixed student details.

This type of structure is useful for representing real-world information.

---

# 📝 Practice Tasks

Today I practiced:

- Creating Lists
- Using List indexing and slicing
- Changing List values
- Using List methods
- Creating Tuples
- Tuple unpacking
- Using Tuple methods
- Creating Sets
- Adding and removing Set elements
- Performing Set operations
- Creating Dictionaries
- Using Dictionary methods
- Looping through Dictionaries
- Finding total and average
- Converting between data structures
- Removing duplicate values
- Working with mixed data structures
- Choosing an appropriate data structure

The solutions are available in [`tasks.py`](tasks.py).

---

# 📊 Data Science Connection

Python data structures are an important foundation for Data Science.

Lists help store collections of values.

Tuples can represent fixed groups of information.

Sets are useful for unique values and comparing groups.

Dictionaries are useful for structured key-value information.

These concepts will help me later when working with:

- NumPy
- Pandas
- DataFrames
- Data cleaning
- Real-world datasets

Understanding the Python fundamentals first will make the transition to Data Science tools easier.

---

# 🧠 Final Revision

### List

**Ordered + Mutable + Duplicates allowed**

```python
[10, 20, 30]
```

### Tuple

**Ordered + Immutable + Duplicates allowed**

```python
(10, 20, 30)
```

### Set

**Unique values + Mutable + No indexing**

```python
{10, 20, 30}
```

### Dictionary

**Key-value pairs**

```python
{"name": "Akanksha", "age": 20}
```

---

# 🎯 Progress

**Day 23 completed!** ✅

I completed my full revision of Python Data Structures.

I revised Lists, Tuples, Sets, Dictionaries, their methods, loops, conversions, and practical use cases.

I am continuing to build my Python foundation step by step toward my goal of becoming a Data Scientist. 🚀
