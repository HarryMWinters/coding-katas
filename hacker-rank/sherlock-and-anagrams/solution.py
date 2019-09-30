import math


def sherlockAndAnagrams(s):
    """
    Return an integer denoting the number of substring anagrams within s.
    Args:
       s: S string containing only asci characters.
    Returns:
       A nonnegative integer.
    Raises:
        (someTypeOf)Error: if things go wrong.
    """
    # A Dict of palindromes and their counts.
    palindrome_counts = {}

    # Get all substrings of length len(s)/c
    for substring_length in range(len(s) - 1):
        for substring_starting_index in range(len(s) - substring_length):
            substring_end_index = substring_starting_index + substring_length + 1
            substring = s[substring_starting_index:substring_end_index]
            # TODO: Sorting is an inefficient way to "hash" by palindrome.
            # A letter count dict would be more efficient (in the initial grouping).
            substring_arr = list(substring)
            substring_arr.sort()
            sorted_substring = "".join(substring_arr)

            if palindrome_counts.get(sorted_substring):
                palindrome_counts[sorted_substring] += 1
            else:
                palindrome_counts[sorted_substring] = 1

    return sum([_two_of_m(val) for val in palindrome_counts.values()])


def _two_of_m(m):
    """
    Return the number of combinations possable by choosing two of m elements 
    without replacement and without considering ordering.
    """
    return (m * (m - 1) / 2)
