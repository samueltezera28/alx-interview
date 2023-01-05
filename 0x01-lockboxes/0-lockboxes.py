#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes):
    """Check if all boxes can be opened"""
    unlocked = set()
    stack = [0]
    while stack:
        box = stack.pop()
        if box not in unlocked:
            unlocked.add(box)
            stack.extend(boxes[box])
    return len(unlocked) == len(boxes)


if __name__ == '__main__':
    canUnlockAll([[]])
