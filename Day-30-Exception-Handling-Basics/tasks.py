# Day 30 - Exception Handling Basics
# Tasks with Solutions


# ==========================================
# Task 1
# Divide 10 by 0 and handle ZeroDivisionError
# ==========================================

try:
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ==========================================
# Task 2
# Ask the user to enter a number
# Handle ValueError
# ==========================================

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Invalid input. Please enter a number.")


# ==========================================
# Task 3
# Ask for two numbers and divide them
# Handle ValueError and ZeroDivisionError
# ==========================================

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2

    print("Result:", result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ==========================================
# Task 4
# Create divide(a, b)
# ==========================================

def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero."


print(divide(10, 2))
print(divide(10, 0))


# ==========================================
# Task 5
# Create convert_number(value)
# ==========================================

def convert_number(value):
    try:
        return int(value)

    except ValueError:
        return "Invalid number."


print(convert_number("100"))
print(convert_number("hello"))


# ==========================================
# Task 6
# Ask for age and handle invalid input
# ==========================================

try:
    age = int(input("Enter your age: "))

    print("Your age is:", age)

except ValueError:
    print("Invalid age. Please enter a number.")


# ==========================================
# Task 7
# Use try-except-else
# ==========================================

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("You entered:", number)


# ==========================================
# Task 8
# Use try-except-finally
# ==========================================

try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Invalid input.")

finally:
    print("Program completed.")


# ==========================================
# Task 9
# Open data.txt and handle FileNotFoundError
# ==========================================

try:
    with open("data.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("data.txt was not found.")


# ==========================================
# Task 10
# Calculate average and handle empty list
# ==========================================

def calculate_average(numbers):
    try:
        total = sum(numbers)
        average = total / len(numbers)

        return average

    except ZeroDivisionError:
        return "Cannot calculate average of an empty list."


print(calculate_average([10, 20, 30]))
print(calculate_average([]))


# ==========================================
# Task 11
# Convert valid values and skip invalid values
# ==========================================

values = ["10", "20", "abc", "30"]

numbers = []

for value in values:

    try:
        number = int(value)
        numbers.append(number)

    except ValueError:
        print("Skipping invalid value:", value)

print("Valid numbers:", numbers)


# ==========================================
# Task 12
# Simple calculator with exception handling
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
