# Day 4 - Input and Type Conversion 🐍

## 📚 Topics Learned

- `input()`
- Taking input from the user
- Why `input()` returns a string
- `int()`
- `float()`
- `str()`
- Type conversion

## 💻 Taking Input

The `input()` function allows a Python program to receive information from the user.

```python
name = input("Enter your name: ")

print("Hello", name)
```

## 🔍 Important: `input()` Returns a String

Even when the user enters a number, `input()` initially gives the value as a string.

```python
age = input("Enter your age: ")

print(type(age))
```

The output will be:

```text
<class 'str'>
```

## 🔄 Type Conversion

We can convert values from one data type to another.

### String to Integer

```python
age = int("20")

print(age)
print(type(age))
```

### String to Float

```python
height = float("5.5")

print(height)
print(type(height))
```

### Number to String

```python
number = 100

text = str(number)

print(text)
print(type(text))
```

## 📝 Practice Tasks

Today I practiced:

- Taking input from the user
- Checking the type returned by `input()`
- Converting strings to integers
- Converting strings to floats
- Converting numbers to strings
- Performing calculations using user input

The solutions are available in [`tasks.py`](tasks.py).

## 📊 Data Science Connection

Input and type conversion are useful foundations for working with data.

When data enters a program, it may need to be converted into the correct type before calculations or analysis can be performed.

For example, numerical data should be treated as numbers when performing mathematical operations.

## 🎯 Progress

**Day 4 completed!** ✅

Today I learned how to take input from users and convert values between different data types.

Continuing to build my Python foundation for Data Science. 🚀
