#!/usr/bin/python3

"""
Prints lowercase English letters from 'a' to 'z' using ASCII values.

Usage:
- Run the script to display the sequence of lowercase letters.
"""

i = 97
while i < 123:
    print(chr(i), end="")
    i += 1
