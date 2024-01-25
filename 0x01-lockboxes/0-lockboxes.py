#!/usr/bin/python3
"""
    This Module Contains the LockBox Practice
    Author: Peter Ekwere
"""


def canUnlockAll(boxes):
    """
        This is the CanUnlockALL Function
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # The first box is unlocked

    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
