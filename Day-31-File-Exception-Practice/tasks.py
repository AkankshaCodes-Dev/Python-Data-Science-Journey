# Day 31 - File Handling Practice + Exception Handling Practice
# Tasks with Solutions


# ==========================================
# Task 1
# Create notes.txt and write three lines
# ==========================================

with open("notes.txt", "w") as file:
    file.write("I am learning Python.\n")
    file.write("I am practicing File Handling.\n")
    file.write("My goal is Data Science.\n")

print("Notes saved.")


# ==========================================
# Task 2
# Read notes.txt
# ==========================================

with open("notes.txt", "r") as file:
    content = file.read()

print("Notes:")
print(content)


# ==========================================
# Task 3
# Append one more line
# ==========================================

with open("notes.txt", "a") as file:
    file.write("I am also learning Exception Handling.\n")

print("New line added.")


# ==========================================
# Task 4
# Read notes.txt using readlines()
# ==========================================

with open("notes.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())


# ==========================================
# Task 5
# Save five numbers to numbers.txt
# ==========================================

numbers = [10, 20, 30, 40, 50]

with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(str(number) + "\n")

print("Numbers saved.")


# ==========================================
# Task 6
# Read numbers and convert to integers
# ==========================================

with open("numbers.txt", "r") as file:
    values = file.readlines()

numbers = []

for value in values:
    numbers.append(int(value.strip()))

print("Numbers:", numbers)


# ==========================================
# Task 7
# Calculate sum and average
# ==========================================

total = sum(numbers)
average = total / len(numbers)

print("Total:", total)
print("Average:", average)


# ==========================================
# Task 8
# Handle FileNotFoundError
# ==========================================

try:
    with open("data.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("data.txt was not found.")


# ==========================================
# Task 9
# Divide two user-entered numbers
# Handle ValueError and ZeroDivisionError
# ==========================================

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2

    print("Result:", result)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ==========================================
# Task 10
# save_message(message)
# Use exception handling
# ==========================================

def save_message(message):
    try:
        with open("message.txt", "w") as file:
            file.write(message)

        print("Message saved successfully.")

    except Exception:
        print("Something went wrong while saving the message.")


save_message("I am learning Python.")


# ==========================================
# Task 11
# read_message()
# Handle FileNotFoundError
# ==========================================

def read_message():
    try:
        with open("message.txt", "r") as file:
            return file.read()

    except FileNotFoundError:
        return "Message file not found."


print(read_message())


# ==========================================
# Task 12
# safe_average(numbers)
# Handle empty list
# ==========================================

def safe_average(numbers):
    try:
        return sum(numbers) / len(numbers)

    except ZeroDivisionError:
        return "Cannot calculate average of an empty list."


print(safe_average([10, 20, 30]))
print(safe_average([]))


# ==========================================
# Task 13
# Convert valid values and skip invalid values
# ==========================================

values = ["10", "20", "abc", "40", "hello"]

numbers = []

for value in values:
    try:
        number = int(value)
        numbers.append(number)

    except ValueError:
        print("Skipping invalid value:", value)

print("Valid numbers:", numbers)


# ==========================================
# Task 14
# Create marks.txt and calculate:
# Total, Average, Highest, Lowest
# ==========================================

marks = [80, 75, 90, 65, 88]

with open("marks.txt", "w") as file:
    for mark in marks:
        file.write(str(mark) + "\n")


try:
    with open("marks.txt", "r") as file:
        values = file.readlines()

    marks = []

    for value in values:
        try:
            marks.append(int(value.strip()))

        except ValueError:
            print("Invalid mark:", value.strip())

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("Total:", total)
    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)

except FileNotFoundError:
    print("marks.txt was not found.")


# ==========================================
# Task 15
# process_numbers(filename)
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


# Create a sample file for testing
with open("data_numbers.txt", "w") as file:
    file.write("10\n")
    file.write("20\n")
    file.write("abc\n")
    file.write("30\n")


result = process_numbers("data_numbers.txt")

print("Processed result:", result)
