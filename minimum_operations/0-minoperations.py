#!/usr/bin/python3
"""
Calculates the fewest number of operations needed to
result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed to result in exactly n H
    characters in the file
    """
    if n < 2:
        return 0
    count = 1
    li = list()
    value = n
    while value != 1:
        count += 1
        if value % count == 0:
            while value % count == 0 and value != 1:
                value /= count
                li.append(count)
    return sum(li)
