# Day 24 - Function Basics Practice Tasks


# Task 1: Create a function that prints your name

def print_name():
    print("Akanksha")


print_name()


# Task 2: Create a function that prints your goal

def my_goal():
    print("My goal is to become a Data Scientist")


my_goal()


# Task 3: Create a function that greets a person

def greet(name):
    print("Hello", name)


greet("Akanksha")


# Task 4: Create a function that adds two numbers

def add(a, b):
    print(a + b)


add(10, 20)


# Task 5: Create a function that subtracts two numbers

def subtract(a, b):
    print(a - b)


subtract(20, 10)


# Task 6: Create a function that multiplies two numbers

def multiply(a, b):
    print(a * b)


multiply(5, 4)


# Task 7: Create a function that returns the square of a number

def square(number):
    return number * number


result = square(6)

print("Square:", result)


# Task 8: Create a function that returns a person's age

def get_age():
    return 20


age = get_age()

print("Age:", age)


# Task 9: Create a function that checks whether a number is positive

def check_positive(number):
    if number > 0:
        return True
    else:
        return False


print(check_positive(10))
print(check_positive(-5))


# Task 10: Create a function with three parameters

def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_info("Akanksha", 20, "BCA")
