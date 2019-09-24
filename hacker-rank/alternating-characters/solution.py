def alternatingCharacters(string):
    """
    The number of deletions required 
    so that no two adjacent characters are the same.

    Args:
        string: A string of "A"s and "B"s
    Returns:
       An non-negative integer.
    Raises:
        (someTypeOf)Error: if things go wrong.
    """
    delCount = 0
    i = 1
    while i < len(string):
        if string[i] == string[i - 1]:
            delCount += 1
        i += 1
    return delCount
