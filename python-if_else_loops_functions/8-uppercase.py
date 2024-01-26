#!/usr/bin/env python3

"""
Converts lowercase letters in a string to uppercase.

Parameters:
- str (str): Input string.

Usage:
- Call with string argument,convert lowercase letters to uppercase.
"""


def islower(c):
    letter = ord(c)
    return 97 <= letter <= 122


def uppercase(str):
    verdict = ""
    for char in str:
        if islower(char):
            verdict += chr(ord(char) - 32)
        else:
            verdict += char

    print("{:s}".format(verdict))
