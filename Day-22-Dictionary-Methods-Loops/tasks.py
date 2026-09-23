# Day 22 - Dictionary Methods and Loops Practice Tasks


# Task 1: Print all keys

student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

for key in student.keys():
    print(key)


# Task 2: Print all values

for value in student.values():
    print(value)


# Task 3: Print key-value pairs

for key, value in student.items():
    print(key, ":", value)


# Task 4: Use get() to access a value

print(student.get("name"))
print(student.get("course"))


# Task 5: Use get() with a missing key

print(student.get("city", "City not found"))


# Task 6: Update a dictionary

student.update({"age": 21})

print(student)


# Task 7: Add a new key using update()

student.update({"goal": "Data Scientist"})

print(student)


# Task 8: Remove a value using pop()

student.pop("age")

print(student)


# Task 9: Create a marks dictionary and print subjects

marks = {
    "Python": 85,
    "Maths": 90,
    "OS": 88,
    "DBMS": 82
}

for subject in marks.keys():
    print(subject)


# Task 10: Print marks using a loop

for mark in marks.values():
    print(mark)


# Task 11: Print subject and marks

for subject, mark in marks.items():
    print(subject, ":", mark)


# Task 12: Find total marks

total = 0

for mark in marks.values():
    total = total + mark

print("Total:", total)


# Task 13: Find average marks

total = 0

for mark in marks.values():
    total = total + mark

average = total / len(marks)

print("Average:", average)


# Task 14: Find subjects with marks greater than 85

for subject, mark in marks.items():
    if mark > 85:
        print(subject, ":", mark)
