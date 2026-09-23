# Day 22 - Dictionary Methods + Loops 🐍

## 📚 Topics Learned

### Dictionary Methods
- `keys()`
- `values()`
- `items()`
- `get()`
- `update()`
- `pop()`
- `clear()`

### Dictionary Loops
- Looping through keys
- Looping through values
- Looping through key-value pairs
- Using `for` with `items()`
- Working with dictionaries and marks
- Finding total and average values

---

## 🤔 What is a Dictionary?

A Dictionary stores data using **key-value pairs**.

Example:

```python
student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}
```

Here:

- `"name"` is a key
- `"Akanksha"` is its value
- `"age"` is a key
- `20` is its value
- `"course"` is a key
- `"BCA"` is its value

---

# 🔑 Dictionary Methods

## 1️⃣ `keys()`

The `keys()` method returns all the keys in a dictionary.

```python
student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

print(student.keys())
```

It is useful when we want to work only with the keys.

---

## 2️⃣ `values()`

The `values()` method returns all the values.

```python
print(student.values())
```

This is useful when we want to work with the stored values.

---

## 3️⃣ `items()`

The `items()` method gives us both keys and values.

```python
print(student.items())
```

It is especially useful with loops.

---

## 4️⃣ `get()`

The `get()` method is used to access a value using its key.

```python
print(student.get("name"))
```

Output:

```text
Akanksha
```

We can also provide a default value if the key does not exist.

```python
print(student.get("city", "Not Available"))
```

Output:

```text
Not Available
```

This is useful because it avoids an error when the key is missing.

---

## 5️⃣ `update()`

The `update()` method is used to change an existing value or add a new key-value pair.

```python
student.update({"age": 21})

print(student)
```

We can also add a new key:

```python
student.update({"goal": "Data Scientist"})
```

---

## 6️⃣ `pop()`

The `pop()` method removes a key-value pair from the dictionary.

```python
student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

student.pop("age")

print(student)
```

The `"age"` key and its value are removed.

---

## 7️⃣ `clear()`

The `clear()` method removes all items from a dictionary.

```python
student = {
    "name": "Akanksha",
    "age": 20
}

student.clear()

print(student)
```

Output:

```text
{}
```

The dictionary still exists, but it is empty.

---

# 🔄 Dictionary Loops

Loops allow us to process dictionary data one item at a time.

---

## 1️⃣ Loop Through Keys

We can loop directly through a dictionary.

```python
student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

for key in student:
    print(key)
```

We can also use:

```python
for key in student.keys():
    print(key)
```

---

## 2️⃣ Loop Through Values

Use `values()` when we want only the values.

```python
for value in student.values():
    print(value)
```

---

## 3️⃣ Loop Through Keys and Values

Use `items()` when we want both the key and value.

```python
for key, value in student.items():
    print(key, ":", value)
```

Output:

```text
name : Akanksha
age : 20
course : BCA
```

---

# 📊 Dictionary with Marks

Dictionaries are very useful for storing related data.

Example:

```python
marks = {
    "Python": 85,
    "Maths": 90,
    "OS": 88
}
```

We can use a loop to print every subject and its mark.

```python
for subject, mark in marks.items():
    print(subject, ":", mark)
```

Output:

```text
Python : 85
Maths : 90
OS : 88
```

---

# ➕ Finding Total Marks

We can use a loop with `values()`.

```python
total = 0

for mark in marks.values():
    total = total + mark

print("Total:", total)
```

---

# 📈 Finding Average Marks

We can calculate the average using the total and number of subjects.

```python
total = 0

for mark in marks.values():
    total = total + mark

average = total / len(marks)

print("Average:", average)
```

---

# 🔍 Using Dictionary with `if`

We can also combine dictionaries, loops, and conditions.

```python
for subject, mark in marks.items():
    if mark > 85:
        print(subject, ":", mark)
```

This prints subjects whose marks are greater than 85.

---

# 📝 Practice Tasks

Today I practiced:

- Printing dictionary keys
- Printing dictionary values
- Printing key-value pairs
- Using `get()`
- Handling a missing key with `get()`
- Updating dictionary values
- Adding new dictionary items
- Removing items using `pop()`
- Looping through dictionary keys
- Looping through dictionary values
- Looping through key-value pairs
- Working with student marks
- Finding total marks
- Finding average marks
- Using `if` with dictionary loops

The solutions are available in [`tasks.py`](tasks.py).

---

# 📊 Data Science Connection

Dictionaries are an important Python foundation for Data Science.

They can be used to represent structured information such as:

- Student information
- Subject marks
- Product information
- Categories
- Counts and frequencies
- Configuration data

Loops allow us to process this information one item at a time.

Later, these concepts will help when working with structured data and Pandas.

---

# 🧠 Key Takeaways

- `keys()` gives dictionary keys.
- `values()` gives dictionary values.
- `items()` gives keys and values together.
- `get()` safely accesses a value.
- `update()` changes or adds data.
- `pop()` removes a specific key-value pair.
- `clear()` removes all dictionary items.
- `for` loops can process dictionary data.
- `items()` is especially useful when we need both key and value.
- Dictionaries and loops can be combined with conditions to solve problems.

---

# 🎯 Progress

**Day 22 completed!** ✅

Today I learned important Dictionary methods and practiced looping through dictionaries.

I am continuing to strengthen my Python fundamentals step by step toward my goal of becoming a Data Scientist.
