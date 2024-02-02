#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for index, value in enumerate(my_list):
        if value == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[index])
    return new_list
