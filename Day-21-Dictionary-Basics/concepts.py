# Day 21 - Dictionary Basics

# Creating a dictionary
student = {
    "name": "Akanksha",
    "course": "BCA",
    "year": 3
}

print(student)

# Accessing values
print(student["name"])
print(student["course"])

# Adding a new item
student["goal"] = "Data Scientist"
print(student)

# Updating a value
student["year"] = 3
print(student)

# Dictionary keys
print(student.keys())

# Dictionary values
print(student.values())

# Dictionary items
print(student.items())

# Checking if a key exists
print("name" in student)
print("age" in student)

# Removing an item
student.pop("goal")
print(student)
