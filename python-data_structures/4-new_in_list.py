#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return (my_list)
    if idx > len(my_list):
        return (my_list)
    for num in my_list:
        while num < idx + 1:
            num += 1
            if num == idx:
                my_list[num] = element
    return (element)
