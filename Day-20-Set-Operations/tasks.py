# Day 20 - Set Operations Practice Tasks


# Task 1: Find the union of two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1.union(set2))


# Task 2: Find the intersection of two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Intersection:", set1.intersection(set2))


# Task 3: Find the difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Difference:", set1.difference(set2))


# Task 4: Find the symmetric difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Symmetric Difference:", set1.symmetric_difference(set2))


# Task 5: Use the | operator
set1 = {"Python", "SQL"}
set2 = {"SQL", "Excel"}

print("All skills:", set1 | set2)


# Task 6: Use the & operator
set1 = {"Python", "SQL", "Pandas"}
set2 = {"SQL", "Pandas", "Excel"}

print("Common skills:", set1 & set2)


# Task 7: Use the - operator
set1 = {"Python", "SQL", "Pandas"}
set2 = {"SQL", "Excel"}

print("Only in first set:", set1 - set2)


# Task 8: Use the ^ operator
set1 = {"Python", "SQL", "Pandas"}
set2 = {"SQL", "Excel"}

print("Skills in only one set:", set1 ^ set2)


# Task 9: Student subjects
student1 = {"Python", "Maths", "OS"}
student2 = {"Python", "DBMS", "Maths"}

print("All subjects:", student1 | student2)
print("Common subjects:", student1 & student2)
print("Only student 1:", student1 - student2)
