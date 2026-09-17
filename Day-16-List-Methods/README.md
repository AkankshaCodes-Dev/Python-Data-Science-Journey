# Day 16 - List Methods 🐍

## 📚 Topics Learned

Today I learned important Python List methods.

- `append()`
- `insert()`
- `remove()`
- `pop()`
- `sort()`
- `reverse()`
- `clear()`
- `index()`
- `count()`
- Difference between `append()` and `insert()`
- Difference between `remove()` and `pop()`
- Combining list methods

---

## 🤔 What are List Methods?

List methods are built-in functions that allow us to perform different operations on a list.

They help us add, remove, search, sort, and modify elements in a list.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")

print(fruits)
```

Output:

```text
['Apple', 'Banana', 'Mango', 'Orange']
```

---

## ➕ `append()`

The `append()` method adds one item to the **end of a list**.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")

print(fruits)
```

Output:

```text
['Apple', 'Banana', 'Mango', 'Orange']
```

### Simple meaning:

```text
append() → Add an item at the end
```

---

## 📍 `insert()`

The `insert()` method adds an item at a specific position.

Syntax:

```python
list.insert(index, item)
```

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.insert(1, "Orange")

print(fruits)
```

Output:

```text
['Apple', 'Orange', 'Banana', 'Mango']
```

Here, `"Orange"` was inserted at index `1`.

### Simple meaning:

```text
insert() → Add an item at a specific position
```

---

## 🔍 Difference Between `append()` and `insert()`

### `append()`

Adds an item at the end.

```python
fruits.append("Orange")
```

### `insert()`

Adds an item at a particular position.

```python
fruits.insert(1, "Orange")
```

So:

```text
append() → end of list
insert() → specific position
```

---

## ❌ `remove()`

The `remove()` method removes an item by its **value**.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)
```

Output:

```text
['Apple', 'Mango']
```

Here, `"Banana"` was removed from the list.

### Simple meaning:

```text
remove() → Remove using the value
```

---

## 🗑️ `pop()`

The `pop()` method removes an item using its **index**.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.pop(1)

print(fruits)
```

Output:

```text
['Apple', 'Mango']
```

Index `1` contained `"Banana"`, so it was removed.

### Simple meaning:

```text
pop() → Remove using the index
```

---

## 🔍 Difference Between `remove()` and `pop()`

### `remove()`

Uses the value:

```python
fruits.remove("Banana")
```

### `pop()`

Uses the index:

```python
fruits.pop(1)
```

So:

```text
remove() → value
pop()    → index
```

---

## 🔢 `sort()`

The `sort()` method arranges list elements in ascending order.

Example:

```python
numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)
```

Output:

```text
[1, 2, 3, 5, 8]
```

---

## 🔄 `reverse()`

The `reverse()` method reverses the order of elements in a list.

Example:

```python
numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)
```

Output:

```text
[5, 4, 3, 2, 1]
```

---

## 🧹 `clear()`

The `clear()` method removes all elements from a list.

Example:

```python
numbers = [1, 2, 3, 4, 5]

numbers.clear()

print(numbers)
```

Output:

```text
[]
```

The list still exists, but it is now empty.

---

## 🔎 `index()`

The `index()` method returns the position of an item in a list.

Example:

```python
fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Banana"))
```

Output:

```text
1
```

Because `"Banana"` is at index `1`.

---

## 🔢 `count()`

The `count()` method tells us how many times a value appears in a list.

Example:

```python
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))
```

Output:

```text
3
```

The number `10` appears three times.

---

## 🔗 Combining List Methods

Multiple list methods can be used together.

Example:

```python
numbers = [5, 2, 8, 1, 3]

numbers.append(10)
numbers.sort()
numbers.reverse()

print(numbers)
```

Output:

```text
[10, 8, 5, 3, 2, 1]
```

Here:

1. `append()` added `10`.
2. `sort()` arranged the numbers.
3. `reverse()` reversed their order.

---

## 📝 Practice Tasks

Today I practiced:

- Adding an item using `append()`
- Inserting an item using `insert()`
- Removing an item using `remove()`
- Removing an item using `pop()`
- Sorting a list
- Reversing a list
- Finding the position of an item
- Counting occurrences of an item
- Clearing a list

The solutions are available in [`tasks.py`](tasks.py).

---

## 💻 Practice Example

```python
numbers = [5, 2, 8, 1, 3]

numbers.append(10)
numbers.sort()

print(numbers)
```

Output:

```text
[1, 2, 3, 5, 8, 10]
```

This helped me understand how list methods can be used to modify and organize data.

---

## 📊 Data Science Connection

List methods are useful for understanding how collections of data can be modified and processed.

For example, a list could contain:

```python
marks = [85, 72, 90, 65, 88]
```

We may need to:

- Add new values
- Remove unwanted values
- Sort values
- Search for values
- Count repeated values

These are basic operations that help build programming and data-processing skills.

Later, when I work with NumPy arrays and Pandas DataFrames, I will use more powerful tools for processing larger datasets.

Understanding Python lists and their methods first will make those concepts easier to learn.

---

## 🧠 Key Takeaways

After completing Day 16, I can:

- Add items using `append()`.
- Insert items using `insert()`.
- Remove values using `remove()`.
- Remove elements using `pop()`.
- Sort lists using `sort()`.
- Reverse lists using `reverse()`.
- Remove all elements using `clear()`.
- Find an item's position using `index()`.
- Count occurrences using `count()`.
- Combine multiple list methods.
- Understand the difference between `append()` and `insert()`.
- Understand the difference between `remove()` and `pop()`.

---

## 🚀 Progress

**Day 16 completed!** ✅

Today I learned important Python List methods and practiced using them to add, remove, search, sort, and modify list elements.

These concepts are helping me build stronger Python programming and data-processing skills.

Continuing my Python journey step by step toward my goal of becoming a **Data Scientist**. 🐍📊🚀
