# Day 24 - Function Basics


# ==========================================
# 1. Simple Function
# ==========================================

def greet():
    print("Hello, Akanksha!")


# Calling the function
greet()


# ==========================================
# 2. Function to Print a Message
# ==========================================

def welcome():
    print("Welcome to Python learning!")


welcome()


# ==========================================
# 3. Function with One Parameter
# ==========================================

def greet_person(name):
    print("Hello", name)


greet_person("Akanksha")
greet_person("Rahul")


# ==========================================
# 4. Function with Two Parameters
# ==========================================

def add_numbers(a, b):
    print(a + b)


add_numbers(10, 20)
add_numbers(5, 15)


# ==========================================
# 5. Function with Multiple Parameters
# ==========================================

def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_info("Akanksha", 20, "BCA")


# ==========================================
# 6. Function with return
# ==========================================

def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)


# ==========================================
# 7. Another return Example
# ==========================================

def multiply(a, b):
    return a * b


result = multiply(5, 4)

print("Multiplication:", result)


# ==========================================
# 8. Function Returning a String
# ==========================================

def get_message():
    return "I am learning Python"


message = get_message()

print(message)


# ==========================================
# 9. Function with Parameter and return
# ==========================================

def square(number):
    return number * number


result = square(5)

print("Square:", result)


# ==========================================
# 10. Function with Condition
# ==========================================

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even(10))
print(check_even(7))
