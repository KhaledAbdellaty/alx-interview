#!/usr/bin/python3
"""def minOperations(n)"""


def minOperations(n):
    """A function that calculate fewest no.
    of operations needed to result in n H characters"""
    i = 0
    m = 2
    while n > 1:
        while not n % m:
            i += m
            n /= m
        m += 1
    return i
