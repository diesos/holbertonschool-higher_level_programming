#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    temp_dict = dict(a_dictionary)
    for key, value in temp_dict.items():
        temp_dict[key] = value * 2
    return temp_dict
