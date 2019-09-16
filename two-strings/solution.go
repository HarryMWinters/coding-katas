package solution

import "fmt"

// Complete the twoStrings function below.
func twoStrings(s1 string, s2 string) bool {
	// Should return true if s1 and s2 have a common substring

	// These could run concurrently
	s1LettersSet := makeRuneSet(s1)
	s2LettersSet := makeRuneSet(s2)

	if doIntersect(s1LettersSet, s2LettersSet) {
		return true
	}
	return false

}
func doIntersect(runeSet1 map[rune]bool, runeSet2 map[rune]bool) bool {
	for r := range runeSet1 {
		if runeSet2[r] {
			fmt.Printf("%c", r)
			return true
		}
	}
	return false
}

func makeRuneSet(s string) map[rune]bool {
	letterSet := map[rune]bool{}
	for _, letter := range s {
		letterSet[letter] = true
	}
	return letterSet
}
