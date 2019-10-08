def luckBalance(max_losses, contestArr):
    """
    Return the maximum amount on luck (an integer) possible.

    Args:
        max_losses: A non negative integer denoting the maximum number of 
            contest that important contests that can be lost.
        contestArr: A 2D array whose elements are [contest luck rating, contest importance rating]
    Returns:
        An integer.
    Raises:
        (someTypeOf)Error: if things go wrong.
    """
    luck = 0
    important_contests = []
    for contest in contestArr:
        if not contest[1]:
            luck += contest[0]
        else:
            important_contests.append(contest[0])
    important_contests.sort()
    minimum_wins = len(important_contests) - max_losses
    if minimum_wins > 0:
        luck -= sum(important_contests[:minimum_wins])
        luck += sum(important_contests[minimum_wins:])
    else:
        luck += sum(important_contests)
    return luck
