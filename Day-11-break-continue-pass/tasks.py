# Day 11 - break, continue and pass Practice Tasks


# Task 1: Print numbers from 1 to 10,
# but stop when the number reaches 6

for i in range(1, 11):
    if i == 6:
        break
    print(i)


# Task 2: Print numbers from 1 to 10,
# but skip number 5

for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# Task 3: Print even numbers from 1 to 20,
# but stop when the number reaches 12

for i in range(2, 21, 2):
    if i == 12:
        break
    print(i)


# Task 4: Print numbers from 1 to 10,
# but skip 3 and 7

for i in range(1, 11):
    if i == 3 or i == 7:
        continue
    print(i)


# Task 5: Use pass when the number is 5

for i in range(1, 11):
    if i == 5:
        pass
    print(i)
