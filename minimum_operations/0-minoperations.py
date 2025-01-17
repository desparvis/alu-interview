#!/usr/bin/python3

"""
first documentation
minimum operations to reach character n
"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    i = 2

    while n > 1:
        while n % i == 0:
            operations += i
            n /= i
        i += 1


    return operations