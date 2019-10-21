def fraudulentActivityNotifications(lookbackWindow, spendingArr):
    """
    Return the number of times spendingArr[i] >= 2*median(spendingArr[i -lookbackWindow:i])

    Args:
        lookbackWindow: A positive integer.
        spendingArr: An array of non-negative integers.
    Returns:
        A non-negative integer.
    """
    warningCount = 0
    myMedianTracker = MedianTracker(spendingArr[:lookbackWindow])

    i = lookbackWindow
    while i < len(spendingArr):
        med = myMedianTracker.getMedian()
        dailySpending = spendingArr[i]

        if dailySpending >= 2 * med:
            warningCount += 1

        myMedianTracker.update(spendingArr[i])
        i += 1

    return warningCount


class MedianTracker:

    def __init__(self, arr, maxValue=200):
        self.arr = arr
        self.values = [0] * (maxValue + 1)
        for val in arr:
            self.values[val] += 1

    def update(self, newValue):
        oldValue = self.arr[0]
        self.values[oldValue] -= 1
        del self.arr[0]
        self.values[newValue] += 1
        self.arr.append(newValue)

    def getMedian(self):
        firstIndex = (len(self.arr) + 1) // 2
        secondIndex = firstIndex + 1
        val1, val2 = None, None

        runningCount = 0
        # Intentionally backwards
        for val, count in enumerate(self.values):
            runningCount += count
            if runningCount >= firstIndex and val1 is None:
                val1 = val
            if runningCount >= secondIndex:
                val2 = val
                break

        if len(self.arr) % 2 == 0:
            return (val1 + val2) / 2
        else:
            return val1
