# Day 25 - Function Arguments and Return


# ==========================================
# 1. Function with One Argument
# ==========================================

def greet(name):
    print("Hello", name)


greet("Akanksha")


# ==========================================
# 2. Function with Two Arguments
# ==========================================

def add_numbers(a, b):
    print(a + b)


add_numbers(10, 20)


# ==========================================
# 3. Positional Arguments
# ==========================================

def student_info(name, age):
    print("Name:", name)
    print("Age:", age)


student_info("Akanksha", 20)


# ==========================================
# 4. Multiple Arguments
# ==========================================

def introduce(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


introduce("Akanksha", 20, "BCA")


# ==========================================
# 5. Parameter vs Argument
# ==========================================

def square(number):       # number is a parameter
    return number * number


result = square(5)        # 5 is an argument

print("Square:", result)


# ==========================================
# 6. Function Returning a Value
# ==========================================

def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)


# ==========================================
# 7. Using Returned Value in Another Calculation
# ==========================================

def multiply(a, b):
    return a * b


result = multiply(5, 4)

final_result = result + 10

print("Final result:", final_result)


# ==========================================
# 8. Returning a String
# ==========================================

def get_course():
    return "BCA"


course = get_course()

print("Course:", course)


# ==========================================
# 9. Returning a Boolean Value
# ==========================================

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(10))
print(is_even(7))


# ==========================================
# 10. Function with Argument and return
# ==========================================

def calculate_square(number):
    return number * number


number = 8

result = calculate_square(number)

print("Square:", result)


# ==========================================
# 11. Function Returning Difference
# ==========================================

def subtract(a, b):
    return a - b


result = subtract(50, 20)

print("Difference:", result)


# ==========================================
# 12. Function Returning Average
# ==========================================

def calculate_average(a, b, c):
    total = a + b + c
    average = total / 3
    return average


result = calculate_average(80, 90, 70)

print("Average:", result)
