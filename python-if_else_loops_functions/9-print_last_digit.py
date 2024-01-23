#!/usr/bin/env python3

"""
Prints and returns the last digit of a given number.

Parameters:
- number (int): The input number.

Returns:
- int: The last digit of the input number.
"""


def print_last_digit(number):
    if number < 0:
        number = number * (-1)
        print(number % 10, end="")
        return (number % 10)

    else:
        print(number % 10, end="")
        return number % 10
