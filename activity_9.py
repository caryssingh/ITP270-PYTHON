#!/bin/python3
def uppercase_conversion(input_string):
    return input_string.upper()

# Example usage:
input_str = "hello, python!"
result = uppercase_conversion(input_str)
print(result)  # Output: "HELLO, PYTHON!"

def count_substring_occurrences(input_string, substring):
    return input_string.count(substring)

# Example usage:
input_str = "abracadabra"
sub_str = "a"
result = count_substring_occurrences(input_str, sub_str)
print(result)  # Output: 5

def reverse_words(input_string):
    words = input_string.split()
    reversed_string = " ".join(reversed(words))
    return reversed_string

# Example usage:
input_str = "Hello, Python!"
result = reverse_words(input_str)
print(result)  # Output: "Python! Hello,"


def clean_and_title_case(input_string):
    cleaned_string = input_string.strip()
    return cleaned_string.title()

# Example usage:
input_str = "   hello, python!   "
result = clean_and_title_case(input_str)
print(result)  # Output: "Hello, Python!"

def is_alphanumeric(input_string):
    return input_string.isalnum()

# Example usage:
input_str = "Hello123"
result = is_alphanumeric(input_str)
print(result)  # Output: True

