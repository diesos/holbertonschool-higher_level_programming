#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list) or idx < 0:
        return None
    for i in range(0, idx + 1):
        if i == idx:
            return my_list[i]
        i += 1