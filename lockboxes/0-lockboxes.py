#!/usr/bin/python3
"""
    Each box is numbered
    sequentially from 0 to n - 1 and each
    box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened.

    Args:
        boxes (list): List of lists. Each index of the list contains a list
        with the keys to open the next box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if boxes is None or len(boxes) == 0:
        return False

    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)

    if len(keys) == len(boxes):
        return True
    return False
