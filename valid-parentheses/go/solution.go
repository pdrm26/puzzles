package main

import "fmt"

func isBalanced(s string) bool {
	matchers := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}

	var chars []rune

	for _, char := range s {
		if char == '(' || char == '{' || char == '[' {
			chars = append(chars, char)
		} else {
			if len(chars) == 0 {
				return false
			}

			if matchers[char] == chars[len(chars)-1] {
				chars = chars[:len(chars)-1]
			}
		}

	}

	return len(chars) == 0
}

func main() {
	s := "([])"
	result := isBalanced(s)

	fmt.Println(result)
}
