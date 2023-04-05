"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
"""
input_number = int(input('Enter the number: '))

MEGA_COUNT = 0

# Python3 program to convert a
# decimal number to binary number

# function to convert
# decimal to binary


def decToBinary(n):
    return format(n, 'b')


def func(n):
    global MEGA_COUNT

    binary = list(str(decToBinary(n)))
    count = 0

    for item in binary:
        if item == '1':
            count += 1
        elif item == '0':
            count = 0
        if count > MEGA_COUNT:
            MEGA_COUNT = count


func(input_number)
print(f'{input_number} in binary is {decToBinary(input_number)}')
print(f'Maximum length: {MEGA_COUNT}')
