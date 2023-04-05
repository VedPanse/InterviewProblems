'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether
or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is
considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.
'''
from collections import Counter

rectangles = [
    {
        "top_left": (1, 4),
        "dimensions": (3, 3)
    },
    {
        "top_left": (-1, 3),
        "dimensions": (2, 1)
    },
    {
        "top_left": (0, 5),
        "dimensions": (4, 3)
    }
]


def myFunc():
    area = []

    for item in rectangles:
        top_x = item["top_left"][0]
        top_y = item["top_left"][1]

        width = item["dimensions"][0]
        height = item["dimensions"][1]
        my_list = []

        iteration = 0

        while iteration < height:
            for items in range(top_x, top_x + width + 1):
                my_list.append((items, top_y + iteration))
            iteration += 1

        area.append(my_list)

    area_super = [element for innerList in area for element in innerList]

    return len(area_super) == len(list(set(area_super)))


print(myFunc())
