package solution

import (
	"testing"
)

var solutionTests = []struct {
	operations [][2]int
	result     []int
}{
	{
		[][2]int{
			[2]int{1, 5},
			[2]int{1, 6},
			[2]int{3, 2},
			[2]int{1, 10},
			[2]int{1, 10},
			[2]int{1, 6},
			[2]int{2, 5},
			[2]int{3, 2},
		},
		[]int{0, 1},
	},
}

func TestAbs(t *testing.T) {
	for _, testCase := range solutionTests {
		got := freqQuery(testCase.operations)
		if !_sliceEquality(got, testCase.result) {
			t.Errorf("Expected '%d' got '%d'", testCase.result, got)
		}
	}
}

func Test_sliceEquality(t *testing.T) {
	if !_sliceEquality([]int{1, 2, 3}, []int{1, 2, 3}) {
		t.Errorf("Expected '%t' got '%t'", true, false)
	}
	if _sliceEquality([]int{1, 2, 3}, []int{1, 2, 4}) {
		t.Errorf("Expected '%t' got '%t'", false, true)
	}
	if _sliceEquality([]int{1, 2}, []int{1, 2, 3}) {
		t.Errorf("Expected '%t' got '%t'", false, true)
	}
}

// _sliceEquality returns true if slice1 and slice2 have identical integer elements
// in the same order. Otherwise returns false.
func _sliceEquality(slice1 []int, slice2 []int) bool {
	if len(slice1) != len(slice2) {
		return false
	}
	for i, val := range slice1 {
		if val != slice2[i] {
			return false
		}
	}
	return true

}
