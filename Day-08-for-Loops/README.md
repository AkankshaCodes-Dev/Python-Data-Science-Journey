# Day 8 - for Loops 🐍

## 📚 Topics Learned

* Loops
* `for` loop
* `range()`
* Loop flow
* Repeating code
* Using `for` with `range()`

## 🤔 What is a Loop?

A loop allows us to repeat a block of code multiple times.

Instead of writing the same code again and again, we can use a loop to repeat it efficiently.

## 🔄 for Loop

Basic syntax:

```python
for variable in sequence:
    statement
```

Example:

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

## 🔢 Using range()

The `range()` function is used to generate a sequence of numbers.

Example:

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

The ending value in `range()` is not included.

## 🔁 Using Step

We can also provide a step value.

```python
for i in range(2, 21, 2):
    print(i)
```

This prints even numbers from 2 to 20.

## 📝 Practice Tasks

Today I practiced:

* Printing numbers from 1 to 10
* Printing even numbers from 1 to 20
* Printing the multiplication table of 5
* Printing my name 5 times
* Reverse counting from 10 to 1

The solutions are available in [`tasks.py`](tasks.py).

## 📊 Data Science Connection

Loops are an important programming foundation for Data Science.

They help us understand how repeated operations can be performed on data.

Later, I will learn tools such as NumPy and Pandas for working with larger datasets.

## 🎯 Progress

**Day 8 completed!** ✅

Today I learned how to use `for` loops and `range()` to repeat tasks efficiently.

Continuing to build my Python foundation for Data Science. 🚀
