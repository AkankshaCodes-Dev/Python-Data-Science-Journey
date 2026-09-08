# Day 7 - elif and Nested if


# Example 1: Basic if-elif-else

marks = 75

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


# Example 2: Checking a number

number = 0

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Example 3: Nested if

age = 20
has_id = True

if age >= 18:
    print("Age requirement satisfied.")

    if has_id:
        print("You can enter.")
    else:
        print("ID is required.")
else:
    print("You are under 18.")


# Example 4: User input with elif

temperature = int(input("Enter temperature: "))

if temperature >= 35:
    print("It is very hot.")
elif temperature >= 25:
    print("It is warm.")
elif temperature >= 15:
    print("It is cool.")
else:
    print("It is cold.")
