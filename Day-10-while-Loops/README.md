# Day 10 - while Loops 🐍

## 📚 Topics Learned

* `while` loop
* `while` loop syntax
* Conditions in `while`
* Loop flow
* Updating variables
* `while` with numbers
* `while` with user input
* Difference between `for` and `while`

## 🤔 What is a `while` Loop?

A `while` loop repeats a block of code as long as a condition is `True`.

Basic syntax:

```python
while condition:
    statement
```

## 💻 Example

```python
i = 1

while i <= 5:
    print(i)
    i = i + 1
```

Output:

```text
1
2
3
4
5
```

The loop continues while `i <= 5` is true.

## 🔄 Updating the Variable

It is important to update the variable used in the condition.

```python
i = i + 1
```

Without updating `i`, the condition may remain true and the loop could continue indefinitely.

## 🔢 Reverse Counting

```python
i = 5

while i >= 1:
    print(i)
    i = i - 1
```

Output:

```text
5
4
3
2
1
```

## 🔍 `for` vs `while`

### `for` loop

Usually used when we know how many times we want to repeat something or when we are iterating over a sequence.

```python
for i in range(5):
    print(i)
```

### `while` loop

Used when repetition depends on a condition.

```python
i = 1

while i <= 5:
    print(i)
    i = i + 1
```

## 📝 Practice Tasks

Today I practiced:

* Printing numbers from 1 to 10
* Printing even numbers from 1 to 20
* Reverse counting from 10 to 1
* Printing the multiplication table of 5
* Finding the sum of numbers from 1 to 10

The solutions are available in [`tasks.py`](tasks.py).

## 📊 Data Science Connection

Loops are an important programming foundation for Data Science.

A `while` loop helps build problem-solving skills when a process needs to continue until a condition is satisfied.

Understanding different types of loops will help me understand how repeated operations and data-processing logic work.

## 🎯 Progress

**Day 10 completed!** ✅

Today I learned how to use `while` loops and how to control repetition using conditions.

Continuing to build my Python foundation for Data Science. 🚀
