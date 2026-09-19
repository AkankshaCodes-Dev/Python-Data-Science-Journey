# Day 18 - Tuple Methods and Tuple Unpacking


# Example 1: count()

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))


# Example 2: index()

fruits = ("Apple", "Banana", "Mango")

print(fruits.index("Banana"))


# Example 3: Tuple unpacking

student = ("Akanksha", 20, "BCA")

name, age, course = student

print(name)
print(age)
print(course)


# Example 4: Tuple unpacking with marks

marks = (85, 90, 78)

maths, science, english = marks

print("Maths:", maths)
print("Science:", science)
print("English:", english)


# Example 5: Accessing unpacked values

student = ("Akanksha", 20, "Data Science")

name, age, goal = student

print("Name:", name)
print("Age:", age)
print("Goal:", goal)


# Example 6: Tuple with repeated values

numbers = (5, 10, 5, 20, 5, 30)

print("Count:", numbers.count(5))
print("Position:", numbers.index(5))


# Example 7: Tuple unpacking with different data types

data = ("Akanksha", 85.5, True)

name, score, passed = data

print(name)
print(score)
print(passed)
