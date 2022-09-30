#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = 0
    sum_weight = 0
    for sub in my_list:
        total += sub[0] * sub[1]
        sum_weight += sub[1]
    average = total / sum_weight
    return average
