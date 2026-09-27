# Day 26 - Function Practice and Revision 🐍

## 📚 Topics Revised

- Defining functions
- Calling functions
- Parameters
- Arguments
- Multiple arguments
- `return`
- `print()` vs `return`
- Functions with conditions
- Functions with calculations
- Functions with loops
- Functions with strings
- Functions with lists
- Problem-solving using functions

---

# 🔄 Function Revision

A function is a reusable block of code that performs a specific task.

Example:

```python
def greet():
    print("Hello!")
```

To execute the function:

```python
greet()
```

---

# 📦 Parameters and Arguments

A parameter is a variable written inside the function definition.

```python
def greet(name):
    print("Hello", name)
```

Here:

```text
name → parameter
```

When we call:

```python
greet("Akanksha")
```

`"Akanksha"` is the argument.

### Remember:

```text
Parameter → variable in function definition

Argument → actual value passed to function
```

---

# 🔙 `return`

`return` sends a value back from a function.

Example:

```python
def add(a, b):
    return a + b
```

We can store the returned value:

```python
result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

# 🖨️ `print()` vs `return`

### `print()`

Displays a value.

```python
def add(a, b):
    print(a + b)
```

### `return`

Sends the value back so that it can be stored or used again.

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

### Simple rule:

```text
print() → display

return → send value back
```

---

# 🔀 Functions with Conditions

Functions can contain `if` and `else`.

Example:

```python
def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

Calling:

```python
print(check_even(10))
```

Output:

```text
Even
```

---

# 🔢 Functions with Calculations

Functions can perform calculations and return the result.

Example:

```python
def calculate_average(a, b, c):
    total = a + b + c
    average = total / 3

    return average
```

Calling:

```python
result = calculate_average(80, 90, 70)

print(result)
```

Output:

```text
80.0
```

---

# 🔁 Functions with Loops

A function can contain a loop.

Example:

```python
def print_numbers():
    for i in range(1, 6):
        print(i)

print_numbers()
```

Output:

```text
1
2
3
4
5
```

This combines two concepts:

- Functions
- `for` loops

---

# 🔤 Functions with Strings

Functions can also process strings.

Example:

```python
def count_characters(text):
    return len(text)
```

Calling:

```python
result = count_characters("Python")

print(result)
```

Output:

```text
6
```

---

# 📋 Functions with Lists

Functions can receive lists as arguments.

Example:

```python
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total
```

Calling:

```python
marks = [80, 90, 70]

result = calculate_sum(marks)

print(result)
```

Output:

```text
240
```

---

# 🔎 Problem-Solving with Functions

Functions can be used to break a problem into smaller parts.

Example:

```python
def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest
```

Calling:

```python
numbers = [10, 25, 7, 40, 15]

print(find_largest(numbers))
```

Output:

```text
40
```

---

# 📝 Practice Completed

Today I practiced:

- Creating functions
- Calling functions
- Passing arguments
- Using multiple arguments
- Using `return`
- Using conditions inside functions
- Using loops inside functions
- Working with strings inside functions
- Working with lists inside functions
- Returning calculated values
- Solving small problems using functions

The solutions are available in [`tasks.py`](tasks.py).

---

# 📊 Data Science Connection

Functions are an important part of Python programming and will be useful in Data Science.

When working with datasets, we may need to perform the same operation many times.

Instead of repeating the same code, we can create a function and reuse it.

For example, functions can later be used for:

- Data cleaning
- Calculations
- Data transformation
- Checking values
- Processing lists of data
- Preparing data before analysis

Today I practiced combining functions with Python concepts I already learned, such as:

- Conditions
- Loops
- Strings
- Lists
- Operators

---

# 🧠 Key Takeaways

- Functions make code reusable.
- Parameters receive values inside functions.
- Arguments are the values passed to functions.
- `return` sends a value back.
- Returned values can be stored and reused.
- Functions can contain conditions.
- Functions can contain loops.
- Functions can work with strings.
- Functions can work with lists.
- Functions help break larger problems into smaller tasks.

---

# 🎯 Progress

**Day 26 completed!** ✅

Today I revised Python Functions and practiced solving small problems using arguments, `return`, conditions, loops, strings, and lists.

I am continuing to strengthen my Python foundation step by step toward my goal of becoming a Data Scientist. 🚀
