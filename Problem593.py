"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Mailchimp.

You are given an array representing the heights of neighboring buildings on a city street, from east to west. The
city assessor would like you to write an algorithm that returns how many of these buildings have a view of the
setting sun, in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since the top floors of the buildings with
heights 8, 6, and 1 all have an unobstructed view to the west.

Can you do this using just one forward pass through the array?
"""


def func(arr):
    return_lst = []
    inp_lst = []

    for ind in range(len(arr)):
        if ind == 0:
            return_lst.append(arr[ind] > arr[ind + 1])
        elif ind == len(arr) - 1:
            return_lst.append(True)
        else:
            return_lst.append(arr[ind] > arr[ind + 1] and arr[ind] > arr[ind - 1])

    return return_lst.count(True)


print(func([1, 2, 3, 4, 5, 6, 7]))
