def bonetrousle(targetSum, maxValue, choices):
    """
    If possbale retuen Aalist of ints whose sum is sumRequired and whose length is lengthRequired.
    See URL in README for fuller description.

    Args:
        sumRequired: An integer value specifying the sum of the returned elements
        maxValue: An integer value specifying the max value of a returned element
        valuesRequired: The number of elements that must be returned.
    Returns:
        A list of ints whose sum is sumRequired and whose length is lengthRequired.
    Raises:
        AttributeError: if non ints are passed in as paramters.
    """
    maxPossible = (choices / 2) * ((maxValue - choices + 1) + maxValue)
    minPossible = (choices / 2) * (1 + choices)
    if minPossible > targetSum or targetSum > maxPossible:
        return [-1]
    sol = [i + 1 for i in range(choices)]
    i = 1
    maxBump = maxValue - choices
    # TODO Keep track of sum and decrement it instead of calling it each time.
    while sum(sol) < targetSum:
        #print(f"sol = {sol}\nsum = {sum(sol)}\ntargetSum = {targetSum}")
        sol[-i] += min(targetSum - sum(sol), maxBump)
        i += 1
    return sol
