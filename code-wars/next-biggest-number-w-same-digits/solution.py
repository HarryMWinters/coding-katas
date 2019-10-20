def nextBiggestNumberWSameDigits(n):
    """
    Return the next greatest number that can be made with
    the same digits or -1 if no greater number can be made.

    Args:
        n: An positive integer
    Returns:
        A positive integer or -1.
    """

    n = [char for char in str(n)][::-1]
    for i, char in enumerate(n[:-1]):
        if char > n[i+1]:
            tail, head = n[:i + 2][::-1], n[i + 2:][::-1]

            # find greatest number less than tail[0] in tail
            first = tail[0]
            swapCandidate, swapCandidateIndex = tail[1], 1
            for j, tailChar in enumerate(tail[1:]):
                if int(tailChar) == int(first) + 1:
                    swapCandidateIndex = j + 1
                    break
                elif swapCandidate > tailChar > first:
                    swapCandidate = tailChar
                    swapCandidateIndex = j + 1

            # Swap
            tail[0], tail[swapCandidateIndex] = tail[swapCandidateIndex], tail[0]

            # Sort remaining
            tail[1:] = sorted(tail[1:])

            n = head + tail
            return int("".join(n))

    return -1
