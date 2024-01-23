#!/usr/bin/python3
"""
Defines a method that calculates the fewest number of operations needed
to result in exactly n copies of a character in a text file, whose
only operations are Copy All and Paste
"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n copies of a character in a text file,
    whose only operations are Copy All and Paste

    parameters:
        n [int]: number of copies of the character desired

    returns:
        the minimum number of operations needed to result in n characters
        or 0 if n is impossible to achieve
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
