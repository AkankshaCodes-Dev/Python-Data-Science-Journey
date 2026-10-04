# 🐍 Day 32 — OOP Basics

## 📚 Topics Learned

Today I learned the basics of Object-Oriented Programming (OOP) in Python.

### Concepts Covered

- What is OOP?
- Class
- Object
- `__init__()`
- `self`
- Attributes
- Methods
- Multiple Objects
- Real-world examples
- OOP and Data Science connection

---

## 🧠 What is OOP?

OOP stands for **Object-Oriented Programming**.

It is a programming approach where we organize code using:

- Classes
- Objects
- Attributes
- Methods

---

## 🏗️ Class

A class is like a blueprint.

Example:

```python
class Student:
    pass
```

---

## 📦 Object

An object is created from a class.

```python
student1 = Student()
```

Here:

- `Student` = class
- `student1` = object

---

## 🔧 `__init__()`

`__init__()` is used to initialize object data.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---

## 👤 self

`self` refers to the current object.

```python
student1 = Student("Akanksha", 20)
```

Here:

```python
self.name
```

stores the name of the current object.

---

## 📊 Attributes

Attributes are data stored inside an object.

Example:

```python
self.name
self.age
self.course
```

---

## ⚙️ Methods

Methods are functions defined inside a class.

Example:

```python
class Student:

    def greet(self):
        print("Hello")
```

---

## 🔁 Multiple Objects

One class can create many objects.

```python
student1 = Student("Akanksha", 20)
student2 = Student("Rahul", 21)
```

Both objects use the same class but can contain different data.

---

## 📈 Data Science Connection

OOP is important in Data Science because many Python libraries use objects and classes.

Examples include:

- Machine Learning models
- Dataset-related objects
- Data preprocessing
- Custom data processing classes
- Scikit-learn models

For example, later in Machine Learning we may use objects like:

```python
model = SomeModel()
```

and then call methods such as:

```python
model.fit()
model.predict()
```

So learning OOP now will make advanced Python and Machine Learning easier later.

---

## 📝 Practice

I practiced:

- Creating classes
- Creating objects
- Using `__init__()`
- Using `self`
- Creating attributes
- Creating methods
- Working with multiple objects
- Building Calculator, Student, BankAccount, Product and DataProcessor classes

---

## 🚀 Progress

Day 32 completed — OOP Basics.

Next, I will continue building my Python foundation for Data Science.
