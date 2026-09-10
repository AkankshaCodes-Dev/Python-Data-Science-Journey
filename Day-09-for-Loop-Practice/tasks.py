# Day 9 - for Loop Practice Tasks


# Task 1: Find factorial of a number

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial:", factorial)


# Task 2: Print multiplication tables from 1 to 5

for number in range(1, 6):
    print("Table of", number)

    for i in range(1, 11):
        print(number * i)


# Task 3: Reverse counting from 10 to 1

for i in range(10, 0, -1):
    print(i)


# Task 4: Find sum of even numbers from 1 to 50

total = 0

for i in range(2, 51, 2):
    total = total + i

print("Sum of even numbers:", total)


# Task 5: Count digits of a number

num = int(input("Enter a number: "))

count = 0

for digit in str(num):
    count = count + 1

print("Number of digits:", count)
