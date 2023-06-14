#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    tmp = set(my_list)
    for i in tmp:
        sum += i
    return sum
