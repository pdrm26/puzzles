package main

import "fmt"

func twoSum(nums []int, target int) []int {
	nums_map := make(map[int]int)

	for index, num := range nums {
		diff := target - num
		if _, ok := nums_map[diff]; ok {
			return []int{index, nums_map[diff]}
		}
		nums_map[num] = index
	}

	return []int{}
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}
