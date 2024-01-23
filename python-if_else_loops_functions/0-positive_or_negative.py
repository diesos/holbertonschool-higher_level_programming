#!/usr/bin/python3

"""
Generates a random integer between -10 and 10, then categorizes and prints its nature.

Usage:
- Run the script to display whether the generated number is negative, positive, or zero.
"""

import random
number = random.randint(-10, 10)
if number < 0:
    print(number, " is negative\n")
if number > 0:
    print(number, " is positive\n")
if number == 0:
    print(number, " is zero\n")
