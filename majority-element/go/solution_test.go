package main

import "testing"

func TestMajorityElement(t *testing.T) {
	tests := []struct {
		input    []int
		expected int
	}{
		{input: []int{3, 2, 3}, expected: 3},
		{input: []int{2, 2, 1, 1, 1, 2, 2}, expected: 2},
		{input: []int{1}, expected: 1},
		{input: []int{1, 1, 2, 2, 1}, expected: 1},
	}

	for _, test := range tests {
		result := majorityElement(test.input)
		if result != test.expected {
			t.Errorf("For input %v, expected %d but got %d", test.input, test.expected, result)
		}
	}
}
