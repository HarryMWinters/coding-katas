def arrayManipulation(n, queries):
    """
    The maximum value of an element in an array of length arrLength
    after the operations in queries have been performed on it.

    Complexity:
        O(arrLength * len(queries)
    Args:
        arrLength: Non negative integer denoting length of array.
        queries: A list of operation to perform on the array. Format is
         [start_index, end_index, increment]
    Returns:
        A non negative integer.
    Raises:
        (someTypeOf)Error: if things go wrong.

    # NB: query indexing starts at 1!!
    """

    arr = [0] * (n + 1)
    for q in queries:
        x, y, incr = q
        arr[x - 1] += incr
        if y <= len(arr):
            arr[y] -= incr

    maxi = x = 0
    for i in arr:
        x += i
        if maxi < x:
            maxi = x

    return maxi
