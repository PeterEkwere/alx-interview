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

    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                operations_count += i
                break
    return operations_count
