# Day 20 - Set Operations 🐍

## 📚 Topics Learned

- `union()`
- `intersection()`
- `difference()`
- `symmetric_difference()`
- Union operator `|`
- Intersection operator `&`
- Difference operator `-`
- Symmetric difference operator `^`
- Applying Set operations to problems

## 🤔 What are Set Operations?

Set operations allow us to compare two or more Sets and find relationships between their elements.

For example, we can find:

- All unique elements from two Sets
- Common elements
- Elements that exist only in one Set
- Elements that exist in only one of the two Sets

---

## 1️⃣ Union

Union combines all unique elements from two Sets.

We can use the `union()` method.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))
```

Output:

```text
{1, 2, 3, 4, 5, 6}
```

We can also use the `|` operator.

```python
print(set1 | set2)
```

### Meaning:

**Union = Everything from both Sets**

---

## 2️⃣ Intersection

Intersection finds the elements that are common in both Sets.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.intersection(set2))
```

Output:

```text
{3, 4}
```

We can also use the `&` operator.

```python
print(set1 & set2)
```

### Meaning:

**Intersection = Common elements**

---

## 3️⃣ Difference

Difference finds elements that exist in the first Set but not in the second Set.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.difference(set2))
```

Output:

```text
{1, 2}
```

We can also use the `-` operator.

```python
print(set1 - set2)
```

### Meaning:

**Difference = Elements only in the first Set**

The order matters.

```python
set1 - set2
```

is not necessarily the same as:

```python
set2 - set1
```

---

## 4️⃣ Symmetric Difference

Symmetric difference finds elements that exist in only one of the two Sets.

Common elements are removed.

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.symmetric_difference(set2))
```

Output:

```text
{1, 2, 5, 6}
```

We can also use the `^` operator.

```python
print(set1 ^ set2)
```

### Meaning:

**Symmetric Difference = Elements that are not common**

---

## 🔍 Set Operations Comparison

| Operation | Method | Operator | Meaning |
|---|---|---|---|
| Union | `union()` | `\|` | All unique elements |
| Intersection | `intersection()` | `&` | Common elements |
| Difference | `difference()` | `-` | Only in first Set |
| Symmetric Difference | `symmetric_difference()` | `^` | Only in one Set |

---

## 🎓 Example with Students

Suppose two groups of students are learning different programming languages.

```python
python_students = {"Akanksha", "Rahul", "Priya", "Anu"}

java_students = {"Rahul", "Priya", "Kiran"}
```

### All students

```python
print(python_students | java_students)
```

This gives all unique students from both groups.

### Students learning both

```python
print(python_students & java_students)
```

This gives students who are present in both Sets.

### Students learning only Python

```python
print(python_students - java_students)
```

This gives students who are in the Python Set but not the Java Set.

### Students learning only one of the two

```python
print(python_students ^ java_students)
```

This gives students who are present in only one Set.

---

## 📝 Practice Tasks

Today I practiced:

- Finding the union of two Sets
- Finding the intersection of two Sets
- Finding the difference between Sets
- Finding the symmetric difference
- Using `|`
- Using `&`
- Using `-`
- Using `^`
- Comparing student subjects
- Comparing programming skills

The solutions are available in [`tasks.py`](tasks.py).

---

## 📊 Data Science Connection

Set operations are useful when working with unique values and comparing groups of data.

For example, in Data Science we may want to:

- Find unique categories
- Find common categories
- Compare two groups
- Identify values present in one dataset but not another
- Remove duplicate values

These concepts become useful when working with real datasets.

---

## 🧠 Key Takeaways

- `union()` combines unique elements from both Sets.
- `intersection()` finds common elements.
- `difference()` finds elements only in the first Set.
- `symmetric_difference()` finds elements that are not common.
- `|` is the union operator.
- `&` is the intersection operator.
- `-` is the difference operator.
- `^` is the symmetric difference operator.

---

## 🎯 Progress

**Day 20 completed!** ✅

Today I learned how to compare Sets using different Set operations.

I am continuing to strengthen my Python fundamentals step by step toward my goal of becoming a Data Scientist.
