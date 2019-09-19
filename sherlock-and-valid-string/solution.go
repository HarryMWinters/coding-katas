package solution

import (
	"math"
)

// isValid check whether an input string meets the "sherlock" criteries specifed in the ReadMe
// and returns true if it does and false if it does not.
func isValid(s string) bool {

	lettersSet := makeRuneSet(s)
	deletionAvailable := true
	initialValue := lettersSet[rune(s[0])]

	for _, count := range lettersSet {
		delta := math.Abs(float64(initialValue - count))

		if (delta == 1) || (count == 1) {
			if deletionAvailable {
				deletionAvailable = false
			} else {
				return false
			}
		} else {
			if delta > 1 {
				return false
			}
		}

	}
	return true
}

// makeRuneSet creates a map of rune frequencies in a given input string. I.E. {s: 2, h: 4} for "sshhhh"
func makeRuneSet(s string) map[rune]int {
	letterSet := map[rune]int{}
	for _, letter := range s {
		if val, ok := letterSet[letter]; ok {
			letterSet[letter] = val + 1
		} else {
			letterSet[letter] = 1
		}
	}
	return letterSet
}
