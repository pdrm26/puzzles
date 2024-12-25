package main

import (
	"fmt"
	"unicode"
)

func isAlphanumeric(char rune) bool {
	return unicode.IsLetter(char) || unicode.IsDigit(char)
}

func isPalindrome(s string) bool {

	left_pointer, right_pointer := 0, len(s)-1
	for left_pointer < right_pointer {
		left_char := s[left_pointer]
		right_char := s[right_pointer]

		if !isAlphanumeric(rune(left_char)) {
			left_pointer += 1
			continue
		}

		if !isAlphanumeric(rune(right_char)) {
			right_pointer -= 1
			continue
		}

		lowerLeftChar := unicode.ToLower(rune(left_char))
		lowerRightChar := unicode.ToLower(rune(right_char))

		if lowerLeftChar != lowerRightChar {
			return false
		}

		left_pointer += 1
		right_pointer -= 1
	}

	return true
}

func main() {
	fmt.Println(isPalindrome("AMA"))
	fmt.Println(isPalindrome("Pedi"))
	fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))
	fmt.Println(isPalindrome("race a car"))
	fmt.Println(isPalindrome(" "))

}
