# Day 29 - File Handling Basics

# ==========================================
# 1. What is File Handling?
# ==========================================

File handling allows Python to create,
 read, write and update files.

# ==========================================
# 2. Creating and Writing to a File
# ==========================================

file = open("student.txt", "w")
file.write("Name: Akanksha\n")
file.write("Course: BCA\n")
file.write("Goal: Data Scientist\n")
file.close()

print("File created and written successfully.")


# ==========================================
# 3. Reading a File
# ==========================================

file = open("student.txt", "r")

content = file.read()

print("\nFile Content:")
print(content)

file.close()


# ==========================================
# 4. Reading One Line
# ==========================================

file = open("student.txt", "r")

first_line = file.readline()

print("First Line:")
print(first_line)

file.close()


# ==========================================
# 5. Reading All Lines
# ==========================================

file = open("student.txt", "r")

lines = file.readlines()

print("All Lines:")
print(lines)

file.close()


# ==========================================
# 6. Appending to a File
# ==========================================

file = open("student.txt", "a")

file.write("Skill: Python\n")

file.close()

print("\nNew information added successfully.")


# ==========================================
# 7. Reading After Appending
# ==========================================

file = open("student.txt", "r")

print("\nUpdated File:")
print(file.read())

file.close()


# ==========================================
# 8. Using with open()
# ==========================================

with open("student.txt", "r") as file:
    content = file.read()

print("\nUsing with open():")
print(content)


# ==========================================
# 9. Writing Multiple Lines
# ==========================================

with open("students.txt", "w") as file:
    file.write("Akanksha\n")
    file.write("Rahul\n")
    file.write("Priya\n")

print("Multiple students written.")


# ==========================================
# 10. Reading Multiple Lines
# ==========================================

with open("students.txt", "r") as file:
    students = file.readlines()

print("\nStudents:")
for student in students:
    print(student.strip())


# ==========================================
# 11. File Modes
# ==========================================

# "r" = Read
# "w" = Write
# "a" = Append

# Example:

with open("example.txt", "w") as file:
    file.write("Python File Handling")


with open("example.txt", "r") as file:
    print("\nExample File:")
    print(file.read())


# ==========================================
# 12. File Handling with a Function
# ==========================================

def save_name(name):
    with open("name.txt", "w") as file:
        file.write(name)

save_name("Akanksha")

print("\nName saved successfully.")


# ==========================================
# 13. Function to Read a File
# ==========================================

def read_name():
    with open("name.txt", "r") as file:
        return file.read()

name = read_name()

print("Saved Name:", name)


# ==========================================
# 14. File Handling with a List
# ==========================================

students = ["Akanksha", "Rahul", "Priya"]

with open("student_list.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("\nStudent list saved.")


# ==========================================
# 15. Reading List from File
# ==========================================

with open("student_list.txt", "r") as file:
    students_from_file = file.readlines()

students_from_file = [student.strip() for student in students_from_file]

print("Students from file:")
print(students_from_file)


# ==========================================
# Data Science Connection
# ==========================================

# File handling is useful in Data Science because
# data can be stored in files and later processed.

# Examples:
# - Reading text files
# - Saving results
# - Storing simple datasets
# - Working with CSV files
# - Loading data for analysis

print("\nFile handling is an important step toward working with datasets.")
