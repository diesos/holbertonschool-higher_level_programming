#!/usr/bin/python3

"""
Prints a grid of two-digit numbers from 00 to 99.

Usage:
- Run the script to display a grid of two-digit numbers separated by commas.
"""

for i in range(10):
    for j in range(10):
        if i == 9 and j == 9:
            print(f'{i}{j}')
        else:
            print(f'{i}{j}{", "}', end="")
