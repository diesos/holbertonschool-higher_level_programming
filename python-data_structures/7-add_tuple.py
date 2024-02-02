#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 2:
        value_a1 = tuple_a[0]
        value_a2 = tuple_a[1]
    elif len(tuple_a) < 2:
        value_a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
        value_a2 = 0

    if len(tuple_b) == 2:
        value_b1 = tuple_b[0]
        value_b2 = tuple_b[1]
    elif len(tuple_b) < 2:
        value_b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
        value_b2 = 0

    return (value_a1 + value_b1, value_a2 + value_b2)
