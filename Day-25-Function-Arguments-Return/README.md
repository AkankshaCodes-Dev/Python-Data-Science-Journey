# Day 25 - Function Arguments and Return 🐍

## 📚 Topics Learned

- Function arguments
- Positional arguments
- Multiple arguments
- Parameters vs Arguments
- `return`
- Returning values
- Storing returned values
- Using returned values in calculations
- Returning strings
- Returning Boolean values
- Functions with arguments and `return`
- Basic function practice

---

## 🤔 What are Function Arguments?

Arguments are the actual values that we pass to a function when calling it.

Example:

```python
def greet(name):
    print("Hello", name)

greet("Akanksha")
```

Here:

- `name` is the parameter.
- `"Akanksha"` is the argument.

### Simple meaning:

**Parameter → variable written in the function definition**

**Argument → actual value passed when calling the function**

---

## 📦 Function with Multiple Arguments

A function can accept multiple arguments.

Example:

```python
def add_numbers(a, b):
    print(a + b)

add_numbers(10, 20)
```

Here:

- `a` receives `10`
- `b` receives `20`

Output:

```text
30
```

---

## 📍 Positional Arguments

When arguments are passed according to their position, they are called positional arguments.

Example:

```python
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info("Akanksha", 20)
```

The first argument goes to `name`.

The second argument goes to `age`.

So:

```text
"Akanksha" → name
20 → age
```

---

# 🔙 What is `return`?

The `return` statement sends a value back from a function.

Example:

```python
def add(a, b):
    return a + b
```

When we call:

```python
result = add(10, 20)
```

The function returns:

```text
30
```

And `30` is stored in:

```python
result
```

We can then use it:

```python
print(result)
```

Output:

```text
30
```

---

# 🖨️ `print()` vs `return`

This is one of the most important concepts from today.

### Using `print()`

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

The result is displayed directly.

### Using `return`

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

The function sends the value back, so we can store and use it.

### Simple difference:

```text
print() → displays the value

return → sends the value back from the function
```

---

# 💾 Storing a Returned Value

A returned value can be stored in a variable.

Example:

```python
def multiply(a, b):
    return a * b

result = multiply(5, 4)

print(result)
```

Output:

```text
20
```

Here:

```python
result = multiply(5, 4)
```

stores the returned value.

---

# ➕ Using a Returned Value Again

One important advantage of `return` is that we can use the returned value in another calculation.

Example:

```python
def multiply(a, b):
    return a * b

result = multiply(5, 4)

final_result = result + 10

print(final_result)
```

Output:

```text
30
```

The returned value can be used like any other value.

---

# 🔤 Returning a String

A function can return a string.

Example:

```python
def get_course():
    return "BCA"

course = get_course()

print(course)
```

Output:

```text
BCA
```

---

# ✅ Returning Boolean Values

A function can also return `True` or `False`.

Example:

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
```

Calling:

```python
print(is_even(10))
print(is_even(7))
```

Output:

```text
True
False
```

This type of function is useful when we need to check a condition.

---

# 🔢 Arguments + `return` Together

Arguments and `return` are often used together.

Example:

```python
def square(number):
    return number * number

result = square(8)

print(result)
```

Here:

```text
number → parameter
8 → argument
number * number → calculation
return → sends result back
result → stores returned value
```

---

# 📊 Example: Average

We can use multiple arguments and `return` together.

```python
def calculate_average(a, b, c):
    total = a + b + c
    average = total / 3
    return average

result = calculate_average(80, 90, 70)

print(result)
```

Output:

```text
80.0
```

---

# 📝 Practice Tasks

Today I practiced:

- Passing arguments to functions
- Using one argument
- Using multiple arguments
- Understanding parameters and arguments
- Returning numbers
- Returning strings
- Returning Boolean values
- Storing returned values
- Using returned values in calculations
- Creating functions with arguments and `return`

The solutions are available in [`tasks.py`](tasks.py).

---

# 📊 Data Science Connection

Functions with arguments and `return` are very important for Data Science.

When working with data, we often need to perform the same operation on different values.

Instead of writing the same logic again and again, we can create a function and provide different data as arguments.

For example, later we may create functions to:

- Calculate averages
- Clean values
- Transform data
- Check conditions
- Process dataset values
- Perform calculations

This makes programs more reusable and organized.

---

# 🧠 Key Takeaways

- Arguments are values passed to a function.
- Parameters are variables that receive those values.
- A function can have multiple parameters.
- Positional arguments are matched according to their position.
- `return` sends a value back from a function.
- Returned values can be stored in variables.
- Returned values can be used in further calculations.
- Functions can return numbers, strings, Boolean values, and other data.
- Arguments and `return` are commonly used together.

---

# 🎯 Progress

**Day 25 completed!** ✅

Today I learned how to use function arguments and `return` values in Python.

I am continuing to build my Python foundation step by step toward my goal of becoming a Data Scientist. 🚀
