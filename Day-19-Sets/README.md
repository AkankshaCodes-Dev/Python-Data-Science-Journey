# Day 19 - Sets 🐍

## 📚 Topics Learned

Today I learned the basics of Python Sets.

- What is a Set?
- Creating a Set
- Set properties
- Unordered collection
- No duplicate values
- Adding elements
- Removing elements
- `len()` with Sets
- Using `for` loops with Sets
- `update()`
- `discard()`
- Difference between List, Tuple, and Set

---

## 🤔 What is a Set?

A Set is a collection of values that does not contain duplicate elements.

Sets are created using curly brackets `{}`.

Example:

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

Output:

```text
{10, 20, 30, 40}
```

A Set is useful when we want to work with unique values.

---

## 🔢 Creating a Set

A Set can be created by placing values inside curly brackets.

Example:

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

---

## 🚫 No Duplicate Values

One important property of a Set is that it does not store duplicate values.

Example:

```python
numbers = {10, 20, 10, 30, 20, 40}

print(numbers)
```

Output:

```text
{10, 20, 30, 40}
```

The duplicate values are automatically removed.

So:

```text
Set → Unique values
```

---

## 🔀 Sets are Unordered

Sets are unordered collections.

This means we should not depend on a particular position or order when working with Set elements.

For example:

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

The order displayed by Python is not something we should use as a fixed index-based order.

Unlike Lists and Tuples, Sets do not support normal indexing.

For example:

```python
numbers = {10, 20, 30}

# print(numbers[0])
```

This produces an error because Sets do not support indexing.

---

## ➕ Adding Elements

The `add()` method is used to add one element to a Set.

Example:

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

Output:

```text
{10, 20, 30, 40}
```

### Simple meaning:

```text
add() → Add one element
```

---

## ➕ Adding Multiple Elements

The `update()` method can be used to add multiple elements.

Example:

```python
numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)
```

The Set now contains the additional values.

### Simple meaning:

```text
update() → Add multiple elements
```

---

## ❌ Removing Elements Using `remove()`

The `remove()` method removes a specified element from a Set.

Example:

```python
numbers = {10, 20, 30, 40}

numbers.remove(30)

print(numbers)
```

Output:

```text
{10, 20, 40}
```

If the specified element does not exist, `remove()` produces an error.

---

## 🗑️ Removing Elements Using `discard()`

The `discard()` method also removes an element from a Set.

Example:

```python
numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)
```

Output:

```text
{10, 30}
```

The difference is that `discard()` does not produce an error if the element does not exist.

Example:

```python
numbers = {10, 20, 30}

numbers.discard(50)

print(numbers)
```

The program continues normally.

---

## 📏 Finding the Length of a Set

The `len()` function tells us how many unique elements are present in a Set.

Example:

```python
numbers = {10, 20, 30, 40}

print(len(numbers))
```

Output:

```text
4
```

---

## 🔁 Using a `for` Loop with a Set

A `for` loop can be used to access Set elements one by one.

Example:

```python
subjects = {"Python", "Maths", "OS"}

for subject in subjects:
    print(subject)
```

The loop processes each element in the Set.

Remember that the order should not be relied upon because Sets are unordered.

---

## 📚 Set of Student Subjects

A Set can be useful for storing unique subjects.

Example:

```python
subjects = {"Python", "Maths", "OS", "Python"}

print(subjects)
```

The duplicate `"Python"` is stored only once.

---

## 🔍 List vs Tuple vs Set

### List

```python
numbers = [10, 20, 30]
```

- Uses `[]`
- Ordered
- Allows duplicates
- Mutable
- Supports indexing

### Tuple

```python
numbers = (10, 20, 30)
```

- Uses `()`
- Ordered
- Allows duplicates
- Immutable
- Supports indexing

### Set

```python
numbers = {10, 20, 30}
```

- Uses `{}`
- Unordered
- Does not allow duplicate values
- Mutable
- Does not support normal indexing

---

## 📊 Comparison

| Feature | List | Tuple | Set |
|---|---|---|---|
| Brackets | `[]` | `()` | `{}` |
| Ordered | Yes | Yes | No |
| Duplicates | Yes | Yes | No |
| Mutable | Yes | No | Yes |
| Indexing | Yes | Yes | No |
| Main use | Collection of values | Fixed collection | Unique values |

---

## 📝 Practice Tasks

Today I practiced:

- Creating a Set of numbers
- Creating a Set with duplicate values
- Adding an element
- Removing an element
- Finding the length of a Set
- Creating a Set of student subjects
- Printing Set elements using a `for` loop
- Adding multiple elements using `update()`
- Removing an element using `discard()`

The solutions are available in [`tasks.py`](tasks.py).

---

## 💻 Practice Example

```python
numbers = {10, 20, 10, 30, 20, 40}

numbers.add(50)

print(numbers)
print(len(numbers))
```

The duplicate values are automatically removed because Sets store unique values.

---

## 📊 Data Science Connection

Sets are useful when working with **unique values**.

For example, imagine a dataset containing student subjects:

```python
subjects = [
    "Python",
    "Maths",
    "Python",
    "OS",
    "Maths"
]
```

We may want to find the unique subjects.

A Set can help:

```python
unique_subjects = set(subjects)

print(unique_subjects)
```

The result contains each subject only once.

This idea of finding unique values is very important in Data Science and data cleaning.

Later, I will learn how similar operations can be performed using Pandas on real datasets.

---

## 🧠 Key Takeaways

After completing Day 19, I can:

- Create a Set.
- Understand that Sets store unique values.
- Understand that Sets are unordered.
- Understand that Sets do not support normal indexing.
- Add elements using `add()`.
- Add multiple elements using `update()`.
- Remove elements using `remove()`.
- Remove elements safely using `discard()`.
- Find the number of elements using `len()`.
- Use a `for` loop with a Set.
- Understand the difference between Lists, Tuples, and Sets.

---

## 🚀 Progress

**Day 19 completed!** ✅

Today I learned the basics of Python Sets and understood how they differ from Lists and Tuples.

I practiced creating Sets, handling duplicate values, adding and removing elements, and working with unique data.

This is another important step in building my Python data-structure foundation for Data Science.

Continuing my Python journey step by step toward my goal of becoming a **Data Scientist**. 🐍📊🚀
