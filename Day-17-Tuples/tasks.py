# Day 17 - Tuples Practice Tasks


# Task 1: Create a student details tuple

student = ("Akanksha", 20, "BCA")

print(student)


# Task 2: Print the first item

print(student[0])


# Task 3: Print the last item

print(student[-1])


# Task 4: Print the second item using negative indexing

print(student[-2])


# Task 5: Slice the tuple

marks = (85, 90, 78, 92, 88)

print(marks[0:3])


# Task 6: Find the length of the tuple

print(len(marks))


# Task 7: Create a single-element tuple

number = (100,)

print(number)

print(type(number))


# Task 8: Print all elements one by one

for mark in marks:
    print(mark)


# Task 9: Try changing an element

# Tuples are immutable, so this will produce an error:
# marks[0] = 100
