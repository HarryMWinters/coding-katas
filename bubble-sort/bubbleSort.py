
def bubbleSort(arr):
    """
    Sort and return the input arr and number of swaps required
     using the bubble sort algorithm.

    Args:
        arr: An array of elements comparable by inequality in python.
    Returns:
        The input array and the number of swaps required as an integer.
    Raises:
        TypeError: if elements of the array do not have compatable 
        inequality methods defined. I.E. string and int.
    """
    swapCount = 0
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapCount += 1
    return arr, swapCount
