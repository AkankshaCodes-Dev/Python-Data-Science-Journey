# Day 21 - Data Structures Revision

# ==========================================
# 1. LIST
# ==========================================

marks = [85, 90, 78, 92, 88]

print("List:", marks)
print("First mark:", marks[0])

marks.append(95)
print("After append:", marks)


# ==========================================
# 2. TUPLE
# ==========================================

student = ("Akanksha", 20, "BCA")

print("Tuple:", student)
print("Name:", student[0])

name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)


# ==========================================
# 3. SET
# ==========================================

numbers = {10, 20, 10, 30, 20, 40}

print("Set:", numbers)

numbers.add(50)
print("After add:", numbers)


# ==========================================
# 4. DICTIONARY
# ==========================================

student = {
    "name": "Akanksha",
    "age": 20,
    "course": "BCA"
}

print("Dictionary:", student)
print("Name:", student["name"])
print("Course:", student["course"])


# ==========================================
# 5. LIST TO TUPLE
# ==========================================

numbers = [10, 20, 30, 40]

numbers_tuple = tuple(numbers)

print("List:", numbers)
print("Tuple:", numbers_tuple)


# ==========================================
# 6. TUPLE TO LIST
# ==========================================

numbers = (10, 20, 30, 40)

numbers_list = list(numbers)

print("Tuple:", numbers)
print("List:", numbers_list)


# ==========================================
# 7. LIST TO SET
# ==========================================

numbers = [10, 20, 10, 30, 20, 40]

numbers_set = set(numbers)

print("Original List:", numbers)
print("Set:", numbers_set)


# ==========================================
# 8. REMOVING DUPLICATES
# ==========================================

numbers = [10, 20, 10, 30, 20, 40, 10]

unique_numbers = list(set(numbers))

print("Original:", numbers)
print("Without duplicates:", unique_numbers)


# ==========================================
# 9. COMMON VALUES
# ==========================================

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

common = set1.intersection(set2)

print("Common values:", common)


# ==========================================
# 10. UNIQUE VALUES FROM BOTH SETS
# ==========================================

set1 = {10, 20, 30}
set2 = {30, 40, 50}

unique = set1.symmetric_difference(set2)

print("Unique values:", unique)
