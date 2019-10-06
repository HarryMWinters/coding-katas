def fibonacci(n):
    """
    Return the nth element of the fibonacci sequence.
    Args:
        n: A non-negative integer.
    Returns:
        A non negative integer.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
