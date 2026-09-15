# Day 14 - String Practice Tasks


# Task 1: Print the first and last character of a word

word = "Python"

print(word[0])
print(word[-1])


# Task 2: Print the first three characters of a word

word = "Programming"

print(word[0:3])


# Task 3: Find the length of your name

name = "Akanksha"

print(len(name))


# Task 4: Convert a sentence to lowercase

sentence = "PYTHON IS FUN"

print(sentence.lower())


# Task 5: Remove extra spaces from a string

text = "   Hello Python   "

print(text.strip())


# Task 6: Replace "Java" with "Python"

text = "I am learning Java"

print(text.replace("Java", "Python"))


# Task 7: Find the position of "Python"

text = "I love Python"

print(text.find("Python"))


# Task 8: Count the number of "a" characters

text = "banana"

print(text.count("a"))


# Task 9: Split a sentence into words

sentence = "Python is easy to learn"

print(sentence.split())


# Task 10: Clean and format a string

text = "   PYTHON DATA SCIENCE   "

text = text.strip()
text = text.lower()
text = text.replace(" ", "-")

print(text)
