package main

func mostWordsFound(sentences []string) int {
	var maximumWordsNumber int

	for _, s := range sentences {
		lettersCount := 1
		for _, letter := range s {
			if letter == ' ' {
				lettersCount++
			}
		}

		if lettersCount > maximumWordsNumber {
			maximumWordsNumber = lettersCount
		}
	}

	return maximumWordsNumber
}
