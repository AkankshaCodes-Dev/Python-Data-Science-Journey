# Day 11 - break, continue and pass


# Example 1: break

for i in range(1, 11):
    if i == 6:
        break
    print(i)


# Example 2: continue

for i in range(1, 11):
    if i == 6:
        continue
    print(i)


# Example 3: pass

for i in range(1, 6):
    if i == 3:
        pass
    print(i)


# Example 4: break with while loop

i = 1

while i <= 10:
    if i == 6:
        break
    print(i)
    i = i + 1


# Example 5: continue with while loop

i = 0

while i < 5:
    i = i + 1

    if i == 3:
        continue

    print(i)
