def twoArrays(k, arr1, arr2):
    """
    Return True if the arrays can be permutated such that for any index, 
    arr2[index] + arr1[index] >= k otherwise return false.

    Args:
        k: An integer which elements of arr1 and arr2 must be summable to. 
        arr1: An array of non-negative integers
        arr2: An array of non-negative integers
    Returns:
        A boolean. True if a permutation exists such that arr1[i] + arr2[i] >= k for all i's in 
            arr1 (or arr2). Otherwise returns False.
    Raises:
        (someTypeOf)Error: if things go wrong.
    """
    arr1.sort()
    arr2.sort()

    for iVal in arr1:
        # find the minimum val in arr2 that is >= val - k
        for j, jVal in enumerate(arr2):
            if iVal + jVal >= k:
                arr2.pop(j)
                break
            elif j == len(arr2) - 1:
                return False
    return True
