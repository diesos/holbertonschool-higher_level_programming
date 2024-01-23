#!/usr/bin/python3

"""
Creates a modified string by concatenating specific substrings from the original string.

Usage:
- Run the script to see the output.

Note:
- The original string is taken from indices 38 to 66, followed by a space, and then indices 0 to 6.
"""
ORIGINAL_STRING = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
ORIGINAL_STRING = ORIGINAL_STRING[38:66] + " " + ORIGINAL_STRING[0:6] + "\n"
print(ORIGINAL_STRING)
