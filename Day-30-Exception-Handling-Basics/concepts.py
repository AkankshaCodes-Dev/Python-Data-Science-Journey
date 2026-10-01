# Day 30 - Exception Handling Basics


# ==========================================
# 1. What is an Error?
# ==========================================

An error is a problem that preventsa program from running as expected.


# ==========================================
# 2. What is an Exception?
# ==========================================

An exception is an error that occurs while the program is running.

# Example:
# print(10 / 0)

# This produces ZeroDivisionError.


# ==========================================
# 3. Basic try-except
# ==========================================

try:
    number = 10 / 0
except:
    print("An error occurred.")


# ==========================================
# 4. Handling ZeroDivisionError
# ==========================================

try:
    number = 10 / 0
    print(number)
except ZeroDivisionError:
    print("Cannot divide by zero.")


# ==========================================
# 5. Handling ValueError
# ==========================================

try:
    number = int("hello")
    print(number)
except ValueError:
    print("Invalid number.")


# ==========================================
# 6. Invalid User Input
# ==========================================

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)
except ValueError:
    print("Please enter a valid number.")


# ==========================================
# 7. Division with User Input
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
# 8. Multiple Exceptions
# ==========================================

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    print(number1 / number2)

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("Cannot divide by zero.")


# ==========================================
# 9. try-except-else
# ==========================================

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print("You entered:", number)


# ==========================================
# 10. try-except-finally
# ==========================================

try:
    number = int(input("Enter a number: "))
    print("Number:", number)

except ValueError:
    print("Invalid input.")

finally:
    print("This block always executes.")


# ==========================================
# 11. File Handling with Exception Handling
# ==========================================

try:
    with open("student.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")


# ==========================================
# 12. Function with Exception Handling
# ==========================================

def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero."


print(divide(10, 2))
print(divide(10, 0))


# ==========================================
# 13. Function for Safe Number Conversion
# ==========================================

def convert_number(value):
    try:
        return int(value)

    except ValueError:
        return "Invalid number."


print(convert_number("100"))
print(convert_number("abc"))


# ==========================================
# 14. Average with Exception Handling
# ==========================================

def calculate_average(numbers):
    try:
        total = sum(numbers)
        average = total / len(numbers)

        return average

    except ZeroDivisionError:
        return "List cannot be empty."


print(calculate_average([10, 20, 30]))
print(calculate_average([]))


# ==========================================
# 15. List Processing with Exception Handling
# ==========================================

def convert_values(values):
    numbers = []

    for value in values:
        try:
            numbers.append(int(value))

        except ValueError:
            print("Skipping invalid value:", value)

    return numbers


values = ["10", "20", "hello", "30"]

result = convert_values(values)

print("Valid numbers:", result)


# ==========================================
# Data Science Connection
# ==========================================

# Exception handling is useful in Data Science
# when working with real-world data.

# Real datasets may contain:
# - Missing values
# - Invalid numbers
# - Incorrect data types
# - Missing files
# - Unexpected input

# Exception handling helps prevent the
# entire program from crashing.
