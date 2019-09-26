def ctciIceCreamParlor(money, costArr):
    """
    Returns the (base 1) indeces of the first two value in costArr whose sum
    us equal to moneyy.

    Args:
        money: A positive integer
        costArr: An array of positive integers.
    Returns:
        A length two array of positive integers.
    Raises:
        (someTypeOf)Error: if things go wrong.
    """
    complementMap = dict()
    for i, price in enumerate(costArr):
        if complementMap.get(price) is not None:
            return [complementMap[price] + 1, i + 1]
        else:
            complementMap[money - price] = i
    raise(ValueError(f"No complementary prices in costArr.\n\
                     complement map={complementMap}"))
