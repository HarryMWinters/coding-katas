def minimumSwaps2(arr):
    """
    The integer counts of the number of swaps required to sort the
    array.

    Args:
        arr: An array of integers.
    Returns:
        A non-negative integer.
    Raises:
        (someTypeOf)Error: if things go wrong.
    """
    def _swap(i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    disordered = True
    swap_count = 0
    while disordered:
        disordered = False
        for i, val in enumerate(arr):
            if val != i + 1:
                disordered = True
                swap_count += 1
                _swap(i, val - 1)

    return swap_count
