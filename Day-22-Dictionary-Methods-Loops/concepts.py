# Day 22 - Dictionary Methods and Loops


# ==========================================
# 1. keys()
# ==========================================

student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

print(student.keys())


# ==========================================
# 2. values()
# ==========================================

student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

print(student.values())


# ==========================================
# 3. items()
# ==========================================

student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

print(student.items())


# ==========================================
# 4. get()
# ==========================================

student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

print(student.get("name"))
print(student.get("course"))


# ==========================================
# 5. get() with a missing key
# ==========================================

print(student.get("city"))
print(student.get("city", "Not Available"))


# ==========================================
# 6. update()
# ==========================================

student = {
    "name": "Akanksha",
    "age": 20
}

student.update({"age": 21})

print(student)


# ==========================================
# 7. Adding a new key using update()
# ==========================================

student.update({"goal": "Data Scientist"})

print(student)


# ==========================================
# 8. pop()
# ==========================================

student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

removed_value = student.pop("age")

print(student)
print("Removed value:", removed_value)


# ==========================================
# 9. clear()
# ==========================================

student = {
    "name": "Akanksha",
    "age": 20
}

student.clear()

print(student)


# ==========================================
# 10. Loop through keys
# ==========================================

student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

for key in student:
    print(key)


# ==========================================
# 11. Loop through values
# ==========================================

for value in student.values():
    print(value)


# ==========================================
# 12. Loop through key-value pairs
# ==========================================

for key, value in student.items():
    print(key, ":", value)


# ==========================================
# 13. Dictionary with marks
# ==========================================

marks = {
    "Python": 85,
    "Maths": 90,
    "OS": 88
}

for subject, mark in marks.items():
    print(subject, ":", mark)


# ==========================================
# 14. Find total marks
# ==========================================

marks = {
    "Python": 85,
    "Maths": 90,
    "OS": 88
}

total = 0

for mark in marks.values():
    total = total + mark

print("Total marks:", total)


# ==========================================
# 15. Find number of subjects
# ==========================================

marks = {
    "Python": 85,
    "Maths": 90,
    "OS": 88
}

print("Number of subjects:", len(marks))
