# ==========================================
# DAY 32 - OOP BASICS
# ==========================================


# ------------------------------------------
# 1. What is OOP?
# ------------------------------------------

# OOP = Object-Oriented Programming
# It organizes programs using Classes and Objects.


# ------------------------------------------
# 2. Creating a Class
# ------------------------------------------

class Student:
    pass


# Creating an object
student1 = Student()

print(student1)


# ------------------------------------------
# 3. Class with __init__()
# ------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Akanksha", 20)

print(student1.name)
print(student1.age)


# ------------------------------------------
# 4. Understanding self
# ------------------------------------------

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course


student1 = Student("Akanksha", "BCA")

print(student1.name)
print(student1.course)


# ------------------------------------------
# 5. Attributes
# ------------------------------------------

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student1 = Student("Akanksha", 20, "BCA")

print("Name:", student1.name)
print("Age:", student1.age)
print("Course:", student1.course)


# ------------------------------------------
# 6. Methods
# ------------------------------------------

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)


student1 = Student("Akanksha")

student1.greet()


# ------------------------------------------
# 7. Method with More Information
# ------------------------------------------

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
        print("My name is", self.name)
        print("I am studying", self.course)


student1 = Student("Akanksha", "BCA")

student1.introduce()


# ------------------------------------------
# 8. Multiple Objects
# ------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Akanksha", 20)
student2 = Student("Rahul", 21)

student1.display()
student2.display()


# ------------------------------------------
# 9. Method with Calculation
# ------------------------------------------

class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        return self.number * self.number


calculator1 = Calculator(5)

print("Square:", calculator1.square())


# ------------------------------------------
# 10. Student Marks Example
# ------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)


student1 = Student("Akanksha", [80, 75, 90, 85])

print("Student:", student1.name)
print("Total:", student1.calculate_total())
print("Average:", student1.calculate_average())


# ------------------------------------------
# 11. OOP with Condition
# ------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        average = sum(self.marks) / len(self.marks)

        if average >= 40:
            return "Pass"
        else:
            return "Fail"


student1 = Student("Akanksha", [80, 75, 90])

print(student1.name, "-", student1.check_result())


# ------------------------------------------
# 12. Real-World Example
# ------------------------------------------

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


account1 = BankAccount("Akanksha", 1000)

account1.deposit(500)

account1.display_balance()


# ------------------------------------------
# 13. Data Science Connection
# ------------------------------------------

# OOP is useful in Data Science and Machine Learning.
#
# Examples:
# - Dataset objects
# - Model objects
# - Data preprocessing objects
# - Custom ML classes
#
# Libraries such as scikit-learn use objects extensively.
