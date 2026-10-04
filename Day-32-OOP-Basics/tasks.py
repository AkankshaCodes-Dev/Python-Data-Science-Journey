# ==========================================
# DAY 32 - OOP BASICS
# TASKS + SOLUTIONS
# ==========================================


# ------------------------------------------
# Task 1
# Create a class called Student.
# Create one object from the class.
# ------------------------------------------

class Student:
    pass


student1 = Student()

print("Student object created:", student1)


# ------------------------------------------
# Task 2
# Create a Student class with name and age.
# Display the values.
# ------------------------------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Akanksha", 20)

print("Name:", student1.name)
print("Age:", student1.age)


# ------------------------------------------
# Task 3
# Create a Student class with:
# name, course, year
# Display all information.
# ------------------------------------------

class Student:
    def __init__(self, name, course, year):
        self.name = name
        self.course = course
        self.year = year

    def display_info(self):
        print("Name:", self.name)
        print("Course:", self.course)
        print("Year:", self.year)


student1 = Student("Akanksha", "BCA", 3)

student1.display_info()


# ------------------------------------------
# Task 4
# Create a method greet() that prints:
# Hello, I am <name>
# ------------------------------------------

class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am", self.name)


student1 = Student("Akanksha")

student1.greet()


# ------------------------------------------
# Task 5
# Create a Calculator class.
# Store two numbers.
# Create a method add().
# ------------------------------------------

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2


calculator1 = Calculator(10, 20)

print("Addition:", calculator1.add())


# ------------------------------------------
# Task 6
# Add subtract(), multiply(), and divide()
# methods to Calculator.
# ------------------------------------------

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        if self.number2 == 0:
            return "Cannot divide by zero."
        return self.number1 / self.number2


calculator1 = Calculator(20, 5)

print("Add:", calculator1.add())
print("Subtract:", calculator1.subtract())
print("Multiply:", calculator1.multiply())
print("Divide:", calculator1.divide())


# ------------------------------------------
# Task 7
# Create a Rectangle class.
# Store length and width.
# Create area() method.
# ------------------------------------------

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle1 = Rectangle(10, 5)

print("Rectangle Area:", rectangle1.area())


# ------------------------------------------
# Task 8
# Create a Student class with a list of marks.
# Create total() and average() methods.
# ------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return sum(self.marks) / len(self.marks)


student1 = Student("Akanksha", [80, 75, 90, 85])

print("Student:", student1.name)
print("Total:", student1.total())
print("Average:", student1.average())


# ------------------------------------------
# Task 9
# Create a Student class.
# Check whether the student passed.
# Average >= 40 = Pass
# ------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        average = sum(self.marks) / len(self.marks)

        if average >= 40:
            return "Pass"
        else:
            return "Fail"


student1 = Student("Akanksha", [60, 70, 80])

print(student1.name, "-", student1.result())


# ------------------------------------------
# Task 10
# Create multiple Student objects.
# Display their information.
# ------------------------------------------

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)


student1 = Student("Akanksha", "BCA")
student2 = Student("Rahul", "BCA")
student3 = Student("Priya", "BCA")

student1.display()
student2.display()
student3.display()


# ------------------------------------------
# Task 11
# Create an Employee class.
# Store name and salary.
# Create a method to display details.
# ------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)


employee1 = Employee("Akanksha", 25000)

employee1.display()


# ------------------------------------------
# Task 12
# Create a BankAccount class.
# Store account holder and balance.
# Create deposit() and withdraw() methods.
# ------------------------------------------

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


account1 = BankAccount("Akanksha", 5000)

account1.deposit(1000)
account1.withdraw(2000)

account1.display()


# ------------------------------------------
# Task 13
# Create a Product class.
# Store product name and price.
# Create a method to calculate price
# after discount.
# ------------------------------------------

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)


product1 = Product("Laptop", 50000)

print("Product:", product1.name)
print("Final Price:", product1.discounted_price(10))


# ------------------------------------------
# Task 14
# Create a Dataset class.
# Store dataset name and number of rows.
# Display dataset information.
# ------------------------------------------

class Dataset:
    def __init__(self, name, rows):
        self.name = name
        self.rows = rows

    def display(self):
        print("Dataset:", self.name)
        print("Rows:", self.rows)


dataset1 = Dataset("Student Performance Dataset", 1000)

dataset1.display()


# ------------------------------------------
# Task 15
# Create a DataProcessor class.
# Store a list of numbers.
# Create methods for:
# total
# average
# maximum
# minimum
# ------------------------------------------

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def total(self):
        return sum(self.data)

    def average(self):
        return sum(self.data) / len(self.data)

    def maximum(self):
        return max(self.data)

    def minimum(self):
        return min(self.data)


data1 = DataProcessor([10, 20, 30, 40, 50])

print("Total:", data1.total())
print("Average:", data1.average())
print("Maximum:", data1.maximum())
print("Minimum:", data1.minimum())
