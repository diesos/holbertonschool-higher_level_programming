#!/usr/bin/python3

"""
Checks if a given character is a lowercase letter.

Parameters:
- c (str): The character to be checked.

Returns:
- bool: True if the character is a lowercase letter, False otherwise.
"""


def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
