# Day 10 - while Loops


# Example 1: Print numbers 1 to 5

i = 1

while i <= 5:
    print(i)
    i = i + 1


# Example 2: Reverse counting

i = 5

while i >= 1:
    print(i)
    i = i - 1


# Example 3: Print even numbers from 2 to 10

i = 2

while i <= 10:
    print(i)
    i = i + 2


# Example 4: while loop with user input

number = int(input("Enter a number greater than 0: "))

while number <= 0:
    number = int(input("Please enter a number greater than 0: "))

print("Valid number:", number)
