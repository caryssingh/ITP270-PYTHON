#!/bin/python3
import re
def word_frequency(sentences):
    # Define a list of common English stop words to exclude
    stop_words = set([
        "the", "and", "is", "in", "a", "of", "over", "are", "not", "and", "or", "it"
        # Add more stop words as needed
    ])

    # Initialize an empty dictionary to store word frequencies
    word_freq = {}

    # Loop through each sentence in the list
    for sentence_index, sentence in enumerate(sentences):
        # Tokenize the sentence into words using regular expressions
        words = re.findall(r'\b\w+\b', sentence.lower())

        # Filter out stop words and keep only unique words in the sentence
        unique_words = set(word for word in words if word not in stop_words)

        # Update the word frequencies in the dictionary
        for word in unique_words:
            if word in word_freq:
                word_freq[word].append(sentence_index)
            else:
                word_freq[word] = [sentence_index]

    return word_freq

# Example usage:
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A quick brown dog jumps over a lazy cat.",
    "The dog and the cat are friends.",
    "The fox and the dog are not friends."
]

result = word_frequency(sentences)
print(result)
