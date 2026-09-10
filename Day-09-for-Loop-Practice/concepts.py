# Day 9 - for Loop Practice


# Example 1: Factorial of a number

num = 5
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("Factorial:", factorial)


# Example 2: Reverse counting

for i in range(10, 0, -1):
    print(i)


# Example 3: Sum of even numbers from 1 to 50

total = 0

for i in range(2, 51, 2):
    total = total + i

print("Sum of even numbers:", total)


# Example 4: Count digits of a number

num = 12345
count = 0

for digit in str(num):
    count = count + 1

print("Number of digits:", count)
