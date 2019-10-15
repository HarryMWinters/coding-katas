package solution

// largestPermutation returns the largest possible semantic
// value of an input array achievable by swapping k elements.
func largestPermutation(k int32, arr []int32) []int32 {
	for k > 0 {
		_swap(arr)
		k--
	}
	return arr

}

func _swap(arr []int32) []int32 {
	max := len(arr)
	noPreviousMisMatch := true
	for i, val := range arr {
		if val != int32(max-i) && noPreviousMisMatch {
			// The value is too low and should be
			// swapped with the highest value following.
			var position int32
			arr[i], position = _max(arr[i:])
			position = position + int32(i)
			arr[position] = val

			return arr
		}
	}
	return arr
}

func _max(arr []int32) (int32, int32) {
	var maxValue, indexOfMaxValue int32
	for i, val := range arr {
		if val > maxValue {
			maxValue, indexOfMaxValue = val, int32(i)
		}
	}

	return maxValue, indexOfMaxValue
}
