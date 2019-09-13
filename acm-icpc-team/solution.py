def acmTeam(topicArr):
    """
    Return an array with the first element the maximum number of 1's that can be found by
    inclusive OR of two elements of topicArr and the second element the number of
    permutation that yield sucha value.

    Args:
        topicArr: An array with at least two elements of equal length binary sequences.
    Returns:
        An array[int] of length two.
    Raises:
        (someTypeOf)Error: if things go wrong.
    """

    def _countOnes(binaryNumber):
        return bin(binaryNumber).count("1")

    maxSkillzBin = permutationWithMax = 0
    while topicArr:
        competitor = topicArr[0]

        for otherCompetitor in topicArr[1:]:
            binarySkillzSum = int(competitor, 2) | int(otherCompetitor, 2)
            if _countOnes(binarySkillzSum) > _countOnes(maxSkillzBin):
                maxSkillzBin = binarySkillzSum
                permutationWithMax = 1
            elif _countOnes(binarySkillzSum) == _countOnes(maxSkillzBin):
                permutationWithMax += 1

        topicArr = topicArr[1:]

    return [_countOnes(maxSkillzBin), permutationWithMax]
