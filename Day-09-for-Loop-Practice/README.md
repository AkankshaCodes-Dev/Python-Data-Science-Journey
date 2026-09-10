# Day 9 - for Loop Practice 🐍

## 📚 Topics Practiced

* Factorial of a number
* Multiplication tables from 1 to 5
* Reverse counting
* Sum of even numbers from 1 to 50
* Counting digits of a number
* Applying `for` loops to problems

## 🔢 Factorial

The factorial of a number is the product of all positive integers from 1 up to that number.

Example:

```python
num = 5
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print(factorial)
```

Output:

```text
120
```

## ✖️ Multiplication Tables

I practiced generating multiplication tables from 1 to 5 using loops.

Example:

```python
for number in range(1, 6):
    for i in range(1, 11):
        print(number * i)
```

This also gave me practice with nested loops.

## 🔄 Reverse Counting

```python
for i in range(10, 0, -1):
    print(i)
```

Output:

```text
10
9
8
7
6
5
4
3
2
1
```

## ➕ Sum of Even Numbers

I practiced finding the sum of even numbers from 1 to 50.

```python
total = 0

for i in range(2, 51, 2):
    total = total + i
```

## 🔢 Counting Digits

I also practiced counting the digits of a number using a loop.

```python
num = 12345
count = 0

for digit in str(num):
    count = count + 1

print(count)
```

Output:

```text
5
```

## 📝 Practice Tasks

Today I practiced:

* Finding factorial
* Printing multiplication tables from 1 to 5
* Reverse counting from 10 to 1
* Finding the sum of even numbers from 1 to 50
* Counting digits of a number

The solutions are available in [`tasks.py`](tasks.py).

## 📊 Data Science Connection

Loop practice helps build the problem-solving skills needed for Data Science.

Loops can be used to:

* Process repeated values
* Perform calculations
* Apply operations to data
* Build logical solutions
* Understand how data is processed step by step

Later, I will learn how tools such as NumPy and Pandas can perform many of these operations more efficiently on datasets.

## 🎯 Progress

**Day 9 completed!** ✅

Today I practiced using `for` loops to solve different programming problems instead of only repeating simple statements.

Continuing to strengthen my Python foundation for Data Science. 🚀
