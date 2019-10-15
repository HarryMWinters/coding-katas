package solution

import (
	"math"
)

// maxSubsetSum returns the largest value that can be made by summing elements of
// the input arr which are not adjacent.
func maxSubsetSum(arr []int) int {
	var maxArr []float64
	maxAtFirst := math.Max(float64(arr[0]), 0.0)
	maxAtSecond := math.Max(float64(arr[0]), math.Max(float64(arr[1]), 0.0))
	maxArr = append(maxArr, maxAtFirst)
	maxArr = append(maxArr, maxAtSecond)
	for i := range arr[2:] {
		i = i + 2
		maxAtIMinus1 := math.Max(maxArr[i-1], 0.0)
		putativeMax := float64(arr[i]) + maxArr[i-2]
		maxAtI := math.Max(maxAtIMinus1, putativeMax)
		maxArr = append(maxArr, maxAtI)
	}
	return int(maxArr[len(maxArr)-1])
}
