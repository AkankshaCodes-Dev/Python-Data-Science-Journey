# Day 11 - break, continue & pass 🐍

## 📚 Topics Learned

* `break` statement
* `continue` statement
* `pass` statement
* Using `break` with loops
* Using `continue` with loops
* Using `pass` as a placeholder
* Difference between `break`, `continue`, and `pass`
* Using control statements with `for` and `while` loops

## 🤔 What is `break`?

The `break` statement is used to **stop a loop immediately**.

When Python reaches `break`, the loop ends and the program continues with the code after the loop.

### 💻 Example

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

Output:

```text
1
2
3
4
```

When `i` becomes `5`, the `break` statement stops the loop.

## 🛑 Using `break` with `while`

```python
i = 1

while i <= 10:
    if i == 6:
        break
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

The loop stops when `i` becomes `6`.

---

## 🤔 What is `continue`?

The `continue` statement is used to **skip the current iteration** of a loop.

The loop does not stop completely. It simply moves to the next iteration.

### 💻 Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```text
1
2
4
5
```

When `i` is `3`, `continue` skips that iteration.

The loop then continues with `4`.

## 🔢 Example - Printing Only Odd Numbers

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```

Output:

```text
1
3
5
7
9
```

Here, `continue` skips all the even numbers.

---

## 🤔 What is `pass`?

The `pass` statement is used as a **placeholder**.

It tells Python to do nothing for now.

It is useful when we want to create a block of code but do not want to write its actual logic yet.

### 💻 Example

```python
for i in range(1, 6):
    if i == 3:
        pass
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

`pass` does not stop or skip the loop.

It simply does nothing when Python reaches it.

## 🧩 Example with a Function

```python
def calculate():
    pass
```

This allows us to create the function now and add its actual code later.

---

## 🔍 Difference Between `break`, `continue` and `pass`

| Statement  | What it does                        |
| ---------- | ----------------------------------- |
| `break`    | Stops the entire loop               |
| `continue` | Skips the current iteration         |
| `pass`     | Does nothing; acts as a placeholder |

### Easy way to remember:

```text
break     → STOP the loop 🛑
continue  → SKIP this iteration ⏭️
pass      → DO NOTHING 🤐
```

---

## 💻 Example Using All Three

```python
for i in range(1, 6):

    if i == 2:
        continue

    if i == 4:
        break

    print(i)
```

Output:

```text
1
3
```

### How it works:

* `i = 1` → printed
* `i = 2` → `continue` → skipped
* `i = 3` → printed
* `i = 4` → `break` → loop stops
* `i = 5` → never reached

---

## 📝 Practice Tasks

Today I practiced:

* Stop a loop using `break`
* Skip a number using `continue`
* Print odd numbers using `continue`
* Stop a loop when a specific number is reached
* Use `pass` as a placeholder
* Understand the difference between `break`, `continue`, and `pass`
* Practice `break` and `continue` with loops

The solutions are available in `tasks.py`.

## 📊 Data Science Connection

`break`, `continue`, and `pass` are useful for controlling how loops behave.

In Data Science, loops can be used when processing data, checking values, searching for conditions, or performing repeated operations.

For example:

* `break` can stop processing when a required condition is found.
* `continue` can skip unwanted or invalid values.
* `pass` can be used temporarily while building program logic.

Understanding these control statements will help me write more flexible and efficient Python programs.

## 🎯 Progress

**Day 11 completed!** ✅

Today I learned how to control the flow of loops using `break`, `continue`, and `pass`.

I also learned the difference between stopping a loop, skipping an iteration, and doing nothing.

Continuing to build my Python foundation for Data Science. 🚀
