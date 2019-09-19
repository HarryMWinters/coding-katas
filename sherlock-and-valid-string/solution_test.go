package solution

import (
	"testing"
)

var twoStringTests = []struct {
	s      string
	result bool
}{
	{"cat", true},
}

func TestAbs(t *testing.T) {
	for _, tcase := range twoStringTests {
		got := isValid(tcase.s)
		if got != tcase.result {
			t.Errorf("Expected '%t' got '%t'", tcase.result, got)
		}
	}
}
