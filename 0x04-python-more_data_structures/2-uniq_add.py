#!/usr/bin/python3
def uniq_add(my_list=[]):
    conv_list = set(my_list)
    total = 0
    unique_list = list(conv_list)
    n = len(unique_list)
    for i in range(n):
        total += unique_list[i]
    return total
