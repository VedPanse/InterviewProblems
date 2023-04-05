"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
"""


def func(arr):
    return_list = []
    for items in arr:
        if items == arr.index(items):
            return_list.append(items)

    if len(return_list) == 0:
        return False
    return return_list


print(func([1, 5, 7, 8]))
