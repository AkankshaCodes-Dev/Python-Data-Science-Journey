# Day 27 - Local Variables and Function Scope


# ==========================================
# 1. Local Variable
# ==========================================

def greet():
    message = "Hello, Akanksha!"
    print(message)


greet()


# ==========================================
# 2. Local Variable with a Parameter
# ==========================================

def square(number):
    result = number * number
    print(result)


square(5)


# ==========================================
# 3. Local Variable with return
# ==========================================

def add(a, b):
    total = a + b
    return total


result = add(10, 20)

print("Total:", result)


# ==========================================
# 4. Multiple Local Variables
# ==========================================

def student_result(marks1, marks2, marks3):
    total = marks1 + marks2 + marks3
    average = total / 3

    return total, average


total, average = student_result(80, 90, 70)

print("Total:", total)
print("Average:", average)


# ==========================================
# 5. Local Variable Used for Calculation
# ==========================================

def calculate_area(length, width):
    area = length * width
    return area


result = calculate_area(10, 5)

print("Area:", result)


# ==========================================
# 6. Local Variable with Condition
# ==========================================

def check_number(number):
    if number > 0:
        result = "Positive"
    elif number < 0:
        result = "Negative"
    else:
        result = "Zero"

    return result


print(check_number(10))
print(check_number(-5))
print(check_number(0))


# ==========================================
# 7. Local Variable with Loop
# ==========================================

def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


numbers = [10, 20, 30, 40]

print("Sum:", calculate_sum(numbers))


# ==========================================
# 8. Local Variable for Counting
# ==========================================

def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count = count + 1

    return count


numbers = [2, 5, 8, 11, 14]

print("Even count:", count_even(numbers))


# ==========================================
# 9. Local Variable with String Processing
# ==========================================

def clean_name(name):
    cleaned_name = name.strip().lower()
    return cleaned_name


result = clean_name("   AKANKSHA   ")

print("Cleaned name:", result)


# ==========================================
# 10. Same Variable Name in Different Functions
# ==========================================

def first_function():
    message = "Hello from first function"
    print(message)


def second_function():
    message = "Hello from second function"
    print(message)


first_function()
second_function()
