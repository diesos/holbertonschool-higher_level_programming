"""
Defines a function 'inherits_from' to check if an object is a subclass of a specified class.
"""
def inherits_from(obj, a_class):
    """Returns True if the object is a subclass of the specified class, False otherwise."""
    return issubclass(obj, a_class)
