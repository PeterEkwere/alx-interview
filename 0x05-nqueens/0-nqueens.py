#!/usr/bin/python3
"""
    This module contains the Nqueens problem.
    Author: Peter Ekwere
"""
import sys
import asyncio


async def place_queens(N, i, current_queens, valid_combinations, col, pos, neg):
    """
    Asynchronous function to place non-attacking queens
    """
    if len(current_queens) == N:
        valid_combinations.append(current_queens)
        return valid_combinations
    for j in range(N):
        if j not in col and i + j not in pos and i - j not in neg:
            await place_queens(N, i + 1, current_queens + [[i, j]], valid_combinations,
                               col + [j], pos + [i + j], neg + [i - j])
    return valid_combinations


async def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        return

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        return

    if N < 4:
        print("N must be at least 4")
        return

    valid_queen_combinations = []
    await place_queens(N, 0, [], valid_queen_combinations, [], [], [])
    for queen_combination in valid_queen_combinations:
        print(queen_combination)


if __name__ == "__main__":
    asyncio.run(main())
