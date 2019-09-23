package solution

import (
	"testing"
)

var solutionTests = []struct {
	k        int32
	arr      []int32
	expected []int32
}{
	{1, []int32{4, 2, 3, 5, 1}, []int32{5, 2, 3, 4, 1}},
	{0, []int32{4, 2, 3, 5, 1}, []int32{4, 2, 3, 5, 1}},
	{1, []int32{2, 1, 3}, []int32{3, 2, 1}},
	{1, []int32{2, 1}, []int32{2, 1}},
}

func TestAbs(t *testing.T) {
	for _, tcase := range solutionTests {
		got := largestPermutation(tcase.k, tcase.arr)
		if !_slicesAreEqual(got, tcase.expected) {
			t.Errorf("Expected '%d' got '%d'", tcase.expected, got)
		}
	}
}

// _sliceAreEqual returns true if both []int32 parameters are equal. Otherwise returns false.
func _slicesAreEqual(s1 []int32, s2 []int32) bool {
	if len(s1) != len(s2) {
		return false
	}
	for i, val := range s1 {
		if val != s2[i] {
			return false
		}
	}
	return true
}
