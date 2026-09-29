# Day 28 - Default Arguments and Keyword Arguments Practice Tasks


# Task 1
# Create a function that greets a person.
# Use "Akanksha" as the default name.

def greet(name="Akanksha"):
    print("Hello", name)


greet()
greet("Priya")


# Task 2
# Create a function that calculates
# the square of a number.
# Use 5 as the default number.

def square(number=5):
    return number * number


print("Square:", square())
print("Square:", square(10))


# Task 3
# Create a function with a default course.

def student(name, course="BCA"):
    print("Name:", name)
    print("Course:", course)


student("Akanksha")
student("Akanksha", "Data Science")


# Task 4
# Create a function that adds two numbers.
# Give the second number a default value of 10.

def add(a, b=10):
    return a + b


print("Sum:", add(5))
print("Sum:", add(5, 20))


# Task 5
# Create a function using keyword arguments.

def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_info(
    name="Akanksha",
    age=20,
    course="BCA"
)


# Task 6
# Call the function from Task 5
# using the arguments in a different order.

student_info(
    course="Data Science",
    name="Akanksha",
    age=20
)


# Task 7
# Create a function that calculates
# the total price.
# Quantity should have a default value of 1.

def calculate_total(price, quantity=1):
    return price * quantity


print("Total:", calculate_total(100))
print("Total:", calculate_total(100, 5))


# Task 8
# Create a function that checks whether
# a student passed.
# Passing marks should default to 40.

def check_pass(marks, passing=40):
    if marks >= passing:
        return "Pass"
    else:
        return "Fail"


print(check_pass(60))
print(check_pass(35))
print(check_pass(35, 30))


# Task 9
# Create a function that calculates
# the area of a rectangle.
# Use keyword arguments when calling it.

def rectangle_area(length, width):
    return length * width


print(rectangle_area(length=10, width=5))


# Task 10
# Create a function that creates
# a student introduction using a default goal.

def introduction(name, goal="Data Scientist"):
    return name + " wants to become a " + goal


print(introduction("Akanksha"))
print(introduction("Akanksha", "Python Developer"))
