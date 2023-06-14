#!/usr/bin/python3
def search_replace(my_list, search, replace):
    tmp = my_list[:]
    for i in range(0, len(tmp)):
        if tmp[i] == search:
            tmp[i] = replace
    return tmp
