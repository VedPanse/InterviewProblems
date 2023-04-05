"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other
words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and
negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def func(arr):
    arr.sort()
    compare_lst = [k for k in range(arr[0], arr[-1] + 1)]
    not_in_list = [k for k in compare_lst if k not in arr]

    if len(not_in_list) == 0:
        return max(arr) + 1
    return [k for k in not_in_list if k > 0][0]


print(func([6, 5, 3, 1, -1]))
