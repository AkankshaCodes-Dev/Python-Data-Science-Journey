# Day 21 - Dictionary Practice Tasks

# Task 1
student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

print(student["name"])
print(student["course"])


# Task 2
student["year"] = 3
print(student)


# Task 3
student["goal"] = "Data Scientist"
print(student)


# Task 4
student["age"] = 21
print(student)


# Task 5
print(student.keys())
print(student.values())
print(student.items())


# Task 6
if "course" in student:
    print("Course exists")


# Task 7
student.pop("goal")
print(student)
