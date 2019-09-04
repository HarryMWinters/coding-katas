def maximumToys(moneyAvailable, priceList):
    """
    Return an integer equal the maximum number of elements from priceList 
    whose sum <= moneyAvailable.

    Args:
        moneyAvailable: An integer.
        priceList: An unsorted list of integers
    Returns:
       An integer
    Raises:
        TypeError: if non number elements in priceList.
    """
    priceList.sort()
    count = 0
    for toyPrice in priceList:
        if toyPrice <= moneyAvailable:
            count += 1
            moneyAvailable -= toyPrice
        else:
            return count
