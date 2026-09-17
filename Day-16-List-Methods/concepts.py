# Day 16 - List Methods


# Example 1: append()

fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")

print(fruits)


# Example 2: insert()

fruits = ["Apple", "Banana", "Mango"]

fruits.insert(1, "Orange")

print(fruits)


# Example 3: remove()

fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)


# Example 4: pop()

fruits = ["Apple", "Banana", "Mango"]

fruits.pop(1)

print(fruits)


# Example 5: sort()

numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)


# Example 6: reverse()

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print(numbers)


# Example 7: clear()

numbers = [1, 2, 3, 4, 5]

numbers.clear()

print(numbers)


# Example 8: index()

fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Banana"))


# Example 9: count()

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))


# Example 10: Combining list methods

numbers = [5, 2, 8, 1, 3]

numbers.append(10)
numbers.sort()
numbers.reverse()

print(numbers)
