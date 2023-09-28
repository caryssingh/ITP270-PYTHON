#!/bin/python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# Problem 2 Solution
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Problem 3 Solution
num = int(input("Enter a positive integer: "))
factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    while num > 0:
        factorial *= num
        num -= 1
    print("The factorial is:", factorial)

# Problem 4 Solution
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Problem 5 Solution
terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

first_term = 0
second_term = 1

if terms <= 0:
    print("Please enter a positive integer.")
elif terms == 1:
    print("Fibonacci sequence up to", terms, "term:", first_term)
else:
    print("Fibonacci sequence up to", terms, "terms:")
    for i in range(terms):
        print(first_term, end=" ")
        temp = first_term + second_term
        first_term = second_term
        second_term = temp
