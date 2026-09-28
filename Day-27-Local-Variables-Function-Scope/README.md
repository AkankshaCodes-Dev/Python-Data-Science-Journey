# Day 27 - Local Variables and Function Scope 🐍

## 📚 Topics Learned

- Local variables
- Function scope
- Creating variables inside functions
- Using local variables with parameters
- Local variables with `return`
- Local variables with conditions
- Local variables with loops
- Local variables with strings
- Difference between local variables and outside variables

---

## 🤔 What is a Local Variable?

A local variable is a variable created inside a function.

Example:

```python
def greet():
    message = "Hello!"
    print(message)

greet()
```

Here:

```text
message
```

is a local variable because it is created inside the `greet()` function.

---

# 📦 Function Scope

Scope means the area of the program where a variable can be accessed.

A local variable belongs to the function where it is created.

Example:

```python
def add(a, b):
    total = a + b
    return total
```

Here:

```text
a
b
total
```

are available inside the function.

The variable `total` is a local variable.

---

# 🔢 Local Variable with Parameters

Example:

```python
def square(number):
    result = number * number
    return result
```

Here:

```text
number → parameter
result → local variable
```

When we call:

```python
answer = square(5)
```

The function calculates:

```text
5 × 5 = 25
```

and returns `25`.

---

# 🔙 Local Variable with `return`

A local variable can be returned from a function.

Example:

```python
def add(a, b):
    total = a + b
    return total
```

Calling:

```python
result = add(10, 20)

print(result)
```

Output:

```text
30
```

The variable `total` is local to the function, but its value is returned to the caller.

---

# 📊 Multiple Local Variables

A function can have more than one local variable.

Example:

```python
def student_result(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3

    return total, average
```

Here:

```text
total → local variable
average → local variable
```

The function returns both values.

```python
total, average = student_result(80, 90, 70)
```

---

# 🔀 Local Variables with Conditions

Local variables can also be created depending on a condition.

Example:

```python
def check_number(number):
    if number > 0:
        result = "Positive"
    elif number < 0:
        result = "Negative"
    else:
        result = "Zero"

    return result
```

Calling:

```python
print(check_number(10))
```

Output:

```text
Positive
```

---

# 🔁 Local Variables with Loops

Local variables are often used with loops.

Example:

```python
def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total
```

Here:

```text
total
number
```

are variables used inside the function.

Calling:

```python
numbers = [10, 20, 30]

print(calculate_sum(numbers))
```

Output:

```text
60
```

---

# 🔤 Local Variables with Strings

We can also use local variables when processing strings.

Example:

```python
def clean_name(name):
    cleaned_name = name.strip().lower()
    return cleaned_name
```

Calling:

```python
result = clean_name("   AKANKSHA   ")

print(result)
```

Output:

```text
akanksha
```

Here:

```text
name → parameter
cleaned_name → local variable
```

---

# 🆚 Local Variable vs Variable Outside Function

Example:

```python
name = "Akanksha"

def greet():
    message = "Hello"
    print(message)
```

Here:

```text
name
```

is created outside the function.

But:

```text
message
```

is created inside the function.

So:

```text
name → outside the function
message → local to greet()
```

For now, the important rule is:

**A variable created inside a function is local to that function.**

---

# ⚠️ Important Example

Consider:

```python
def greet():
    message = "Hello"
    print(message)

greet()
```

This works because `message` is used inside the function where it was created.

The following is different:

```python
def greet():
    message = "Hello"

greet()

print(message)
```

The variable `message` is local to `greet()`, so we should not use it as though it were created outside the function.

---

# 📝 Practice Tasks

Today I practiced:

- Creating local variables
- Using local variables with parameters
- Returning local variables
- Using local variables with calculations
- Using local variables with conditions
- Using local variables with loops
- Using local variables with strings
- Finding the largest value using a local variable

The solutions are available in [`tasks.py`](tasks.py).

---

# 📊 Data Science Connection

Local variables are useful when writing functions for Data Science tasks.

For example, a function may receive dataset values as arguments and use local variables to:

- Calculate totals
- Calculate averages
- Count values
- Clean text
- Process numbers
- Transform data

This helps keep temporary calculations inside the function instead of unnecessarily creating variables outside it.

---

# 🧠 Key Takeaways

- A local variable is created inside a function.
- Local variables belong to the function where they are created.
- Parameters are available inside the function.
- Local variables can be used with calculations.
- Local variables can be used with conditions.
- Local variables can be used with loops.
- Local variables can be returned using `return`.
- Keeping temporary calculations inside functions makes code more organized.

---

# 🎯 Progress

**Day 27 completed!** ✅

Today I learned about local variables and function scope and practiced using them with parameters, conditions, loops, strings, and `return`.

I am continuing to strengthen my Python foundation step by step toward my goal of becoming a Data Scientist. 🚀
