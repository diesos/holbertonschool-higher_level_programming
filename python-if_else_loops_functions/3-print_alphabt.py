#!/usr/bin/python3

"""
Prints lowercase  letters from 'a' to 'z', excluding 'e' and 'q'.

Usage:
- Run the script to display the sequence of
lowercase letters skipping 'e' and 'q'.
"""

i = 97
while i < 123:
    if i == 101 or i == 113:
        i += 1
    print(chr(i), end="")
    i += 1
