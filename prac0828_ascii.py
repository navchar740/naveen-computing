'''
# Exercise 1: Sum of ASCII Values
# Write a Python program that calculates the sum of the ASCII values of 
all characters in a given string.
# Example input: text = "hello"
# Expected output: 532
'''

# Solution for Exercise 1
text = "hello"
ascii_sum = 0
for char in text:
    ascii_sum += ord(char)
print(f"The sum of the ASCII values is {ascii_sum}")
# Output: The sum of the ASCII values is 532


'''
# Exercise 2: Character from ASCII Value
# Write a Python program that takes an ASCII value as input and prints 
the corresponding character.
# Example input: ascii_value = 97
# Expected output: 'a'
'''
# Solution for Exercise 2
ascii_value = 97
character = chr(ascii_value)
print(f"The character for ASCII value {ascii_value} is '{character}'")
# Output: The character for ASCII value 97 is 'a'


'''
# Exercise 3: Uppercase to Lowercase Conversion
# Write a Python program that converts an uppercase letter to its lowercase 
equivalent using ASCII values.
# Example input: letter = 'A'
# Expected output: 'a'
'''
# Solution for Exercise 3
letter = 'A'
lowercase_letter = chr(ord(letter) + 32)
print(f"The lowercase of '{letter}' is '{lowercase_letter}'")
# Output: The lowercase of 'A' is 'a'


'''
# Exercise 4: Lowercase to Uppercase Conversion
# Write a Python program that converts a lowercase letter to its 
uppercase equivalent using ASCII values.
# Example input: letter = 'b'
# Expected output: 'B'
'''


'''
# Exercise 5: ASCII Value Difference
# Write a Python program that calculates the difference between the 
ASCII values of two characters.
# Example input: char1 = 'a', char2 = 'd'
# Expected output: 3
'''


'''
# Exercise 6: Alphabetical Sequence
# Write a Python program that prints the next 5 characters in the ASCII 
sequence from a given character.
# Example input: start_char = 'x'
# Expected output: 'y', 'z', '{', '|', '}'
'''
start_char = "X"
startidx = ord(start_char)
for i in range(1,6):
    print(chr(startidx  + i))
    
'''    
# Exercise 7: Sum of ASCII Values of Digits
# Write a Python program that calculates the sum of the ASCII values of all 
# digit characters in a given string.
# Example input: text = "a1b2c3"
# Expected output: 150
'''


'''
# Exercise 8: Replace Characters with ASCII Sum
# Write a Python program that replaces each character in a string with the 
# sum of its ASCII value and a given integer.
# Example input: text = "abc", increment = 1
# Expected output: 'b', 'c', 'd'
'''



##################### ASCII PASSWORD GENERATION #######################
'''
# Exercise 1: Generate a Simple Password
# Write a Python program that generates a random password of a given length 
# using ASCII printable characters.
# Example input: length = 8
# Expected output: A random password of 8 characters, e.g., 'aB3#xG2!'
# HINT: ASCII printable characters range from 33 to 126
'''

import random 
startidx = ord(start_char)
start_char = random.randint()
for i in range(8):
startidx = ord(start_char)
    print(chr(startidx  + i))