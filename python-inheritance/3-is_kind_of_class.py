"""
Defines a function 'is_kind_of_class' to check if an object is an instance or a subclass of a specified class.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance or a subclass of the specified class, False otherwise."""
    return isinstance(obj, a_class)
