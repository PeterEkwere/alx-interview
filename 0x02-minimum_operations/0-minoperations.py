#!/usr/bin/python3
"""
    This Module contains Minimum Operations interview practice
    Author: Peter Ekwere
"""


def copy_all(n: str) -> str:
    """ This function multiplies a string
    """
    return n * 2


def minOperations(n: int) -> int:
    """ This function calculates the fewest number of operations needed

    Args:
        n (int): n is the amount of H characters

    Returns:
        int: the fewest of operations
    """
    operations_count = 0
    characters = ""

    for i in range(n):
        if len(characters) == n:
            return operations_count
        elif len(characters) < n:
            if len(characters) < 1:
                characters = "H"
            if (len(characters) * 2) < n:
                characters = copy_all(characters)
                operations_count += 2
            else:
                characters += "H"
                operations_count += 1
