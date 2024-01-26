#!/usr/bin/env python3

"""
Implements the FizzBuzz game for numbers from 1 to 100.

Usage:
- Run the script to play FizzBuzz and print the results.
"""


def fizzbuzz():
    i = 1
    while i <= 100:
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz", end=" ")
        elif (i % 3 == 0):
            print("Fizz", end=" ")
        elif (i % 5 == 0):
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
        i += 1
