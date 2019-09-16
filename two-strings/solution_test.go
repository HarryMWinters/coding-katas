package solution

import (
	"testing"
)

var twoStringTests = []struct {
	s1     string
	s2     string
	result bool
}{
	{"cat", "pan", true},
	{"dog", "cat", false},
	{"ZXCVB", "QWERTY", false},
	{"hello", "world", true},
	{"hi", "world", false},
}

func TestAbs(t *testing.T) {
	for _, tcase := range twoStringTests {
		got := twoStrings(tcase.s1, tcase.s2)
		if got != tcase.result {
			t.Errorf("Expected '%t' got '%t'", tcase.result, got)
		}
	}
}
