# Day 19 - Sets Practice Tasks


# Task 1: Create a Set of numbers

numbers = {10, 20, 30, 40, 50}

print(numbers)


# Task 2: Create a Set with duplicate values

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)


# Task 3: Add an element to the Set

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)


# Task 4: Remove an element from the Set

numbers = {10, 20, 30, 40}

numbers.remove(20)

print(numbers)


# Task 5: Find the length of the Set

numbers = {10, 20, 30, 40, 50}

print(len(numbers))


# Task 6: Create a Set of student subjects

subjects = {"Python", "Maths", "OS", "DBMS"}

print(subjects)


# Task 7: Print Set elements one by one

for subject in subjects:
    print(subject)


# Task 8: Add multiple elements

numbers = {10, 20, 30}

numbers.update([40, 50])

print(numbers)


# Task 9: Remove an element using discard()

numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)
