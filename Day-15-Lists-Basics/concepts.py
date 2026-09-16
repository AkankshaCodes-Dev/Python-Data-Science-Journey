# Day 15 - Lists Basics


# Example 1: Creating a list

marks = [85, 90, 78, 92, 88]

print(marks)


# Example 2: List indexing

marks = [85, 90, 78, 92, 88]

print(marks[0])
print(marks[1])


# Example 3: Negative indexing

marks = [85, 90, 78, 92, 88]

print(marks[-1])
print(marks[-2])


# Example 4: List slicing

marks = [85, 90, 78, 92, 88]

print(marks[0:3])


# Example 5: Lists are mutable

marks = [85, 90, 78, 92, 88]

marks[2] = 80

print(marks)


# Example 6: Mixed data types

student = ["Akanksha", 20, 85.5, True]

print(student)


# Example 7: Printing list elements one by one

marks = [85, 90, 78, 92, 88]

for mark in marks:
    print(mark)


# Example 8: Finding length of a list

marks = [85, 90, 78, 92, 88]

print(len(marks))
