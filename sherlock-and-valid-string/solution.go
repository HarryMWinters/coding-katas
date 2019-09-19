package solution

// Should return true if s1 and s2 have a common substring
func isValid(s string) bool {

	//s1LettersSet := makeRuneSet(s)
	return true
}

func makeRuneSet(s string) map[rune]bool {
	letterSet := map[rune]bool{}
	for _, letter := range s {
		letterSet[letter] = true
	}
	return letterSet
}
