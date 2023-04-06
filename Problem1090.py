"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of words, find all pairs of unique indices such that the concatenation of the two
words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
"""


def myFunc(arr):
    tuple_list = []
    for item in arr:
        reverse_item = item[::-1]
        last_excl = item[:-1]

        if reverse_item in arr:
            tuple_list.append((arr.index(item), arr.index(reverse_item)))
        elif last_excl in arr:
            tuple_list.append((arr.index(item), arr.index(last_excl)))

    return tuple_list


print(myFunc(["code", "edoc", "da", "d"]))
