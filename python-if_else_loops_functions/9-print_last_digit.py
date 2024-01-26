#!/usr/bin/env python3

"""
Prints and returns the last digit of a given number.

Parameters:
- number (int): The input number.

Returns:
- int: The last digit of the input number.
"""


#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
