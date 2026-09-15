# Day 14 - String Practice


# Example 1: String indexing

word = "Python"

print(word[0])
print(word[-1])


# Example 2: String slicing

word = "Python"

print(word[0:3])
print(word[2:6])


# Example 3: Find string length

name = "Akanksha"

print(len(name))


# Example 4: Combining lower() and strip()

text = "   PYTHON   "

text = text.strip()
text = text.lower()

print(text)


# Example 5: Using replace()

sentence = "I am learning Java"

sentence = sentence.replace("Java", "Python")

print(sentence)


# Example 6: Using find()

text = "I love Python"

position = text.find("Python")

print(position)


# Example 7: Using count()

text = "banana"

print(text.count("a"))


# Example 8: Using split()

sentence = "Python is easy to learn"

words = sentence.split()

print(words)


# Example 9: Combining multiple string methods

text = "   PYTHON DATA SCIENCE   "

text = text.strip()
text = text.lower()
text = text.replace(" ", "-")

print(text)
