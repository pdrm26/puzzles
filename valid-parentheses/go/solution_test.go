package main

import "testing"

func TestIsBalanced(t *testing.T) {
	cases := []struct {
		input    string
		expected bool
	}{
		{"()", true},
		{"({[]})", true},
		{"(]", false},
		{"", true},
		{"{[()]}", true},
		{"{[(])}", false},
	}

	for _, c := range cases {
		result := isBalanced(c.input)

		if result != c.expected {
			t.Errorf("isBalanced(%q) = %v; want %v", c.input, result, c.expected)
		}
	}

}
