# Day 26 - Function Practice and Revision Tasks


# Task 1
# Create a function that takes a name
# and returns a greeting message.

def greet(name):
    return "Hello " + name


print(greet("Akanksha"))


# Task 2
# Create a function that returns
# the sum of two numbers.

def add(a, b):
    return a + b


print("Sum:", add(15, 25))


# Task 3
# Create a function that returns
# the largest of two numbers.

def largest(a, b):
    if a > b:
        return a
    else:
        return b


print("Largest:", largest(50, 30))


# Task 4
# Create a function that checks
# whether a number is even or odd.

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even_odd(20))
print(check_even_odd(13))


# Task 5
# Create a function that returns
# the square of a number.

def square(number):
    return number * number


print("Square:", square(9))


# Task 6
# Create a function that returns
# the average of three numbers.

def average(a, b, c):
    return (a + b + c) / 3


print("Average:", average(70, 80, 90))


# Task 7
# Create a function that counts
# the number of vowels in a string.

def count_vowels(text):
    count = 0

    for character in text.lower():
        if character in "aeiou":
            count = count + 1

    return count


print("Vowels:", count_vowels("Data Science"))


# Task 8
# Create a function that returns
# the largest number in a list.

def largest_in_list(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


numbers = [12, 45, 7, 30, 60]

print("Largest:", largest_in_list(numbers))


# Task 9
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


# Task 10
# Create a function that returns
# the sum of all numbers in a list.

def list_sum(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


numbers = [10, 20, 30, 40]

print("List sum:", list_sum(numbers))


# Task 11
# Create a function that returns
# only positive numbers from a list.

def positive_numbers(numbers):
    result = []

    for number in numbers:
        if number > 0:
            result.append(number)

    return result


numbers = [-5, 10, -2, 20, 0, 15]

print("Positive numbers:", positive_numbers(numbers))


# Task 12
# Create a function that checks
# whether a word is a palindrome.

def is_palindrome(word):
    word = word.lower()

    if word == word[::-1]:
        return True
    else:
        return False


print(is_palindrome("madam"))
print(is_palindrome("python"))
