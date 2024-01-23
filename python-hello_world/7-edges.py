#!/usr/bin/python3

"""
Manipulates the string 'WORD' to extract substrings and display specific information.

Constants:
- WORD (str): The original string.

Variables:
- WORD_FIRST_3 (str): The first three letters of 'WORD'.
- WORD_LAST_2 (str): The last two letters of 'WORD'.
- MIDDLE_WORD (str): The middle character of 'WORD'.

Usage:
- Run the script to display information about the substrings of 'WORD'.
"""

WORD = "Holberton"
WORD_FIRST_3 = WORD[0:3]
WORD_LAST_2 = WORD[-2:]
MIDDLE_WORD = WORD[int(len(WORD)/2)]
print(f"First 3 letters: {WORD_FIRST_3}")
print(f"Last 2 letters: {WORD_LAST_2}")
print(f"Middle word: {MIDDLE_WORD}")
