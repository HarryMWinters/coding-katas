def toys(arrA):
    """
    Return an integer value the number of containers required. 
    Really the minimum number of sublist that arrA must be broken 
    into such that the minimum value of a sublist is <= the maximum 
    value of s sublist minus 4.

    Args:
        arrA: An array of positive integers.
    Returns:
       A positive integer.
    Raises:
        (someTypeOf)Error: if things go wrong.
    """
    # ToDo: Does this _need_ to be sorted?
    arrA.sort()

    # Ideally everybox has 5 items
    boxArr = [[arrA[0]]]
    for weight in arrA[1:]:
        if weight > 4 + boxArr[-1][0]:
            boxArr.append([weight])
        else:
            boxArr[-1].append(weight)
    return len(boxArr)
