#!/bin/python3
# Exercise 1 Solution
try:
    error_count = 0
    with open('log.txt', 'r') as log_file, open('errors.txt', 'w') as error_file:
        for line in log_file:
            if 'ERROR' in line:
                error_count += 1
                error_file.write(line)
    print(f"Total errors found: {error_count}")
except FileNotFoundError:
    print("Log file not found.")
except Exception as e:
    print(f"An error occurred: {e}")
# Exercise 2 Solution
try:
    total = 0
    row_count = 0
    with open('data.csv', 'r') as csv_file:
        for line in csv_file:
            try:
                values = line.strip().split(',')
                column_3_value = float(values[2])
                total += column_3_value
                row_count += 1
            except (IndexError, ValueError):
                pass  # Skip invalid data
    if row_count > 0:
        average = total / row_count
        print(f"Average of column 3: {average:.2f}")
    else:
        print("No valid data found.")
except FileNotFoundError:
    print("CSV file not found.")
except Exception as e:
    print(f"An error occurred: {e}")
# Exercise 3 Solution
def encrypt(text):
    encrypted_text = ""
    for char in text:
        encrypted_char = chr(ord(char) + 1)  # Simple Caesar cipher shift by 1
        encrypted_text += encrypted_char
    return encrypted_text

try:
    with open('plain.txt', 'r') as input_file, open('encrypted.txt', 'w') as output_file:
        plain_text = input_file.read()
        encrypted_text = encrypt(plain_text)
        output_file.write(encrypted_text)
    print("Encryption complete.")
except FileNotFoundError:
    print("Input file not found.")
except Exception as e:
    print(f"An error occurred: {e}")
# Exercise 4 Solution
try:
    total = 0
    with open('data.bin', 'rb') as binary_file:
        while True:
            try:
                value = int.from_bytes(binary_file.read(4), byteorder='big')
                total += value
            except ValueError:
                break  # Reached the end of the file
    print(f"Sum of integers in binary file: {total}")
except FileNotFoundError:
    print("Binary data file not found.")
except Exception as e:
    print(f"An error occurred: {e}")
# Exercise 5 Solution
import json

try:
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            try:
                name = item['name']
                age = item['age']
                print(f"Name: {name}, Age: {age}")
            except KeyError:
                print("Incomplete data in JSON.")
except FileNotFoundError:
    print("JSON file not found.")
except json.JSONDecodeError:
    print("Invalid JSON format.")
except Exception as e:
    print(f"An error occurred: {e}")

