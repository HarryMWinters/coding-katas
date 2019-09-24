import math


def isPrime(n, primeList=[2]):
    """
    Return True if prime else False.

    Args:
        n: A integer greater than 0,
    Returns:
        Boolean. True if n is prime.
    Raises:
        (someTypeOf)Error: if things go wrong.
    """
    if n == 1:
        return False
    elif n == 2:
        return True

    ceiling = math.sqrt(n)
    _extendPrimeList(math.floor(ceiling), prime_list=primeList)
    for prime in primeList:
        if n % prime == 0:
            return False
        elif prime > ceiling:
            return True
    return True


def _extendPrimeList(m, prime_list=None):
    if prime_list[-1] < m:
        for i in range(prime_list[-1]+1, m + 1):
            isPrime = True
            for j in prime_list:
                if i % j == 0:
                    isPrime = False
                    break
                elif math.sqrt(i) < j:
                    break
            if isPrime:
                prime_list.append(i)
