#!/usr/bin/python3

"""
Prints a triangular pattern of two-digit numbers from 01 to 89.

Usage:
- Run the script to display a triangular pattern of two-digit numbers separated by commas.
"""

for i in range(9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print(f'{i}{j}')
        else:
            print(f'{i}{j}{", "}', end="")
