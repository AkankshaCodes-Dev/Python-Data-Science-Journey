# Day 28 - Default Arguments and Keyword Arguments 🐍

## 📚 Topics Learned

- Default arguments
- Default values
- Overriding default values
- Multiple default arguments
- Keyword arguments
- Positional arguments
- Mixing positional and keyword arguments
- Default arguments with `return`
- Practical functions using arguments

---

## 🤔 What are Default Arguments?

A default argument is an argument that already has a value in the function definition.

Example:

```python
def greet(name="Akanksha"):
    print("Hello", name)
```

If we call the function without an argument:

```python
greet()
```

Output:

```text
Hello Akanksha
```

The function uses the default value.

---

# 🔄 Changing the Default Value

We can provide a different value when calling the function.

Example:

```python
def greet(name="Akanksha"):
    print("Hello", name)

greet()
greet("Rahul")
```

Output:

```text
Hello Akanksha
Hello Rahul
```

When `"Rahul"` is provided, it replaces the default value for that function call.

---

# 🔢 Default Arguments with Numbers

Example:

```python
def calculate_square(number=5):
    return number * number
```

Calling:

```python
print(calculate_square())
```

uses the default value `5`.

Calling:

```python
print(calculate_square(8))
```

uses `8` instead.

---

# 📦 Required Argument + Default Argument

A function can have both required and default arguments.

Example:

```python
def introduce(name, course="BCA"):
    print("Name:", name)
    print("Course:", course)
```

Calling:

```python
introduce("Akanksha")
```

uses:

```text
name = Akanksha
course = BCA
```

We can also change the course:

```python
introduce("Akanksha", "Data Science")
```

---

# 🧩 Multiple Default Arguments

A function can have multiple default arguments.

Example:

```python
def student_info(name, age=20, course="BCA"):
    print(name)
    print(age)
    print(course)
```

Calling:

```python
student_info("Akanksha")
```

uses both default values.

We can also provide different values:

```python
student_info("Akanksha", 21, "Data Science")
```

---

# 🔙 Default Arguments with `return`

Default arguments can also be used with `return`.

Example:

```python
def add(a, b=10):
    return a + b
```

Calling:

```python
print(add(5))
```

Output:

```text
15
```

Calling:

```python
print(add(5, 20))
```

Output:

```text
25
```

---

# 🏷️ What are Keyword Arguments?

Keyword arguments are arguments passed using the parameter name.

Example:

```python
def student(name, age, course):
    print(name)
    print(age)
    print(course)

student(
    name="Akanksha",
    age=20,
    course="BCA"
)
```

Here we explicitly specify which value belongs to which parameter.

---

# 🔀 Keyword Arguments Can Be in Different Order

With keyword arguments, we can provide arguments in a different order.

Example:

```python
student(
    course="BCA",
    name="Akanksha",
    age=20
)
```

Python matches each value with its parameter name.

---

# 📍 Positional vs Keyword Arguments

### Positional Arguments

Values are matched according to their position.

```python
def add(a, b):
    return a + b

add(10, 20)
```

Here:

```text
10 → a
20 → b
```

### Keyword Arguments

Values are matched using parameter names.

```python
add(a=10, b=20)
```

Here the parameter names are explicitly written.

---

# 🔀 Mixing Positional and Keyword Arguments

We can use a positional argument followed by a keyword argument.

Example:

```python
def calculate_area(length, width):
    return length * width

calculate_area(10, width=5)
```

Here:

```text
10 → positional argument
width=5 → keyword argument
```

The positional argument comes first.

---

# 🧾 Practical Example: Bill Calculation

Default arguments can be useful when a value normally has a common default.

Example:

```python
def calculate_bill(price, quantity=1):
    total = price * quantity
    return total
```

Calling:

```python
calculate_bill(100)
```

means:

```text
price = 100
quantity = 1
```

Calling:

```python
calculate_bill(100, 3)
```

means:

```text
price = 100
quantity = 3
```

---

# 📊 Practical Example: Passing Marks

We can also use default values in conditions.

```python
def check_marks(marks, passing=40):
    if marks >= passing:
        return "Pass"
    else:
        return "Fail"
```

Calling:

```python
check_marks(60)
```

uses `40` as the passing mark.

We can also change it:

```python
check_marks(35, 30)
```

Now the passing mark is `30`.

---

# 📝 Practice Tasks

Today I practiced:

- Creating functions with default arguments
- Changing default values
- Using multiple default arguments
- Using keyword arguments
- Using positional arguments
- Mixing positional and keyword arguments
- Using default arguments with `return`
- Creating practical functions using arguments

The solutions are available in [`tasks.py`](tasks.py).

---

# 📊 Data Science Connection

Default and keyword arguments are useful when creating reusable functions for Data Science.

For example, a data-processing function might have a common default setting but allow us to change it when needed.

Keyword arguments can also make function calls easier to understand when a function has several parameters.

These concepts will become useful as Python programs become larger and more structured.

---

# 🧠 Key Takeaways

- Default arguments already have a value.
- A default value is used when no argument is provided.
- We can override a default value by providing another argument.
- Keyword arguments use parameter names.
- Positional arguments depend on position.
- Keyword arguments make the parameter being assigned explicit.
- Positional arguments should come before keyword arguments when mixing them.
- Default arguments can be used with `return`.

---

# 🎯 Progress

**Day 28 completed!** ✅

Today I learned about default arguments and keyword arguments and practiced using them in reusable Python functions.

I am continuing to strengthen my Python foundation step by step toward my goal of becoming a Data Scientist. 🚀
