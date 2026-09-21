# Day 20 - Set Operations

# Example 1: Union
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.union(set2)
print("Union:", result)


# Example 2: Intersection
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.intersection(set2)
print("Intersection:", result)


# Example 3: Difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.difference(set2)
print("Difference:", result)


# Example 4: Symmetric Difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = set1.symmetric_difference(set2)
print("Symmetric Difference:", result)


# Example 5: Union using |
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)


# Example 6: Intersection using &
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Intersection:", set1 & set2)


# Example 7: Difference using -
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Difference:", set1 - set2)


# Example 8: Symmetric Difference using ^
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Symmetric Difference:", set1 ^ set2)


# Example 9: Students learning Python
python_students = {"Akanksha", "Rahul", "Priya", "Anu"}
java_students = {"Rahul", "Priya", "Kiran"}

print("All students:", python_students | java_students)
print("Students learning both:", python_students & java_students)
print("Only Python:", python_students - java_students)
print("Only one subject:", python_students ^ java_students)
