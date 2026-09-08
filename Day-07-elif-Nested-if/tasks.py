# Day 7 - elif and Nested if Practice Tasks


# Task 1: Grade calculator

marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")


# Task 2: Check whether a number is positive, negative, or zero

number = -10

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Task 3: Check age category

age = 20

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")


# Task 4: Nested if

age = 20
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter.")
    else:
        print("You need a ticket.")
else:
    print("You are not eligible.")


# Task 5: Weekly revision - even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Task 6: Weekly revision - largest of two numbers

a = 25
b = 40

if a > b:
    print("a is larger")
elif b > a:
    print("b is larger")
else:
    print("Both are equal")
