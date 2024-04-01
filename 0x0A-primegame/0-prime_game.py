#!/usr/bin/python3
"""
    alx interview practice
    Author: peter ekwere
"""


def is_prime(n):
    """
    Efficiently checks if a number is prime using a loop up to the
    square root of n.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def remove_multiples(nums, prime):
    """
    Removes multiples of a prime number from the nums list efficiently.
    """
    new_nums = []
    for num in nums:
        if num % prime != 0:
            new_nums.append(num)
    return new_nums  # Minor correction: typo fixed


def isWinner(x, nums):
    """
    Determines the winner of the prime game for
    x rounds and a given list of numbers.
    """
    maria_wins = 0
    ben_wins = 0
    for _ in range(x):  # Iterate for x rounds
        # Check if there are any prime numbers left
        has_prime = False
        for num in nums:
            if is_prime(num):
                has_prime = True
                break

        if not has_prime:  # No prime numbers, Ben wins
            ben_wins += 1
            continue

        # Maria picks the first prime number and removes its multiples
        for i, num in enumerate(nums):
            if is_prime(num):
                nums = remove_multiples(nums[i:], num)
                break

        # Check if Ben can still make a move
        has_prime = False
        for num in nums:
            if is_prime(num):
                has_prime = True
                break

        if not has_prime:  # Ben can't move, Maria wins
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
