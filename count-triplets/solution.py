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
    # {element: [indeces]}
    secondary_elements = {}
    triplet_count = 0
    for val in arr:

        if val % ratio == 0:
            # Check if it's a final element
            if secondary_elements.get(val / ratio):
                triplet_count += (secondary_elements.get(val / ratio)
                                  * primary_elements.get(val / ratio**2))
            # Check if it could be a second element
            if primary_elements.get(val / ratio):
                if secondary_elements.get(val) is None:
                    secondary_elements[val] = 1
                else:
                    secondary_elements[val] += 1

        # Add it to possible first elements of progression.
        if primary_elements.get(val) is None:
            primary_elements[val] = 1
        else:
            primary_elements[val] += 1

    return triplet_count
