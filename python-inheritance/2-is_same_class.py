"""
Defines a function 'is_same_class' to check if an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Returns True if the object is an instance of the specified class, False otherwise."""
    return type(obj) is a_class
