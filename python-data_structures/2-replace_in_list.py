#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in range(0,idx + 1):
        i += 1
        if i == idx:
            my_list[i] = element
            return (my_list)