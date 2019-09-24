def stones(numStones, diffA, diffB):
    """
    An array of possible values for the final stone in a series of
    length numStones with intrastones value differences of either
    diffA or diffB.

    Args:
        numStones: An integer greater than 0.
        diffA: An integer greater than 0.
        diffB: An integer greater than 0.

    Returns:
       An array of integers
    Raises:
        (someTypeOf)Error: if things go wrong.
    """
    valueSet = {0}
    for _ in range(numStones - 1):
        tempValueSet = set()
        for v in valueSet:
            tempValueSet.add(v + diffA)
            tempValueSet.add(v + diffB)
        valueSet = tempValueSet

    output = list(valueSet)
    output.sort()
    return output
