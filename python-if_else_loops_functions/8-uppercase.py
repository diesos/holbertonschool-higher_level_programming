#!/usr/bin/env python3

"""
Converts lowercase letters in a string to uppercase.

Parameters:
- str (str): Input string.

Usage:
- Call with a string argument to convert lowercase letters to uppercase.
"""


def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print(char, end="")
    print("")
