# Day 17 - Tuples


# Example 1: Creating a tuple

marks = (85, 90, 78, 92, 88)

print(marks)


# Example 2: Tuple indexing

marks = (85, 90, 78, 92, 88)

print(marks[0])
print(marks[1])


# Example 3: Negative indexing

marks = (85, 90, 78, 92, 88)

print(marks[-1])
print(marks[-2])


# Example 4: Tuple slicing

marks = (85, 90, 78, 92, 88)

print(marks[0:3])


# Example 5: Tuple length

marks = (85, 90, 78, 92, 88)

print(len(marks))


# Example 6: Tuples are immutable

student = ("Akanksha", 20, "BCA")

print(student)

# The following line would cause an error:
# student[1] = 21


# Example 7: Mixed data types

student = ("Akanksha", 20, 85.5, True)

print(student)


# Example 8: Single-element tuple

number = (10,)

print(number)

print(type(number))


# Example 9: Accessing tuple elements using a for loop

marks = (85, 90, 78, 92, 88)

for mark in marks:
    print(mark)
