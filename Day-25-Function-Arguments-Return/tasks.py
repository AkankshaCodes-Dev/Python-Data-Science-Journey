# Day 25 - Function Arguments and Return Practice Tasks


# Task 1: Create a function that accepts a name
# and prints a greeting

def greet(name):
    print("Hello", name)


greet("Akanksha")


# Task 2: Create a function that accepts
# two numbers and returns their sum

def add(a, b):
    return a + b


result = add(10, 20)

print("Sum:", result)


# Task 3: Create a function that returns
# the subtraction of two numbers

def subtract(a, b):
    return a - b


result = subtract(30, 10)

print("Difference:", result)


# Task 4: Create a function that returns
# the multiplication of two numbers

def multiply(a, b):
    return a * b


result = multiply(5, 6)

print("Product:", result)


# Task 5: Create a function that returns
# the square of a number

def square(number):
    return number * number


result = square(7)

print("Square:", result)


# Task 6: Create a function that returns
# the average of three numbers

def average(a, b, c):
    total = a + b + c
    return total / 3


result = average(80, 90, 70)

print("Average:", result)


# Task 7: Create a function that checks
# whether a number is positive

def is_positive(number):
    if number > 0:
        return True
    else:
        return False


print(is_positive(10))
print(is_positive(-5))


# Task 8: Create a function that checks
# whether a number is even

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(8))
print(is_even(7))


# Task 9: Create a function with three arguments
# and return the largest number

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


result = largest(10, 25, 15)

print("Largest:", result)


# Task 10: Create a function that returns
# the full name

def full_name(first_name, last_name):
    return first_name + " " + last_name


name = full_name("Akanksha", "Kumari")

print("Full Name:", name)
