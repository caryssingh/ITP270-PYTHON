#!/bin/python3
def merge_and_sort_unique_lists(list1, list2):
    # Merge the lists without duplicates
    merged_list = list(set(list1 + list2))
    
    # Sort the merged list
    merged_list.sort()
    
    return merged_list

# Test the function
list1 = [2, 4, 6, 8]
list2 = [5, 4, 9, 2]
result = merge_and_sort_unique_lists(list1, list2)
print(result)  # Output: [2, 4, 5, 6, 8, 9]

def squares_of_even_numbers(numbers):
    # Use list comprehension to create a new list with squares of even numbers
    squares = [x ** 2 for x in numbers if x % 2 == 0]
    
    return squares

# Test the function
numbers = [1, 2, 3, 4, 5, 6]
result = squares_of_even_numbers(numbers)
print(result)  # Output: [4, 16, 36]

def find_longest_words(word_list):
    max_length = max(len(word) for word in word_list)
    longest_words = [word for word in word_list if len(word) == max_length]
    
    return longest_words

# Test the function
words = ["apple", "banana", "cherry", "date", "grape", "kiwi"]
result = find_longest_words(words)
print(result)  # Output: ["banana", "cherry"]

def find_second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    
    if len(unique_numbers) < 2:
        return None  # Not enough unique elements
    
    unique_numbers.sort()  # Sort the unique elements
    return unique_numbers[-2]  # Return the second last element

# Test the function
numbers = [5, 3, 9, 7, 3, 8]
result = find_second_largest(numbers)
print(result)  # Output: 8

def remove_names_with_a(names):
    filtered_names = [name for name in names if 'a' not in name.lower()]
    
    return filtered_names

# Test the function
names = ["Alice", "Bob", "Eva", "Grace", "John", "Oscar"]
result = remove_names_with_a(names)
print(result)  # Output: ["Bob", "John"]
