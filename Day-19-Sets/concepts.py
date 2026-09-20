# Day 19 - Sets


# Example 1: Creating a Set

numbers = {10, 20, 30, 40}

print(numbers)


# Example 2: Set with duplicate values

numbers = {10, 20, 10, 30, 20, 40}

print(numbers)


# Example 3: Adding an element

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)


# Example 4: Removing an element

numbers = {10, 20, 30, 40}

numbers.remove(30)

print(numbers)


# Example 5: Finding the length of a Set

numbers = {10, 20, 30, 40}

print(len(numbers))


# Example 6: Set of student subjects

subjects = {"Python", "Maths", "OS", "Python"}

print(subjects)


# Example 7: Accessing Set elements using a for loop

subjects = {"Python", "Maths", "OS"}

for subject in subjects:
    print(subject)


# Example 8: Adding multiple elements using update()

numbers = {10, 20, 30}

numbers.update([40, 50, 60])

print(numbers)


# Example 9: Removing an element using discard()

numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)
