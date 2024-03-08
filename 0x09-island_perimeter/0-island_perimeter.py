#!/usr/bin/python3
"""
    This Module contains an island perimeter solution
    Author: Peter Ekwere
"""


def island_perimeter(grid):
    """
      This function calculates the perimeter of the island in a grid.

        Args:
        grid: A list of lists of integers,
        where 0 represents water and 1 represents land.

        Returns:
        The perimeter of the island in the grid.
    """
    m = len(grid)
    n = len(grid[0])
    q = []
    perimeter = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                q.append([i, j])
                perimeter += 4

    while q:
        x, y = q.pop(0)
        edges = get_edges(grid, x, y, m, n)
        perimeter -= len(edges)  # Subtract the number of valid neighbors`

    return perimeter


def get_edges(grid, x, y, r, c):
    """
    get all edges
    """
    edge = []

    if x + 1 < r and grid[x + 1][y]:
        edge.append((x + 1, y))

    if x - 1 >= 0 and grid[x - 1][y]:
        edge.append((x - 1, y))

    if y + 1 < c and grid[x][y + 1]:
        edge.append((x, y + 1))

    if y - 1 >= 0 and grid[x][y - 1]:
        edge.append((x, y - 1))

    return edge
