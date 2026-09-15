# Day 14 - String Practice 🐍

## 📚 Topics Practiced

Today I practiced the string concepts and string methods learned in the previous days.

- String indexing
- Negative indexing
- String slicing
- `len()`
- `lower()`
- `upper()`
- `strip()`
- `replace()`
- `find()`
- `count()`
- `split()`
- Combining string methods
- Applying strings to programming problems

---

## 🎯 Purpose of Day 14

Day 14 is a practice-focused day.

Instead of learning a completely new concept, I practiced using the string concepts and methods I learned in Days 12 and 13.

The goal was to become more comfortable with working with text in Python.

---

## 🔢 String Indexing

Indexing is used to access individual characters in a string.

Example:

```python
word = "Python"

print(word[0])
print(word[-1])
```

Output:

```text
P
n
```

Positive indexing starts from the left, while negative indexing starts from the right.

---

## ✂️ String Slicing

Slicing is used to extract a part of a string.

Example:

```python
word = "Python"

print(word[0:3])
```

Output:

```text
Pyt
```

The starting index is included and the ending index is not included.

---

## 📏 `len()`

The `len()` function returns the number of characters in a string.

Example:

```python
name = "Akanksha"

print(len(name))
```

Output:

```text
8
```

---

## 🔤 `lower()`

The `lower()` method converts a string to lowercase.

Example:

```python
text = "PYTHON"

print(text.lower())
```

Output:

```text
python
```

---

## 🔠 `upper()`

The `upper()` method converts a string to uppercase.

Example:

```python
text = "python"

print(text.upper())
```

Output:

```text
PYTHON
```

---

## 🧹 `strip()`

The `strip()` method removes spaces from the beginning and end of a string.

Example:

```python
text = "   Hello Python   "

print(text.strip())
```

Output:

```text
Hello Python
```

---

## 🔄 `replace()`

The `replace()` method replaces one part of a string with another.

Example:

```python
text = "I am learning Java"

print(text.replace("Java", "Python"))
```

Output:

```text
I am learning Python
```

---

## 🔎 `find()`

The `find()` method searches for text and returns its position.

Example:

```python
text = "I love Python"

print(text.find("Python"))
```

Output:

```text
7
```

If the text is not found, `find()` returns `-1`.

Example:

```python
text = "I love Python"

print(text.find("Java"))
```

Output:

```text
-1
```

---

## 🔢 `count()`

The `count()` method counts how many times a character or substring appears.

Example:

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

---

## ✂️ `split()`

The `split()` method divides a string into smaller parts and returns them as a list.

Example:

```python
sentence = "Python is easy to learn"

print(sentence.split())
```

Output:

```text
['Python', 'is', 'easy', 'to', 'learn']
```

---

## 🔗 Combining String Methods

Multiple string methods can be used together.

Example:

```python
text = "   PYTHON DATA SCIENCE   "

text = text.strip()
text = text.lower()
text = text.replace(" ", "-")

print(text)
```

Output:

```text
python-data-science
```

Here:

1. `strip()` removed the extra spaces.
2. `lower()` converted the text to lowercase.
3. `replace()` replaced spaces with hyphens.

---

## 📝 Practice Tasks

Today I practiced:

- Printing the first and last character of a word
- Using negative indexing
- Extracting characters using slicing
- Finding the length of a string
- Converting text to lowercase
- Removing extra spaces
- Replacing text
- Finding the position of text
- Counting characters
- Splitting a sentence into words
- Combining multiple string methods

The solutions are available in [`tasks.py`](tasks.py).

---

## 💻 Practice Example

```python
text = "   PYTHON DATA SCIENCE   "

text = text.strip()
text = text.lower()
text = text.replace(" ", "-")

print(text)
```

Output:

```text
python-data-science
```

This practice helped me understand how multiple string operations can be combined to process text.

---

## 📊 Data Science Connection

String processing is an important part of Data Science.

Real-world datasets often contain text values such as:

```text
Name
City
Product
Category
Email
Customer Review
```

The data may contain:

- Extra spaces
- Different uppercase and lowercase formats
- Unwanted text
- Repeated values
- Text that needs to be separated into smaller parts

For example:

```python
name = "   AKANKSHA   "

name = name.strip()
name = name.lower()

print(name)
```

Output:

```text
akanksha
```

This is a simple example of data cleaning.

Later, when I learn Pandas, I will use similar string operations on columns of real datasets.

---

## 🧠 Key Takeaways

After completing Day 14, I can:

- Access characters using indexes.
- Use negative indexing.
- Extract parts of strings using slicing.
- Find the length of strings using `len()`.
- Convert text using `lower()` and `upper()`.
- Remove extra spaces using `strip()`.
- Replace text using `replace()`.
- Search for text using `find()`.
- Count occurrences using `count()`.
- Split sentences using `split()`.
- Combine multiple string methods.
- Apply string operations to simple programming problems.

---

## 🚀 Progress

**Day 14 completed!** ✅

Today I practiced different Python string concepts and methods and learned how to combine them to solve small programming problems.

This practice is helping me become more comfortable with text processing and is building a strong Python foundation for Data Science.

Continuing my Python journey step by step toward my goal of becoming a **Data Scientist**. 🐍📊🚀
