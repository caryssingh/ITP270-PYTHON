#!/bin/python3

#Problem 1
def dict_intersection(dict1, dict2):
    intersection = {}
    for key in dict1.keys() & dict2.keys():
        intersection[key] = (dict1[key], dict2[key])
    return intersection

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
result = dict_intersection(dict1, dict2)

# Output: {'b': (2, 4), 'c': (3, 5)}

def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
#Problem 2
def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
text = "This is a simple example. This is a simple example."
result = word_frequency(text)
# Output: {'this': 2, 'is': 2, 'a': 2, 'simple': 2, 'example': 2}

#Problem 3
def inverse_dict(input_dict):
    inverted_dict = {}
    for key, value in input_dict.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    return inverted_dict
input_dict = {'a': 1, 'b': 2, 'c': 1}
result = inverse_dict(input_dict)
# Output: {1: ['a', 'c'], 2: ['b']}

#Problem 4
def merge_dicts(*dicts):
    merged_dict = {}
    for d in dicts:
        for key, value in d.items():
            if key in merged_dict:
                if isinstance(merged_dict[key], list):
                    merged_dict[key].append(value)
                else:
                    merged_dict[key] = [merged_dict[key], value]
            else:
                merged_dict[key] = value
    return merged_dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3 = {'d': 5}
result = merge_dicts(dict1, dict2, dict3)
# Output: {'a': 1, 'b': [2, 3], 'c': 4, 'd': 5}

#Problem 5
# Output: {'a': 1}
def dict_diff(dict1, dict2):
    difference = {}
    for key, value in dict1.items():
        if key not in dict2 or dict2[key] != value:
            difference[key] = value
    return difference
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 5}
result = dict_diff(dict1, dict2)
# Output: {'a': 1}
print (result)

