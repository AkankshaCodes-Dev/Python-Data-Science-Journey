# Day 24 - Function Basics 🐍

## 📚 Topics Learned

- What is a Function?
- Why Functions are used
- Defining a Function
- Calling a Function
- Function Syntax
- Simple Functions
- Parameters
- Arguments
- Multiple Parameters
- `return`
- Function with `return`
- Difference between `print()` and `return`
- Functions with Conditions
- Basic Function Practice

---

## 🤔 What is a Function?

A function is a reusable block of code that performs a specific task.

Instead of writing the same code again and again, we can create a function once and call it whenever we need it.

Example:

```python
def greet():
    print("Hello, Akanksha!")
```

The function can then be called using:

```python
greet()
```

Output:

```text
Hello, Akanksha!
```

---

# 🛠️ Creating a Function

We use the `def` keyword to create a function.

Basic syntax:

```python
def function_name():
    statement
```

Example:

```python
def welcome():
    print("Welcome to Python learning!")
```

Here:

- `def` is used to define the function.
- `welcome` is the function name.
- `()` contains parameters if needed.
- The indented code is the function body.

---

# 📞 Calling a Function

Creating a function does not automatically execute it.

We need to call the function.

Example:

```python
def greet():
    print("Hello!")

greet()
```

The line:

```python
greet()
```

calls the function.

---

# 🎯 Why Use Functions?

Functions help us:

- Reuse code
- Avoid repeating code
- Organize programs
- Make code easier to understand
- Break large problems into smaller parts

For example, instead of writing addition code multiple times, we can create one function.

```python
def add(a, b):
    print(a + b)
```

Then we can use it many times:

```python
add(10, 20)
add(5, 15)
add(100, 200)
```

---

# 📦 Function with a Parameter

A parameter is a variable that receives a value when the function is called.

Example:

```python
def greet_person(name):
    print("Hello", name)
```

Calling the function:

```python
greet_person("Akanksha")
```

Output:

```text
Hello Akanksha
```

Here:

```text
name
```

is the parameter.

---

# 📝 Parameter vs Argument

These two terms are important.

Example:

```python
def greet_person(name):
    print("Hello", name)
```

Here `name` is the **parameter**.

When we call:

```python
greet_person("Akanksha")
```

`"Akanksha"` is the **argument**.

### Simple meaning:

**Parameter → variable in the function definition**

**Argument → actual value passed to the function**

---

# ➕ Function with Two Parameters

A function can have more than one parameter.

Example:

```python
def add_numbers(a, b):
    print(a + b)
```

Calling:

```python
add_numbers(10, 20)
```

Output:

```text
30
```

Here:

- `a` receives `10`
- `b` receives `20`

---

# 👩‍🎓 Function with Multiple Parameters

A function can have multiple parameters.

Example:

```python
def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
```

Calling:

```python
student_info("Akanksha", 20, "BCA")
```

Output:

```text
Name: Akanksha
Age: 20
Course: BCA
```

---

# 🔙 What is `return`?

The `return` statement sends a value back from a function.

Example:

```python
def add(a, b):
    return a + b
```

Now we can store the returned value:

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

This is an important difference.

### `print()`

`print()` displays something on the screen.

```python
def add(a, b):
    print(a + b)
```

The result is displayed.

### `return`

`return` sends the result back to the place where the function was called.

```python
def add(a, b):
    return a + b
```

We can store the result:

```python
result = add(10, 20)

print(result)
```

### Simple difference:

```text
print() → displays the result

return → sends the result back
```

---

# ✖️ Function Returning a Value

Example:

```python
def multiply(a, b):
    return a * b
```

Calling:

```python
result = multiply(5, 4)

print(result)
```

Output:

```text
20
```

---

# 🔢 Function Returning a String

A function can return different types of values.

Example:

```python
def get_message():
    return "I am learning Python"

message = get_message()

print(message)
```

Output:

```text
I am learning Python
```

---

# ⬛ Function with a Parameter and `return`

Example:

```python
def square(number):
    return number * number
```

Calling:

```python
result = square(5)

print(result)
```

Output:

```text
25
```

The function receives a number and returns its square.

---

# 🔀 Function with a Condition

Functions can also contain `if-else`.

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
print(check_even(7))
```

Output:

```text
Even
Odd
```

This shows that functions can combine with concepts we have already learned, such as:

- Variables
- Operators
- Conditions
- Strings
- `return`

---

# 📝 Practice Tasks

Today I practiced:

- Creating simple functions
- Calling functions
- Using parameters
- Passing arguments
- Using multiple parameters
- Returning values
- Using `print()`
- Understanding `print()` vs `return`
- Creating functions with conditions
- Creating functions for simple problems

The solutions are available in [`tasks.py`](tasks.py).

---

# 📊 Data Science Connection

Functions are an important Python foundation for Data Science.

When working with data, we often need to perform the same operation multiple times.

Functions allow us to write the logic once and reuse it.

For example, later we may create functions for:

- Cleaning data
- Calculating values
- Transforming data
- Checking data
- Processing dataset values

Understanding functions now will make it easier to work with larger Data Science programs later.

---

# 🧠 Key Takeaways

- A function is a reusable block of code.
- `def` is used to create a function.
- A function must be called to execute it.
- Parameters receive values inside a function.
- Arguments are the actual values passed to a function.
- A function can have multiple parameters.
- `return` sends a value back from a function.
- `print()` displays a value.
- Functions can contain conditions and other Python concepts.

---

# 🎯 Progress

**Day 24 completed!** ✅

Today I learned the basics of Python Functions and practiced creating, calling, and using functions with parameters and `return`.

I am continuing to build my Python foundation step by step toward my goal of becoming a Data Scientist. 🚀
