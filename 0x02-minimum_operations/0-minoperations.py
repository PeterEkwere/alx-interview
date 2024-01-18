#!/usr/bin/python3
"""
    This Module contains Minimum Operations interview practice
    Author: Peter Ekwere
"""


def minOperations(n: int) -> int:
    """ This function calculates the fewest number of operations needed

    Args:
        n (int): n is the amount of H characters

    Returns:
        int: the fewest of operations
    """
    operations_count = 0
    characters = "H"

    for i in range(n):
        if len(characters) == n:
            return operations_count
        elif len(characters) < n:
            if (len(characters) * 2) < n:
                characters *= 2
                operations_count += 2
            else:
                characters += "H"
                operations_count += 1
