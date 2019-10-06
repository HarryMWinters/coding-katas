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
        fibonacci_list = [0, 1]
        # n + 1 to account for zero based indexing
        while len(fibonacci_list) < n + 1:
            fibonacci_list.append(
                fibonacci_list[-1] + fibonacci_list[-2])
        return fibonacci_list[-1]
