#!/usr/bin/env python3

"""Defines the 'BaseGeometry' class with an abstract 'area()' method."""


class BaseGeometry:
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
