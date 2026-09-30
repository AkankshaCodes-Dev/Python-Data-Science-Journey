# Day 29 - File Handling Basics
# Tasks with Solutions


# ==========================================
# Task 1 - Create and write to a file
# ==========================================

with open("welcome.txt", "w") as file:
    file.write("Welcome to Python!")

print("File created successfully.")


# ==========================================
# Task 2 - Read the file
# ==========================================

with open("welcome.txt", "r") as file:
    content = file.read()

print(content)


# ==========================================
# Task 3 - Create student information file
# ==========================================

with open("student.txt", "w") as file:
    file.write("Name: Akanksha\n")
    file.write("Course: BCA\n")
    file.write("Goal: Data Scientist\n")

print("Student information saved.")


# ==========================================
# Task 4 - Read the first line
# ==========================================

with open("student.txt", "r") as file:
    first_line = file.readline()

print("First line:")
print(first_line)


# ==========================================
# Task 5 - Create skills file
# ==========================================

with open("skills.txt", "w") as file:
    file.write("Python\n")
    file.write("GitHub\n")
    file.write("Data Science\n")

print("Skills saved.")


# ==========================================
# Task 6 - Append another skill
# ==========================================

with open("skills.txt", "a") as file:
    file.write("Pandas\n")

print("New skill added.")


# ==========================================
# Task 7 - Read and print each skill
# ==========================================

with open("skills.txt", "r") as file:
    skills = file.readlines()

for skill in skills:
    print(skill.strip())


# ==========================================
# Task 8 - save_message() function
# ==========================================

def save_message(message):
    with open("message.txt", "w") as file:
        file.write(message)


save_message("I am learning Python.")

print("Message saved.")


# ==========================================
# Task 9 - read_message() function
# ==========================================

def read_message():
    with open("message.txt", "r") as file:
        return file.read()


message = read_message()

print("Message:")
print(message)


# ==========================================
# Task 10 - Save student names
# ==========================================

students = ["Akanksha", "Rahul", "Priya", "Anjali", "Ravi"]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("Student names saved.")


# ==========================================
# Task 11 - Read students into a list
# ==========================================

with open("students.txt", "r") as file:
    students = file.readlines()

students = [student.strip() for student in students]

print("Students:")
print(students)


# ==========================================
# Task 12 - Save numbers using a function
# ==========================================

def save_numbers(numbers):
    with open("numbers.txt", "w") as file:
        for number in numbers:
            file.write(str(number) + "\n")


save_numbers([10, 20, 30, 40, 50])

print("Numbers saved.")


# ==========================================
# Task 13 - Read numbers and convert to integers
# ==========================================

with open("numbers.txt", "r") as file:
    numbers = file.readlines()

numbers = [int(number.strip()) for number in numbers]

print("Numbers:")
print(numbers)


# ==========================================
# Task 14 - Calculate sum of numbers
# ==========================================

with open("numbers.txt", "r") as file:
    numbers = file.readlines()

numbers = [int(number.strip()) for number in numbers]

total = sum(numbers)

print("Sum:", total)


# ==========================================
# Task 15 - Create goal.txt
# ==========================================

with open("goal.txt", "w") as file:
    file.write("My goal is to become a Data Scientist.")

print("Goal saved successfully.")
