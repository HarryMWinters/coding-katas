def flippingBits(base10Number):
    """
    The result of converting to base 2, flipping all the bits,
    and converting back into base 10.

    Args:
        base10Number: An integer.
    Returns:
        An integer.
    """
    binary = "{0:b}".format(base10Number)
    binZero = "0" * 32
    binary = binZero[:-len(binary)] + binary
    newBinary = "".join(["1" if c == "0" else "0" for c in binary])
    return int(newBinary, 2)
