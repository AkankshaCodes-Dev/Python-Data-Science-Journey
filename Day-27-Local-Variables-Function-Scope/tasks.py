# Day 27 - Local Variables and Function Scope Practice Tasks


# Task 1
# Create a function with a local variable
# that stores your name.

def show_name():
    name = "Akanksha"
    print(name)


show_name()


# Task 2
# Create a function that accepts a number
# and uses a local variable to calculate its square.

def square(number):
    result = number * number
    return result


print("Square:", square(6))


# Task 3
# Create a function that accepts two numbers
# and uses a local variable to calculate their sum.

def add(a, b):
    total = a + b
    return total


print("Sum:", add(15, 25))


# Task 4
# Create a function that accepts three marks.
# Use local variables for total and average.

def calculate_result(mark1, mark2, mark3):
    total = mark1 + mark2 + mark3
    average = total / 3

    return total, average


total, average = calculate_result(80, 90, 70)

print("Total:", total)
print("Average:", average)


# Task 5
# Create a function that calculates
# the area of a rectangle.

def rectangle_area(length, width):
    area = length * width
    return area


print("Area:", rectangle_area(10, 5))


# Task 6
# Create a function that checks whether
# a number is positive, negative, or zero.

def check_number(number):
    if number > 0:
        result = "Positive"
    elif number < 0:
        result = "Negative"
    else:
        result = "Zero"

    return result


print(check_number(15))
print(check_number(-8))
print(check_number(0))


# Task 7
# Create a function that calculates
# the sum of numbers in a list.

def list_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


numbers = [10, 20, 30, 40]

print("Sum:", list_sum(numbers))


# Task 8
# Create a function that counts
# even numbers in a list.

def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count = count + 1

    return count


numbers = [2, 5, 8, 11, 14, 20]

print("Even count:", count_even(numbers))


# Task 9
# Create a function that cleans a name
# using strip() and lower().

def clean_name(name):
    cleaned_name = name.strip().lower()
    return cleaned_name


print(clean_name("   AKANKSHA   "))


# Task 10
# Create a function that finds the largest
# number in a list using a local variable.

def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


numbers = [15, 40, 7, 25, 60]

print("Largest:", find_largest(numbers))
