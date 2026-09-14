# Day 13 - String Methods 🐍

## 📚 Topics Learned

* `lower()`
* `upper()`
* `strip()`
* `replace()`
* `find()`
* `count()`
* `split()`
* Combining multiple string methods
* String cleaning and basic text processing

## 🤔 What are String Methods?

String methods are built-in Python functions that are used to perform different operations on strings.

They help us modify, search, count, and process text easily.

Example:

```python
name = "AKANKSHA"

print(name.lower())
```

Output:

```text
akanksha
```

## 🔹 1. lower()

The `lower()` method converts all uppercase letters into lowercase letters.

```python
text = "HELLO PYTHON"

print(text.lower())
```

Output:

```text
hello python
```

## 🔹 2. upper()

The `upper()` method converts all lowercase letters into uppercase letters.

```python
text = "hello python"

print(text.upper())
```

Output:

```text
HELLO PYTHON
```

## 🔹 3. strip()

The `strip()` method removes extra spaces from the beginning and end of a string.

```python
text = "   Hello Python   "

print(text.strip())
```

Output:

```text
Hello Python
```

It does not remove spaces between words.

```python
text = "Hello   Python"

print(text.strip())
```

Output:

```text
Hello   Python
```

## 🔹 4. replace()

The `replace()` method replaces one part of a string with another.

Syntax:

```python
string.replace(old, new)
```

Example:

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

Output:

```text
I like Python
```

## 🔹 5. find()

The `find()` method searches for a character or substring and returns its position.

```python
text = "Python"

print(text.find("t"))
```

Output:

```text
2
```

If the text is not found, `find()` returns `-1`.

```python
text = "Python"

print(text.find("z"))
```

Output:

```text
-1
```

## 🔹 6. count()

The `count()` method counts how many times a character or substring appears.

```python
text = "banana"

print(text.count("a"))
```

Output:

```text
3
```

## 🔹 7. split()

The `split()` method divides a string into a list.

```python
text = "Python is easy"

print(text.split())
```

Output:

```text
['Python', 'is', 'easy']
```

By default, `split()` separates the string using spaces.

We can also specify a separator:

```python
text = "apple,banana,mango"

print(text.split(","))
```

Output:

```text
['apple', 'banana', 'mango']
```

## 🔗 Combining String Methods

We can use multiple string methods together.

```python
text = "   HELLO PYTHON   "

result = text.strip().lower()

print(result)
```

Output:

```text
hello python
```

Another example:

```python
text = "  I LOVE PYTHON  "

result = text.strip().lower().replace("python", "data science")

print(result)
```

Output:

```text
i love data science
```

## 🌍 Real-World / Data Science Connection

String methods are very important in Data Science because real-world datasets often contain messy or inconsistent text data.

For example, a dataset may contain:

```text
" AKANKSHA "
"akanksha"
"AKANKSHA"
```

Using string methods, we can clean and standardize the data:

```python
name = "  AKANKSHA  "

clean_name = name.strip().lower()

print(clean_name)
```

Output:

```text
akanksha
```

Methods such as `lower()`, `strip()`, `replace()`, `find()`, `count()`, and `split()` are useful for basic text cleaning and processing before analyzing data.

✅ Day 10 completed!

Continuing to strengthen my Python foundation step by step toward my goal of becoming a Data Scientist. 🚀
