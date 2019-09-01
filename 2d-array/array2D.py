def _mask(i, j):
    """
    Generate a list of 2D indexes in a "I" formation.

    Args:
        i: The smallest (highest) i value of an element in the output.
        j: The smallest j (leftmost) value of an element in the output.
    Returns:
        A 2D array of ints
    Raises:
        TypeError: if i or j is not a number or does not have + operand defined.
    """
    mask = [
        # Row 1
        [i, j],
        [i, j + 1],
        [i, j + 2],
        # Row 2
        [i + 1, j + 1],
        # Row 3
        [i + 2, j],
        [i + 2, j + 1],
        [i + 2, j + 2]
    ]
    return mask


def hourglassSum(arr):
    """
    Iterate over a 2D array and return the highest sum of values in a I formation. 
    See _mask for implentation of I shape.

    Args:
        arr: A 2D array of integers where len(arr[i]) is constant and len(arr) >= 3
    Returns:
        The maximum value of the sum of the components determined by _mask. 
    Raises:
        TypeError: if arr[i][j] is not a number.
    """
    i, j = 0, 0
    highestSum = sum([arr[a[0]][a[1]] for a in _mask(i, j)])
    while i + 2 < len(arr):
        j = 0
        while j + 2 < len(arr[i]):
            hourGlassShape = _mask(i, j)
            highestSum = max(
                [sum([arr[a[0]][a[1]] for a in hourGlassShape]),
                 highestSum]
            )
            j += 1
        i += 1
    return highestSum
