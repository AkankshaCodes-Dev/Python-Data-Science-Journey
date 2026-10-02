# Day 31 - File Handling Practice + Exception Handling Practice


# ==========================================
# 1. Write Data to a File
# ==========================================

with open("student.txt", "w") as file:
    file.write("Akanksha\n")
    file.write("BCA\n")
    file.write("Data Science\n")

print("Student data saved.")


# ==========================================
# 2. Read Data from a File
# ==========================================

with open("student.txt", "r") as file:
    content = file.read()

print("\nStudent Data:")
print(content)


# ==========================================
# 3. Append Data
# ==========================================

with open("student.txt", "a") as file:
    file.write("Python\n")

print("New information added.")


# ==========================================
# 4. Read Lines from a File
# ==========================================

with open("student.txt", "r") as file:
    lines = file.readlines()

print("\nLines:")
for line in lines:
    print(line.strip())


# ==========================================
# 5. Write a List to a File
# ==========================================

students = ["Akanksha", "Rahul", "Priya"]

with open("students.txt", "w") as file:
    for student in students:
        file.write(student + "\n")

print("\nStudent list saved.")


# ==========================================
# 6. Read a File into a List
# ==========================================

with open("students.txt", "r") as file:
    students_from_file = file.readlines()

students_from_file = [
    student.strip()
    for student in students_from_file
]

print("Students:", students_from_file)


# ==========================================
# 7. Save Numbers to a File
# ==========================================

numbers = [10, 20, 30, 40, 50]

with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")

print("\nNumbers saved.")


# ==========================================
# 8. Read Numbers from a File
# ==========================================

with open("numbers.txt", "r") as file:
    numbers = file.readlines()

numbers = [int(number.strip()) for number in numbers]

print("Numbers:", numbers)


# ==========================================
# 9. Calculate Sum from File Data
# ==========================================

total = sum(numbers)

print("Total:", total)


# ==========================================
# 10. Calculate Average from File Data
# ==========================================

average = total / len(numbers)

print("Average:", average)


# ==========================================
# 11. Handle Missing File
# ==========================================

try:
    with open("missing.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("\nFile does not exist.")


# ==========================================
# 12. Handle Invalid Number
# ==========================================

value = "hello"

try:
    number = int(value)
    print(number)

except ValueError:
    print("\nInvalid number:", value)


# ==========================================
# 13. Safe Division
# ==========================================

try:
    number1 = 100
    number2 = 0

    result = number1 / number2

    print(result)

except ZeroDivisionError:
    print("\nCannot divide by zero.")


# ==========================================
# 14. File + Exception Handling
# ==========================================

try:
    with open("numbers.txt", "r") as file:
        values = file.readlines()

    numbers = []

    for value in values:
        try:
            numbers.append(int(value.strip()))

        except ValueError:
            print("Invalid value:", value.strip())

    print("\nValid numbers:", numbers)

except FileNotFoundError:
    print("numbers.txt not found.")


# ==========================================
# 15. Function to Save Data
# ==========================================

def save_data(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)

        return "Data saved successfully."

    except Exception:
        return "Something went wrong."


print(save_data("message.txt", "I am learning Python."))


# ==========================================
# 16. Function to Read Data
# ==========================================

def read_data(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        return "File not found."


print(read_data("message.txt"))


# ==========================================
# 17. Safe Average Function
# ==========================================

def safe_average(numbers):
    try:
        return sum(numbers) / len(numbers)

    except ZeroDivisionError:
        return "Cannot calculate average of an empty list."


print(safe_average([10, 20, 30]))
print(safe_average([]))


# ==========================================
# 18. Process Data from File
# ==========================================

def process_numbers(filename):

    try:
        with open(filename, "r") as file:
            values = file.readlines()

        numbers = []

        for value in values:
            try:
                numbers.append(int(value.strip()))

            except ValueError:
                print("Skipping invalid value:", value.strip())

        if len(numbers) == 0:
            return "No valid numbers found."

        total = sum(numbers)
        average = total / len(numbers)

        return total, average

    except FileNotFoundError:
        return "File not found."


result = process_numbers("numbers.txt")

print("\nProcessed Result:", result)


# ==========================================
# Data Science Connection
# ==========================================

# Real-world datasets can contain:
# - Missing files
# - Invalid values
# - Empty data
# - Incorrect data types
# - Unexpected values
#
# File handling allows us to read and save data.
# Exception handling helps us deal with
# unexpected problems while processing data.
