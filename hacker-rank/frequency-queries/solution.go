package solution

// freqQuery takes a list of operations and returns a list of
// responses to 'frequencyQuery' operations.
func freqQuery(operations [][2]int) []int {
	responses := []int{}
	frequencyMap := map[int]int{}
	fastFrequencyMap := map[int]map[int]bool{}
	for _, val := range operations {
		if val[0] == 1 {
			// Add value
			oldFreq := frequencyMap[val[1]]
			newFreq := oldFreq + 1
			frequencyMap[val[1]] = newFreq
			_updateFastFreq(fastFrequencyMap, newFreq, oldFreq, val[1])

		} else if val[0] == 2 {
			// Remove Value
			if frequencyMap[val[1]] != 0 {
				oldFreq := frequencyMap[val[1]]
				newFreq := oldFreq - 1
				frequencyMap[val[1]] = newFreq
				_updateFastFreq(fastFrequencyMap, newFreq, oldFreq, val[1])

			}
		} else if val[0] == 3 {
			// Execute and store frequency query
			if _valueAtFrequency(fastFrequencyMap, val[1]) {
				responses = append(responses, 1)
			} else {
				responses = append(responses, 0)
			}
		}
	}
	return responses
}

// _valueAtFrequency checks whether a given frequency has any values.
func _valueAtFrequency(freqDict map[int]map[int]bool, number int) bool {
	for _, val := range freqDict[number] {
		if val {
			return true
		}
	}
	return false
}

// _updateFastFreq updates the map of frequencies and values used for fast frequency look ups.
func _updateFastFreq(freqMap map[int]map[int]bool, newFreq int, oldFreq int, number int) {
	_, ok := freqMap[oldFreq]
	if ok {
		freqMap[oldFreq][number] = false
	}
	_, ok = freqMap[newFreq]
	if !ok {
		freqMap[newFreq] = map[int]bool{number: true}
	} else {
		freqMap[newFreq][number] = true
	}
}
