# Day 26 - Function Practice and Revision


# ==========================================
# 1. Simple Function
# ==========================================

def greet():
    print("Hello, Akanksha!")


greet()


# ==========================================
# 2. Function with One Argument
# ==========================================

def greet_person(name):
    print("Hello", name)


greet_person("Akanksha")


# ==========================================
# 3. Function with Two Arguments
# ==========================================

def add(a, b):
    return a + b


result = add(10, 20)

print("Sum:", result)


# ==========================================
# 4. Function with Multiple Arguments
# ==========================================

def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student_info("Akanksha", 20, "BCA")


# ==========================================
# 5. Function with Condition
# ==========================================

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even(10))
print(check_even(7))


# ==========================================
# 6. Function to Find Largest Number
# ==========================================

def largest(a, b):
    if a > b:
        return a
    else:
        return b


print("Largest:", largest(25, 15))


# ==========================================
# 7. Function with Calculation
# ==========================================

def calculate_average(a, b, c):
    total = a + b + c
    average = total / 3
    return average


print("Average:", calculate_average(80, 90, 70))


# ==========================================
# 8. Function with a Loop
# ==========================================

def print_numbers():
    for i in range(1, 6):
        print(i)


print_numbers()


# ==========================================
# 9. Function to Calculate Sum
# ==========================================

def calculate_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


marks = [80, 90, 70, 85]

print("Total:", calculate_sum(marks))


# ==========================================
# 10. Function with a String
# ==========================================

def count_characters(text):
    return len(text)


print("Characters:", count_characters("Python"))


# ==========================================
# 11. Function to Count Vowels
# ==========================================

def count_vowels(text):
    count = 0

    for character in text.lower():
        if character in "aeiou":
            count = count + 1

    return count


print("Vowels:", count_vowels("Python Programming"))


# ==========================================
# 12. Function with a List
# ==========================================

def find_largest(numbers):
    largest_number = numbers[0]

    for number in numbers:
        if number > largest_number:
            largest_number = number

    return largest_number


numbers = [10, 25, 7, 40, 15]

print("Largest number:", find_largest(numbers))


# ==========================================
# 13. Function to Count Even Numbers
# ==========================================

def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count = count + 1

    return count


numbers = [10, 15, 20, 25, 30]

print("Even numbers:", count_even(numbers))


# ==========================================
# 14. Function to Check Positive Number
# ==========================================

def is_positive(number):
    if number > 0:
        return True
    else:
        return False


print(is_positive(10))
print(is_positive(-5))


# ==========================================
# 15. Function Combining Condition and Loop
# ==========================================

def sum_even_numbers(numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total = total + number

    return total


numbers = [1, 2, 3, 4, 5, 6]

print("Sum of even numbers:", sum_even_numbers(numbers))
