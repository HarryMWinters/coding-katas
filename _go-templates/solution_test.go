package solution

import (
	"testing"
)

var solutionTests = []struct {
	s      string
	result bool
}{
	{"foo", true},
}

func TestAbs(t *testing.T) {
	for _, tcase := range solutionTests {
		got := f(tcase.s)
		if got != tcase.result {
			t.Errorf("Expected '%t' got '%t'", tcase.result, got)
		}
	}
}
