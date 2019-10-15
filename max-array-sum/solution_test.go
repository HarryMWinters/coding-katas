package solution

import (
	"testing"
)

var solutionTests = []struct {
	input  []int
	result int
}{
	{[]int{1, 2, 3}, 4},
	{[]int{3, 7, 4, 6, 5}, 13},
	{[]int{2, 1, 5, 8, 4}, 11},
	{[]int{3, 5, -7, 8, 10}, 15},
	{[]int{10, -1, -1, -1, -1, 10}, 20},
	{[]int{10, -1, 10}, 20},
	{[]int{-1, 1}, 1},
	{[]int{10, 9}, 10},
	{[]int{9, 10}, 10},
	{[]int{-1, -1, -1}, 0},
	{[]int{-1, -1, -1, 4}, 4},
	// {[]int{}, },
	// {[]int{}, },
}

func TestAbs(t *testing.T) {
	for _, testCase := range solutionTests {
		got := maxSubsetSum(testCase.input)
		if got != testCase.result {
			t.Errorf("Expected '%d' got '%d' with input: %d",
				testCase.result, got, testCase.input)
		}
	}
}
