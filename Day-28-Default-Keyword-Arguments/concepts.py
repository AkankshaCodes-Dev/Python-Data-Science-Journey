# Day 28 - Default Arguments and Keyword Arguments


# ==========================================
# 1. Function with a Default Argument
# ==========================================

def greet(name="Akanksha"):
    print("Hello", name)


greet()
greet("Rahul")


# ==========================================
# 2. Default Argument with a Number
# ==========================================

def calculate_square(number=5):
    return number * number


print("Square:", calculate_square())
print("Square:", calculate_square(8))


# ==========================================
# 3. Function with One Required and
# One Default Argument
# ==========================================

def introduce(name, course="BCA"):
    print("Name:", name)
    print("Course:", course)


introduce("Akanksha")
introduce("Akanksha", "Data Science")


# ==========================================
# 4. Multiple Default Arguments
# ==========================================

def student_info(name, age=20, course="BCA"):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_info("Akanksha")
student_info("Akanksha", 21)
student_info("Akanksha", 21, "Data Science")


# ==========================================
# 5. Default Argument with return
# ==========================================

def add(a, b=10):
    return a + b


print("Result:", add(5))
print("Result:", add(5, 20))


# ==========================================
# 6. Keyword Arguments
# ==========================================

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student(name="Akanksha", age=20, course="BCA")


# ==========================================
# 7. Keyword Arguments in Different Order
# ==========================================

student(course="BCA", name="Akanksha", age=20)


# ==========================================
# 8. Positional Arguments
# ==========================================

def add_numbers(a, b):
    return a + b


print(add_numbers(10, 20))


# ==========================================
# 9. Keyword Arguments
# ==========================================

print(add_numbers(a=10, b=20))


# ==========================================
# 10. Mixing Positional and Keyword Arguments
# ==========================================

def calculate_area(length, width):
    return length * width


print(calculate_area(10, width=5))


# ==========================================
# 11. Function with Default and Keyword
# Arguments
# ==========================================

def employee(name, role="Student"):
    return name + " - " + role


print(employee("Akanksha"))
print(employee("Akanksha", role="Data Science Student"))


# ==========================================
# 12. Practical Example
# ==========================================

def calculate_bill(price, quantity=1):
    total = price * quantity
    return total


print("Bill:", calculate_bill(100))
print("Bill:", calculate_bill(100, 3))


# ==========================================
# 13. Default Argument with Condition
# ==========================================

def check_marks(marks, passing=40):
    if marks >= passing:
        return "Pass"
    else:
        return "Fail"


print(check_marks(60))
print(check_marks(35))
print(check_marks(35, 30))
