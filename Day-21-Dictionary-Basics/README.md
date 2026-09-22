
# Day 21 - Dictionary Basics 🐍

## 📚 Topics Learned

- What is a Dictionary?
- Creating a Dictionary
- Key-Value Pairs
- Accessing Dictionary Values
- Adding Items
- Updating Items
- Removing Items
- `keys()`
- `values()`
- `items()`
- Checking if a Key Exists
- Dictionary Practice

## 🤔 What is a Dictionary?

A dictionary is a Python data structure that stores data in the form of key-value pairs.

Example:

    student = {
        "name": "Akanksha",
        "course": "BCA",
        "year": 3
    }

Here:

- `"name"` is a key and `"Akanksha"` is its value.
- `"course"` is a key and `"BCA"` is its value.
- `"year"` is a key and `3` is its value.

## 🏗️ Creating a Dictionary

A dictionary is created using curly brackets `{}`.

Example:

    student = {
        "name": "Akanksha",
        "course": "BCA",
        "year": 3
    }

    print(student)

Output:

    {'name': 'Akanksha', 'course': 'BCA', 'year': 3}

## 🔑 Accessing Dictionary Values

We can access a value using its key.

Example:

    student = {
        "name": "Akanksha",
        "course": "BCA"
    }

    print(student["name"])
    print(student["course"])

Output:

    Akanksha
    BCA

## ➕ Adding Items

We can add a new key-value pair to a dictionary.

Example:

    student = {
        "name": "Akanksha",
        "course": "BCA"
    }

    student["year"] = 3

    print(student)

Output:

    {'name': 'Akanksha', 'course': 'BCA', 'year': 3}

## 🔄 Updating Items

We can update the value of an existing key.

Example:

    student = {
        "name": "Akanksha",
        "course": "BCA"
    }

    student["course"] = "Data Science"

    print(student)

Output:

    {'name': 'Akanksha', 'course': 'Data Science'}

## ❌ Removing Items

We can remove an item using the `pop()` method.

Example:

    student = {
        "name": "Akanksha",
        "course": "BCA",
        "year": 3
    }

    student.pop("year")

    print(student)

Output:

    {'name': 'Akanksha', 'course': 'BCA'}

## 🔑 Using `keys()`

The `keys()` method returns all the keys in a dictionary.

Example:

    student = {
        "name": "Akanksha",
        "course": "BCA",
        "year": 3
    }

    print(student.keys())

## 📦 Using `values()`

The `values()` method returns all the values in a dictionary.

Example:

    student = {
        "name": "Akanksha",
        "course": "BCA",
        "year": 3
    }

    print(student.values())

## 🔄 Using `items()`

The `items()` method returns all key-value pairs.

Example:

    student = {
        "name": "Akanksha",
        "course": "BCA",
        "year": 3
    }

    print(student.items())

## 🔍 Checking if a Key Exists

We can use the `in` operator to check whether a key exists.

Example:

    student = {
        "name": "Akanksha",
        "course": "BCA"
    }

    print("name" in student)
    print("age" in student)

Output:

    True
    False

## 🌐 Dictionary and Data Science

Dictionaries are very useful in Data Science and Python programming.

They can be used to represent structured information such as:

- Student records
- Customer information
- Product information
- Dataset records
- JSON data
- API responses

Example:

    customer = {
        "name": "Rahul",
        "age": 25,
        "city": "Bangalore",
        "purchase": 1500
    }

    print(customer["purchase"])

Dictionaries help represent real-world information using meaningful keys and values.

## 📝 Practice Completed

- Created dictionaries
- Accessed dictionary values
- Added new key-value pairs
- Updated existing values
- Removed dictionary items
- Used `keys()`
- Used `values()`
- Used `items()`
- Checked whether a key exists
- Solved basic dictionary problems

## 📂 Files

- `concepts.py` - Dictionary concepts and examples
- `tasks.py` - Dictionary practice tasks
- `README.md` - Day 21 learning notes

## 🎯 Day 21 Goal

The goal of Day 21 was to understand how Python dictionaries store and manage data using key-value pairs.

## 🚀 Progress

Python Data Science Journey

Day 21 - Dictionary Basics Completed ✅
```
