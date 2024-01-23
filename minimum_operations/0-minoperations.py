#!/usr/bin/python3
"""
Defines a method that calculates the fewest number of operations needed
to result in exactly n copies of a character in a text file, whose
only operations are Copy All and Paste
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    n copies of a character in a text file, whose only operations are Copy
    All and Paste

    parameters:
        n [int]: the number of copies desired

    returns:
        the fewest number of operations needed to result in exactly n copies
        of a character in a text file, or 0 if n is impossible to achieve
    """
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(int(n / i)) + i
    return n
