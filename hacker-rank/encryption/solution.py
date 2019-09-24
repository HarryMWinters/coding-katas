import math


def encryption(string):
    """
    Return and encrypted string.

    Args:
        param1: An input string of asci characters.
    Returns:
       A string of the encrypted input.
    Raises:
        (someTypeOf)Error: if things go wrong.
    """
    rowLength = math.ceil(math.sqrt(len(string)))
    matrix = []
    for i, val in enumerate(string):
        if i % rowLength == 0:
            matrix.append([val])
        else:
            matrix[-1].append(val)

    encodedWordist = []
    for i in range(rowLength):
        word = []
        for j in matrix:
            if i < len(j):
                word.append(j[i])
        encodedWordist.append("".join(word))

    return " ".join(encodedWordist)
