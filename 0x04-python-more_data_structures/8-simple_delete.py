#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dict = a_dictionary.copy()
    for v in b_dict.keys():
        b_dict[v] = b_dict[v] * 2
    return (b_dict)
