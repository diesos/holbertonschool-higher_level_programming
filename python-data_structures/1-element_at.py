#!/usr/bin/python3
def element_at(my_list, idx):
    for i in range(0,idx + 1):
        i += 1
        if i == idx:
            return my_list[i]