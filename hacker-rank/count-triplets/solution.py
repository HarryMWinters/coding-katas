def countTriplets(ratio, arr):
    """
    Return the number of ordered (but not necessarily consecutive) triplets in arr that 
    satisfy the geometric progression ratio. 

    Args:
        ratio: A positive integer denoting the rate of progression.
        arr: An array of integers to be searched for triplets matching the progression.
    Returns:
        A non-negative integer.
    Raises:
        (someTypeOf)Error: if things go wrong.
    """
    primary_elements = {}
    secondary_elements = {}
    triplet_count = 0
    for val in arr:
        if val % ratio == 0:
            # If val completes triplet
            triplet_count += secondary_elements.get(val / ratio, 0)
            # If val completes doublet
            if primary_elements.get(val / ratio):
                if secondary_elements.get(val):
                    secondary_elements[val] += \
                        primary_elements.get(val / ratio)
                else:
                    secondary_elements[val] = \
                        primary_elements.get(val / ratio)

        # Single val
        if primary_elements.get(val):
            primary_elements[val] += 1
        else:
            primary_elements[val] = 1

    return triplet_count
