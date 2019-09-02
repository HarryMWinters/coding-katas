def cavityMap(grid):
    """
    Generate a list of of string with 'cavities' replaced by the the uppercase letter X.
    See README for fuller description of cavity.

    Args:
        grid: A list of strings.
    Returns:
        A list of strings of with the same dimensions as grid.
    Raises:
        TypeError:
    """
    gridHeight, gridWidth = len(grid), len(grid[0])
    cavityGrid = []
    for rowNumber, row in enumerate(grid):
        newRow = ""
        if rowNumber and rowNumber < gridHeight - 1:
            # Skip first & last row.
            for colNumber, letter in enumerate(row):
                if colNumber and colNumber < gridWidth - 1:
                    # Skip first & last column.
                    if _isCavity(grid, rowNumber, colNumber):
                        newRow += "X"
                    else:
                        newRow += letter
                else:
                    newRow += letter
        else:
            newRow = row
        cavityGrid.append(newRow)
    return cavityGrid


def _isCavity(grid, rowNumber, colNumber):
    """
    Check if grid[rowNumber][colNumber] is less than its neighboors.
    Args:
        grid: A list of strings.
        rowNumber: The row index of the value to be checked
        colNumber: The column index of the value to be checked.
    Returns:
        A boolean. True if the indexes are at a cavity.
    Raises:
        IndexError: If the indexes are next to an edge or out of bounds.
    """

    val = int(grid[rowNumber][colNumber])

    neighboors = [
        # It would be faster to check values on at a time and return at first
        # failure but IMHO less readable.
        int(grid[rowNumber][colNumber + 1]),
        int(grid[rowNumber][colNumber - 1]),
        int(grid[rowNumber + 1][colNumber]),
        int(grid[rowNumber - 1][colNumber]),
    ]
    if val >= max(neighboors):
        return True
    else:
        return False
