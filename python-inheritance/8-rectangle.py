#!/usr/bin/env python3
BaseGeometry = __import__('8-rectangle').BaseGeometry

class Rectangle(BaseGeometry):
	def __init__(self, width, height):
		super().integer_validator("width", width)
		self.__width:
