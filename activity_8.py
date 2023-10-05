#!/bin/python3
def fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1
    while a < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

limit = 50
result = fibonacci_sequence(limit)
print(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 17 
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

 
def is_palindrome(s):
    s = s.lower().replace(" ", "").replace(",", "").replace(".", "")
    return s == s[::-1]

word = "Racecar"  
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
def is_palindrome(s):
		s = s.lower().replace(" ", "").replace(",", "").replace(".", "")
		return s == s[::-1]
word = "Racecar"  # Replace with the word or phrase you want to check
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5  # Replace with the number for which you want to calculate the factorial
print(f"The factorial of {number} is {factorial(number)}.")
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

number = 12345  # Replace with the number for which you want to calculate the sum of digits
print(f"The sum of digits in {number} is {sum_of_digits(number)}.")
