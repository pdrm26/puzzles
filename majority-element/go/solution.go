package main

import "fmt"

func majorityElement(nums []int) int {
	m := map[int]int{}

	for _, num := range nums {
		m[num]++

		if m[num] > len(nums)/2 {
			return num
		}
	}

	return -1
}

func main() {
	r1 := majorityElement([]int{2, 2, 1, 1, 1, 2, 2})
	r2 := majorityElement([]int{3, 2, 3})

	fmt.Println(r1, r2)
}
