#!/usr/bin/python3

"""
Creates a modified string, concatenating specific substrings from original str

Usage:
- Run the script to see the output.

"""
O_STRING = "Python is an interpreted, interactive,object-oriented programming\
 language that combines remarkable power with very clear syntax"
O_STRING = O_STRING[38:66] + O_STRING[-22:-17] + O_STRING[0:6] + "\n"
print(O_STRING)
