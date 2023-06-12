#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    sort_list = sorted(my_list)
    return(sort_list[-1])
