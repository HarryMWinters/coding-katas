def snail(snail_map):
    """
    Create a 1-D array of ints constructed from a snail traversal of the input array.

    Args:
        snail_map: An array of equal length integer arrays.
    Returns:
        A 1-D array of integers.
    """
    outputArr = []
    while snail_map:
        outputArr.extend(snail_map[0])
        del snail_map[0]
        if snail_map:
            outputArr.extend(traverseRight(snail_map))
        if snail_map:
            outputArr.extend(snail_map[-1][::-1])
            del snail_map[-1]
        if snail_map:
            outputArr.extend(traverseLeft(snail_map))
    return outputArr


def traverseRight(arr):
    out = []
    for subArr in arr:
        out.append(subArr[-1])
        del subArr[-1]
        if not subArr:
            del subArr
    return out


def traverseLeft(arr):
    out = []
    for subArr in arr:
        out.append(subArr[0])
        del subArr[0]
        if not subArr:
            del subArr
    return out[::-1]
