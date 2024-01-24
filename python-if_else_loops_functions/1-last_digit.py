#!/usr/bin/python3

"""
Generates a random integer between -10000 and 10000
analyzes and prints info about its last digit.

Usage:
- Run the script to display information about
 the last digit of a randomly generated number.
"""

import random

number = random.randint(-10000, 10000)
print("Last digit of ", number, " is ", end="")
if number < 0:
    print("-", end="")
    number = number * (-1)
if number > 10:
    last_Digit = number % 10
if number > 0 and number < 9:
    last_Digit = number
if last_Digit < 6 and (last_Digit != 0):
    print(last_Digit, " and is less than 6 and not 0")
if last_Digit > 5:
    print(last_Digit, " and is greater than 5")
if last_Digit == 0:
    print(last_Digit, " and is 0")

# What did i learn with this project ?
# I learnt that in Python each "Print"
# function adds automatically a New Line...
# Sor for stopping this behaviour we need to add
# at the end of print :
# end="" . Doing this will append each print line together.
