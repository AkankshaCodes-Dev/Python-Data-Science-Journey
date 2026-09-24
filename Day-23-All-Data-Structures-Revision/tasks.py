# Day 23 - All Data Structures Revision Practice


# ==========================================
# TASK 1 - LIST
# ==========================================

marks = [85, 90, 78, 92, 88]

print("First mark:", marks[0])
print("Last mark:", marks[-1])

marks[2] = 80

print("Updated marks:", marks)


# ==========================================
# TASK 2 - LIST METHODS
# ==========================================

numbers = [50, 20, 40, 10, 30]

numbers.append(60)
numbers.sort()

print("Sorted numbers:", numbers)

numbers.reverse()

print("Reversed numbers:", numbers)


# ==========================================
# TASK 3 - TUPLE
# ==========================================

student = ("Akanksha", 20, "BCA")

name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)


# ==========================================
# TASK 4 - TUPLE METHODS
# ==========================================

numbers = (10, 20, 10, 30, 10, 40)

print("Count:", numbers.count(10))
print("Position:", numbers.index(30))


# ==========================================
# TASK 5 - SET
# ==========================================

numbers = {10, 20, 10, 30, 20, 40}

print("Set:", numbers)

numbers.add(50)

print("After add:", numbers)


# ==========================================
# TASK 6 - SET OPERATIONS
# ==========================================

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union:", set1 | set2)
print("Common:", set1 & set2)
print("Only first:", set1 - set2)
print("Only one set:", set1 ^ set2)


# ==========================================
# TASK 7 - REMOVE DUPLICATES
# ==========================================

numbers = [10, 20, 10, 30, 20, 40, 10]

unique_numbers = list(set(numbers))

print("Original:", numbers)
print("Without duplicates:", unique_numbers)


# ==========================================
# TASK 8 - DICTIONARY
# ==========================================

student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

print(student["name"])
print(student["course"])

student["goal"] = "Data Scientist"

print(student)


# ==========================================
# TASK 9 - DICTIONARY METHODS
# ==========================================

print(student.keys())
print(student.values())
print(student.items())

print(student.get("goal"))

student.update({"age": 21})

print(student)

student.pop("age")

print(student)


# ==========================================
# TASK 10 - DICTIONARY LOOP
# ==========================================

marks = {
    "Python": 85,
    "Maths": 90,
    "OS": 88,
    "DBMS": 82
}

for subject, mark in marks.items():
    print(subject, ":", mark)


# ==========================================
# TASK 11 - TOTAL AND AVERAGE
# ==========================================

total = 0

for mark in marks.values():
    total = total + mark

average = total / len(marks)

print("Total:", total)
print("Average:", average)


# ==========================================
# TASK 12 - CHOOSE THE CORRECT DATA STRUCTURE
# ==========================================

# Ordered and changeable collection
student_marks = [85, 90, 88]

# Fixed collection
student_details = ("Akanksha", 20, "BCA")

# Unique values
subjects = {"Python", "Maths", "Python"}

# Key-value information
student = {
    "name": "Akanksha",
    "age": 20
}

print(student_marks)
print(student_details)
print(subjects)
print(student)


# ==========================================
# TASK 13 - MIXED DATA STRUCTURE
# ==========================================

student_data = {
    "name": "Akanksha",
    "marks": [85, 90, 88],
    "subjects": {"Python", "Maths", "OS"},
    "details": ("BCA", 20)
}

print("Name:", student_data["name"])
print("Marks:", student_data["marks"])
print("Subjects:", student_data["subjects"])
print("Details:", student_data["details"])
