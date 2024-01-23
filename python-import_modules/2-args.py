#!/usr/bin/env python3

"""
Prints the command-line arguments along with their respective indices.

Usage:
- Provide command-line arguments when running the script.

Example:
$ python script.py arg1 arg2 arg3
"""

import sys
argv = len(sys.argv) - 1
i = 1
if (argv < 1):
    print("0 arguments.")
else:
    print(f'{argv} arguments:')
    while (i <= argv):
        print(f'{i}: {sys.argv[i]}')
        i += 1
