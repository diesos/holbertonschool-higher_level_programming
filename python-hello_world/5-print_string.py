#!/usr/bin/python3
"""
This module demonstrates a simple script that prints a string multiple times and a substring.

Author: [diesos]
Date: [24/01/24]

Usage:
- Run the script to see the output.

Description:
This script defines a string variable 'str' containing the value 'Holberton School'. It then prints this string three times, separated by spaces, followed by a newline character. Finally, it prints a substring of the string, containing the characters from index 0 to 8 (excluding the character at index 9).

Output:
Holberton School Holberton School Holberton School
Holberton
"""
ORIGINAL_STRING = "Holberton School"
print(ORIGINAL_STRING, ORIGINAL_STRING,
      ORIGINAL_STRING, "\n", ORIGINAL_STRING[:9])
