"""
COLLATZ SEQUENCE: APPLE
"""


def collatz(n):
    if n == 1:
        return n
    if n % 2 == 0:
        return collatz(n/2)
    return collatz(3*n + 1)


print(collatz(1000000))
