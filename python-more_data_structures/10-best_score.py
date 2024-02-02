#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:  # Check if the dictionary is empty
        return None

    max_value = float("-inf")  # Initialize max_value to negative infinity

    for key, value in a_dictionary.items():
        if value is not None:  # Check if the value is not None
            if max_value < value:
                max_value = value

    return max_value
