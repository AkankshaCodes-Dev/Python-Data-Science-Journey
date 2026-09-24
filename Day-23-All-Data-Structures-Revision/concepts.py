# Day 23 - All Data Structures Revision


# ==========================================
# 1. LIST
# ==========================================

marks = [85, 90, 78, 92, 88]

print("List:", marks)
print("First:", marks[0])
print("Last:", marks[-1])
print("Slice:", marks[0:3])

marks[2] = 80
print("Updated list:", marks)

marks.append(95)
print("After append:", marks)

marks.insert(1, 87)
print("After insert:", marks)

marks.remove(87)
print("After remove:", marks)

marks.pop()
print("After pop:", marks)

marks.sort()
print("Sorted:", marks)

marks.reverse()
print("Reversed:", marks)

print("Length:", len(marks))
print("Count of 90:", marks.count(90))


# ==========================================
# 2. TUPLE
# ==========================================

student = ("Akanksha", 20, "BCA")

print("Tuple:", student)
print("First:", student[0])
print("Last:", student[-1])
print("Slice:", student[0:2])

print("Length:", len(student))

name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)

print("Count of 20:", student.count(20))
print("Position of BCA:", student.index("BCA"))


# ==========================================
# 3. SET
# ==========================================

numbers = {10, 20, 10, 30, 20, 40}

print("Set:", numbers)

numbers.add(50)
print("After add:", numbers)

numbers.update([60, 70])
print("After update:", numbers)

numbers.remove(70)
print("After remove:", numbers)

numbers.discard(100)
print("After discard:", numbers)

print("Length:", len(numbers))


# ==========================================
# 4. SET OPERATIONS
# ==========================================

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))

print("Union using |:", set1 | set2)
print("Intersection using &:", set1 & set2)
print("Difference using -:", set1 - set2)
print("Symmetric Difference using ^:", set1 ^ set2)


# ==========================================
# 5. DICTIONARY
# ==========================================

student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

print("Dictionary:", student)

print("Name:", student["name"])
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("Goal:", student.get("goal", "Not available"))

student.update({"age": 21})
student.update({"goal": "Data Scientist"})

print("Updated dictionary:", student)

student.pop("age")

print("After pop:", student)


# ==========================================
# 6. DICTIONARY LOOPS
# ==========================================

marks = {
    "Python": 85,
    "Maths": 90,
    "OS": 88,
    "DBMS": 82
}

for subject in marks:
    print("Subject:", subject)

for mark in marks.values():
    print("Mark:", mark)

for subject, mark in marks.items():
    print(subject, ":", mark)


# ==========================================
# 7. FIND TOTAL AND AVERAGE
# ==========================================

total = 0

for mark in marks.values():
    total = total + mark

average = total / len(marks)

print("Total:", total)
print("Average:", average)


# ==========================================
# 8. LIST TO SET
# ==========================================

numbers = [10, 20, 10, 30, 20, 40, 10]

unique_numbers = set(numbers)

print("Original list:", numbers)
print("Unique values:", unique_numbers)


# ==========================================
# 9. SET TO LIST
# ==========================================

unique_list = list(unique_numbers)

print("Set converted to list:", unique_list)


# ==========================================
# 10. TUPLE TO LIST
# ==========================================

data = (10, 20, 30)

data_list = list(data)

print("Tuple:", data)
print("List:", data_list)


# ==========================================
# 11. LIST TO TUPLE
# ==========================================

data_tuple = tuple(data_list)

print("List:", data_list)
print("Tuple:", data_tuple)


# ==========================================
# 12. MIXED DATA STRUCTURE
# ==========================================

student_data = {
    "name": "Akanksha",
    "marks": [85, 90, 88],
    "subjects": {"Python", "Maths", "OS"},
    "details": ("BCA", 20)
}

print("Student data:", student_data)

print("Name:", student_data["name"])
print("Marks:", student_data["marks"])
print("Subjects:", student_data["subjects"])
print("Details:", student_data["details"])
