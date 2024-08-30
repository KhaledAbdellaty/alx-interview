#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    Args:
    grid (List[List[int]]): A 2D list representing the island and water.
                            0 represents water, 1 represents land.

    Returns:
    int: The perimeter of the island.

    Algorithm:
    1. Iterate through each cell in the grid.
    2. If a cell is land (1), check its four adjacent cells.
    3. For each adjacent cell that is water or out of bounds,
        add 1 to the perimeter.
    4. Return the total perimeter.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check top
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                # Check bottom
                if row == rows-1 or grid[row+1][col] == 0:
                    perimeter += 1
                # Check left
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                # Check right
                if col == cols-1 or grid[row][col+1] == 0:
                    perimeter += 1

    return perimeter
